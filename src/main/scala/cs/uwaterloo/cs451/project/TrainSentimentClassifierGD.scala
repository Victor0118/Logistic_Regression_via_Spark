package ca.uwaterloo.cs451.project

import org.apache.hadoop.fs.{FileSystem, Path}
import org.apache.log4j.Logger
import org.apache.spark.{SparkConf, SparkContext}
import org.rogach.scallop._

/**
  * Created by shipeng on 18-3-25.
  */

class Conf_Trainer(args: Seq[String]) extends ScallopConf(args) {
  mainOptions = Seq(input, model)
  val input = opt[String](descr = "input path", required = true)
  val model = opt[String](descr = "output path", required = true)
  val shuffle = opt[Boolean](required = false, default = Some(false))
  verify()
}


object TrainSentimentClassifier {
  val log = Logger.getLogger(getClass().getName())

  def main(argv: Array[String]) {
    val args = new Conf_Trainer(argv)
    log.info("Input: " + args.input())
    log.info("Model: " + args.model())
    log.info("Shuffle: " + args.shuffle())

    val conf = new SparkConf().setAppName("Trainer")
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

    if (args.shuffle()) {
      inputFeature = inputFeature.sortBy(pair => pair._2._4)
    }

    var w_total = scala.collection.mutable.Map[Int, Double]()

    for (iter <- 1 to 10) {
      val w = sc.broadcast(w_total)
      val gradient = inputFeature.map(pair => {
        val g = scala.collection.mutable.Map[Int, Double]()

        def spamminess(features: Array[Int]): Double = {
          var score = 0d
          features.foreach(f => if (w.value.contains(f)) score += w.value(f))
          score
        }

        val delta = 0.002
        val instance = pair._2
        val docid = instance._1
        val pos = instance._2
        val features = instance._3

        val score = spamminess(features)
        val prob = 1.0 / (1 + math.exp(-score))
        features.foreach(f => {
          if (w.value.contains(f)) {
            g(f) += (pos - prob) * delta
          } else {
            g(f) = (pos - prob) * delta
          }
        })

        (0, g)
      }).reduceByKey((g1, g2) => {
        g1.keys.foreach(f => {
          if (g2.contains(f)) {
            g2(f) += g1(f)
          } else {
            g2(f) = g1(f)
          }
        })
        g2
      }).collect()

      gradient.foreach(x => {
        x._2.foreach(f => if (w_total.contains(f._1)) {
          w_total(f._1) += f._2
        } else {
          w_total(f._1) = f._2
        }
        )
      }
      )

    }
    sc.parallelize(w_total.toSeq).saveAsTextFile(args.model())
  }
}
