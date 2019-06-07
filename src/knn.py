from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix



# Class contains methods for initializing the classifier and training in on training data.
class kNN:
    # Constructor passes data into arrays.
    def __init__(self, training_data, training_results, validation_data, validation_results):
        self.training_data = training_data
        self.training_results = training_results
        self.validation_data = validation_data
        self.validation_results = validation_results

    # Finds the best k-value (gives the most precise results) from range [1,50] for kNN.
    def best_k(self):
        accuracy = 0
        k = 1

        for i in range(1, 50):
            self.classifier = KNeighborsClassifier(n_neighbors = i)
            self.classifier.fit(self.training_data, self.training_results)
            if self.classifier.score(self.validation_data, self.validation_results) > accuracy:
                accuracy = self.classifier.score(self.validation_data, self.validation_results)
                k = i
                
        return k

    # initializes the kNN classifier and fits the training data
    def train_on_values(self):
        k = self.best_k()
        self.knn_classifier = KNeighborsClassifier(n_neighbors = k)
        self.knn_classifier.fit(self.training_data, self.training_results)

    def predict(self, data):
        return self.knn_classifier.predict(data)