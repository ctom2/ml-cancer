import numpy as np
import math
from sklearn.neighbors import KNeighborsClassifier
import random
import copy

# Class App contains all functions needed for the learning based on the values from csv file and calculating the predictions

class App:
    # class constructor
    def __init__(self):
        self.get_data()
        self.split_data()
        self.train_on_values()

    # reads data from dataset, saves the result values and deletes first two columns
    def get_data(self):
        self.data_array = np.genfromtxt('../breast_cancer_dataset.csv', delimiter=',', 
            dtype='float64, U1, float64, float64, float64, float64, float64, float64, float64, float64, float64, float64')
        tmp = np.array([list(elem) for elem in self.data_array])

        tmp = np.delete(tmp, 0, 1)
        self.results_array = tmp[:,0]
        tmp = np.delete(tmp, 0, 1)
        self.data_array = tmp.astype(np.float)

    # splits data into two datasets, first part is intended for learning and second part is intended for validation
    # and choosing the best k-value used in following functions
    def split_data(self, training_size = 0.67):
        training_length = math.ceil(len(self.data_array) * training_size)
        for i in range(training_length):
            self.training_data_array.append(self.data_array[i])
            self.training_results_array.append(self.results_array[i])

        for i in range(len(self.data_array) - training_length):
            self.validation_data_array.append(self.data_array[i + training_length])
            self.validation_results_array.append(self.results_array[i + training_length])

        self.training_data_array = np.array(self.training_data_array)
        self.training_results_array = np.array(self.training_results_array)
        self.validation_data_array = np.array(self.validation_data_array)
        self.validation_results_array = np.array(self.validation_results_array)

    # finds the best k-value (gives the most precise results) from range [1,30]
    def bek(self):
        accuracy = 0
        k = 1

        for i in range(1, 36):
            classifier = KNeighborsClassifier(n_neighbors = i)
            classifier.fit(self.training_data_array, self.training_results_array)
            if classifier.score(self.validation_data_array, self.validation_results_array) > accuracy:
                accuracy = classifier.score(self.validation_data_array, self.validation_results_array)
                k = i
                print(k, accuracy)

        return k

    # initializes the classifier and fits the training data
    def train_on_values(self):
        k = self.bek()
        self.main_classifier = KNeighborsClassifier(n_neighbors = k)
        self.main_classifier.fit(self.training_data_array, self.training_results_array)

    # predicts the result of entered data
    def predict(self, entries):
        data = []
        for i in range(len(entries)):
            data.append(entries[i].get())

        data = np.array(data)
        data = data.reshape(1, -1)
        data = data.astype(np.float64)

        return self.main_classifier.predict(data)

    # CLASS VARIABLES
    main_classifier = None      # used for training and predicting
    data_array = []             # used for storing the data from csv file and creating graphs
    results_array = []          # array with results from csv file (second column of the original file)
    training_data_array = []    # training data (first 67% of the original dataset) = first part
    training_results_array = []     # results of the training data 
    validation_data_array = []      # validation data (remaining 33% of the original dataset) = second part
    validation_results_array = []   # results of the validation data
    data_columns = ['radius', 'texture', 'perimeter', 'area', 'smoothness', 'compactness', 
                    'concavity', 'concave points', 'symetry', 'fractal dimension']
                                    # names of the columns from the original file