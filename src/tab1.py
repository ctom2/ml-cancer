from tkinter import *
from tkinter import ttk

# Checks if string is float or not.
def is_float(string):
    try:
        return float(string) # true if string is a number
    except ValueError: # string is not a number
        return False

# Result of clicking the 'Calculate' button.
def clicked(entries, lbl_result, app): # app is instance of App class from app.py
    # Checks if all entry fields contain data in the proper format.
    for i in range(len(entries)):
        if not is_float(entries[i].get()):
            lbl_result.configure(text = 'Value \'' + app.data_columns[i] + '\' is not the right type.', fg = 'red')
            app.input_set = False
            return

    # Predicts the result based on learned data.
    if app.predict(entries) == ['B']: # function predict() is from app.py
        lbl_result.configure(text = 'Cell is benign.', fg = 'RoyalBlue3')
    else:
        lbl_result.configure(text = 'Cell is malignant.', fg = 'RoyalBlue3')

# Sets the first tab, creates needed labels, text entries and button.
def set_first_tab(tab_control, tab1, app):
    entries = []

    lbl1 = Label(tab1, text = 'radius', bg = 'gray93')
    lbl1.grid(column = 0, row = 0)
    txt1 = Entry(tab1, width = 10)
    txt1.grid(column = 1, row = 0, padx = 9, pady = 5)
    entries.append(txt1)

    lbl2 = Label(tab1, text = 'texture', bg = 'gray93')
    lbl2.grid(column = 0, row = 1)
    txt2 = Entry(tab1, width = 10)
    txt2.grid(column = 1, row = 1, padx = 9, pady = 5)
    entries.append(txt2)

    lbl3 = Label(tab1, text = 'perimeter', bg = 'gray93')
    lbl3.grid(column = 0, row = 2)
    txt3 = Entry(tab1, width = 10)
    txt3.grid(column = 1, row = 2, padx = 9, pady = 5)
    entries.append(txt3)

    lbl4 = Label(tab1, text = 'area', bg = 'gray93')
    lbl4.grid(column = 0, row = 3)
    txt4 = Entry(tab1, width = 10)
    txt4.grid(column = 1, row = 3, padx = 9, pady = 5)
    entries.append(txt4)

    lbl5 = Label(tab1, text = 'smoothness', bg = 'gray93')
    lbl5.grid(column = 0, row = 4)
    txt5 = Entry(tab1, width = 10)
    txt5.grid(column = 1, row = 4, padx = 9, pady = 5)
    entries.append(txt5)

    lbl6 = Label(tab1, text = 'compactness', bg = 'gray93')
    lbl6.grid(column = 2, row = 0)
    txt6 = Entry(tab1, width = 10)
    txt6.grid(column = 3, row = 0, padx = 9, pady = 5)
    entries.append(txt6)

    lbl7 = Label(tab1, text = 'concavity', bg = 'gray93')
    lbl7.grid(column = 2, row = 1)
    txt7 = Entry(tab1, width = 10)
    txt7.grid(column = 3, row = 1, padx = 9, pady = 5)
    entries.append(txt7)

    lbl8 = Label(tab1, text = 'concave points', bg = 'gray93')
    lbl8.grid(column = 2, row = 2)
    txt8 = Entry(tab1, width = 10)
    txt8.grid(column = 3, row = 2, padx = 9, pady = 5)
    entries.append(txt8)

    lbl9 = Label(tab1, text = 'symetry', bg = 'gray93')
    lbl9.grid(column = 2, row = 3)
    txt9 = Entry(tab1, width = 10)
    txt9.grid(column = 3, row = 3, padx = 9, pady = 5)
    entries.append(txt9)

    lbl10 = Label(tab1, text = 'fractal dimension', bg = 'gray93')
    lbl10.grid(column = 2, row = 4)
    txt10 = Entry(tab1, width = 10)
    txt10.grid(column = 3, row = 4, padx = 9, pady = 5)
    entries.append(txt10)

    s = ttk.Separator(tab1, orient = HORIZONTAL)
    s.grid(columnspan = 4, row = 5, sticky = "ew", pady = 10)

    lbl_result = Label(tab1, text = 'result', width = 44, height = 2, fg = 'grey80')
    lbl_result.grid(columnspan = 4, row = 6)

    btn = Button(tab1, text = 'Calculate', command = lambda: clicked(entries, lbl_result, app), highlightthickness = 0)
    btn.grid(column = 3, row = 7, padx = 10, pady = 10)

    tab_control.pack(expand = 1, fill = 'both')