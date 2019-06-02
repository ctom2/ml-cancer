import sys
from data_operator import get_data, split_data

# Class Setter is responsible for getting the user input about the dataset and algorithm
# that will be later used in making predictions.
class Setter:
    # Constructor reads the type of the dataset that will be used for learning.
    def __init__(self):
        self.dataset = ''
        # Loop breaks when user inputs the right type of dataset.
        while True:
            self.dataset = input('Enter type of dataset (UCI/random): ')

            if self.dataset == 'UCI':
                self.dataset = '../breast_cancer_dataset.csv'
                break
            elif self.dataset == 'SMOTE':
                self.over_sample()
                self.dataset = '../breast_cancer_dataset_smote.csv'
                break

    # Method for reading the type of algorithm. The loop works the same way as the previous method.
    def pick_algo(self):
        while True:
            self.algo = input('Enter algorithm for prediction: ')
            if self.algo != 'kNN' or self.algo != 'SVC' or self.algo != 'GaussianNB' or self.algo != 'RandomForest':
                break

    def over_sample(self):
        # Reads data and formats it into array that is required for oversampling.
        self.data_array, self.results_array = get_data('../breast_cancer_dataset.csv')
        self.training_data_array, self.training_results_array, self.validation_data_array, self.validation_results_array = split_data(self.data_array, self.results_array)
   
        # generate new dataset based on kNN and save it into new file

        # f = open('../breast_cancer_dataset_smote.csv','w+')
        # for i in range(len(smote_X))
        #     f.write(smote_X[i])
        # f.close()