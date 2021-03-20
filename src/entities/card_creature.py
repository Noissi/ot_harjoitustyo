import uuid
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
        self.manacost = None
        self.power = None
        self.toughness = None
        
        
    def set_manacost(self, manacost):
        self.manacost = manacost
        
    def set_power(self, power):
        self.power = power
        
    def set_toughness(self, toughness):
        self.toughness = toughness
        
        
