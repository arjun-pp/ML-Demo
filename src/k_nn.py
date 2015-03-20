# -*- coding: utf-8 -*-

import csv
import random
import constants
import math

def load_data_set(training_set = [], test_set = [], split):
    with open(constants.IRIS_DATA, 'rb') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            training_set.append(dataset[x])
	        else:
	            test_set.append(dataset[x])
             
             
def euclidean_distance(instance1, instance2, length):
    distance = 0
    for i in range(length):
        distance += pow(instance1[i] - instance2[i], 2) 
    return math.sqrt(distance)

def get_neighbors(training_set, test_instance, k):
    distances = []
    test_length = len(test_instance)
    for trset in training_set:
        dist = euclidean_distance(test_instance, trset, test_length)
        distances.append(trset, distt)
        
    distances.sort(key = operator.itemgetter(1) )
    neighbors = []
    for i in range(k):
        neighbors.append(distances[i][0])
        
    return neighbors
        
    
        
    
