from sklearn.neighbors import KNeighborsClassifier

class kNN:
    def __init__(self, training_data_array, training_results_array, validation_data_array, validation_results_array):
        self.training_data_array = training_data_array
        self.training_results_array = training_results_array
        self.validation_data_array = validation_data_array
        self.validation_results_array = validation_results_array

    # finds the best k-value (gives the most precise results) from range [1,30]
    def best_k(self):
        accuracy = 0
        k = 1

        for i in range(1, 36):
            self.classifier = KNeighborsClassifier(n_neighbors = i)
            self.classifier.fit(self.training_data_array, self.training_results_array)
            if self.classifier.score(self.validation_data_array, self.validation_results_array) > accuracy:
                accuracy = self.classifier.score(self.validation_data_array, self.validation_results_array)
                k = i
                print(k, accuracy)

        return k

    # initializes the self.classifier and fits the training data
    def train_on_values(self):
        k = self.best_k()
        self.main_classifier = KNeighborsClassifier(n_neighbors = k)
        self.main_classifier.fit(self.training_data_array, self.training_results_array)