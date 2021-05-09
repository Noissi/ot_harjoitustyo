import sys
import os
from PySide6.QtWidgets import *
from initialise_database import initialise_database
from ui.ui import UI

def main():
    # Build the database if it does not exist
    initialise_database()

    # Create the imgcards and imguser folders if they do not exist
    if not os.path.exists('imgcards'):
        os.makedirs('imgcards')
    if not os.path.exists('imguser'):
        os.makedirs('imguser')

    # Create the Qt Application
    app = QApplication(sys.argv)
    app.setApplicationName("KorttiKube")

    ui = UI()
    ui.start()
    ui.current_view.show()

    # Run the main Qt loop
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
