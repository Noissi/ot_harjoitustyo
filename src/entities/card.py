import uuid
#import User

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
    
    def __init__(self, name):
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
        self.card_id = str(uuid.uuid4())
        self.colour = []
        self.multicolour = False
        self.image = None
        self.maintype = None
        self.subtype = []
        self.feature = []
        self.ruletext = ""
        self.flavourtext = ""
        self.creator = None
        self.seticon = None
        self.rarity = None
    
    ## Set
    def set_name(self, name):
        self.name = name
        
    def set_image(self, image):
        self.image = image
        
    def set_maintype(self, maintype):
        self.maintype = maintype
    
    def set_subtype(self, subtype):
        self.subtype = subtype
        
    def set_ruletext(self, ruletext):
        self.ruletext = ruletext
        
    def set_flavourtext(self, flavoutext):
        self.flavourtext = flavourtext
        
    def set_creator(self, creator):
        self.creator = creator
        
    def set_seticon(self, seticon):
        self.seticon = seticon
    
    def set_rarity(self, rarity):
        self.rarity = rarity
        
    #def set_(self, ):
    #    self. = 
    
    ## Get
    def get_card_colour(self):
        if self.multicolour:
            return "Kulta"
        elif not self.colour:
            return "Sininen"
        return self.colour[0]
        
    def get_colour(self):
        return ', '.join(self.colour)
        
    def get_subtype(self):
        return ', '.join(self.subtype)
        
    ## Add    
    def add_colour(self, colour):
        self.colour.append(colour)
        self._check_if_multicolour()  
        
    def add_feature(self, feature):
        self.feature.append(feature)
        
    ## Remove    
    def remove_colour(self, colour):
        if colour in self.colour:
            print("remove colour:")
            print(self.colour)
            self.colour.remove(colour)
        self._check_if_multicolour()
        
    def remove_feature(self, feature):
        if feature in self.feature:
            self.feature.remove(feature)
    
    ## Other
    def _string_to_list(self, string):
        list = split(string, ",")
        return list
        

        
    def _check_if_multicolour(self):
        if len(self.colour) > 1:
            self.multicolour = True
        else:
            self.multicolour = False
        
    def show_card(self):
        print('show card')
        
        
