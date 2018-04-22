# tweets_sentiment

spark-submit --driver-memory 2g --class ca.uwaterloo.cs451.a6.TrainSentimentClassifierGD \
 target/project-1.0.jar --input /shared/au/train_small.txt \
 --model cs451-small-train-model
