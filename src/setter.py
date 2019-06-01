import sys

class Setter:
    def __init__(self):
        self.dataset = ''
        while True:
            self.dataset = input('Enter type of dataset (UCI/random/my): ')

            if self.dataset == 'UCI':
                self.dataset = '../breast_cancer_dataset.csv'
                break
            elif self.dataset == 'random':
                print('random')
                # random dataset creator
                break
            elif self.dataset == 'my':
                print('my')
                # set path
                break

        while True:
            self.algo = input('Enter algorithm for prediction: ')

            if self.algo == 'kNN':
                break
