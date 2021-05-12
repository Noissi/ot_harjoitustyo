from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Window(QWidget):
    """ Class responsible for ui geometries.
    """

    def __init__(self):
        super().__init__()

        self._outer_layout   = QGridLayout()
        self._stacked_layout = QStackedLayout()
        self._page_combo     = QComboBox()

        self.left   = 10
        self.top    = 10
        self.width  = 1500
        self.height = 1000
        self.setGeometry(self.left, self.top, self.width, self.height)

        #self._initialise_menu()

    def get_outer_layout(self):
        return self._outer_layout

    def get_stacked_layout(self):
        return self._stacked_layout

    def add_stacked_widget(self, widget):
        self._stacked_layout.addWidget(widget)

    def switch_page(self):
        self.stacked_layout.setCurrentIndex(self.pageCombo.currentIndex())

    def _initialise_menu(self):
        # Create menu
        menubar = QMenuBar()
        #menubar.setGeometry(0,0,100,100)
        self._outer_layout.addWidget(menubar, 0, 0)
        action_main_page = menubar.addMenu("Etusivu")
        action_main_page.addAction("Open")
        action_main_page.addAction("Save")
        action_main_page.addSeparator()
        action_main_page.addAction("Quit")
        menubar.addMenu("Edit")
        menubar.addMenu("View")
        menubar.addMenu("Help")
