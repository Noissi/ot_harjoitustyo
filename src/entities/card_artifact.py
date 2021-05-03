from entities.card import Card

class Artifact(Card):
    """ Card subclass that represents a single Artifact card.

    Attributes:
        _maintype: [String] Card's maintype is Artifact.
        _feature2: [List String] If the card has a limited set
                   of features, the available features are listed here.
        _power: [Integer] Artifact has no power (unless subtype includes 'Vehicle').
        _toughness: [Integer] Artifact has no toughness (unless subtype includes 'Vehicle').
    """

    def __init__(self, name):
        """ Class constructor. Creates a new card.
        Args:
            name: [String] Name of the card.
        """

        super().__init__(name)
        self._maintype = "Artifact"
        self._feature2 = ["Hexproof", "Indestructible", "Flash"]
        self._power = None
        self._toughness = None

    def set_subtype(self, subtype):
        """ Sets card's subtypes. If subtype includes 'Vehicle', power and toughness are set on.
        Args:
            subtype: [List or String] List of subtypes or a string of them to be set.
        """

        if subtype is not None:
            if isinstance(subtype, list):
                self._subtype = subtype
            else:
                self._subtype = subtype.split(" ")
            if self.get_subtype() == ["Vehicle"]:
                self._power = 0
                self._toughness = 0
            else:
                self._power = None
                self._toughness = None
