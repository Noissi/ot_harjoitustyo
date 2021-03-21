from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from ui.window import Window
from entities.card_creature import Creature

class EditCardView(Window):
    def __init__(self, card, handle_show_game_view, handle_show_card_view):
        super().__init__()
        self._handle_show_card_view = handle_show_card_view
        self._handle_show_game_view = handle_show_game_view
        
        self._card = card        
        self._card_frame = None
        
        self._outer_layout = self.get_outer_layout()
        self._middle_layout = QGridLayout()
        self._bottom_layout = QHBoxLayout()
        
        self._left_layout = QFormLayout()
        self._right_layout = QFormLayout() 
        self._card_layout = QGridLayout()
        
        self._initialise()
        
    def _set_layouts(self):    
        #self._outer_layout = self.get_outer_layout()
        #self._outer_layout = QGridLayout()
        #self._clear_layout(self._outer_layout)
        # Set all layouts to outer layout grid
        self._outer_layout.addLayout(self._middle_layout, 1, 0)
        self._outer_layout.addLayout(self._bottom_layout, 2, 0)
        
        self._middle_layout.setContentsMargins(50,50,50,0)
        self._outer_layout.setContentsMargins(50,50,50,50)
        self._outer_layout.setSpacing(20)
        
        self.setLayout(self._outer_layout)
        
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
        #self._middle_layout = QGridLayout()
        self._middle_layout.addLayout(self._left_layout, 0, 0)
        self._middle_layout.addLayout(self._card_layout, 0, 1)
        self._middle_layout.addLayout(self._right_layout, 0, 3)
        
    def _set_bottom_layout(self):
        # Draw bottom edit box        
        #self._bottom_layout = QHBoxLayout()
        btn_edit = QPushButton('Tallenna')
        btn_edit.setMaximumWidth(100)
        btn_edit.clicked.connect(lambda: self._handle_show_card_view(self._card))
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
        name_label.setText('<font color="red", font size="4"> Kiljukuikka </font>')
        name_label.move(500,-700)
        self._card_layout.addWidget(name_label)        
        
        feature_label = QLabel(''.join(self._card.feature))
        feature_label.setStyleSheet('color: white')
        #self._card_layout.addWidget(feature_label)
        
    def _set_leftpanel_layout(self):
        # Draw left side panel
        # Draw card name edit box
        self._left_layout.addRow("Nimi:", QLineEdit())
        
        # Draw card type selection
        type_combo = QComboBox()
        type_combo.addItem("Creature")
        type_combo.addItem("Artifact")
        type_combo.addItem("Enchantment")
        type_combo.addItem("Land")
        type_combo.addItem("Instant")
        type_combo.addItem("Sorcery")
        type_combo.addItem("Planeswalker")
        self._left_layout.addRow("Tyyppi:", type_combo)
        #self._card.set_maintype()
        self._left_layout.addRow("Alatyyppi:", QLineEdit())
        
        # Draw colour checkboxes
        colour_red_box = QCheckBox("Punainen")
        colour_blue_box = QCheckBox("Sininen")
        colour_green_box = QCheckBox("Vihreä")
        colour_white_box = QCheckBox("Valkoinen")
        colour_black_box = QCheckBox("Musta")
        colour_colourless_box = QCheckBox("Väritön")
        colour_boxes = [colour_red_box, colour_blue_box, colour_green_box, \
                        colour_white_box, colour_black_box, colour_colourless_box]
        self._left_layout.addRow("Väri:", colour_red_box)
        self._left_layout.addRow(colour_blue_box, colour_green_box)
        self._left_layout.addRow(colour_white_box, colour_black_box)
        self._left_layout.addRow(colour_colourless_box)
        
        self._set_colour_boxes(colour_boxes)
        self._change_colour_state(colour_boxes)
        
        
    def _set_rightpanel_layout(self):
        # Set the right side panel        
        
        # Draw feature checkboxes
        feature_flying_box = QCheckBox("Flying")
        feature_vigilance_box = QCheckBox("Vigilance")
        feature_haste_box = QCheckBox("Haste")
        feature_deathtouch_box = QCheckBox("Deathtouch")
        feature_trample_box = QCheckBox("Trample")
        feature_firststrike_box = QCheckBox("First strike")
        feature_doublestrike_box = QCheckBox("Double strike")
        feature_lifelink_box = QCheckBox("Lifelink")
        feature_menace_box = QCheckBox("Menace")
        feature_hexproof_box = QCheckBox("Hexproof")
        feature_defender_box = QCheckBox("Defender")
        feature_reach_box = QCheckBox("Reach")
        feature_indestructible_box = QCheckBox("Indestructible")
        feature_flash_box = QCheckBox("Flash")
        feature_boxes = [feature_flying_box, feature_vigilance_box, feature_haste_box, \
                         feature_deathtouch_box, feature_trample_box, feature_firststrike_box, \
                         feature_doublestrike_box, feature_lifelink_box, feature_menace_box, \
                         feature_hexproof_box, feature_defender_box, feature_reach_box, \
                         feature_indestructible_box, feature_flash_box]        
        self._right_layout.addRow("Ominaisuus:", feature_flying_box)
        self._right_layout.addRow(feature_vigilance_box, feature_haste_box)
        self._right_layout.addRow(feature_deathtouch_box, feature_trample_box)
        self._right_layout.addRow(feature_firststrike_box, feature_doublestrike_box)        
        self._right_layout.addRow(feature_lifelink_box, feature_menace_box)
        self._right_layout.addRow(feature_hexproof_box, feature_defender_box)
        self._right_layout.addRow(feature_reach_box, feature_indestructible_box)
        self._right_layout.addRow(feature_flash_box)
        
        self._change_feature_state(feature_boxes)
        self._set_feature_boxes(feature_boxes)
        
        ruletext_line = QLineEdit()
        self._right_layout.addRow("Sääntöteksti:", ruletext_line)
        self._card.set_ruletext(ruletext_line.text())
        self._right_layout.addRow("Tarina:", QLineEdit())
        self._right_layout.addRow("Tekijä:", QLineEdit())
        
        print("ruletext")
        print(self._card.ruletext)
        
    def _update_layout(self):
        self._set_card_layout()
        #self._set_leftpanel_layout()
        #self._set_rightpanel_layout()
        
        self._set_middle_layout()
        #self._set_bottom_layout()
        self._set_layouts()        
        
        self.setLayout(self._outer_layout)
        
    def _set_colour(self, colour_box):
        print(colour_box.text())
        if colour_box.isChecked() == True:            
            self._card.add_colour(colour_box.text())
            print("set colour2")
        else:
            if colour_box.text() in self._card.colour:
                self._card.remove_colour(colour_box.text())
        self._set_card_frame()
             
        self._update_layout()
        
        print(self._card.colour) 
    
    def _change_feature_state(self, feature_boxes):
        feature_boxes[0].stateChanged.connect(lambda: self._set_feature(feature_boxes[0]))
        feature_boxes[1].stateChanged.connect(lambda: self._set_feature(feature_boxes[1]))
        feature_boxes[2].stateChanged.connect(lambda: self._set_feature(feature_boxes[2]))
        feature_boxes[3].stateChanged.connect(lambda: self._set_feature(feature_boxes[3]))
        feature_boxes[4].stateChanged.connect(lambda: self._set_feature(feature_boxes[4]))
        feature_boxes[5].stateChanged.connect(lambda: self._set_feature(feature_boxes[5]))
        feature_boxes[6].stateChanged.connect(lambda: self._set_feature(feature_boxes[6]))
        feature_boxes[7].stateChanged.connect(lambda: self._set_feature(feature_boxes[7]))
        feature_boxes[8].stateChanged.connect(lambda: self._set_feature(feature_boxes[8]))
        feature_boxes[9].stateChanged.connect(lambda: self._set_feature(feature_boxes[9]))
        feature_boxes[10].stateChanged.connect(lambda: self._set_feature(feature_boxes[10]))
        feature_boxes[11].stateChanged.connect(lambda: self._set_feature(feature_boxes[11]))
        feature_boxes[12].stateChanged.connect(lambda: self._set_feature(feature_boxes[12]))
        feature_boxes[13].stateChanged.connect(lambda: self._set_feature(feature_boxes[13]))
        
        
    def _set_feature(self, feature):
        if feature.isChecked() == True:
            self._card.add_feature(feature.text())
        else:
            self._card.remove_feature(feature.text())
        self._update_layout()
        
        print("set feature")
        print(self._card.feature)
        
    def _set_feature_boxes(self, feature_boxes):
        for feature_box in feature_boxes:
            self._check_if_card_has(feature_box, self._card.feature)
        
    def _set_colour_boxes(self, colour_boxes):
        print("set colour")
        for colour_box in colour_boxes:            
            self._check_if_card_has(colour_box, self._card.colour)
            
    def _change_colour_state(self, colour_boxes):
        colour_boxes[0].stateChanged.connect(lambda: self._set_colour(colour_boxes[0]))        
        colour_boxes[1].stateChanged.connect(lambda: self._set_colour(colour_boxes[1]))
        colour_boxes[2].stateChanged.connect(lambda: self._set_colour(colour_boxes[2]))
        colour_boxes[3].stateChanged.connect(lambda: self._set_colour(colour_boxes[3]))
        colour_boxes[4].stateChanged.connect(lambda: self._set_colour(colour_boxes[4]))
        colour_boxes[5].stateChanged.connect(lambda: self._set_colour(colour_boxes[5]))
            
    def _set_card_frame(self):
        if self._card.get_card_colour() == "Punainen":
            self._card_frame = QPixmap("img/redcard.png")
        elif self._card.get_card_colour() == "Sininen":
            self._card_frame = QPixmap("img/bluecard.png")
        elif self._card.get_card_colour() == "Vihreä":
            self._card_frame = QPixmap("img/greencard.png")
        elif self._card.get_card_colour() == "Valkoinen":
            self._card_frame = QPixmap("img/whitecard.png")
        elif self._card.get_card_colour() == "Musta":
            self._card_frame = QPixmap("img/blackcard.png")
        elif self._card.get_card_colour() == "Väritön":
            self._card_frame = QPixmap("img/colourlesscard.png")
        elif self._card.get_card_colour() == "Kulta":
            self._card_frame = QPixmap("img/goldcard.png")
        
    def _check_if_card_has(self, checkbox, cards_list):
        print("card list")
        print(cards_list)
        if checkbox.text() in cards_list:
            checkbox.setChecked(True)
        else:
            checkbox.setChecked(False)
        
    def _clear_layout(self, layout):
        print('before: ' +str(layout.count()))
        for i in range(layout.count()):
            print('i: ' +str(i))
            layout_item = layout.takeAt(i)
            if layout_item:
                widget = layout_item.widget()
                if widget:
                    widget.setParent(None)
        print('after: ' + str(layout.count()))
        
    def _initialise(self):        
        # Set background image
        image = QImage("img/card.jpg")
        image_scaled = image.scaled(QSize(self.width, self.height)) # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(image_scaled))                        
        self.setPalette(palette)
        
        # Set layouts
        left2_layout = QStackedLayout()        
        
        # Modify layouts
        button_back = QPushButton('Takaisin peleihin')
        button_back.clicked.connect(self._handle_show_game_view)
        #top_layout.addWidget(button_back)   
     
        self._set_card_layout()
        self._set_leftpanel_layout()
        self._set_rightpanel_layout()
        
        self._set_middle_layout()
        self._set_bottom_layout()
        self._set_layouts()
        
        self.setLayout(self._outer_layout)

        print('edit card')