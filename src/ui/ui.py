import sys
from ui.login_view import LoginView
from ui.create_user_view import CreateUserView
from ui.main_view import MainView
from ui.game_view import GameView
from ui.card_view import CardView
from ui.edit_card_view import EditCardView
from PySide6.QtWidgets import QWidget

class UI:
    def __init__(self):
        print("ui")
        super().__init__()
        self._current_view = None
        
    def start(self):
        self._show_login_view()
        
    def _end(self):
        sys.exit()
        
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.hide()
        self._current_view = None
        
    def _add_stacked_views(self):
        if self._current_view:
            self.stackedLayout.addWidget()
        
    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(self._show_create_user_view, self._show_card_view, self._end)
        self._current_view.show()
        
    def _show_create_user_view(self):
        self._hide_current_view()
        self._current_view = CreateUserView(self._show_login_view)
        self._current_view.show()
        
    def _show_main_view(self):
        self._hide_current_view()
        self._current_view = MainView(self._show_login_view, self._show_game_view)
        self._current_view.show()
        
    def _show_game_view(self):
        self._hide_current_view()
        self._current_view = GameView(self._show_main_view, self._show_card_view)
        self._current_view.show()
        
    def _show_card_view(self):
        self._hide_current_view()
        self._current_view = CardView(self._show_game_view, self._show_edit_card_view)
        self._current_view.show()
        
    def _show_edit_card_view(self):
        self._hide_current_view()
        self._current_view = EditCardView(self._show_game_view, self._show_card_view)
        self._current_view.show()
