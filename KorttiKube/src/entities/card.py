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
        
        self._card_id = str(uuid.uuid4())
        self._cubes = []
        self._name = name
        self._image = ""
        self._colour = []
        self._multicolour = False
        self._maintype = ""
        self._legendary = False
        self._tribal = False
        self._subtype = []
        self._manacost = ""
        self._power = 0
        self._toughness = 0
        self._feature = []
        self._feature2 = []
        self._ruletext = ""
        self._flavourtext = ""
        self._creator = ""
        self._seticon = ""
        self._rarity = ""
        
    
    ## Set
    def set_id(self, card_id):
        self._card_id = card_id
        
    def set_cubes(self, cubes):
        self._cubes = cubes
    
    def set_name(self, name):
        self._name = name
        
    def set_image(self, image):
        if image is not None:
            self._image = image
        
    def set_maintype(self, maintype):
        self._maintype = maintype
        
    def set_legendary(self, boolean):
        if boolean is not None:
            self._legendary = boolean
        
    def set_tribal(self, boolean):
        if boolean is not None:
            self._tribal = boolean
    
    def set_subtype(self, subtype):
        if subtype is not None:
            if type(subtype) is list:
                self._subtype = subtype
            else:
                self._subtype = subtype.split(" ")  

    def set_colour(self, colour):
        if colour is not None:
            if type(colour) is list:
                self._colour = colour
            else:
                self._colour = colour.split(",")
            
    def set_manacost(self, manacost):
        if manacost is not None:
            self._manacost = manacost
            
    def set_power(self, power):
        if power is not None:
            self._power = power
        
    def set_toughness(self, toughness):
        if toughness is not None:
            self._toughness = toughness
            
    def set_feature(self, feature):
        if feature is not None:
            if type(feature) is not list:
                feature = feature.split(",")
            
            if self._feature2:
                for f in feature:
                    if f in self._feature2:
                        self.add_feature(f)
            else:
                self._feature = feature
                    
                
        
    def set_ruletext(self, ruletext):
        if ruletext is not None:
            self._ruletext = ruletext
        
    def set_flavourtext(self, flavourtext):
        if flavourtext is not None:
            self._flavourtext = flavourtext
        
    def set_creator(self, creator):
        if creator is not None:
            self._creator = creator
        
    def set_seticon(self, seticon):
        if seticon is not None:
            self._seticon = seticon
    
    def set_rarity(self, rarity):
        if rarity is not None:
            self._rarity = rarity
    
    ## Get
    def get_id(self):
        return self._card_id
        
    def get_cubes(self):
        return self._cubes
    
    def get_name(self):
        return self._name
        
    def get_image(self):
        return self._image
        
    def get_maintype(self):
        return self._maintype
    
    def get_legendary(self):
        return self._legendary
    
    def get_tribal(self):
        return self._tribal
        
    def get_subtype(self):
        return self._subtype
        
    def get_colour(self):
        return self._colour
        
    def get_manacost(self):
    	return self._manacost 
    
    def get_power(self):
        return self._power
    
    def get_toughness(self):
        return self._toughness
        
    def get_feature(self):
        return self._feature
        
    def get_feature2(self):
        return self._feature2
        
    def get_ruletext(self):
        return self._ruletext
        
    def get_flavourtext(self):
        return self._flavourtext
        
    def get_creator(self):
        return self._creator
    
    def get_seticon(self):
        return self._seticon
        
    def get_rarity(self):
        return self._rarity
        
    ## Get print
    def get_colour_print(self):
        if not self._colour:
            return "Väritön"
        return ', '.join(self._colour)
    
    def get_card_colour(self):
        if self._multicolour:
            return "Kulta"
        elif not self._colour:
            return "Väritön"
        return self._colour[0]
        
    def get_legendary_print(self):
        if self._legendary:
            return "Kyllä"
        return "Ei"
        
    def get_tribal_print(self):
        if self._tribal:
            return "Kyllä"
        return "Ei"
        
    def get_subtype_print(self):
        if self._subtype is None:
            return ""
        return ' '.join(self._subtype)
        
    def get_power_print(self):
        if self._power is None:
            return 0
        return self._power
        
    def get_toughness_print(self):
        if self._toughness is None:
            return 0
        return self._toughness
        
    def get_feature_print(self):
        if self._feature is None:
            return ""
        return ', '.join(self._feature)
    
    ## Get list
    def get_subtype_list(self):
        if self._subtype is None:
            return []
        return self._subtype
        
    def get_feature_list(self):
        if self._feature is None:
            return []
        return self._feature
        
    def get_feature2_list(self):
        if self._feature2 is None:
            return []
        return self._feature2
        
    ## Add
    def add_cube(self, cube_id):
        if cube_id not in self._cubes:
            self._cubes.append(cube_id)
        
    def add_colour(self, colour):
        if colour not in self._colour:
            self._colour.append(colour)
            self._check_if_multicolour()  
        
    def add_feature(self, feature):
        if feature not in self._feature:
            if not self._feature2:
                self._feature.append(feature)
            else:
                if feature in self._feature2:
                    self._feature.append(feature)
        
    ## Remove
    def remove_cube(self, cube_id):
        if cube_id in self._cubes:
            self._cubes.remove(cube_id)
            
    def remove_colour(self, colour):
        if colour in self._colour:
            self._colour.remove(colour)
            self._check_if_multicolour()
        
    def remove_feature(self, feature):
        if self._feature is not None:
            if feature in self._feature:
                self._feature.remove(feature)
        
    ## Other
    def _check_if_multicolour(self):
        if len(self._colour) > 1:
            self._multicolour = True
        else:
            self._multicolour = False
        
    def show_card(self):
        print('show card')
        
        
