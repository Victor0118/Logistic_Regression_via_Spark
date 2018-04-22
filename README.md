# tweets_sentiment

spark-submit --driver-memory 2g --class ca.uwaterloo.cs451.project.TrainSentimentClassifierGD \
 target/project-1.0.jar --input /shared/au/small_train.txt \
 --model cs451-small-train-model


# Data Statistics

|         | train_all           | test_all  | train_small           | test_small  |
| ------------- |:-------------:|:-----:|:-----:|:-----:|
| File Size      | 25G | 6.1G | 361 M| 73 M|
| Avg \# of Characters     |  |  | | |
| Avg \# of Terms     |  |  | | |
| \# of Pos       | 33,870,264 | 8,467,134 | 500206 | 99918 |
| \# of Neg      | 33,869,640   |   8,467,758 | 499794 | 100082 |
