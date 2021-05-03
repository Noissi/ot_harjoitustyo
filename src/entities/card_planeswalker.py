from entities.card import Card

class Planeswalker(Card):
    """ Card subclass that represents a single Planeswalker card.

    Attributes:
        _maintype: [String] Card's maintype is Planeswalker.
        _tribal: [None] Planeswalker does not have tribal.
    """

    def __init__(self, name):
        """ Class constructor. Creates a new card.
        Args:
            name: [String] Name of the card.
        """

        super().__init__(name)
        self._maintype = "Planeswalker"
        self._tribal = None
