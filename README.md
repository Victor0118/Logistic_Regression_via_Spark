# tweets_sentiment

## GD

Train GD
```
spark-submit --driver-memory 2g --class ca.uwaterloo.cs451.project.TrainSentimentClassifierGD target/project-1.0.jar --input /shared/au/small_train_shuf.txt --model small_train_shuf_gd --epoch 5
```
Test GD
```
spark-submit --driver-memory 2g --class ca.uwaterloo.cs451.project.ApplySentimentClassifier target/project-1.0.jar --input /shared/au/small_test_shuf.txt --model small_train_shuf_gd --output small_test_output_gd

sh ./eval_hdfs.sh small_test_output_gd
 ```
 
## SGD 

Train SGD
```
spark-submit --driver-memory 2g --class ca.uwaterloo.cs451.project.TrainSentimentClassifier target/project-1.0.jar --input /shared/au/small_train_shuf.txt --model small_train_shuf_sgd --epoch 5
```

Test SGD
```
spark-submit --driver-memory 2g --class ca.uwaterloo.cs451.project.ApplySentimentClassifier target/project-1.0.jar --input /shared/au/small_test_shuf.txt --model small_train_shuf_sgd --output small_test_output_sgd

sh ./eval_hdfs.sh small_test_output_sgd
```
 
 ## MBSGD
 
 Train MBSGD
```
spark-submit --driver-memory 2g --class ca.uwaterloo.cs451.project.TrainSentimentClassifierMBSGD target/project-1.0.jar --input /shared/au/small_train_shuf.txt --model small_train_shuf_mbsgd --epoch 5
```
Test MBSGD
```
spark-submit --driver-memory 2g --class ca.uwaterloo.cs451.project.ApplySentimentClassifier target/project-1.0.jar --input /shared/au/small_test_shuf.txt --model small_train_shuf_bgd --output small_test_output_mbsgd 

sh ./eval_hdfs.sh small_test_output_bgd
 ```


# Data Statistics

|         | train_all           | test_all  | train_small           | test_small  |
| ------------- |:-------------:|:-----:|:-----:|:-----:|
| File Size      | 25G | 6.1G | 361 M| 73 M|
| Avg \# of Characters     |  |  | | |
| Avg \# of Terms     |  |  | | |
| \# of Pos       | 33,870,264 | 8,467,134 | 500206 | 99918 |
| \# of Neg      | 33,869,640   |   8,467,758 | 499794 | 100082 |
