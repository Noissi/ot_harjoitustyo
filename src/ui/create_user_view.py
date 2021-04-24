from PySide6.QtWidgets import *
from PySide6.QtGui import QImage, QPalette, QBrush
from PySide6.QtCore import QSize, QRect, Qt
from services.korttikube_service import korttikube_service as kks

class CreateUserView(QWidget):
    def __init__(self, handle_show_login_view=None):
        super().__init__()
        self._handle_show_login_view = handle_show_login_view
        self._username_entry = None
        self._password_entry = None
        
        self.left=10
        self.top=10
        self.width=1500
        self.height=1000
        
        self._username_line = QLineEdit()
        self._password_line = QLineEdit()
        self._unique_username = False
        
        self._initialise()  

    def _create_user(self):
        msg = QMessageBox()
        user = kks.create_user(self._username_line.text(), self._password_line.text())
        
        if not user:
            msg.setText('Käyttäjätunnus on jo käytössä')
            msg.exec_()
        else:
            msg.setText('Uusi käyttäjä luotu')
            msg.exec_()            
            app.quit()

    def _initialise(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        layout = QGridLayout()

        # Set background image
        image = QImage("img/login.jpg")
        image_scaled = image.scaled(QSize(self.width, self.height)) # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(image_scaled))                        
        self.setPalette(palette)

        # Set username label
        label_name = QLabel('<font size="3"> Käyttäjätunnus </font>')
        self._username_line.setPlaceholderText('Anna käyttäjätunnus')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self._username_line, 0, 1)

        # Set password label
        label_password = QLabel('<font size="3"> Salasana </font>')
        self._password_line.setPlaceholderText('Anna salasana')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self._password_line, 1, 1)

        btn_create = QPushButton('Luo uusi käyttäjä')
        btn_create.clicked.connect(self._create_user)
        layout.addWidget(btn_create, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 10)

        btn_back = QPushButton('Takaisin')
        btn_back.clicked.connect(self._handle_show_login_view)
        layout.addWidget(btn_back, 3, 0, 1, 2)
        layout.setRowMinimumHeight(1, 10)

        layout.setContentsMargins(600,400,600,400)
        self.setLayout(layout)

        self.setLayout(layout)