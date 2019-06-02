from classifiers import Classifiers
from data_operator import *
import random
import setter

# Class App contains all functions needed for the learning based on the values from csv file and calculating the predictions.
class App:
    # Class constructor
    def __init__(self, setter):
        # Definition of names of the parameters that are used for computation. The names are later
        # used in initialization of the user interface.
        self.data_columns = ['radius', 'texture', 'perimeter', 'area', 'smoothness', 'compactness', 
                             'concavity', 'concave points', 'symetry', 'fractal dimension']

        # Reads data and formats it into array that is required for training and making predictions.
        self.data_array, self.results_array = get_data(setter.dataset)
        self.training_data_array, self.training_results_array, self.validation_data_array, self.validation_results_array = split_data(self.data_array, self.results_array)

        # Trains every classifier on the datasets and prints the precision score of each classifier.
        # Based on this information the user can pick one of the classifiers for the application.
        self.train_on_data()

        # Using the Setter class method user chooses which classifier he/she wants to use.
        setter.pick_algo()

        # "Switch" for setting the main classifier based on the user's decision. This classifier is
        # later used for making predictions.
        if setter.algo == 'kNN':
            self.main_classifier = self.classifiers.knn_classifier
        elif setter.algo == 'SVC':
            self.main_classifier = self.classifiers.svc_classifier
        elif setter.algo == 'GaussianNB':
            self.main_classifier = self.classifiers.gauss_classifier
        elif setter.algo == 'RandomForest':
            self.main_classifier = self.classifiers.forest_classifier

    # Trains on data passed by the previous methods and initializes the classifiers. Then it produces
    # scores based on validation datasets.
    def train_on_data(self):
        self.classifiers = Classifiers(self.training_data_array, self.training_results_array, self.validation_data_array, self.validation_results_array)
        self.classifiers.train_on_values_knn()
        self.classifiers.train_on_values_svc()
        self.classifiers.train_on_values_gauss()
        self.classifiers.train_on_values_forest()
        print('--------')
        print('kNN\naccuracy score =', self.classifiers.knn_classifier.score(self.validation_data_array, self.validation_results_array), '\n--------')
        print('SVC\naccuracy score =', self.classifiers.svc_classifier.score(self.validation_data_array, self.validation_results_array), '\n--------')
        print('GaussianNB\naccuracy score =', self.classifiers.gauss_classifier.score(self.validation_data_array, self.validation_results_array), '\n--------')
        print('RandomForest\naccuracy score =', self.classifiers.forest_classifier.score(self.validation_data_array, self.validation_results_array), '\n--------')

    # Predicts the result of entered data.
    def predict(self, entries):
        # Creating the array for classifier that is used for making predictions.
        data = []
        for i in range(len(entries)):
            data.append(entries[i].get())

        data = np.array(data)
        data = data.reshape(1, -1)
        data = data.astype(np.float64)

        return self.main_classifier.predict(data)