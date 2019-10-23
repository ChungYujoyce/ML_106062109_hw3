import random 
import matplotlib.pyplot as plt
def load_dataset(dataset): # process the dataset
    new_data = []
    for i in range(len(dataset)):
        ex, attributes = dataset[i].split(" ", 1)
        new_data.append(attributes)
    return new_data

def change_type(dataset): # change string to int
    int_data = list()
    for i in range(len(dataset)):
        Object = []
        for a in range(len(dataset[i])):
                if dataset[i][a] == "1":
                    Object.append(1)
                elif dataset[i][a] == "0":
                    Object.append(0)
        int_data.append(Object)
    return int_data
def process_label(row): # determine if the object is positive or not (numbers of 1 >= 3)
    labels = []
    for i in range(len(row)):
        num = 0
        pos = False
        for a in range(len(row[i])):
            if row[i][a]=="1":
                num = num + 1
            if num >= 3:
                row[i] += "1"
                pos = True
                break
        if pos==False:
            row[i] += "0" # add the labels directly ibto dataset instead of another list
    return 0

def predict(row, weights):
    activation = weights[0]
    for i in range(len(row)-1):
        activation += weights[i+1] * row[i]
    return 1.0 if activation >= 10e-7 else 0.0

def train_weights(train, learning_rate, n_epoch):
    zero_error_epoch = 0
    weights = [0.2 for i in range(len(train[-1]))]
    record = False
    for epoch in range(n_epoch):
        sum_error = 0.0
        for row in train:
            prediction = predict(row, weights)
            error = row[-1] - prediction #list indices must be integers or slices, not list
            #print(error)
            sum_error += error**2 # get the abs of -1 1 0
            weights[0] = weights[0] + learning_rate * error
            for i in range(len(row)-1):
                weights[i+1] = weights[i+1] + learning_rate * error * row[i]
                #print(weights[i+1])
        
        if sum_error == 0 and record == False:
            print("sss")
            zero_error_epoch = epoch + 1
            record = True
        #print('>epoch=%d, learning_rate=%.3f, error=%.3f' % (epoch, learning_rate, sum_error))
        print(weights[0], weights[1],weights[2] ,weights[3],weights[4], weights[5])

    return weights, zero_error_epoch * len(train) #, example_presentations

def draw_func(learning_rate, example_pres):
    plt.plot(learning_rate, example_pres, 'ro')
    plt.ylabel('Number of example-presentations')
    plt.xlabel('Learning rate')
    plt.axis([0, 1, 0, 300])
    plt.show()
    
filename = 'hw3_dataset.txt'
f = open(filename, "r")
lines = f.readlines()
dataset = list(lines)
new_data = load_dataset(dataset)
#print(new_data)
process_label(new_data)
new_int_data = change_type(new_data)
example_pres = []
learning_rate = 0.2
n_epoch = 20
weights ,example_presentations = train_weights(new_int_data, learning_rate, n_epoch)
example_pres.append(example_presentations)
print(weights)
print(new_int_data)
print("----------Leanring rate: 0.2----------")
print("Example-presentations:%d "% example_presentations)

learning_rate = 0.4
n_epoch = 20
weights ,example_presentations = train_weights(new_int_data, learning_rate, n_epoch)
example_pres.append(example_presentations)
print(weights)
print(new_int_data)
print("----------Leanring rate: 0.4----------")
print("Example-presentations:%d "% example_presentations)

learning_rate = 0.6
n_epoch = 20
weights ,example_presentations = train_weights(new_int_data, learning_rate, n_epoch)
example_pres.append(example_presentations)
print(weights)
print("----------Leanring rate: 0.6----------")
print("Example-presentations:%d "% example_presentations)

learning_rate = 0.8
n_epoch = 20
weights ,example_presentations = train_weights(new_int_data, learning_rate, n_epoch)
example_pres.append(example_presentations)
print(weights)
print("----------Leanring rate: 0.8----------")
print("Example-presentations:%d "% example_presentations)

draw_func([0.2, 0.4, 0.6, 0.8], example_pres)