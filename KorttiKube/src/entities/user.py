class User:
    """Luokka joka kuvaa yksittaista kayttajaa
    
    Attributes:
        username: Merkkijono, joka kuvaa kayttajan nimea.
        password: Merkkijono, joka kuvaa kayttajan salasanaa.
        games: Lista peleista, joka kuvaa pelaajan luomia peleja.
        shared_games: Lista peleista, joka kuvaa pelaajalle jaettuja peleja.
    """
    
    def __init__(self, username, password):
        """Luokan konstruktori. Luo uuden kayttajan.
    
        Args:
            username: 
                Merkkijono, joka kuvaa kayttajan nimea.
            password:
                Merkkijono, joka kuvaa kayttajan salasanaa.
            games:
                Luodessa lista on tyhja.
                Lista peleista, joka kuvaa pelaajan luomia peleja.
            shared_games:
                Luodessa lista on tyhja.
                Lista peleista, joka kuvaa pelaajalle jaettuja peleja.
        """
        
        self.username = username
        self.password = password
        self.games = []
        self.shared_games = []
        
