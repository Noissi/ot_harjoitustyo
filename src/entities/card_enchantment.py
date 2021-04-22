from entities.card import Card

class Enchantment(Card):
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
        self._maintype = "Enchantment"
        self._feature2 = ["Hexproof", "Indestructible", "Flash"]
        self._power = None
        self._toughness = None
