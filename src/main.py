from interface import *

# Function main creates an instance of the App class and calls its contructor (reads the data from csv file
# and learns from them). After that the user interface is initialized.

def main():
    app = App()
    initialize_interface(app)

if __name__ == "__main__":
    main()