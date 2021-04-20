import uuid
import User

class Game:
    """Luokka joka kuvaa yksittaista pelia.
    
    Attributes:
        name: Merkkijono, joka kuvaa pelin nimea.
        users: Lista kayttajista, joilla on oikeus peliin.
        game_id: , joka kuvaa pelin yksilollista tunnistetta.
    """
    
    def __init__(self, name, users=[user]):
        """Luokan konstruktori. Luo uuden pelin.
    
        Args:
            name:
                Merkkijono, joka kuvaa pelin nimea.
            users:
                Luodessa oletusarvoisesti lisataan pelin luoja.
                Lista kayttajista, joilla on oikeus peliin.
            game_id:
                , joka kuvaa pelin yksilollista tunnistetta.
        """
        
        self.name = name
        self.users = users
        self.card_id = str(uuid.uuid4())
        
