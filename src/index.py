import sys
from PySide6.QtWidgets import QApplication
from initialise_database import initialise_database
from ui.ui import UI

def main():
    # Build database if it does not exist
    initialise_database()

    # Create the Qt Application
    app = QApplication(sys.argv)
    app.setApplicationName("KorttiKube")
    print("index")

    ui = UI()
    ui.start()
    ui.current_view.show()

    # Run the main Qt loop
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
