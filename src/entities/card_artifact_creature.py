from entities.card import Card

class ArtifactCreature(Card):
    """ Card subclass that represents a single Artifact Creature card.

    Attributes:
        _maintype: [String] Card's maintype is Artifact Creature.
        _tribal: [None] Artifact Creature does not have tribal.
    """

    def __init__(self, name):
        """ Class constructor. Creates a new card.
        Args:
            name: [String] Name of the card.
        """

        super().__init__(name)
        self._maintype = "Artifact Creature"
        self._tribal = None
