import uuid
#import User

class Card:
    """ Class that represents a single card. """

    def __init__(self, name):
        """ Class constructor. Create a new card.
        Args:
            name: [String] Name of the card.
        """

        self._card_id = str(uuid.uuid4())
        self._name = name
        self._cubes = []
        self._maintype = ""
        self._legendary = False
        self._tribal = False
        self._subtype = []
        self._colour = []
        self._multicolour = False
        self._manacost = ""
        self._power = 0
        self._toughness = 0
        self._feature = []
        self._feature2 = []
        self._ruletext = ""
        self._flavourtext = ""
        self._image = ""
        self._seticon = ""
        self._rarity = ""
        self._creator = ""

    ## Get
    def get_id(self):
        return self._card_id

    def get_name(self):
        return self._name

    def get_cubes(self):
        return self._cubes

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

    def get_image(self):
        return self._image

    def get_seticon(self):
        return self._seticon

    def get_rarity(self):
        return self._rarity

    def get_creator(self):
        return self._creator

    ## Set
    def set_id(self, card_id):
        self._card_id = card_id

    def set_name(self, name):
        self._name = name

    def set_cubes(self, cubes):
        if isinstance(cubes, list):
            self._cubes = cubes
        else:
            self._cubes = cubes.split(",")

    def set_maintype(self, maintype):
        self._maintype = maintype

    def set_legendary(self, boolean):
        if self._legendary is not None and boolean is not None:
            self._legendary = boolean

    def set_tribal(self, boolean):
        if self._tribal is not None and boolean is not None:
            self._tribal = boolean

    def set_subtype(self, subtype):
        if self._subtype is not None and subtype is not None:
            if isinstance(subtype, list):
                self._subtype = subtype
            else:
                self._subtype = subtype.split(" ")

    def set_colour(self, colour):
        if isinstance(colour, list):
            self._colour = colour
        else:
            if colour == "Väritön":
                self._colour = []
            else:
                self._colour = colour.split(",")
        self._check_if_multicolour()

    def set_manacost(self, manacost):
        if self._manacost is not None and manacost is not None:
            self._manacost = manacost

    def set_power(self, power):
        if self._power is not None and power is not None:
            self._power = power

    def set_toughness(self, toughness):
        if self._toughness is not None and toughness is not None:
            self._toughness = toughness

    def set_feature(self, feature):
        if self._feature is not None and feature is not None:
            if not isinstance(feature, list):
                feature = feature.split(", ")
            if self._feature2:
                for single_feature in feature:
                    if single_feature in self._feature2:
                        self.add_feature(single_feature)
            else:
                self._feature = feature

    def set_ruletext(self, ruletext):
        self._ruletext = ruletext

    def set_flavourtext(self, flavourtext):
        self._flavourtext = flavourtext

    def set_image(self, image):
        if image is not None:
            self._image = image

    def set_seticon(self, seticon):
        self._seticon = seticon

    def set_rarity(self, rarity):
        self._rarity = rarity

    def set_creator(self, creator):
        self._creator = creator

    ## Get print
    def get_cubes_print(self):
        if not self._cubes:
            return ""
        return ', '.join(self._cubes)

    def get_colour_print(self):
        if not self._colour:
            return "Väritön"
        return ', '.join(self._colour)

    def get_card_colour(self):
        if self._multicolour:
            return "Kulta"
        if not self._colour:
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
        if not self._power:
            return 0
        return self._power

    def get_toughness_print(self):
        if not self._toughness:
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

    def copy(self, card):
        self.set_id(card.get_id())
        self.set_cubes(card.get_cubes())
        self.set_colour(card.get_colour())
        self.set_legendary(card.get_legendary())
        self.set_tribal(card.get_tribal())
        self.set_subtype(card.get_subtype())
        self.set_manacost(card.get_manacost())
        self.set_power(card.get_power())
        self.set_toughness(card.get_toughness())
        self.set_feature(card.get_feature())
        self.set_ruletext(card.get_ruletext())
        self.set_flavourtext(card.get_flavourtext())
        self.set_image(card.get_image())
        self.set_seticon(card.get_seticon())
        self.set_rarity(card.get_rarity())
        self.set_creator(card.get_creator())

    def show_card(self):
        print('show card')

    def __str__(self):
        return "name: " + self._name + ", " + \
               "cube: " + self.get_cubes_print() + ", " + \
               "maintype: " + self._maintype + ", " + \
               "legendary: " + str(self.get_legendary_print()) + ", " + \
               "tribal: " + str(self.get_tribal_print()) + ", " + \
               "subtype: " + self.get_subtype_print() + ", " + \
               "colour: " + self.get_colour_print() + ", " + \
               "manacost: " + str(self._manacost) + ", " + \
               "power: " + str(self.get_power_print()) + ", " + \
               "toughness: " + str(self.get_toughness_print()) + ", " + \
               "feature: " + self.get_feature_print() + ", " + \
               "ruletext: " + self._ruletext + ", " + \
               "flavourtext: " + self._flavourtext + ", " + \
               "image: " + self._image + ", " + \
               "seticon: " + self._seticon + ", " + \
               "rarity: " + self._rarity + ", " + \
               "creator: " + self._creator
