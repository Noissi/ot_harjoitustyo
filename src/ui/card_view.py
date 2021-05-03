from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from ui.window import Window
from entities.card_creature import Creature
from services.korttikube_service import korttikube_service as kks
from ui.card_image import CardImage
from config import CARD_RATIO, IMAGES_FILE_PATH

class CardView(Window):
    def __init__(self, handle_show_cube_view, handle_show_edit_card_view):
        super().__init__()
        self._handle_show_edit_card_view = handle_show_edit_card_view
        self._handle_show_cube_view = handle_show_cube_view
        
        self._card = kks.get_card()
        
        self._outer_layout = self.get_outer_layout()
        self._middle_layout = QGridLayout()
        self._bottom_layout = QHBoxLayout()
        
        self._left_layout = QFormLayout()
        self._right_layout = QFormLayout()        
        
        self._initialise()
        
    def _set_layouts(self):
        # Set all layouts to outer layout grid
        
        self._outer_layout.addLayout(self._middle_layout, 1, 0)
        self._outer_layout.addLayout(self._bottom_layout, 2, 0)
        
        self._middle_layout.setContentsMargins(50,50,50,0)
        self._outer_layout.setContentsMargins(50,50,50,50)
        self._outer_layout.setSpacing(20)
        
        #self._outer_layout.setColumnStretch(0, 1)
        #self._outer_layout.setColumnStretch(1, 5)
        #self._outer_layout.setColumnStretch(2, 1)
        
        self._outer_layout.setRowStretch(0, 1)        
        self._outer_layout.setRowStretch(1, 10)
        self._outer_layout.setRowStretch(2, 1)
        
        self.setLayout(self._outer_layout)
        
        #widget = QWidget(self)
        #widget.setLayout(self._outer_layout)
        #self.setCentralWidget(widget)
        #self.centralWidget().setLayout(self._outer_layout)

    def _set_middle_layout(self):
        # Add to middle layout
        self._middle_layout.addLayout(self._left_layout, 0, 0)
        self._middle_layout.addLayout(self._card_layout, 0, 1)
        self._middle_layout.addLayout(self._right_layout, 0, 2)
        
    def _set_bottom_layout(self):
        # Draw return button
        btn_back = QPushButton('Takaisin')
        btn_back.setMaximumWidth(100)
        btn_back.clicked.connect(self._handle_show_cube_view)
        self._bottom_layout.addWidget(btn_back)
        
        # Draw bottom edit box
        btn_edit = QPushButton('Muokkaa')
        btn_edit.setMaximumWidth(100)
        btn_edit.clicked.connect(self._handle_show_edit_card_view)
        self._bottom_layout.addWidget(btn_edit)
        
    def _set_card_layout(self):
        # Draw card frame
        self._card_layout = QGridLayout()
        card_image = CardImage()
        card_image.set_card(self._card)
        self._card_layout.addWidget(card_image, 0, Qt.AlignCenter)

    def _set_leftpanel_layout(self):
        # Draw left side panel
        self._left_layout.addRow("Nimi", QLabel(self._card.get_name()))
        self._left_layout.addRow("Tyyppi:", QLabel(self._card.get_maintype()))
        self._left_layout.addRow("Legendary:", QLabel(self._card.get_legendary_print()))
        self._left_layout.addRow("Tribal:", QLabel(self._card.get_tribal_print()))
        self._left_layout.addRow("Subtype:", QLabel(self._card.get_subtype_print()))
        self._left_layout.addRow("Väri:", QLabel(self._card.get_colour_print()))
        self._left_layout.addRow("Hinta:", QLabel(self._card.get_manacost()))
        
        feature_label = QLabel(self._card.get_feature_print())
        feature_label.setWordWrap(True)
        self._left_layout.addRow("Ominaisuus:", feature_label)

    def _set_rightpanel_layout(self):
        ruletext_label = QLabel(self._card.get_ruletext())
        ruletext_label.setWordWrap(True)
        self._right_layout.addRow("Sääntöteksti:", ruletext_label)
        
        flavourtext_label = QLabel(self._card.get_flavourtext())
        flavourtext_label.setWordWrap(True)
        self._right_layout.addRow("Tarina:", flavourtext_label)
        
        self._right_layout.addRow("Voimakkuus:", QLabel(str(self._card.get_power_print())))
        self._right_layout.addRow("Kestävyys:", QLabel(str(self._card.get_toughness_print())))

        image_label = QLabel(self._card.get_image())
        image_label.setWordWrap(True)
        self._right_layout.addRow("Kuva:", image_label)

        seticon_label = QLabel(self._card.get_seticon())
        seticon_label.setWordWrap(True)
        self._right_layout.addRow("Tunnus:", seticon_label)

        rarity_label = QLabel(self._card.get_rarity())
        rarity_label.setWordWrap(True)
        self._right_layout.addRow("Harvinaisuus:", rarity_label)

        creator_label = QLabel(self._card.get_creator())
        creator_label.setWordWrap(True)
        self._right_layout.addRow("Tekijä:", creator_label)

    def _initialise(self):        
        # Set background image
        image = QImage(IMAGES_FILE_PATH + "card.jpg")
        image_scaled = image.scaled(QSize(self.width, self.height)) # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(image_scaled))                        
        self.setPalette(palette)
        
        # Set layouts
        left2_layout = QStackedLayout()
     
        self._set_card_layout()
        self._set_leftpanel_layout()
        self._set_rightpanel_layout()
        
        self._set_middle_layout()
        self._set_bottom_layout()
        self._set_layouts()
        
        self.setLayout(self._outer_layout)