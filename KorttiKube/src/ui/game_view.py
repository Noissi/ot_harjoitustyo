from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QVBoxLayout, QHBoxLayout, QFormLayout

class GameView(QMainWindow):
    def __init__(self, handle_show_main_view=None, handle_show_card_view=None):
        super().__init__()
        self._handle_show_main_view = handle_show_main_view
        self._handle_show_card_view = handle_show_card_view
        
        self.left=10
        self.top=10
        self.width=1500
        self.height=1000
        
        self._initialise()       
        
    def _initialise(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        outer_layout = QVBoxLayout()
        top_layout = QFormLayout()
        game_layout = QVBoxLayout()
        
        top_layout.addRow("Text:", QLineEdit())
        
        
        label_search = QLabel('<font size="4"> Search </font>')
        lineEdit_search = QLineEdit()
        lineEdit_search.setPlaceholderText('Haku...')
        top_layout.addWidget(label_search)        
        top_layout.addWidget(lineEdit_search)
        
        button_skip = QPushButton('Kortti')
        button_skip.clicked.connect(self._handle_show_card_view)
        game_layout.addWidget(button_skip)
        
        outer_layout.addLayout(top_layout)
        outer_layout.addLayout(game_layout)
        self.setLayout(outer_layout)
        
        self.setCentralWidget(QWidget(self))
        self.centralWidget().setLayout(outer_layout)
        
        print('game')

