# ML_Programming_Assignment_2
## Perceptron Learning implementation 
##### Using python
#### There are some functions:
### 1. Handle Data
* load_dataset
    1. load hw3_dataset.txt file 
        * Since it's form is `exn 10001`, I need to split them to get the five 1/0 attributes
        * Use `string.split(" ", 1)`

### 2. Change type string to type int 
* change_type
    1. If it's not int type, the following processes will get wrong
        * Use a new list and append correct type to it, then return
        

### 3. Determine the correct labels
* process_label
    1. Manually calculate the number of 1 (positive) to determine the final label of each example
    2. Append the label in string type, and then change the type afterward.
#### ***Main algorithm***
### **4. Prediction !!!**
* predict
    1. Set the bias (W0) as 0.2
        * Multiply each weight with  attribute one by one and sum them up
        * If result >= 10e-7 the label will set as 1, else as 0
        * ***Note: Can not set the threshold as 0, since there's float error in python. If set it 0, there'll be some labels be identify as 0 but are 1 actually.***
### **5. Update training weights !!!**
* train_weights
    1. Set initial weights to 0.2
    2. Predict the result
    3. Use fomula ![](https://i.imgur.com/mCcyuT7.jpg) to update the weights in each epoch
    4. If the error rate (correct_label - predict_label) gets 0, calculate the example-presentation
    5. return final weights and example-presentation

### 6. Draw the relationship

> import matplotlib.pyplot as plt to draw graph conveniently
> 
Problem 1:

* draw_func -- example_presentations and learning rate

Problem 2:
* draw_func -- example_presentations and the number of adding attributes

### 7. Main()
Problem 1:
* Use different learning rates [0.2, 0.4, 0.6, 0.8] to do the perceptron learning and observe the results

###### Result
![](https://i.imgur.com/WJ98LUv.jpg)
![](https://i.imgur.com/jy4cgko.jpg)


##### Obervation

#### As the learning rate becomes larger, from 0.2 to 0.8, we found out that at learning rate 0.6, the example-presentation becomes especially small, I think it's a local minima (Can't know if it's global minima). 
Problem 2:
* Use different N as the number of adding attributes (randomly choose) [1, 5, 10, 15, 20] to do the perceptron learning and observe the results
###### One of many random result
![](https://i.imgur.com/nqEe851.jpg)

##### Obervation

#### Since the adding attributes are selected randomly, so there're some differences between each run. I can not find any relationship between each run. But after I runned for several times, I found out that the number of example-presentations in most of the N get smaller. Most of them can get under 200, which is better than adding nothing. 

> Since the dataset isn't large enough, my ovservation may have some flaws in it.

