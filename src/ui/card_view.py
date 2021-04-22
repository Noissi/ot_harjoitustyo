from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from ui.window import Window
from entities.card_creature import Creature
from services.korttikube_service import korttikube_service as kks

class CardView(Window):
    def __init__(self, handle_show_cube_view, handle_show_edit_card_view):
        super().__init__()
        self._handle_show_edit_card_view = handle_show_edit_card_view
        self._handle_show_cube_view = handle_show_cube_view
        
        self._card = kks.get_card()
        self._card_frame = None
        
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
        
        self.setLayout(self._outer_layout)
        
        #widget = QWidget(self)
        #widget.setLayout(self._outer_layout)
        #self.setCentralWidget(widget)
        #self.centralWidget().setLayout(self._outer_layout)
        print('layouts')
        
        '''
        outer_layout.setColumnStretch(0, 2)
        outer_layout.setColumnStretch(1, 3)
        outer_layout.setColumnStretch(2, 2)
        outer_layout.setRowStretch(0, 1)        
        outer_layout.setRowStretch(1, 5)
        outer_layout.setRowStretch(2, 1)
        '''
        
    def _set_middle_layout(self):
        # Add to middle layout
        self._middle_layout.addLayout(self._left_layout, 0, 0)
        self._middle_layout.addLayout(self._card_layout, 0, 1)
        self._middle_layout.addLayout(self._right_layout, 0, 3)
        
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
        self._card_layout = QGridLayout()
        # Draw card frame
        self._set_card_frame()
        card_frame_scaled = self._card_frame.scaledToWidth(self.width-1000)
        card_frame_label = QLabel(alignment=Qt.AlignCenter)
        card_frame_label.setPixmap(card_frame_scaled)
        self._card_layout.addWidget(card_frame_label)
        
        # Write card name
        name_label = QLabel()
        #name_label.setText('<font color="red", font size="4"> Kiljukuikka </font>')
        name_label.setText(self._card.get_name())
        name_label.move(500,-700)
        self._card_layout.addWidget(name_label)

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
        # Set the right side panel
        ruletext_label = QLabel(self._card.get_ruletext())
        ruletext_label.setWordWrap(True)
        self._right_layout.addRow("Sääntöteksti:", ruletext_label)
        flavourtext_label = QLabel(self._card.get_flavourtext())
        flavourtext_label.setWordWrap(True)
        self._right_layout.addRow("Tarina:", flavourtext_label)
        self._right_layout.addRow("Voimakkuus:", QLabel(str(self._card.get_power_print())))
        self._right_layout.addRow("Kestävyys:", QLabel(str(self._card.get_toughness_print())))
        self._right_layout.addRow("Kuva:", QLabel(self._card.get_image()))
        self._right_layout.addRow("Tunnus:", QLabel(self._card.get_seticon()))
        self._right_layout.addRow("Harvinaisuus:", QLabel(self._card.get_rarity()))
        self._right_layout.addRow("Tekijä:", QLabel(self._card.get_creator()))

    def _set_card_frame(self):
        self._card_frame = QPixmap(kks.set_card_frame(self._card))

    def _initialise(self):        
        # Set background image
        image = QImage("img/card.jpg")
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

        print('card')
