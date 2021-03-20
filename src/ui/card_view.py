from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from ui.window import Window

class CardView(Window):
    def __init__(self, handle_show_game_view, handle_show_edit_card_view):
        super().__init__()
        self._handle_show_edit_card_view = handle_show_edit_card_view
        self._handle_show_game_view = handle_show_game_view
        
        
        self._initialise()       
        
    def _initialise(self):
        
        # Set background image
        image = QImage("img/card.jpg")
        image_scaled = image.scaled(QSize(self.width, self.height)) # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(image_scaled))                        
        self.setPalette(palette)
        
        # Set layouts
        widget = QWidget(self)
        outer_layout = self.get_outer_layout()
        top_layout = QHBoxLayout()
        middle_layout = QGridLayout()        
        bottom_layout = QHBoxLayout()
        card_layout = QGridLayout()
        left_layout = QFormLayout()
        left2_layout = QStackedLayout()
        right_layout = QFormLayout()
        
        # Modify layouts
        button_back = QPushButton('Takaisin peleihin')
        button_back.clicked.connect(self._handle_show_game_view)
        top_layout.addWidget(button_back)        
        
        
        # Draw card frame
        card_frame = QPixmap("img/bluecard.png")
        card_frame_scaled = card_frame.scaledToWidth(self.width-1000)
        card_frame_label = QLabel(alignment=Qt.AlignCenter)
        card_frame_label.setPixmap(card_frame_scaled)
        card_layout.addWidget(card_frame_label)
        
        # Write card name
        name_label = QLabel()
        name_label.setText('<font color="red", font size="4"> Kiljukuikka </font>')
        name_label.move(500,-200)
        card_layout.addWidget(name_label)
        
        # Draw left side panel
        left_layout.addRow("Nimi:", QLabel("Kiljukuikka"))
        left_layout.addRow("Tyyppi:", QLabel("Creature"))
        left_layout.addRow("Alatyyppi:", QLabel("Beast Bird"))
        left_layout.addRow("Väri:", QLabel("Punainen"))
        
        # Set the right side panel
        right_layout.addRow("Sääntö:", QLabel("When somethind tap everything."))
        right_layout.addRow("Teksti:", QLabel("Kuiik kuiik!"))
        right_layout.addRow("Tekijä:", QLabel("Peruna"))
        
        # Add to middle layout
        middle_layout.addLayout(left_layout, 0, 0)
        middle_layout.addLayout(card_layout, 0, 1)
        middle_layout.addLayout(right_layout, 0, 3)
        
        # Draw bottom edit box
        btn_edit = QPushButton('Muokkaa')
        btn_edit.setMaximumWidth(100)
        btn_edit.clicked.connect(self._handle_show_edit_card_view)
        bottom_layout.addWidget(btn_edit)

        # Set all layouts to outer layout grid
        #outer_layout.addLayout(top_layout, 0, 0)
        outer_layout.addLayout(middle_layout, 1, 0)
        outer_layout.addLayout(bottom_layout, 2, 0)
        
        middle_layout.setContentsMargins(50,50,50,0)
        outer_layout.setContentsMargins(50,50,50,50)
        outer_layout.setSpacing(20)
        
        '''
        outer_layout.setColumnStretch(0, 2)
        outer_layout.setColumnStretch(1, 3)
        outer_layout.setColumnStretch(2, 2)
        outer_layout.setRowStretch(0, 1)        
        outer_layout.setRowStretch(1, 5)
        outer_layout.setRowStretch(2, 1)
        '''
        widget.setLayout(outer_layout)
        
        self.add_stacked_widget(widget)
        self.get_stacked_layout()
        
        self.setCentralWidget(widget)
        self.centralWidget().setLayout(outer_layout)

        print('card')
