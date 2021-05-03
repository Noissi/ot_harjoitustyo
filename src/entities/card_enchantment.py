from entities.card import Card

class Enchantment(Card):
    """ Card subclass that represents a single Enchantment card.

    Attributes:
        _maintype: [String] Card's maintype is Enchantment.
        _feature2: [List String] If the card has a limited set of
                   features, the available features are listed here.
        _power: [None] Enchantment has no power.
        _toughness: [None] Enchantment has no toughness.
    """

    def __init__(self, name):
        """ Class constructor. Creates a new card.
        Args:
            name: [String] Name of the card.
        """

        super().__init__(name)
        self._maintype = "Enchantment"
        self._feature2 = ["Hexproof", "Indestructible", "Flash"]
        self._power = None
        self._toughness = None
