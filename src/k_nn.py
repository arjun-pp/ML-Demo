# -*- coding: utf-8 -*-

import csv
import random
import constants
import math
import operator

def load_data_set( split, filename, training_set = [], test_set = []):
    with open(filename, 'rb') as csvfile:
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
    distance = 0.0
    for i in range(length):
        distance += pow(instance1[i] - instance2[i], 2) 
    return math.sqrt(distance)

def get_neighbors(training_set, test_instance, k):
    distances = []
    test_length = len(test_instance) - 1
    for trset in training_set:
        dist = euclidean_distance(test_instance, trset, test_length)
        distances.append((trset, dist))
        
    distances.sort(key = operator.itemgetter(1) )
    neighbors = []
    for i in range(k):
        neighbors.append(distances[i][0])
        
    return neighbors
    
def get_class(neighbors):
    class_votes = {}
    for i in range(len(neighbors)):
        response = neighbors[i][-1]
        if response in class_votes:
            class_votes[response] += 1
        else:
            class_votes[response] = 1
            
    sorted_votes = sorted(class_votes.iteritems(), key = operator.itemgetter(1), reverse = True)
    return sorted_votes[0][0]
    
def hash_func(x1, x2):
    return 0.5*(x1 +x2)*(x1 + x2 + 1) + x2;
    
def get_accuracy(test_set, predictions):
	correct = 0
	for x in range(len(test_set)):
		if test_set[x][-1] == predictions[x]:
			correct += 1
	return round((correct/float(len(test_set)) * 100.0),2)
    
#    def main():
#    	# prepare data
#    	
#    	
#    main()
                
