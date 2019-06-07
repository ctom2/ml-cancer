# Diagnosing breast cancer using machine learning algorithms

## Overview

*I used this project to gain experience in Python and try out different machine learning algorithms on popular dataset.*

Machine learning project based on Breast Cancer Wisconsin (Diagnostic) Data Set from UCI Machine Learning Repository.

The main purpose of the program is to predict breast cancer based on features computed from a digitised image of a fine needle aspirate (FNA) of a breast mass. For the prediction the program uses the k-nearest neighbours algorithm (k-NN) and data from the dataset mentioned above.

The analysis and comparison is included in the `Jupyter` notebook `ml-cancer.ipynb`.

## Usage
### Packages
Outside the Python’s standard library the applications uses packages `sklearn.neighbors`, `numpy` and `matplotlib`. The user interface is based on the `tkinter` package.

### Files
The whole application is consists of five files:
- **main.py** is used for tying the whole application together and running the program
- **app.py** provides the needed operations for learning and predicting results
- **data_operator.py** provides functions for reading data, splitting data and normalizing dataset
- **knn.py** includes class with functions related to the kNN algorithm
- **interface.py** contains functions needed for initializing the window and tabs for user interface
- **tab1.py** consists of functions that secure the first tab in the user interface
- **tab2.py** consists of functions that secure the second tab in the user interface

### Running the application
`python3 main.py`

### Sample run
![](/images/screenshot1.png?raw=true "Sample of the first tab")
![](/images/screenshot2.png?raw=true "Sample of the second tab")

## Credits
[UCI Machine Learning Repository: Breast Cancer Wisconsin (Diagnostic) Data Set](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))

## Author
Tomáš Chobola, 2019
