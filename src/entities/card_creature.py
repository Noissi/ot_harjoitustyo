from entities.card import Card

class Creature(Card):
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
        self._maintype = "Creature"
        self._tribal = None
