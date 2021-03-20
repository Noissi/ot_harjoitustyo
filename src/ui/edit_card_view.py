from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from ui.window import Window

class EditCardView(Window):
    def __init__(self, handle_show_game_view, handle_show_card_view):
        super().__init__()
        self._handle_show_card_view = handle_show_card_view
        self._handle_show_game_view = handle_show_game_view
        self._card = None
        self._card_frame = QPixmap("img/bluecard.png")
        
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
        
        widget = QWidget(self)
        widget.setLayout(self._outer_layout)
        self.setCentralWidget(widget)
        self.centralWidget().setLayout(self._outer_layout)
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
        # Draw bottom edit box
        btn_edit = QPushButton('Tallenna')
        btn_edit.setMaximumWidth(100)
        btn_edit.clicked.connect(self._handle_show_card_view)
        self._bottom_layout.addWidget(btn_edit)
        
    def _set_card_layout(self):
        self._card_layout = QGridLayout()
        print(self._card_frame)
        # Draw card frame
        card_frame_scaled = self._card_frame.scaledToWidth(self.width-1000)
        card_frame_label = QLabel(alignment=Qt.AlignCenter)
        card_frame_label.setPixmap(card_frame_scaled)
        self._card_layout.addWidget(card_frame_label)
        
        # Write card name
        name_label = QLabel()
        name_label.setText('<font color="red", font size="4"> Kiljukuikka </font>')
        name_label.move(500,-200)
        self._card_layout.addWidget(name_label)
        
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
        self._left_layout.addRow("Alatyyppi:", QLineEdit())
        
        # Draw color checkboxes
        color_red_box = QCheckBox("Punainen")
        color_blue_box = QCheckBox("Sininen")
        color_green_box = QCheckBox("Vihreä")
        color_white_box = QCheckBox("Valkoinen")
        color_black_box = QCheckBox("Musta")
        color_colorless_box = QCheckBox("Väritön")
        self._left_layout.addRow("Väri:", color_red_box)
        self._left_layout.addRow(color_blue_box)
        self._left_layout.addRow(color_green_box)
        self._left_layout.addRow(color_white_box)
        self._left_layout.addRow(color_black_box)
        self._left_layout.addRow(color_colorless_box)
        color_red_box.stateChanged.connect(lambda: self._change_color(color_red_box))
        color_blue_box.stateChanged.connect(self._change_color(color_blue_box))
        color_green_box.stateChanged.connect(self._change_color(color_green_box))
        
    def _set_rightpanel_layout(self):
        # Set the right side panel
        self._right_layout.addRow("Sääntö:", QLineEdit())
        self._right_layout.addRow("Teksti:", QLineEdit())
        self._right_layout.addRow("Tekijä:", QLineEdit())
        
    def _change_color(self, color):
        print(color.isChecked())
        if color.isChecked() == True:
            print("red2")
            if color.text() == "Punainen":
                print("red")
                self._card_frame = QPixmap("img/redcard.png")
                self._set_card_layout()
                self._set_middle_layout()
                self._set_layouts()
                
        
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

        print('card')
