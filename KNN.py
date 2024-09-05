# euclidean distance global function

import numpy as np
from collections import Counter

def euclidean_distance(x1, x2):
    distance = np.sqrt(np.sum(np.sum(x1-x2)**2))
    return distance
    


class KNN:
    def __innit__(self, k=3):
        self.k = K 
        
    def fit(self, X, Y):
        self.x_train = X
        self.y_train = Y
            
        
    def predict(self, X):
        
        #predictions variable will collect all the numbers predicted in _predict and store it 
        predictions = [self._predict(x) for x in X]
        return predictions
        
    # helper function to a single value
    # the little x reepresents a single data point that will be used in the knn classifiers and then be passed on into a list, which will be the bigger X
    def _predict(self, x):
        #compute the distances
        
        #for each data point in the data set, send it to the euclidean distance function, get the distance between x and the x_train training set
        # store that information in the arrray distances
        distances = [euclidean_distance(x, x_train) for x_train in self.x_train]
        
        #get the closest k
        # what argsort does is that after each data point has been sorted, it finds the indices of the closest three neighbors
        np.arg
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train_train_train[i] for i in k_indices]
        
        # majority voye
        # finds the most common 
        most_common = Counter(k_nearest_labels).most_common()
        return most_common
        
        