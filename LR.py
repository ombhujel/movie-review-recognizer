import os
import string
import json
import math
from decimal import Decimal


#initializing two weight vectors of size 10 and 100
weight_arr_100 = []
weight_arr_10 = []
weight_arr_300 = []
i=0
while(i<10):
    weight_arr_10.append(0)
    i=i+1

i=0
while(i<100):
    weight_arr_100.append(0)
    i=i+1

i=0
while(i<300):
    weight_arr_300.append(0)
    i=i+1

#initializing two biases to 0, for wiight vectors 10, and 100
bias_10 = 0
bias_100 = 0
bias_300 = 0

hyper_parameter = 0.75
#Python equivalent to java hasnext() function
def generator(path):
    word = ''
    with open(path) as file:
        while True:
            char = file.read(1)
            if char.isspace():
                if word:
                    yield word
                    word = ''
            elif char == '':
                if word:
                    yield word
                break
            else:
                word += char

#Given the parameter, weight vector and bias, it calculates, and returns "z"
def z_calc(weight, bias, array, num):
    i = 0
    z = 0
    #print(bias)
    while(i < num):
        z = z + (weight[i] * array[i])
        i=i+1
    return z + bias

#Given the parameter y value and z, it returns the y_prime, i.e, the sigmoid of y
def y_prime_calc(y, z):
    #print("beginning calc")
    #print("value of z")
    #print(z)
    if(z > 700.0):
        z = 700.0
    if(z < -700.0):
        z = -700.0
    calc = 1/(1 + math.exp(-z))
    if(y == 1):
        y_prime = calc
    else:
        #print("the value of z")
        #print(z)
        y_prime = 1 - calc
        #y_prime = math.exp(-(z))/(1 + math.exp(-(z)))
    if(y_prime == 0.0):
        y_prime = 0.000001
    if(y_prime == 1.0):
        y_prime = 0.999999
    #print(y_prime)
    return y_prime
    

#Given the value of y and y_prime, it calculates cross entropy, which is our loss function
def cross_entropy(y, y_prime):
    abc = 1 - y_prime
    #(print(y_prime))
    #print("value of abc")
    #print(abc)
    loss = -y*(math.log(y_prime)) - (1-y)*(math.log(abc))
    return loss

#Given the weight vector, bias, the path to the file to extract the value of imput and the size of the vector,
#SGD will calculate the best fitting weight vector for the training example
def SGD(weight_array, bias, words, num):
    theta_arr = []
    flag = 0
    while(flag == 0): 
        y = int(next(words))
        x_array = []
        j=0
        while(j < num):
            x_array.append(int(next(words)))
            j=j+1
        z = z_calc(weight_array, bias, x_array, num)
        y_prime = y_prime_calc(y, z)
        loss_value = cross_entropy(y, y_prime)
        if(loss_value < 0.00001):
            break
        i=0
        while(i < num):
            loss_derivative = ((y_prime - y) * x_array[i])
            theta_arr.append(loss_derivative)
            i = i + 1
        x_array.clear()
        k = 0
        while(k < num):
            weight_array[k] = weight_array[k] - (hyper_parameter * theta_arr[k])
            k = k + 1

        theta_arr.clear()
        bias = bias - hyper_parameter * (y_prime - y)
    return bias


       




#LR_Classifier takes the weight array, bias, the test file path to extract the input vector, the path to write the prediction it mades 
# and the size of the vector in its parameter. Provided the parameter, the function writes the actual label and the predicted label in 
#the
def LR_Classifier(array, bias, word, file, num):
    i=0
    while(i<24999):
        y = int(next(word))
        file.write(str(y)+" ")
        x_array = []
        j=0
        while(j < num):
            x_array.append(int(next(word)))
            j=j+1
        z = z_calc(array, bias, x_array, num )
        y_prime = y_prime_calc(y, z)
        
        if(y_prime >= 0.5):
            file.write(str(1))
            file.write('\n')
        else:
            file.write(str(0))
            file.write('\n')
        i=i+1


#Finally, as the name suggested, the accuracy function will calculate the accuracy of the model.
def accuracy(file):
    correct_prediction = 0
    total_instances = 1
    while(total_instances<24999):
        actual_value = int(next(file))
        predicted_value = int(next(file))
        if(actual_value == predicted_value):
            correct_prediction = correct_prediction+1
        total_instances=total_instances+1
    num = round(((correct_prediction/total_instances)*100),4)
    return num



# Instantiate the word generator.

words_100 = generator('output_file_100.txt')
words_10 = generator('output_file_10.txt')
words_300 = generator('output_file_300.txt')

#Creating the necessary file, path and the word vector to perform the operation on the 
#LR_classifier, where we're doing for the size of 100 and 10.

words_100_test = generator('output_file_test_100.txt')
words_10_test = generator('output_file_test_10.txt')
words_300_test = generator('output_file_test_300.txt')


f100 = open("output_file_accuracy_100.txt", "w", encoding="utf-8")
f10 = open("output_file_accuracy_10.txt", "w", encoding="utf-8")
f300 = open("output_file_accuracy_300.txt", "w", encoding="utf-8")

words_100_accuracy = generator('output_file_accuracy_100.txt')
words_10_accuracy = generator('output_file_accuracy_10.txt')
words_300_accuracy = generator('output_file_accuracy_300.txt')


#calculating weight parameters by stochastic gradient descent for frature vector size 10 and 100
#bias_10 = SGD(weight_arr_10, bias_10, words_10, 10)
bias_100 = SGD(weight_arr_100, bias_100, words_100, 100)
bias_10 = SGD(weight_arr_10, bias_10, words_10, 10)
bias_300 = SGD(weight_arr_300, bias_300, words_300, 300)

LR_Classifier(weight_arr_100, bias_100, words_100_test, f100, 100)
LR_Classifier(weight_arr_10, bias_10, words_10_test, f10, 10)
LR_Classifier(weight_arr_300, bias_300, words_300_test, f300, 300)

f100.close()
f10.close()
f300.close()

accuracy_for_100=accuracy(words_100_accuracy)
accuracy_for_10=accuracy(words_10_accuracy)
accuracy_for_300=accuracy(words_300_accuracy)
print(accuracy_for_100)
print(accuracy_for_10)
print(accuracy_for_300)


f100 = open("output_file_accuracy_10.txt", "r+", encoding="utf-8")
f10 = open("output_file_accuracy_100.txt", "r+", encoding="utf-8")
f300 = open("output_file_accuracy_100.txt", "r+", encoding="utf-8")
f100.write("The accuracy of this modes is: " + str(accuracy_for_100))
f10.write("The accuracy of this modes is: " + str(accuracy_for_10))
f300.write("The accuracy of this modes is: " + str(accuracy_for_300))
f100.close()
f10.close()
f300.close()


print("All the required actions in LR.py are completed!")






