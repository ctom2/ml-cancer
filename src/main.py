from interface import initialize_interface
from app import App
from setter import Setter

# Function main creates an instance of the App class and calls its contructor (reads the data from csv file
# and learns from them). After that the user interface is initialized.
def main():
    # Initialization of the application with settings passed as parameter.
    app = App(Setter())
    # Creating the main user interface of the application.
    initialize_interface(app)

if __name__ == "__main__":
    main()