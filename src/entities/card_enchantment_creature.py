from entities.card import Card

class EnchantmentCreature(Card):
    """ Card subclass that represents a single Enchantment Creature card.

    Attributes:
        _maintype: [String] Card's maintype is Enchantment Creature.
        _tribal: [None] Enchantment Creature does not have tribal.
    """

    def __init__(self, name):
        """ Class constructor. Creates a new card.
        Args:
            name: [String] Name of the card.
        """

        super().__init__(name)
        self._maintype = "Enchantment Creature"
        self._tribal = None
