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
    """ Class responsible for ui.
    """

    def __init__(self):
        """ Class constructor. Creates a new ui control.

        Args:
            current_view: The view that is currently visible to the user.
            layout: The main layout.
        """

        super().__init__()
        self.current_view = None
        
        self._layout = QVBoxLayout()
        self.setLayout(self._layout)
        self._stacked_layout = QStackedLayout()

    def start(self):
        """ Starts the ui control. Shows the login view.
        """

        self._show_login_view()
        
    def _switch_view(self, view):
        print('switch view')
        self._layout = QVBoxLayout()
        self._stacked_layout.addWidget(view)        
        self._layout.addLayout(self._stacked_layout)
        self._stacked_layout.setCurrentIndex(2)
        
    def _end(self):
        """ Ends the program.
        """

        sys.exit()
        
    def _add_stacked_views(self):
        if self._current_view:
            self.stackedLayout.addWidget()
        
    def _show_login_view(self):
        """ Shows the login view and sets it as a current view.
        """

        self._login_view = LoginView(self._show_create_user_view,
                                     self._show_main_view, self._end)
        self.current_view = self._login_view
        self._stacked_layout.addWidget(self._login_view)
        self._stacked_layout.setCurrentWidget(self._login_view)
        
    def _show_create_user_view(self):
        """ Shows the create user view and sets it as a current view.
        """

        self._create_user_view = CreateUserView(self._show_login_view)
        self._current_view = self._create_user_view
        self._stacked_layout.addWidget(self._create_user_view)
        self._stacked_layout.setCurrentWidget(self._create_user_view)
        
    def _show_main_view(self):
        """ Shows the main view and sets it as a current view. Removes the possible
            current cube. If there was no current user, creates one and sets it as
            a curent user.
        """

        kks.exit_cube()
        if not kks.get_user():
            user = kks.create_user("peruna", "salasana")
            kks.set_user(user)
        self._main_view = MainView(self._show_login_view, self._show_cube_view)
        self.current_view = self._main_view
        self._stacked_layout.addWidget(self._main_view)
        self._stacked_layout.setCurrentWidget(self._main_view)
        
    def _show_cube_view(self, cube=None):
        """ Shows the cube view and sets it as a current view. Removes the possible
            current card. If there were no current cube, sets the curent cube.
        Args:
            cube: [Cube] Optional. Current cube.
        """

        kks.exit_card()
        if not kks.get_cube():
            kks.enter_cube(cube)
        self._cube_view = CubeView(self._show_main_view, self._show_card_view,
                                   self._show_edit_card_view)
        self.current_view = self._cube_view
        self._stacked_layout.addWidget(self._cube_view)
        self._stacked_layout.setCurrentWidget(self._cube_view)
        
    def _show_card_view(self, card=None):
        """ Shows the card view and sets it as a current view. If there were no
            current card, sets the curent card.
        Args:
            card: [Card] Optional. Current card.
        """

        if not kks.get_card():
            kks.enter_card(card)
        self._card_view = CardView(self._show_cube_view, self._show_edit_card_view)
        self.current_view = self._card_view
        self._stacked_layout.addWidget(self._card_view)
        self._stacked_layout.setCurrentWidget(self._card_view)

    def _show_edit_card_view(self, new_card=False):
        """ Shows the edit card view and sets it as a current view. If there were no
            current card, creates one and sets it as the curent card.
        Args:
            new: [Boolean] Optional. If True, creates a new Card entity.
        """

        if not kks.get_card():
            card = kks.create_card_entity("")
            kks.set_card(card)
        self._edit_card_view = EditCardView(self._show_cube_view,
                                            self._show_card_view, new_card)
        self.current_view = self._edit_card_view
        self._stacked_layout.addWidget(self._edit_card_view)
        self._stacked_layout.setCurrentWidget(self._edit_card_view)
