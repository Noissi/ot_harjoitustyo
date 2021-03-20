import sys
from PySide6.QtWidgets import QApplication, QPushButton, QTextBrowser
from ui.ui import UI
from ui.login_view import LoginView

def main():
    # Create the Qt Application
    app = QApplication(sys.argv)
    app.setApplicationName("KorttiKube")
    print("index")
    
    ui = UI()
    ui.start()
    
    # Run the main Qt loop
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
