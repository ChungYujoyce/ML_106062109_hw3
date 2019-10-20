import random 
import matplotlib
def load_dataset(filename):
    dataset = list()
    for i in range(len(filename)):
        attributes = filename[i].split(" ", 1)
        dataset.append(attributes)
    return dataset

def process_label(row):
    for i in range(len(row)):
        if row[i]=="1":



def example_presentation():


def evaluate_algorithm(dataset, algorithm, ):

def predict(row, weights):
    activation = weights[0]
    for i in range(len(row)-1):
        activation += weights[i+1] * row[i]
    return 1.0 if activation >= 0.0 else 0.0

def train_weights(train, learning_rate, n_epoch):

def perceptron(train, test, learning_rate, n_epoch):


# execute perceptron algorithm
filename = 'hw3_dataset.txt'
dataset = load_dataset(filename)
print(dataset)
learning_rate = 0.2
#scores = evaluate_algorithm(dataset, perceptron, )

