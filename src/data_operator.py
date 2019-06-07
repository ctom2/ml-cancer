import statistics
from sklearn import preprocessing
import numpy as np
import math

# Reads data from mentioned dataset, saves the result values and deletes first two columns
# (these are not required for making predictions since they only identify the entry)
def get_data(dataset):
    data = np.genfromtxt(dataset, delimiter=',', 
        dtype='float64, U1, float64, float64, float64, float64, float64, float64, float64, float64, float64, float64')
    tmp = np.array([list(elem) for elem in data])

    tmp = np.delete(tmp, 0, 1)
    results = tmp[:,0]
    tmp = np.delete(tmp, 0, 1)
    data = tmp.astype(np.float)
    
    return data, results

# Splits data into two datasets, first part is intended for learning and second part is intended for validation
# and choosing the best k value used in following functions.
def split_data(data, results, training_size = 0.67):
    training_data = [] # training data (first 67% of the original dataset) = first part
    training_results = [] # results of the training data
    validation_data = [] # validation data (remaining 33% of the original dataset) = second part
    validation_results = [] # results of the validation data

    training_length = math.ceil(len(data) * training_size)
    for i in range(training_length):
        training_data.append(data[i])
        training_results.append(results[i])

    for i in range(len(data) - training_length):
        validation_data.append(data[i + training_length])
        validation_results.append(results[i + training_length])

    training_data = np.array(training_data)
    training_results = np.array(training_results)
    validation_data = np.array(validation_data)
    validation_results = np.array(validation_results)

    return training_data, training_results, validation_data, validation_results

# Normalization for the training data and saving the means and standard deviation values for
# normalizing the validation dataset and input entries.
def normalize_training(data):
    means = np.sum(data, axis=0)/len(data)
    stdevs = []
    for i in range(len(data)):
        stdevs.append(statistics.stdev(data[i]))

    data = preprocessing.normalize(data)

    return data, means, stdevs

# Normalizing the validation dataset and input entries.
def normalize(data, means, stdevs):
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = (data[i][j] - means[j])/stdevs[j]
    
    return data