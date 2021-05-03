from entities.card import Card

class Land(Card):
    """ Card subclass that represents a single Land card.

    Attributes:
        _maintype: [String] Card's maintype is Land.
        _tribal: [None] Land does not have tribal.
        _feature2: [List String] If the card has a limited set
                   of features, the available features are listed here.
        _manacost: [None] Instant has no manacost.
        _power: [None] Instant has no power.
        _toughness: [None] Instant has no toughness.
    """

    def __init__(self, name):
        """ Class constructor. Creates a new card.
        Args:
            name: [String] Name of the card.
        """

        super().__init__(name)
        self._maintype = "Land"
        self._tribal = None
        self._feature2 = ["Hexproof", "Indestructible"]
        self._manacost = None
        self._power = None
        self._toughness = None
