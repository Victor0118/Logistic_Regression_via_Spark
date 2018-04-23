# Running Instruction

### GD

Train GD
```
spark-submit --driver-memory 2g --class ca.uwaterloo.cs451.project.TrainSentimentClassifierGD \
             target/project-1.0.jar --input /shared/au/small_train_shuf.txt \
             --model small_train_shuf_gd --epoch 5 --regularization 0.0001 --lr 0.002
```
Test GD
```
spark-submit --driver-memory 2g --class ca.uwaterloo.cs451.project.ApplySentimentClassifier \
             target/project-1.0.jar --input /shared/au/small_test_shuf.txt \
             --model small_train_shuf_gd --output small_test_output_gd 

sh ./eval_hdfs.sh small_test_output_gd
 ```
 
### SGD 

Train SGD
```
spark-submit --driver-memory 2g --class ca.uwaterloo.cs451.project.TrainSentimentClassifierSGD \
             target/project-1.0.jar --input /shared/au/small_train_shuf.txt \
             --model small_train_shuf_sgd --epoch 5 --regularization 0.0001 --lr 0.002
```

Test SGD
```
spark-submit --driver-memory 2g --class ca.uwaterloo.cs451.project.ApplySentimentClassifier \
             target/project-1.0.jar --input /shared/au/small_test_shuf.txt \
             --model small_train_shuf_sgd --output small_test_output_sgd 

sh ./eval_hdfs.sh small_test_output_sgd
```
 
 ### MBSGD
 
 Train MBSGD
```
spark-submit --driver-memory 2g --class ca.uwaterloo.cs451.project.TrainSentimentClassifierMBSGD \
             target/project-1.0.jar --input /shared/au/small_train_shuf.txt \
             --model small_train_shuf_mbsgd --epoch 5 --regularization 0.0001 --lr 0.002 --fraction 0.1
```
Test MBSGD
```
spark-submit --driver-memory 2g --class ca.uwaterloo.cs451.project.ApplySentimentClassifier \
             target/project-1.0.jar --input /shared/au/small_test_shuf.txt \
             --model small_train_shuf_mbsgd --output small_test_output_mbsgd 

sh ./eval_hdfs.sh small_test_output_mbsgd
 ```

# Parameter Test on Epoch Number (epoch) 
`delta=0.002, lambda=0`

|     epoch   |SGD         | MBSGD  (fraction=0.1)       |
| ------------- |:-------------:|:-------------:|
|   1    |  | 
|   2    |  | 
|   3    |  | 
|   4    |  | 
|   5    |  | 

|     epoch   |GD         | 
| ------------- |:-------------:|
|   1    |  | 
|   5    |  | 
|   10    |  | 
|   50    |  | 
|   100    |  | 


# Parameter Test on Batch Size (fraction) 
`delta=0.002, epoch=3, lambda=0`

|     fraction   | MBSGD         |
| ------------- |:-------------:|
|   1    | 0.7178 | 
|   0.1    | 0.7187 | 
|   0.01    | 0.7327 | 


# Parameter Test on Learning Rate (delta) 
`lambda=0`

|     delta    | SGD   (epoch=1)      | MBSGD (fraction=0.1, epoch=3)        | GD  (epoch=5)       |
| ------------- |:-------------:|:-------------:|:-------------:|
|   0.001    | 0.7404 | 0.7173 |
|   0.002    | 0.7424 | 0.7187 | 0.7179| 
|   0.005    | 0.7442 | 0.7231 | 
|   0.01    |  | 0.7283 |
|   0.02    | 0.7302 | 0.7349 |
|   0.05    |  |  0.7444 |
|   0.1    |  |   |


# Parameter Test on Regularization (lambda)

|     lambda    | SGD  (epoch=1, delta=0.002)      | MBSGD (fraction=0.1, delta=0.01, epoch=3)        | GD (epoch=10)        |
| ------------- |:-------------:|:-------------:|:-------------:|
|   0.0    | 0.7424 | 0.7283| 
|   0.00001    | 0.7423 | 
|   0.0001    | 0.7438 |
|   0.001    | 0.7438 |
|   0.005    | 0.7438 |
|   0.01    | 0.7429 |
|   0.05    | 0.7426 |
|   0.5    | 0.7309 |



# Data Statistics

|         | train_all           | test_all  | train_small           | test_small  |
| ------------- |:-------------:|:-----:|:-----:|:-----:|
| File Size      | 25G | 6.1G | 361 M| 73 M|
| Avg \# of Characters     |  |  | | |
| Avg \# of Terms     |  |  | | |
| \# of Pos       | 33,870,264 | 8,467,134 | 500,206 | 99,918 |
| \# of Neg      | 33,869,640   |   8,467,758 | 499,794 | 100,082 |

# Training and Testing on All Data through MBSGD

Train MBSGD
```
spark-submit --deploy-mode client --num-executors 4 --executor-cores 4 --executor-memory 35G \
             --driver-memory 2g --class ca.uwaterloo.cs451.project.TrainSentimentClassifierMBSGD \
             target/project-1.0.jar --input /shared/au/train_all.txt \
             --model train_all_mbsgd --epoch 5 --regularization 0.0 --lr 0.02
             
```
Test MBSGD
```
spark-submit --driver-memory 2g --class ca.uwaterloo.cs451.project.ApplySentimentClassifier \
             target/project-1.0.jar --input /shared/au/test_all.txt \
             --model train_all_mbsgd --output train_all_output_mbsgd 

sh ./eval_hdfs.sh train_all_output_mbsgd
 ```

# Reference

* http://legacydirs.umiacs.umd.edu/~jimmylin/publications/Lin_Kolcz_SIGMOD2012.pdf
* https://courses.cs.washington.edu/courses/cse547/16sp/slides/logistic-SGD.pdf
* https://spark.apache.org/docs/latest/mllib-linear-methods.html
* https://github.com/apache/spark/tree/master/mllib/src/main/scala/org/apache/spark/mllib/optimization
* http://theory.stanford.edu/~tim/s16/l/l6.pdf

