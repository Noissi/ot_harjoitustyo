from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from ui.window import Window

from services.korttikube_service import korttikube_service as kks

from entities.card_creature import Creature

class EditCardView(Window):
    def __init__(self, card, handle_show_game_view, handle_show_card_view):
        super().__init__()
        self._handle_show_card_view = handle_show_card_view
        self._handle_show_game_view = handle_show_game_view
        
        self._card = card        
        self._card_frame = None
        
        self._outer_layout  = self.get_outer_layout()
        self._middle_layout = QGridLayout()
        self._bottom_layout = QHBoxLayout()
        
        self._left_layout  = QFormLayout()
        self._right_layout = QFormLayout() 
        self._card_layout  = QGridLayout()
        
        self._name_line         = QLineEdit()
        self._subtype_line      = QLineEdit()
        self._ruletext_line     = QLineEdit()
        self._flavourtext_line  = QLineEdit()
        self._creator_line      = QLineEdit()
        self._legendary_btn     = QRadioButton("Legendary")
        self._tribal_btn        = QRadioButton("Tribal")
        self._maintype_combo    = QComboBox()
        self._power_spinbox     = QSpinBox()
        self._toughness_spinbox = QSpinBox()
        self._colour_boxes      = []
        self._feature_boxes     = []
        
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
        btn_edit.clicked.connect(self._save_and_return)
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
        
        #feature_label = QLabel(''.join(self._card.feature))
        #feature_label.setStyleSheet('color: white')
        #self._card_layout.addWidget(feature_label)
        
    def _set_leftpanel_layout(self):
        # Draw left side panel
        
        # Draw name edit box
        self._name_line.setText(self._card.get_name())
        self._left_layout.addRow("Nimi:", self._name_line)
        self._name_line.textChanged[str].connect(self._change_name)       
        
        # Draw maintype selection
        self._maintype_combo.addItem("Creature")
        self._maintype_combo.addItem("Artifact")
        self._maintype_combo.addItem("Enchantment")
        self._maintype_combo.addItem("Land")
        self._maintype_combo.addItem("Instant")
        self._maintype_combo.addItem("Sorcery")
        self._maintype_combo.addItem("Planeswalker")
        self._maintype_combo.addItem("Artifact Creature")
        self._maintype_combo.addItem("Enchantment Creature")
        self._left_layout.addRow("Tyyppi:", self._maintype_combo)
        self._set_maintype_combo()
        self._maintype_combo.activated.connect(self._change_maintype)
        
        # Legendary
        self._legendary_btn.setAutoExclusive(False)
        self._left_layout.addRow("Legendary:", self._legendary_btn)
        self._set_legendary_btn()
        self._legendary_btn.toggled.connect(self._change_legendary)
        
        # Tribal
        self._tribal_btn.setAutoExclusive(False)
        self._left_layout.addRow("Tribal:", self._tribal_btn)
        self._set_tribal_btn()        
        self._tribal_btn.toggled.connect(self._change_tribal)
        
        # Subtype
        self._subtype_line.setText(self._card.get_subtype_print())
        self._left_layout.addRow("Alatyyppi:", self._subtype_line)
        self._subtype_line.textChanged[str].connect(self._change_subtype)
        
        # Draw colour checkboxes
        colour_red_box = QCheckBox("Punainen")
        colour_blue_box = QCheckBox("Sininen")
        colour_green_box = QCheckBox("Vihreä")
        colour_white_box = QCheckBox("Valkoinen")
        colour_black_box = QCheckBox("Musta")
        self._colour_boxes = [colour_red_box, colour_blue_box, colour_green_box, \
                        colour_white_box, colour_black_box]
        self._left_layout.addRow("Väri:", colour_red_box)
        self._left_layout.addRow(colour_blue_box, colour_green_box)
        self._left_layout.addRow(colour_white_box, colour_black_box)
        
        self._set_colour_boxes()
        self._change_colour_state()
        
        # Power
        self._power_spinbox.setRange(0, 20)
        self._power_spinbox.setValue(self._card.get_power_print())
        self._left_layout.addRow("Voimakkuus:", self._power_spinbox)
        self._power_spinbox.valueChanged.connect(self._change_power)
        
        # Toughness
        self._toughness_spinbox.setRange(0, 20)
        self._toughness_spinbox.setValue(self._card.get_toughness_print())
        self._left_layout.addRow("Kestävyys:", self._toughness_spinbox)
        self._toughness_spinbox.valueChanged.connect(self._change_toughness)
        
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
        self._change_feature_box_state()
        
        # Rule text
        self._ruletext_line.setText(self._card.get_ruletext())
        self._right_layout.addRow("Sääntöteksti:", self._ruletext_line)
        self._ruletext_line.textChanged[str].connect(self._change_ruletext)
        
        # Flavour text
        self._flavourtext_line.setText(self._card.get_flavourtext())
        self._right_layout.addRow("Tarina:", self._flavourtext_line)
        self._flavourtext_line.textChanged[str].connect(self._change_flavourtext)
        
        # Creature
        self._creator_line.setText(self._card.get_creator())
        self._right_layout.addRow("Tekijä:", self._creator_line)
        self._creator_line.textChanged[str].connect(self._change_creator)
        
    def _update_layout(self):
        self._set_card_layout()
        #self._set_leftpanel_layout()
        #self._set_rightpanel_layout()
        
        self._set_middle_layout()
        #self._set_bottom_layout()
        self._set_layouts()        
        
        self.setLayout(self._outer_layout)
        
    # Save to card
    def _change_name(self):
        kks.update_card(self._card, self._name_line.text(), "name")
    def _change_legendary(self):
        is_checked = self._legendary_btn.isChecked()
        kks.update_card(self._card, is_checked, "legendary")
    def _change_tribal(self):
        is_checked = self._tribal_btn.isChecked()
        kks.update_card(self._card, is_checked, "tribal")
    def _change_subtype(self):
        kks.update_card(self._card, self._subtype_line.text(), "subtype")
        self._disable_edit()
    def _change_colour(self, colour_box):
        add = colour_box.isChecked()
        text = colour_box.text()
        kks.update_card(self._card, text, "colour", add)
        self._set_card_frame()             
        self._update_layout()
    def _change_power(self):
        kks.update_card(self._card, self._power_spinbox.value(), "power")
    def _change_toughness(self):
        kks.update_card(self._card, self._toughness_spinbox.value(), "toughness")
    def _change_feature(self, feature_box):
        add = feature_box.isChecked()
        text = feature_box.text()
        kks.update_card(self._card, text, "feature", add)
        self._update_layout()
    def _change_ruletext(self):
        kks.update_card(self._card, self._ruletext_line.text(), "ruletext")
    def _change_flavourtext(self):
        kks.update_card(self._card, self._flavourtext_line.text(), "flavourtext")
    def _change_creator(self):
        kks.update_card(self._card, self._creator_line.text(), "creator")
    def _change_seticon(self):
        kks.update_card(self._card, self._seticon_line.text(), "seticon")
    
    # Colour
    def _set_colour_boxes(self):
        for colour_box in self._colour_boxes:            
            self._check_if_card_has(colour_box, self._card.get_colour())
    
    def _change_colour_state(self):
        self._colour_boxes[0].stateChanged.connect(lambda: self._change_colour(self._colour_boxes[0]))
        self._colour_boxes[1].stateChanged.connect(lambda: self._change_colour(self._colour_boxes[1]))
        self._colour_boxes[2].stateChanged.connect(lambda: self._change_colour(self._colour_boxes[2]))
        self._colour_boxes[3].stateChanged.connect(lambda: self._change_colour(self._colour_boxes[3]))
        self._colour_boxes[4].stateChanged.connect(lambda: self._change_colour(self._colour_boxes[4]))
    
    # Feature       
    def _set_feature_boxes(self):
        for feature_box in self._feature_boxes:
            self._check_if_card_has(feature_box, self._card.get_feature_list())
            
    def _change_feature_box_state(self):
        self._feature_boxes[0].stateChanged.connect(lambda: self._change_feature(self._feature_boxes[0]))
        self._feature_boxes[1].stateChanged.connect(lambda: self._change_feature(self._feature_boxes[1]))
        self._feature_boxes[2].stateChanged.connect(lambda: self._change_feature(self._feature_boxes[2]))
        self._feature_boxes[3].stateChanged.connect(lambda: self._change_feature(self._feature_boxes[3]))
        self._feature_boxes[4].stateChanged.connect(lambda: self._change_feature(self._feature_boxes[4]))
        self._feature_boxes[5].stateChanged.connect(lambda: self._change_feature(self._feature_boxes[5]))
        self._feature_boxes[6].stateChanged.connect(lambda: self._change_feature(self._feature_boxes[6]))
        self._feature_boxes[7].stateChanged.connect(lambda: self._change_feature(self._feature_boxes[7]))
        self._feature_boxes[8].stateChanged.connect(lambda: self._change_feature(self._feature_boxes[8]))
        self._feature_boxes[9].stateChanged.connect(lambda: self._change_feature(self._feature_boxes[9]))
        self._feature_boxes[10].stateChanged.connect(lambda: self._change_feature(self._feature_boxes[10]))
        self._feature_boxes[11].stateChanged.connect(lambda: self._change_feature(self._feature_boxes[11]))
        self._feature_boxes[12].stateChanged.connect(lambda: self._change_feature(self._feature_boxes[12]))
        self._feature_boxes[13].stateChanged.connect(lambda: self._change_feature(self._feature_boxes[13]))
    
    # Maintype
    def _set_maintype_combo(self):
        index = self._maintype_combo.findText(self._card.get_maintype())  # finds the index of the item wanted
        self._maintype_combo.setCurrentIndex(index)        
        self._disable_edit()
        
    def _change_maintype(self):
        self._card = kks.change_card_type(self._card, self._maintype_combo.currentText())        
        self._disable_edit()
        
  
    # Legendary
    def _set_legendary_btn(self):
        is_checked =  self._card.get_legendary()
        if is_checked is not None:
            self._legendary_btn.setChecked(is_checked)
            
    # Tribal
    def _set_tribal_btn(self):
        is_checked = self._card.get_tribal()
        if is_checked is not None:
            self._tribal_btn.setChecked(is_checked)
            
    # Set card frame image
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
    
    # Set checkboxes
    def _check_if_card_has(self, checkbox, cards_list):
        if checkbox.text() in cards_list:
            checkbox.setChecked(True)
        else:
            checkbox.setChecked(False)
    
    # Disable unused properties
    def _disable_edit(self):
        if self._card.get_legendary() is None:
            self._legendary_btn.setEnabled(False)
            self._legendary_btn.setChecked(False)
        else:
            self._legendary_btn.setEnabled(True)
        if self._card.get_tribal() is None:
            self._tribal_btn.setEnabled(False)
            self._tribal_btn.setChecked(False)
        else:
            self._tribal_btn.setEnabled(True)
        if self._card.get_subtype() is None:
            self._subtype_line.setEnabled(False)
        else:
            self._subtype_line.setEnabled(True)
        if self._card.get_power() is None:
            self._power_spinbox.setEnabled(False)
            self._power_spinbox.setValue(0)
        else:
            self._power_spinbox.setEnabled(True)
        if self._card.get_toughness() is None:
            self._toughness_spinbox.setEnabled(False)
            self._toughness_spinbox.setValue(0)
        else:
            self._toughness_spinbox.setEnabled(True)
        if self._card.get_feature() is None:
            for box in self._feature_boxes:
                box.setEnabled(False)
                box.setChecked(False)
        else:
            for box in self._feature_boxes:
                box.setEnabled(True)
        if self._card.get_feature2_list():
            for box in self._feature_boxes:
                if box.text() not in self._card.get_feature2_list():
                    box.setEnabled(False)
                    box.setChecked(False)
    
    # Save card to database and return to card view
    def _save_and_return(self):
        kks.save_to_database(self._card)
        self._handle_show_card_view(self._card)
        
    # Other
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
