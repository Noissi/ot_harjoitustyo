from entities.card import Card

class Artifact(Card):
    """Luokka joka kuvaa yksittaista korttia

    Attributes:
        manacost:
    """

    def __init__(self, name):
        """Luokan konstruktori. Luo uuden kortin.

        Args:
            manacost:
                ???
        """
        super().__init__(name)
        self._maintype = "Artifact"
        self._feature2 = ["Hexproof", "Indestructible", "Flash"]
        self._power = None
        self._toughness = None

    def set_subtype(self, subtype):
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
