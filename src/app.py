from knn import kNN
from data_operator import *
import random

# Class App contains all functions needed for the learning based on the values from csv file and calculating the predictions.
class App:
    # Class constructor
    def __init__(self):
        # Definition of names of the parameters that are used for computation. The names are later
        # used in initialization of the user interface.
        self.data_columns = ['radius', 'texture', 'perimeter', 'area', 'smoothness', 'compactness', 
                             'concavity', 'concave points', 'symetry', 'fractal dimension']

        # Reads data and formats it into array that is required for training and making predictions.
        # Later the arrays are devided into two parts, one for training and second one for validating.
        self.data, self.results = get_data('../breast_cancer_dataset.csv')
        self.training_data, self.training_results, self.validation_data, self.validation_results = split_data(self.data, self.results)

        # Normalization of the dataset and saving the means and standard deviation values for later
        self.training_data, self.means, self.stdevs = normalize_training(self.training_data)
        self.validation_data = normalize(self.validation_data, self.means, self.stdevs)

        # Creates instance of the kNN class that operates with the classifier.
        self.knn = kNN(self.training_data, self.training_results, self.validation_data, self.validation_results)
        self.knn.train_on_values()

    # Predicts the result of entered data.
    def predict(self, entries):
        # Creating the array for classifier that is used for making predictions.
        data = []
        for i in range(len(entries)):
            data.append(entries[i].get())

        data = np.array(data)
        data = data.reshape(1, -1)
        data = data.astype(np.float64)

        data = normalize(data, self.means, self.stdevs)

        return self.knn.predict(data)