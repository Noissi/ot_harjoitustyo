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
        
        self._feature_boxes = []
        
        self._initialise_feature()
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
        #name_label.setText('<font color="red", font size="4"> Kiljukuikka </font>')
        name_label.setText(self._card.name)
        name_label.move(500,-700)
        self._card_layout.addWidget(name_label)        
        
        feature_label = QLabel(''.join(self._card.feature))
        feature_label.setStyleSheet('color: white')
        #self._card_layout.addWidget(feature_label)
        
    def _set_leftpanel_layout(self):
        # Draw left side panel
        
        # Draw name edit box
        name_line = QLineEdit()
        name_line.setText(self._card.name)
        self._left_layout.addRow("Nimi:", name_line)
        name_line.textChanged[str].connect(lambda: self._save_name_to_card(name_line))        
        
        # Draw maintype selection
        maintype_combo = QComboBox()
        maintype_combo.addItem("Creature")
        maintype_combo.addItem("Artifact")
        maintype_combo.addItem("Enchantment")
        maintype_combo.addItem("Land")
        maintype_combo.addItem("Instant")
        maintype_combo.addItem("Sorcery")
        maintype_combo.addItem("Planeswalker")
        maintype_combo.addItem("Artifact Creature")
        maintype_combo.addItem("Enchantment Creature")
        self._left_layout.addRow("Tyyppi:", maintype_combo)
        self._set_maintype_combo(maintype_combo)
        maintype_combo.activated.connect(lambda: self._save_maintype_to_card(maintype_combo))
        
        # Legendary
        legendary_btn = QRadioButton("Legendary")
        legendary_btn.setAutoExclusive(False)
        self._left_layout.addRow("Legendary:", legendary_btn)
        self._set_legendary_btn(legendary_btn)
        legendary_btn.toggled.connect(lambda: self._set_legendary(legendary_btn))
        
        # Tribal
        tribal_btn = QRadioButton("Tribal")
        tribal_btn.setAutoExclusive(False)
        self._left_layout.addRow("Tribal:", tribal_btn)
        self._set_tribal_btn(tribal_btn)
        tribal_btn.toggled.connect(lambda: self._set_tribal(tribal_btn))
        
        # Subtype
        subtype_line = QLineEdit()
        subtype_line.setText(self._card.get_subtype())
        self._left_layout.addRow("Alatyyppi:", subtype_line)
        subtype_line.textChanged[str].connect(lambda: self._save_subtype_to_card(subtype_line))
        
        # Draw colour checkboxes
        colour_red_box = QCheckBox("Punainen")
        colour_blue_box = QCheckBox("Sininen")
        colour_green_box = QCheckBox("Vihreä")
        colour_white_box = QCheckBox("Valkoinen")
        colour_black_box = QCheckBox("Musta")
        colour_boxes = [colour_red_box, colour_blue_box, colour_green_box, \
                        colour_white_box, colour_black_box]
        self._left_layout.addRow("Väri:", colour_red_box)
        self._left_layout.addRow(colour_blue_box, colour_green_box)
        self._left_layout.addRow(colour_white_box, colour_black_box)
        
        self._set_colour_boxes(colour_boxes)
        self._change_colour_state(colour_boxes)
        
        
    def _set_rightpanel_layout(self):
        # Set the right side panel        
        
        # Draw feature checkboxes
        self._right_layout.addRow("Ominaisuus:", self._feature_boxes[0])
        self._right_layout.addRow(self._feature_boxes[1], self._feature_boxes[2])
        self._right_layout.addRow(self._feature_boxes[3], self._feature_boxes[4])
        self._right_layout.addRow(self._feature_boxes[5], self._feature_boxes[6])        
        self._right_layout.addRow(self._feature_boxes[7], self._feature_boxes[8])
        self._right_layout.addRow(self._feature_boxes[9], self._feature_boxes[10])
        self._right_layout.addRow(self._feature_boxes[11], self._feature_boxes[12])
        self._right_layout.addRow(self._feature_boxes[13])
        
        self._set_feature_boxes()
        self._change_feature_state()
        
        # Rule text
        ruletext_line = QLineEdit()
        ruletext_line.setText(self._card.ruletext)
        self._right_layout.addRow("Sääntöteksti:", ruletext_line)
        ruletext_line.textChanged[str].connect(lambda: self._save_ruletext_to_card(ruletext_line))
        
        # Flavour text
        flavourtext_line = QLineEdit()
        flavourtext_line.setText(self._card.flavourtext)
        self._right_layout.addRow("Tarina:", flavourtext_line)
        flavourtext_line.textChanged[str].connect(lambda: self._save_flavourtext_to_card(flavourtext_line))
        
        # Creature
        creator_line = QLineEdit()
        creator_line.setText(self._card.creator)
        self._right_layout.addRow("Tekijä:", creator_line)
        creator_line.textChanged[str].connect(lambda: self._save_creator_to_card(creator_line))
        
    def _update_layout(self):
        self._set_card_layout()
        #self._set_leftpanel_layout()
        #self._set_rightpanel_layout()
        
        self._set_middle_layout()
        #self._set_bottom_layout()
        self._set_layouts()        
        
        self.setLayout(self._outer_layout)
    
    # Colour
    def _set_colour(self, colour_box):
        if colour_box.isChecked() == True:            
            self._card.add_colour(colour_box.text())
        else:
            if colour_box.text() in self._card.colour:
                self._card.remove_colour(colour_box.text())
        self._set_card_frame()             
        self._update_layout()

    def _set_colour_boxes(self, colour_boxes):
        for colour_box in colour_boxes:            
            self._check_if_card_has(colour_box, self._card.colour)
    
    def _change_colour_state(self, colour_boxes):
        colour_boxes[0].stateChanged.connect(lambda: self._set_colour(colour_boxes[0]))
        colour_boxes[1].stateChanged.connect(lambda: self._set_colour(colour_boxes[1]))
        colour_boxes[2].stateChanged.connect(lambda: self._set_colour(colour_boxes[2]))
        colour_boxes[3].stateChanged.connect(lambda: self._set_colour(colour_boxes[3]))
        colour_boxes[4].stateChanged.connect(lambda: self._set_colour(colour_boxes[4]))
    
    # Feature    
    def _set_feature(self, feature_box):
        if feature_box.isChecked() == True:
            self._card.add_feature(feature_box.text())
        else:
            self._card.remove_feature(feature_box.text())
        self._update_layout()
        
    def _set_feature_boxes(self):
        for feature_box in self._feature_boxes:
            self._check_if_card_has(feature_box, self._card.feature)
            
    def _change_feature_state(self):
        self._feature_boxes[0].stateChanged.connect(lambda: self._set_feature(self._feature_boxes[0]))
        self._feature_boxes[1].stateChanged.connect(lambda: self._set_feature(self._feature_boxes[1]))
        self._feature_boxes[2].stateChanged.connect(lambda: self._set_feature(self._feature_boxes[2]))
        self._feature_boxes[3].stateChanged.connect(lambda: self._set_feature(self._feature_boxes[3]))
        self._feature_boxes[4].stateChanged.connect(lambda: self._set_feature(self._feature_boxes[4]))
        self._feature_boxes[5].stateChanged.connect(lambda: self._set_feature(self._feature_boxes[5]))
        self._feature_boxes[6].stateChanged.connect(lambda: self._set_feature(self._feature_boxes[6]))
        self._feature_boxes[7].stateChanged.connect(lambda: self._set_feature(self._feature_boxes[7]))
        self._feature_boxes[8].stateChanged.connect(lambda: self._set_feature(self._feature_boxes[8]))
        self._feature_boxes[9].stateChanged.connect(lambda: self._set_feature(self._feature_boxes[9]))
        self._feature_boxes[10].stateChanged.connect(lambda: self._set_feature(self._feature_boxes[10]))
        self._feature_boxes[11].stateChanged.connect(lambda: self._set_feature(self._feature_boxes[11]))
        self._feature_boxes[12].stateChanged.connect(lambda: self._set_feature(self._feature_boxes[12]))
        self._feature_boxes[13].stateChanged.connect(lambda: self._set_feature(self._feature_boxes[13]))
    
    # Maintype
    def _set_maintype_combo(self, maintype_combo):
        index = maintype_combo.findText(self._card.maintype)  # finds the index of the item you want
        maintype_combo.setCurrentIndex(index)
        self._disable_boxes(self._feature_boxes)
        
    # Legendary
    def _set_legendary(self, legendary_btn):
        if legendary_btn.isChecked() == True:            
            self._card.set_legendary(True)
        else:
            self._card.set_legendary(False)
            
    def _set_legendary_btn(self, legendary_btn):
        if self._card.legendary == True:
            legendary_btn.setChecked(True)
        else:
            legendary_btn.setChecked(False)
            
    # Tribal
    def _set_tribal(self, tribal_btn):
        if tribal_btn.isChecked() == True:            
            self._card.set_tribal(True)
        else:
            self._card.set_tribal(False)
            
    def _set_tribal_btn(self, tribal_btn):
        if self._card.tribal == True:
            tribal_btn.setChecked(True)
        else:
            tribal_btn.setChecked(False)
            
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
        if checkbox.text() in cards_list:
            checkbox.setChecked(True)
        else:
            checkbox.setChecked(False)
    
    def _disable_boxes(self, boxes):
        disable = True
        if self._card.maintype == "Instant":
            disable = False
        for box in boxes:
            box.setEnabled(disable)
    
    # Save to card
    def _save_name_to_card(self, name_line):
        self._card.set_name(name_line.text())
    def _save_maintype_to_card(self, cb):
        self._card.set_maintype(cb.currentText())
        self._disable_boxes(self._feature_boxes)
    def _save_subtype_to_card(self, subtype_line):
        self._card.set_subtype(subtype_line.text())
    def _save_ruletext_to_card(self, ruletext_line):
        self._card.set_ruletext(ruletext_line.text())
    def _save_flavourtext_to_card(self, flavourtext_line):
        self._card.set_flavourtext(flavourtext_line.text())
    def _save_creator_to_card(self, creator_line):
        self._card.set_creator(creator_line.text())
        
        
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
        
    def _initialise_feature(self):
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
        self._feature_boxes = [feature_flying_box, feature_vigilance_box, feature_haste_box, \
                         feature_deathtouch_box, feature_trample_box, feature_firststrike_box, \
                         feature_doublestrike_box, feature_lifelink_box, feature_menace_box, \
                         feature_hexproof_box, feature_defender_box, feature_reach_box, \
                         feature_indestructible_box, feature_flash_box] 
        
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
