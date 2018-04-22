package ca.uwaterloo.cs451.project

import org.apache.hadoop.fs.{FileSystem, Path}
import org.apache.log4j.Logger
import org.apache.spark.{SparkConf, SparkContext}
import org.rogach.scallop._

import scala.collection.mutable.ArrayBuffer

/**
  * Created by shipeng on 18-3-25.
  */


object TrainSentimentClassifierMBSGD {
  val log = Logger.getLogger(getClass().getName())

  def main(argv: Array[String]) {
    val args = new Conf_Trainer(argv)
    log.info("Input: " + args.input())
    log.info("Model: " + args.model())
    log.info("Shuffle: " + args.shuffle())
    log.info("epoch: " + args.epoch().toString())
    log.info("regularization: " + args.regularization().toString())

    val conf = new SparkConf().setAppName("TrainerMBSGD")
    val sc = new SparkContext(conf)
    val textFile = sc.textFile(args.input())
    val outputDir = new Path(args.model())
    FileSystem.get(sc.hadoopConfiguration).delete(outputDir, true)


    var inputFeature = textFile.map(line => {
      val tokens = line.split(" ")
      val docid = tokens(0)
      val pos = if (tokens(1).trim().equals("pos")) 1 else 0
      val features = tokens.slice(2, tokens.size).map(str => str.toInt)
      val rand = scala.util.Random.nextInt
      (0, (docid, pos, features, rand))
    })

    val batch_size = (inputFeature.count() * args.fraction()).toInt * 1.0

    if (args.shuffle()) {
      inputFeature = inputFeature.sortBy(pair => pair._2._4)
    }

    var w_total = scala.collection.mutable.Map[Int, Double]()
    val reg = args.regularization()

    for (iter <- 1 to (args.epoch() * 1.0 / args.fraction()).toInt) {
      val w = sc.broadcast(w_total)

      val gradient = inputFeature.sample(false, args.fraction()).mapPartitions(partition => {
        val buffer = ArrayBuffer[scala.collection.mutable.Map[Int, Double]]()
        val g = scala.collection.mutable.Map[Int, Double]()
        def sentiment(features: Array[Int]): Double = {
          var score = 0d
          features.foreach(f => if (w.value.contains(f)) score += w.value(f))
          score
        }
        val delta = 0.002
        partition.foreach(pair => {
          val instance = pair._2
          val docid = instance._1
          val pos = instance._2
          val features = instance._3
          val score = sentiment(features)
          val prob = 1.0 / (1 + math.exp(-score))
          features.foreach(f => {
            if (g.contains(f)) {
              g(f) += (pos - prob + 2.0 * w.value.getOrElse(f, 0.0) * reg) * delta
            } else {
              g(f) = (pos - prob + 2.0 * w.value.getOrElse(f, 0.0) * reg) * delta
            }
          })

        })
        buffer.+=(g)
        buffer.iterator
      }
      ).collect().foreach(g => {
        g.keys.foreach(f => {
          if (w_total.contains(f)) {
            w_total(f) += g(f) / batch_size
          } else {
            w_total(f) = g(f) / batch_size
          }
        })
      }
      )
    }
    sc.parallelize(w_total.toSeq).coalesce(1).saveAsTextFile(args.model())
  }
}
