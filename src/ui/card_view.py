from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from ui.window import Window
from entities.card_creature import Creature

class CardView(Window):
    def __init__(self, handle_show_game_view, handle_show_edit_card_view):
        super().__init__()
        self._handle_show_edit_card_view = handle_show_edit_card_view
        self._handle_show_game_view = handle_show_game_view
        
        self._card = Creature("Teemu Kerppu")
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
        # Draw bottom edit box
        btn_edit = QPushButton('Muokkaa')
        btn_edit.setMaximumWidth(100)
        btn_edit.clicked.connect(self._handle_show_edit_card_view)
        self._bottom_layout.addWidget(btn_edit)
        
    def _set_card_layout(self):
        self._card_layout = QGridLayout()
        # Draw card frame
        card_frame_scaled = self._card_frame.scaledToWidth(self.width-1000)
        card_frame_label = QLabel(alignment=Qt.AlignCenter)
        card_frame_label.setPixmap(card_frame_scaled)
        self._card_layout.addWidget(card_frame_label)
        
        # Write card name
        name_label = QLabel()
        name_label.setText('<font color="red", font size="4"> Kiljukuikka </font>')
        name_label.move(500,-700)
        self._card_layout.addWidget(name_label)
        
    def _set_leftpanel_layout(self):
        # Draw left side panel
        self._left_layout.addRow("Name", QLabel("Kiljukuikka"))
        #self._left_layout.addRow("Type:", QLabel(self._card.maintype))
        #self._left_layout.addRow("Subtype:", QLabel(self._card.subtype))
        #self._left_layout.addRow("Colour:", QLabel(self._name.get_colour()))
        
    def _set_rightpanel_layout(self):
        # Set the right side panel
        self._right_layout.addRow("Sääntö:", QLabel("When somethind tap everything."))
        self._right_layout.addRow("Teksti:", QLabel("Kuiik kuiik!"))
        self._right_layout.addRow("Tekijä:", QLabel("Peruna"))
                     
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

        print('card')
