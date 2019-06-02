import numpy as np
import math

# Reads data from mentioned dataset, saves the result values and deletes first two columns
# (these are not required for making predictions since they only identify the entry)
def get_data(dataset):
    data_array = np.genfromtxt(dataset, delimiter=',', 
        dtype='float64, U1, float64, float64, float64, float64, float64, float64, float64, float64, float64, float64')
    tmp = np.array([list(elem) for elem in data_array])

    tmp = np.delete(tmp, 0, 1)
    results_array = tmp[:,0]
    tmp = np.delete(tmp, 0, 1)
    data_array = tmp.astype(np.float)
    
    return data_array, results_array

# Splits data into two datasets, first part is intended for learning and second part is intended for validation
# and choosing the best k-value used in following functions.
def split_data(data_array, results_array, training_size = 0.67):
    training_data_array = [] # training data (first 67% of the original dataset) = first part
    training_results_array = [] # results of the training data
    validation_data_array = [] # validation data (remaining 33% of the original dataset) = second part
    validation_results_array = [] # results of the validation data

    training_length = math.ceil(len(data_array) * training_size)
    for i in range(training_length):
        training_data_array.append(data_array[i])
        training_results_array.append(results_array[i])

    for i in range(len(data_array) - training_length):
        validation_data_array.append(data_array[i + training_length])
        validation_results_array.append(results_array[i + training_length])

    training_data_array = np.array(training_data_array)
    training_results_array = np.array(training_results_array)
    validation_data_array = np.array(validation_data_array)
    validation_results_array = np.array(validation_results_array)

    return training_data_array, training_results_array, validation_data_array, validation_results_array
