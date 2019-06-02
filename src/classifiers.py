from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

class Classifiers:
    def __init__(self, training_data_array, training_results_array, validation_data_array, validation_results_array):
            self.training_data_array = training_data_array
            self.training_results_array = training_results_array
            self.validation_data_array = validation_data_array
            self.validation_results_array = validation_results_array

    # finds the best k-value (gives the most precise results) from range [1,30] for kNN
    def best_k(self):
        accuracy = 0
        k = 1

        for i in range(1, 36):
            self.classifier = KNeighborsClassifier(n_neighbors = i)
            self.classifier.fit(self.training_data_array, self.training_results_array)
            if self.classifier.score(self.validation_data_array, self.validation_results_array) > accuracy:
                accuracy = self.classifier.score(self.validation_data_array, self.validation_results_array)
                k = i

        return k

    # initializes the kNN classifier and fits the training data
    def train_on_values_knn(self):
        k = self.best_k()
        self.knn_classifier = KNeighborsClassifier(n_neighbors = k)
        self.knn_classifier.fit(self.training_data_array, self.training_results_array)

    # initializes the GaussianNB classifier and fits the training data
    def train_on_values_gauss(self):
        self.gauss_classifier = GaussianNB()
        self.gauss_classifier.fit(self.training_data_array, self.training_results_array)

    # initializes the SVC classifier and fits the training data
    def train_on_values_svc(self):
        self.svc_classifier = SVC(gamma='auto')
        self.svc_classifier.fit(self.training_data_array, self.training_results_array)

    # initializes the RandomForest classifier and fits the training data
    def train_on_values_forest(self):
        self.forest_classifier = RandomForestClassifier(n_estimators=100)
        self.forest_classifier.fit(self.training_data_array, self.training_results_array)