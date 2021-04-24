from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from ui.window import Window
from entities.card_creature import Creature
from services.korttikube_service import korttikube_service as kks
from config import CARD_RATIO

class CubeView(Window):
    def __init__(self, handle_show_main_view=None, 
                 handle_show_card_view=None, handle_show_edit_card_view=None):
        super().__init__()
        self._handle_show_main_view = handle_show_main_view
        self._handle_show_card_view = handle_show_card_view
        self._handle_show_edit_card_view = handle_show_edit_card_view
        
        self.left=10
        self.top=10
        self.width=1500
        self.height=1000        
        
        self._outer_layout = self.get_outer_layout()
        self._upper_layout = QHBoxLayout()
        #self._collection_layout = QGridLayout()
        self._bottom_layout = QHBoxLayout()
        
        self._scroll_layout = QGridLayout()
        self._scrollwidget = QWidget()
        #self._scrollwidget.setLayout(self._collection_layout)
        self._scrollwidget.setLayout(self._scroll_layout)
        self._scroll = QScrollArea()
        self._scroll.setWidgetResizable(True)  # Set to make the inner widget resize with scroll area
        self._scroll.setWidget(self._scrollwidget)
        self._initialise()
        
    def _set_upper_layout(self):
        # Upper layout
        btn_new = QPushButton('Uusi kortti')        
        btn_new.setMaximumWidth(100)
        btn_new.clicked.connect(lambda: self._handle_show_edit_card_view(True))
        self._upper_layout.addWidget(btn_new)
        
    def _set_collection_layout(self):
        # Collection layout
        cards = kks.get_cards_in_cube()
        print(cards)
        row = 0
        col = 0
        # Print cards in a 6x? grid 
        for card in cards:
            btn_card = QPushButton("\n      " + card[1] + \
                                   "\n\n\n\n\n\n\n\n      " + card[4] + " - " + card[7] + \
                                   "\n      " + card[12] + \
                                   "\n      " + card[13])
            card_width = 200
            btn_card.setMinimumSize(card_width, card_width * CARD_RATIO)
            btn_card.setMaximumSize(card_width, card_width * CARD_RATIO)
            card_frame_image = kks.set_card_frame(card)
            hover_image = "img/bluecard.png"
            # changing font and size of text
            btn_card.setFont(QFont('Times', 10))
            btn_card.setStyleSheet("QPushButton{border-image: url("+card_frame_image+")}"
                                   "QPushButton:hover{color: red}"
                                   "QPushButton{text-align: top left}")
            btn_card.clicked.connect(lambda checked=False, a=card: self._handle_show_card_view(a))
            #self._collection_layout.addWidget(btn_card, row, col)
            self._scroll_layout.addWidget(btn_card, row, col)
            col += 1
            if col > 5:
                col = 0
                row += 1
            
    def _set_bottom_layout(self):
        # Bottom layout
        btn_back = QPushButton('Takaisin etusivulle')
        btn_back.clicked.connect(self._handle_show_main_view)
        self._bottom_layout.addWidget(btn_back)
        
    def _initialise(self):        
        
        # Set background image
        image = QImage("img/mtg_puu.jpg")
        image_scaled = image.scaled(QSize(self.width, self.height)) # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(image_scaled))
        self.setPalette(palette)
        
        self._set_upper_layout()
        self._set_collection_layout()
        self._set_bottom_layout()
        
        self._outer_layout.addLayout(self._upper_layout, 1, 0)
        self._outer_layout.addWidget(self._scroll, 2, 0, 8, 1)
        #self._outer_layout.addLayout(self._collection_layout, 2, 0, 8, 1)
        self._outer_layout.addLayout(self._bottom_layout, 10, 0)
        
        self.setLayout(self._outer_layout)
        
        
        print('cube')

