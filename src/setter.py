import sys
from imblearn.over_sampling import SMOTE

class Setter:
    def __init__(self):
        self.dataset = ''
        while True:
            self.dataset = input('Enter type of dataset (UCI/SMOTE/my): ')

            if self.dataset == 'UCI':
                self.dataset = '../breast_cancer_dataset.csv'
                break
            elif self.dataset == 'SMOTE':
                print('random')
                # random dataset creator
                break
            elif self.dataset == 'my':
                self.dataset = input('Enter path to the file (it must be in a proper format): ')
                # set path
                break

    def pick_algo(self):
        while True:
            self.algo = input('Enter algorithm for prediction: ')

            if self.algo != 'kNN' or self.algo != 'SVC' or self.algo != 'GaussianNB' or self.algo != 'RandomForest':
                break
