from entities.card import Card

class Land(Card):
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
        self._maintype = "Land"
        self._tribal = None
        self._feature2 = ["Hexproof", "Indestructible"]
        self._manacost = None
        self._power = None
        self._toughness = None
