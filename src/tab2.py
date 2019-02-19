from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math

# result of clicking the 'Plot' button
def clicked(x_axis, y_axis, app):
    x = app.data_columns.index(x_axis) # finds the index (right column) based on selected value
    y = app.data_columns.index(y_axis) 

    x_values_M = []
    y_values_M = []
    x_values_B = []
    y_values_B = []
    # inserts the coordinates of the data into the right arrays 
    for i in range(math.ceil(len(app.data_array) * 0.67)):
        if app.training_results_array[i] == 'M':
            x_values_M.append(app.data_array[i][x])
            y_values_M.append(app.data_array[i][y])
        else:
            x_values_B.append(app.data_array[i][x])
            y_values_B.append(app.data_array[i][y])

    # creating the plot
    plt.scatter(x_values_M, y_values_M, color = '#FF0000', label = 'malignant')
    plt.scatter(x_values_B, y_values_B, color = '#17D190', label = 'benign')

    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.legend(loc = 1)
    plt.show()

# sets the second tab, creates needed labels, option menus and button
def set_second_tab(tab2, app):
    data = ['radius', 'texture', 'perimeter', 'area', 'smoothness', 'compactness', 
            'concavity', 'concave points', 'symetry', 'fractal dimension']

    lbl1 = Label(tab2, text = 'X axis: ', bg = 'gray93')
    lbl1.grid(column = 0, row = 0, padx = 10, pady = 20)

    lbl2 = Label(tab2, text = 'Y axis: ', bg = 'gray93')
    lbl2.grid(column = 0, row = 1, padx = 10, pady = 5)

    variable1 = StringVar(tab2)
    variable1.set(data[0])
    menu1 = OptionMenu(tab2, variable1, *data)
    menu1.configure(width = 15)
    menu1.grid(column = 1, row = 0)

    variable2 = StringVar(tab2)
    variable2.set(data[1])
    menu2 = OptionMenu(tab2, variable2, *data)
    menu2.configure(width = 15)
    menu2.grid(column = 1, row = 1)

    s = ttk.Separator(tab2, orient = HORIZONTAL)
    s.grid(columnspan = 4, row = 2, sticky = "ew", pady = 10)

    btn1 = Button(tab2, text = 'Plot', command = lambda: clicked(variable1.get(), variable2.get(), app), highlightthickness = 0)
    btn1.grid(column = 2, row = 1, padx = 40)
    btn1.configure(width = 15)
