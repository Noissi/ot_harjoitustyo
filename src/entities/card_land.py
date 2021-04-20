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
        
        
    def copy(self, card):
        self.set_id(card.get_id())
        self.set_image(card.get_image())
        self.set_colour(card.get_colour())
        self.set_feature(card.get_feature())
        self.set_legendary(card.get_legendary())
        self.set_subtype(card.get_subtype())      
        self.set_ruletext(card.get_ruletext())
        self.set_flavourtext(card.get_flavourtext())
        self.set_creator(card.get_creator())
        self.set_seticon(card.get_seticon())
        self.set_rarity(card.get_rarity())
        
