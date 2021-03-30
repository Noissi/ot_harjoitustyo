from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from ui.window import Window
from entities.card_creature import Creature

from services.korttikube_service import korttikube_service as kks

class CubeView(Window):
    def __init__(self, handle_show_main_view=None, handle_show_card_view=None):
        super().__init__()
        self._handle_show_main_view = handle_show_main_view
        self._handle_show_card_view = handle_show_card_view
        
        self.left=10
        self.top=10
        self.width=1500
        self.height=1000        
        
        self._outer_layout = self.get_outer_layout()
        self._collection_layout = QFormLayout()
        self._bottom_layout = QHBoxLayout()
        
        self._card = Creature('Teemu Kerppu')
        
        self._initialise()
        
    def _initialise(self):        
        
        # Set background image
        image = QImage("img/card.jpg")
        image_scaled = image.scaled(QSize(self.width, self.height)) # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(image_scaled))                        
        self.setPalette(palette)
        
        # Set layouts
        left2_layout = QStackedLayout()     
        
        # Collection layout
        cards = kks.get_cards_in_cube(1)
        for card in cards:
        	# Print card
            card_label = QLabel()
            card_label.setText(self._card.get_name() + " : " + self._card.get_maintype() + " : " + self._card.get_card_colour())
            card_label.setStyleSheet("color: white;")
            self._collection_layout.addWidget(card_label) 
           
        
        # Bottom layout
        btn_card = QPushButton('Kortti')
        btn_card.clicked.connect(lambda: self._handle_show_card_view(self._card))
        self._bottom_layout.addWidget(btn_card)
        
        btn_back = QPushButton('Takaisin peleihin')
        btn_back.clicked.connect(self._handle_show_main_view)
        self._bottom_layout.addWidget(btn_back)
        
        
        self._outer_layout.addLayout(self._collection_layout, 1, 0)
        self._outer_layout.addLayout(self._bottom_layout, 5, 0)
        
        self.setLayout(self._outer_layout)
        
        
        print('cube')

