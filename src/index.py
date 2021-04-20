import sys
from initialise_database import initialise_database
from PySide6.QtWidgets import QApplication, QPushButton, QTextBrowser, QWidget
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
    
    #widget = QWidget(ui.current_view)
    #outer_layout = ui.current_view.get_outer_layout()
    #widget.setLayout(outer_layout)
    #ui.current_view.setCentralWidget(widget)
    #ui.current_view.centralWidget().setLayout(outer_layout)
    ui.current_view.show()
    
    # Run the main Qt loop
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
