from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from ui.window import Window
from entities.card_creature import Creature
from services.korttikube_service import korttikube_service as kks
from config import CARD_RATIO

class MainView(Window):
    def __init__(self, handle_show_login_view=None, handle_show_cube_view=None):
        super().__init__()
        self._handle_show_login_view = handle_show_login_view
        self._handle_show_cube_view = handle_show_cube_view
        
        self.left=10
        self.top=10
        self.width=1500
        self.height=1000        
        
        self._outer_layout = self.get_outer_layout()
        self._upper_layout = QHBoxLayout()
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
        # Upper layout
        btn_new = QPushButton('Uusi kube')        
        btn_new.setMaximumWidth(100)
        btn_new.clicked.connect(self._create_cube)
        self._upper_layout.addWidget(btn_new)
        
    def _set_cubelist_layout(self):
        # Cubelist layout
        btn_cube = QPushButton("Testi cube")
        btn_cube.setMinimumSize(200, 200)
        btn_cube.setMaximumSize(200, 200)
        image = "img/mri.jpeg"
        # changing font and size of text
        btn_cube.setFont(QFont('Times', 30))
        btn_cube.setStyleSheet("QPushButton{border-image: url("+image+")}"
                               "QPushButton{color: white}")
        btn_cube.clicked.connect(self._handle_show_cube_view)
        self._scroll_layout.addWidget(btn_cube, 1, 0)
        
        btn_cube2 = QPushButton("Cubekube")
        btn_cube2.setMinimumSize(200, 200)
        btn_cube2.setMaximumSize(200, 200)
        image = "img/kana.jpeg"
        # changing font and size of text
        btn_cube2.setFont(QFont('Times', 30))
        btn_cube2.setStyleSheet("QPushButton{border-image: url("+image+")}"
                               "QPushButton{color: white}")
        btn_cube2.clicked.connect(self._handle_show_cube_view)
        self._scroll_layout.addWidget(btn_cube2, 1, 1)
        
        btn_cube3 = QPushButton("Otakube")
        btn_cube3.setMinimumSize(200, 200)
        btn_cube3.setMaximumSize(200, 200)
        image = "img/dipoli.jpeg"
        # changing font and size of text
        btn_cube3.setFont(QFont('Times', 30))
        btn_cube3.setStyleSheet("QPushButton{border-image: url("+image+")}"
                               "QPushButton{color: white}")
        btn_cube3.clicked.connect(self._handle_show_cube_view)
        self._scroll_layout.addWidget(btn_cube3, 1, 2)

    def _set_bottom_layout(self):
        # Bottom layout
        btn_logout = QPushButton('Kirjaudu ulos')
        btn_logout.clicked.connect(self._handle_show_login_view)
        self._bottom_layout.addWidget(btn_logout)
        
    def _create_cube(self):
        msg = QMessageBox()        
        msg.setText('Uusi kube luotu')
        msg.exec_()
        
    def _initialise(self):        
        
        # Set background image
        image = QImage("img/mtg_puu.jpg")
        image_scaled = image.scaled(QSize(self.width, self.height)) # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(image_scaled))
        self.setPalette(palette)
        
        self._set_upper_layout()
        self._set_cubelist_layout()
        self._set_bottom_layout()
        
        self._outer_layout.addLayout(self._upper_layout, 1, 0)
        self._outer_layout.addWidget(self._scroll, 2, 0, 8, 1)
        #self._outer_layout.addLayout(self._collection_layout, 2, 0, 8, 1)
        self._outer_layout.addLayout(self._bottom_layout, 10, 0)
        
        self.setLayout(self._outer_layout)
        
        
        print('cube')

