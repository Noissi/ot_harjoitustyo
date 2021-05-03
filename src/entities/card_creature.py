from entities.card import Card

class Creature(Card):
    """ Card subclass that represents a single Creature card.

    Attributes:
        _maintype: [String] Card's maintype is Creature.
        _tribal: [None] Creature does not have tribal.
    """

    def __init__(self, name):
        """ Class constructor. Creates a new card.
        Args:
            name: [String] Name of the card.
        """

        super().__init__(name)
        self._maintype = "Creature"
        self._tribal = None
