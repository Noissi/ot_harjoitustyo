import uuid
import User

class Card:
    """Luokka joka kuvaa yksittaista korttia
    
    Attributes:
        card_id: , kuvaa kortin yksilollista tunnistetta
        name: Merkkijono, joka kuvaa kortin nimea
        colour: Merkkijono, joka kuvaa kortin varia
        manacost: Kokonaisluku, joka kuvaa kortin manahintaa
        rules: Merkkijono, joka kuvaa kortin saantoja
        text: Merkkijono, joka kuvaa kortin valinnaista teksia
        creator: Merkkijono, joka kuvaa kortin tekijaa
        image: , joka kuvaa osoitetta kortin kuvaan
    """
    
    def __init__(self, name, colour=None, manacost=None, rules=None, text=None, creator=user, image=None):
        """Luokan konstruktori. Luo uuden kortin.
    
        Args:
            name:
                Merkkijono, joka kuvaa kortin nimea
            colour: 
                Vapaaehtoinen, oletusarvoisesti None.
                Merkkijono, joka kuvaa kortin varia
            manacost:
                Vapaaehtoinen, oletusarvoisesti None.
                Kokonaisluku, joka kuvaa kortin manahintaa
            rules:
                Vapaaehtoinen, oletusarvoisesti None.
                Merkkijono, joka kuvaa kortin saantoja
            text:
                Vapaaehtoinen, oletusarvoisesti None.
                Merkkijono, joka kuvaa kortin valinnaista teksia
            creator:
                Vapaaehtoinen, oletusarvoisesti user.
                Merkkijono, joka kuvaa kortin tekijaa
            image:
                Vapaaehtoinen, oletusarvoisesti None.
                , joka kuvaa osoitetta kortin kuvaan
        """
        
        self.name = name
        self.colour = colour
        self.manacost = manacost
        self.card_id = str(uuid.uuid4())
        
