from entities.card import Card

class Sorcery(Card):
    """ Card subclass that represents a single Sorcery card.

    Attributes:
        _maintype: [String] Card's maintype is Sorcery.
        _feature: [None] Sorcery has no feature.
        _power: [None] Sorcery has no power.
        _toughness: [None] Sorcery has no toughness.
    """

    def __init__(self, name):
        """ Class constructor. Creates a new card.
        Args:
            name: [String] Name of the card.
        """

        super().__init__(name)
        self._maintype = "Sorcery"
        self._feature = None
        self._power = None
        self._toughness = None
