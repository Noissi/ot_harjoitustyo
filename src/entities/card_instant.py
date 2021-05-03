from entities.card import Card

class Instant(Card):
    """ Card subclass that represents a single Instant card.

    Attributes:
        _maintype: [String] Card's maintype is Instant.
        _feature: [None] Instant has no feature.
        _power: [None] Instant has no power.
        _toughness: [None] Instant has no toughness.
    """

    def __init__(self, name):
        """ Class constructor. Creates a new card.
        Args:
            name: [String] Name of the card.
        """

        super().__init__(name)
        self._maintype = "Instant"
        self._feature = None
        self._power = None
        self._toughness = None
