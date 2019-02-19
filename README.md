# Diagnosing breast tumor using the k-nearest neighbors algorithm

## Overview

Machine learning project based on Breast Cancer Wisconsin (Diagnostic) Data Set from UCI Machine Learning Repository

The main purpose of the program is to predict breast cancer based on features computed from a digitised image of a fine needle aspirate (FNA) of a breast mass. For the prediction the program uses the k-nearest neighbours algorithm (k-NN) and and data from the UCI Machine Learning Repository, specifically Breast Cancer Wisconsin (Diagnostic) Data Set.

## Usage
### Packages
Outside the Python’s standard library the applications uses packages `sklearn.neighbors`, `numpy` and `matplotlib`. The user interface is based on the `tkinter` package.

### Files
The whole application is consists of five files:
- **main.py** is used for tying the whole application together and running the program
- **app.py** provides the needed calculations for learning and predicting results
- **interface.py** contains functions needed for initializing the window and tabs for user interface
- **tab1.py** consists of functions that secure the first tab in the user interface
- **tab2.py** consists of functions that secure the second tab in the user interface

### Running the application
`python3 main.py`

### Sample run


## Credits
[UCI Machine Learning Repository: Breast Cancer Wisconsin (Diagnostic) Data Set](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))

## Author
Tomáš Chobola, 2019
