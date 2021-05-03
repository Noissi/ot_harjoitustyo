from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from ui.window import Window
from entities.card_creature import Creature
from services.korttikube_service import korttikube_service as kks
from config import CARD_RATIO, IMAGES_FILE_PATH

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

        self._search_parameters = {"name": "", "maintype": "", "colour": ""}
        
        self._outer_layout = self.get_outer_layout()
        self._upper_layout = QGridLayout()
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
        # Uusi kortti
        btn_new = QPushButton('Uusi kortti')
        btn_new.setMaximumWidth(100)
        btn_new.clicked.connect(lambda: self._handle_show_edit_card_view(True))
        self._upper_layout.addWidget(btn_new, 0, 3)

        # Search by name
        search_by_name_label = QLabel('<font size="3", color="white"> Hae korttia </font>')
        search_by_name_line = QLineEdit()
        search_by_name_line.setMaximumWidth(300)
        search_by_name_line.setPlaceholderText('Kortin nimi')
        self._upper_layout.addWidget(search_by_name_label, 1, 0)
        self._upper_layout.addWidget(search_by_name_line, 1, 1)
        search_by_name_line.textChanged[str].connect(lambda: self._search_by_name(search_by_name_line.text()))
        
        # Search by maintype
        search_by_maintype_label = QLabel('<font size="3", color="white"> Korttityyppi </font>')
        maintype_combo = QComboBox()
        maintype_combo.addItem("Ei valittu")
        maintype_combo.addItem("Creature")
        maintype_combo.addItem("Artifact")
        maintype_combo.addItem("Enchantment")
        maintype_combo.addItem("Land")
        maintype_combo.addItem("Instant")
        maintype_combo.addItem("Sorcery")
        maintype_combo.addItem("Planeswalker")
        maintype_combo.addItem("Artifact Creature")
        maintype_combo.addItem("Enchantment Creature")
        maintype_combo.setCurrentIndex(0)
        self._upper_layout.addWidget(search_by_maintype_label, 1, 2)
        self._upper_layout.addWidget(maintype_combo, 1, 3)
        maintype_combo.activated.connect(lambda: self._search_by_maintype(maintype_combo.currentText()))
        
        # Search by colour
        search_by_colour_label = QLabel('<font size="3", color="white"> Väri </font>')
        colour_combo = QComboBox()
        colour_combo.addItem("Ei valittu")
        colour_combo.addItem("Punainen")
        colour_combo.addItem("Sininen")
        colour_combo.addItem("Vihreä")
        colour_combo.addItem("Valkoinen")
        colour_combo.addItem("Musta")
        colour_combo.addItem("Väritön")
        colour_combo.addItem("Monivärinen")
        colour_combo.setCurrentIndex(0)
        self._upper_layout.addWidget(search_by_colour_label, 1, 4)
        self._upper_layout.addWidget(colour_combo, 1, 5)
        colour_combo.activated.connect(lambda: self._search_by_colour(colour_combo.currentText()))
        
    def _set_collection_layout(self):
        # Get cards
        cards = self._get_cards_with_search()

        row = 0
        col = 0
        # Print cards in a 6x? grid
        for card in cards:
            btn_card = QPushButton()
            card_width = 200
            btn_card.setMinimumSize(card_width, card_width * CARD_RATIO)
            btn_card.setMaximumSize(card_width, card_width * CARD_RATIO)
            card_picture = card[18]
            hover_image = IMAGES_FILE_PATH + "bluecard.png"
            # changing font and size of text
            btn_card.setFont(QFont('Times', 10))
            btn_card.setStyleSheet("QPushButton{border-image: url("+card_picture+")}"
                                   "QPushButton:hover{image: url("+hover_image+")}"
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
        
    def _update_cards(self):
        self._scroll_layout = QGridLayout()
        self._scrollwidget = QWidget()
        #self._scrollwidget.setLayout(self._collection_layout)
        self._scrollwidget.setLayout(self._scroll_layout)
        self._scroll = QScrollArea()
        self._scroll.setWidgetResizable(True)  # Set to make the inner widget resize with scroll area
        self._scroll.setWidget(self._scrollwidget)

        self._set_collection_layout()
        self._outer_layout.addWidget(self._scroll, 2, 0, 8, 1)

    def _search_by_name(self, text):
        self._search_parameters["name"] = text
        self._update_cards()

    def _search_by_maintype(self, text):
        if text == "Ei valittu":
            text = ""
        self._search_parameters["maintype"] = text
        self._update_cards()

    def _search_by_colour(self, text):
        if text == "Ei valittu":
            text = ""
        self._search_parameters["colour"] = text
        self._update_cards()

    def _get_cards(self):
        cards = kks.get_cards_in_cube()
        return cards

    def _get_cards_with_search(self):
        cards = kks.get_cards_that_contains(self._search_parameters["name"],
                                               self._search_parameters["maintype"],
                                               self._search_parameters["colour"],)
        return cards

    def _initialise(self):
        # Set background image
        image = QImage(IMAGES_FILE_PATH + "mtg_puu.jpg")
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
