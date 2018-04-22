# tweets_sentiment

spark-submit --driver-memory 2g --class ca.uwaterloo.cs451.project.TrainSentimentClassifierGD \
 target/project-1.0.jar --input /shared/au/small_train.txt \
 --model cs451-small-train-model
