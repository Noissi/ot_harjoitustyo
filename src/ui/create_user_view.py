from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox


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
        
        self._initialise()  

    def check_password(self):
        msg = QMessageBox()
        
        if self.lineEdit_username.text() == 'Usernmae' and self.lineEdit_password.text() == '000':
            msg.setText('Success')
            msg.exec_()
            app.quit()
        else:
            msg.setText('Incorrect Password')
            msg.exec_()        
        
    def _initialise(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        layout = QGridLayout()

        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please enter your password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_create = QPushButton('Create')
        button_create.clicked.connect(self.check_password)
        layout.addWidget(button_create, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)
        
        button_skip = QPushButton('Skip')
        button_skip.clicked.connect(self._handle_show_login_view)
        layout.addWidget(button_skip, 3, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)
