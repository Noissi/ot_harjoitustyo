from PySide6.QtWidgets import *
from PySide6.QtGui import QImage, QPalette, QBrush
from PySide6.QtCore import QSize, QRect, Qt
from ui.window import Window
from services.korttikube_service import korttikube_service as kks
from config import IMAGES_FILE_PATH

class LoginView(QWidget):
    """ Class responsible for login ui.

    Attributes:
        handle_show_create_user_view: A method to open a -create user- ui.
        handle_show_main_view: A method to open a -main- ui.
        handle_end: A method to exit the programme.
    """

    def __init__(self, handle_show_create_user_view, handle_show_main_view, handle_end):
        """ Class constructor. Creates a new login ui.
        
        Args:
	        handle_show_create_user_view: A method to open a -create user- ui.
            handle_show_main_view: A method to open a -main- ui.
            handle_end: A method to exit the programme.
            left, top, width, height: Page geometry values.
        """

        super().__init__()
        self._handle_show_create_user_view = handle_show_create_user_view
        self._handle_show_main_view = handle_show_main_view
        self._handle_end = handle_end

        self.left   = 10
        self.top    = 10
        self.width  = 1500
        self.height = 1000

        self._initialise()

    def _check_password(self):
        """ Checks if the given username and password combo exists. If exist,
            logs the user in and opens the main view. If not, gives an error message.
        """

        msg = QMessageBox()
        login = kks.login(self.lineEdit_username.text(), self.lineEdit_password.text())
        if login:
            self._handle_show_main_view()
        else:
            msg.setText('Väärä käyttäjätunnus tai salasana')
            msg.exec_()

    def _initialise(self):
        """ Draws the login page.
        """

        self.setGeometry(self.left, self.top, self.width, self.height)
        layout = QGridLayout()

        # Set background image
        image = QImage(IMAGES_FILE_PATH + "login.jpg")
        image_scaled = image.scaled(QSize(self.width, self.height)) # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(image_scaled))                        
        self.setPalette(palette)

        # Set username label
        label_name = QLabel('<font size="3"> Käyttäjätunnus </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Anna käyttäjätunnus')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        # Set password label
        label_password = QLabel('<font size="3"> Salasana </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Anna salasana')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Kirjaudu')
        button_login.clicked.connect(self._check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 10)

        button_create = QPushButton('Luo uusi käyttäjä')
        button_create.clicked.connect(self._handle_show_create_user_view)
        layout.addWidget(button_create, 3, 0, 1, 2)
        layout.setRowMinimumHeight(2, 10)

        # Draw close button
        button_close = QPushButton('Lopeta')
        button_close.clicked.connect(self._handle_end)
        layout.addWidget(button_close, 4, 0, 1, 2)
        layout.setRowMinimumHeight(1, 10)

        layout.setContentsMargins(600,400,600,400)
        self.setLayout(layout)