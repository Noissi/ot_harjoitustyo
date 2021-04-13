import sys
from ui.login_view import LoginView
from ui.create_user_view import CreateUserView
from ui.main_view import MainView
from ui.cube_view import CubeView
from ui.card_view import CardView
from ui.edit_card_view import EditCardView
from PySide6.QtWidgets import *
from services.korttikube_service import korttikube_service as kks

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.current_view = None
        
        self._layout = QVBoxLayout()
        self.setLayout(self._layout)
        self._stacked_layout = QStackedLayout()
        
        print("ui")
        
    def start(self):
        self._show_login_view()
        #self._show_card_view(card)
        
    def _switch_view(self, view):
        print('switch view')
        self._layout = QVBoxLayout()
        self._stacked_layout.addWidget(view)        
        self._layout.addLayout(self._stacked_layout)
        self._stacked_layout.setCurrentIndex(2)
        
    def _end(self):
        sys.exit()
        
    def _hide_current_view(self):
        if self.current_view:
            self.current_view.hide()
            print('hide')
        self.current_view = None
        
    def _add_stacked_views(self):
        if self._current_view:
            self.stackedLayout.addWidget()
        
    def _show_login_view(self):
        #self._hide_current_view()
        self._login_view = LoginView(self._show_create_user_view, self._show_cube_view, self._end)
        self.current_view = self._login_view
        self._stacked_layout.addWidget(self._login_view)
        self._stacked_layout.setCurrentWidget(self._login_view)
        print('login ui')
        
    def _show_create_user_view(self):
        self._create_user_view = CreateUserView(self._show_login_view)
        self._current_view = self._create_user_view
        self._stacked_layout.addWidget(self._create_user_view)
        self._stacked_layout.setCurrentWidget(self._create_user_view)
        
    def _show_main_view(self):
        self._hide_current_view()
        self.current_view = MainView(self._show_login_view, self._show_cube_view)
        
    def _show_cube_view(self):
        #self._hide_current_view()
        kks.exit_card()
        self._cube_view = CubeView(self._show_main_view, self._show_card_view, self._show_edit_card_view)
        self.current_view = self._cube_view
        self._stacked_layout.addWidget(self._cube_view)
        self._stacked_layout.setCurrentWidget(self._cube_view)
        
    def _show_card_view(self, card):
        if not kks.get_card():
            kks.enter_card(card)
        self._card_view = CardView(self._show_cube_view, self._show_edit_card_view)
        self.current_view = self._card_view
        self._stacked_layout.addWidget(self._card_view)
        self._stacked_layout.setCurrentWidget(self._card_view)
        print('card ui')
        
    def _show_edit_card_view(self):
        if not kks.get_card():
            kks.create_card("Teemu Teekkari")
        self._edit_card_view = EditCardView(self._show_cube_view, self._show_card_view)
        self.current_view = self._edit_card_view
        self._stacked_layout.addWidget(self._edit_card_view)
        self._stacked_layout.setCurrentWidget(self._edit_card_view)
