# tweets_sentiment

spark-submit --driver-memory 2g --class ca.uwaterloo.cs451.project.TrainSentimentClassifier target/project-1.0.jar --input /shared/au/small_train_shuf.txt --model cs451-small-train-model

spark-submit --driver-memory 2g --class ca.uwaterloo.cs451.project.TrainSentimentClassifier target/project-1.0.jar --input /shared/au/small_train_shuf.txt --model cs451-small-train-model --output small_test_shuf_output



# Data Statistics

|         | train_all           | test_all  | train_small           | test_small  |
| ------------- |:-------------:|:-----:|:-----:|:-----:|
| File Size      | 25G | 6.1G | | |
| Avg \# of Characters     |  |  | | |
| Avg \# of Terms     |  |  | | |
| \# of Pos       | 33,870,264 | 8,467,134 | | |
| \# of Neg      | 33,869,640   |   8,467,758 |  | |
