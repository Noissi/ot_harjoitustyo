from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from ui.window import Window
from entities.card_creature import Creature
from services.korttikube_service import korttikube_service as kks
from config import CARD_RATIO, IMAGES_FILE_PATH, USER_IMAGES_FILE_PATH
import urllib.parse

class CubeView(Window):
    """ Class responsible for cube ui.

    Attributes:
        handle_show_main_view: A method to open a -main- ui.
        handle_show_card_view: A method to open a -card- ui.
        handle_show_edit_card_view: A method to open a -edit card- ui.
    """

    def __init__(self, handle_show_main_view=None, 
                 handle_show_card_view=None, handle_show_edit_card_view=None):
        """ Class constructor. Creates a new cube ui.
        
        Args:
            handle_show_main_view: A method to open a -main- ui.
            handle_show_card_view: A method to open a -card- ui.
            handle_show_edit_card_view: A method to open a -edit card- ui.
            search_parameters: Dictionary of selected searching criteria.
            order: Selected order for cube listing.
            outer_layout, upper_layout, bottom_layout: Main layouts.
            scroll_layout, scroll: Layouts and widgets responsible for the
                                   scrolling view.
        """

        super().__init__()
        self._handle_show_main_view = handle_show_main_view
        self._handle_show_card_view = handle_show_card_view
        self._handle_show_edit_card_view = handle_show_edit_card_view  

        self._search_parameters = {"name": "", "maintype": "", "colour": ""}
        self._order = ["name", "ASC"]

        self._outer_layout = self.get_outer_layout()
        self._upper_layout = QGridLayout()
        self._bottom_layout = QHBoxLayout()

        self._scroll_layout = QGridLayout()
        self._scroll = QScrollArea()
        self._set_scroll()

        self._initialise()

    def _set_upper_layout(self):
        """ Sets the upper layout elements. Divided into two levels.
        """

        upper_hbox = QHBoxLayout()
        lower_hbox = QHBoxLayout()

        # New card button
        btn_new = QPushButton('Uusi kortti')
        btn_new.setMaximumWidth(100)
        btn_new.clicked.connect(lambda: self._handle_show_edit_card_view(True))
        upper_hbox.addWidget(btn_new, 0)

        # Import cards from excel button
        btn_import = QPushButton('Lataa kortit tiedostoon')
        btn_import.setMaximumWidth(180)
        btn_import.clicked.connect(self._export_cards)
        upper_hbox.addWidget(btn_import, 1)
        self._upper_layout.addLayout(upper_hbox, 0, 0)

        # Search by name
        search_by_name_label = QLabel('<font size="3", color="white"> Hae korttia </font>')
        search_by_name_label.setMaximumWidth(80)
        search_by_name_line = QLineEdit()
        search_by_name_line.setMaximumWidth(300)
        search_by_name_line.setPlaceholderText('Kortin nimi')
        lower_hbox.addWidget(search_by_name_label, 0)
        lower_hbox.addWidget(search_by_name_line, 1)
        search_by_name_line.textChanged[str].connect(lambda: self._search_by_name(search_by_name_line.text()))
        
        # Search by maintype
        search_by_maintype_label = QLabel('<font size="3", color="white"> Korttityyppi </font>')
        search_by_maintype_label.setMaximumWidth(85)
        maintype_combo = QComboBox()
        maintype_combo.setMaximumWidth(190)
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
        lower_hbox.addWidget(search_by_maintype_label, 2)
        lower_hbox.addWidget(maintype_combo, 3)
        maintype_combo.activated.connect(lambda: self._search_by_maintype(maintype_combo.currentText()))
        
        # Search by colour
        search_by_colour_label = QLabel('<font size="3", color="white"> Väri </font>')
        search_by_colour_label.setMaximumWidth(30)
        colour_combo = QComboBox()
        colour_combo.setMaximumWidth(120)
        colour_combo.addItem("Ei valittu")
        colour_combo.addItem("Punainen")
        colour_combo.addItem("Sininen")
        colour_combo.addItem("Vihreä")
        colour_combo.addItem("Valkoinen")
        colour_combo.addItem("Musta")
        colour_combo.addItem("Väritön")
        colour_combo.addItem("Monivärinen")
        colour_combo.setCurrentIndex(0)
        lower_hbox.addWidget(search_by_colour_label, 4)
        lower_hbox.addWidget(colour_combo, 5)
        colour_combo.activated.connect(lambda: self._search_by_colour(colour_combo.currentText()))

        # Order
        order_by_label = QLabel('<font size="3", color="white"> Järjestys </font>')
        order_by_label.setMaximumWidth(70)
        order_combo = QComboBox()
        order_combo.setMaximumWidth(170)
        order_combo.addItem("Aakkosjärjestys")
        order_combo.addItem("Suurin voimakkuus")
        order_combo.addItem("Suurin kestävyys")
        order_combo.addItem("Pienin voimakkuus")
        order_combo.addItem("Pienin kestävyys")
        order_combo.setCurrentIndex(0)
        lower_hbox.addWidget(order_by_label, 6)
        lower_hbox.addWidget(order_combo, 7)
        order_combo.activated.connect(lambda: self._order_by(order_combo.currentText()))

        self._upper_layout.addLayout(lower_hbox, 1, 0)
    
    def _set_scroll(self):
        """ Sets the scroll area of the page for the card listing.
        """

        scrollwidget = QWidget()
        scrollwidget.setLayout(self._scroll_layout)
        self._scroll.setWidgetResizable(True) # Set to make the inner widget resize with scroll area
        self._scroll.setWidget(scrollwidget)
        
    def _set_collection_layout(self):
        """ Sets the collection layout elements (list of cards).
        """

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
            hover_image = IMAGES_FILE_PATH + "colourlesscard.png"
            btn_card.setFont(QFont('Times', 10))
            btn_card.setStyleSheet("QPushButton{border-image: url(\""+card_picture+"\")}"
                                   "QPushButton:hover{image: url("+hover_image+")}"
                                   "QPushButton{text-align: top left}")
            btn_card.clicked.connect(lambda checked=False, a=card: self._handle_show_card_view(a))
            self._scroll_layout.addWidget(btn_card, row, col)
            col += 1
            if col > 5:
                col = 0
                row += 1
            
    def _set_bottom_layout(self):
        """ Sets the bottom layout elements.
        """

        # Back button
        btn_back = QPushButton('Takaisin etusivulle')
        btn_back.setMaximumWidth(200)
        btn_back.clicked.connect(self._handle_show_main_view)
        self._bottom_layout.addWidget(btn_back)

        # Change image
        btn_image = QPushButton('Valitse kubekuva')
        btn_image.setMaximumWidth(200)
        btn_image.clicked.connect(self._change_image)
        self._bottom_layout.addWidget(btn_image)
        
    def _update_cards(self):
        """ Updates the card list.
        """

        self._scroll_layout = QGridLayout()
        self._scrollwidget = QWidget()
        self._scrollwidget.setLayout(self._scroll_layout)
        self._scroll = QScrollArea()
        self._scroll.setWidgetResizable(True)  # Set to make the inner widget resize with scroll area
        self._scroll.setWidget(self._scrollwidget)

        self._set_collection_layout()
        self._outer_layout.addWidget(self._scroll, 2, 0, 8, 1)

    def _export_cards(self):
        """ Creates a csv file out of the cards in cube.
        """

        kks.create_csv_file()
        msg = QMessageBox()
        msg.setText('Tiedosto luotu')
        msg.exec_()

    def _change_image(self):
        """ Changes the cube image showed in main page on the cube button.
        """

        fname = QFileDialog.getOpenFileName(self, 'Open file', 
        				     USER_IMAGES_FILE_PATH, "Image files (*.jpg *.png *.jpeg)")
        if fname[0] != "":
            fname = list(fname)[0]
            fname = fname.split("/")
            fname = USER_IMAGES_FILE_PATH + fname[-1]
            kks.update_cube(fname, "image")

    def _search_by_name(self, text):
        """ Shows only cards which name contains the given text.
        Args:
            text: [String] The selected name (part).
        """

        self._search_parameters["name"] = text
        self._update_cards()

    def _search_by_maintype(self, text):
        """ Shows only cards which maintype is the given text.
        Args:
            text: [String] The selected maintype.
        """

        if text == "Ei valittu":
            text = ""
        self._search_parameters["maintype"] = text
        self._update_cards()

    def _search_by_colour(self, text):
        """ Shows only cards which colours contains the given text.
        Args:
            text: [String] The selected colour.
        """

        if text == "Ei valittu":
            text = ""
        self._search_parameters["colour"] = text
        self._update_cards()

    def _order_by(self, text):
        """ Shows cards in the selected order.
        Args:
            text: [String] The ordering parameter.
        """

        if text == "Aakkosjärjestys":
            order = ["name", "ASC"]
        elif text == "Suurin voimakkuus":
            order = ["power", "DESC"]
        elif text == "Suurin kestävyys":
            order = ["toughness", "DESC"]
        elif text == "Pienin voimakkuus":
            order = ["power", "ASC"]
        elif text == "Pienin kestävyys":
            order = ["toughness", "ASC"]

        self._order = order
        self._update_cards()

    def _get_cards_with_search(self):
        """ Get cards from the database that agree with the search parameters.
        """

        cards = kks.get_cards_that_contains(self._search_parameters["name"],
                                            self._search_parameters["maintype"],
                                            self._search_parameters["colour"],
                                            self._order)
        return cards

    def _initialise(self):
        """ Initialise the cube view page. Creates the final layout.
        """
   
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
        self._outer_layout.addLayout(self._bottom_layout, 10, 0)
        
        self.setLayout(self._outer_layout)
