from app import *
from tab1 import *
from tab2 import *

# Defines the window properties.
def set_window(window, title, size):
    window.title(title)
    window.geometry(size)

# Creates the tabs.
def set_tabs(tab_control):
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab1, text = 'Predict')
    tab_control.add(tab2, text = 'Scatter Plot')
    
    return tab1, tab2

# Initializes the interface by creating the main window and the two lists
def initialize_interface(app):
    window = Tk()
    tab_control = ttk.Notebook(window)
    set_window(window, 'Breast Cancer Prediction', '500x500')
    tab1, tab2 = set_tabs(tab_control)
    set_first_tab(tab_control, tab1, app) # initializes the first tab
    set_second_tab(tab2, app) # initializes the second tab

    window.mainloop()