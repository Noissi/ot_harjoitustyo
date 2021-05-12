import uuid
#import User

class Card:
    """ Class that represents a single card. The card has many
        properties that are used to create a printable card image.

    Attributes:
        _card_id: [String] Card's unique id.
        _name: [String] Card's name.
        _cubes: [List String] List of Cube id's which the card belongs to.
        _maintype: [String] Card's maintype.
        _legendary: [Boolean] Tells if the card is legendary.
        _tribal: [Boolean] Tells if the card has tribal.
        _subtype: [List String] List of card's subtypes.
        _colour: [List String] List of card's colours.
        _manacost: [String] Card's manacost.
        _feature: [List String] List of card's features.
        _feature2: [List String] If the card has a limited set
                   of features, the available features are listed here.
        _ruletext: [String] Card's ruletext.
        _flavourtext: [String] Card's flavourtext.
        _power: [Integer] Card's power.
        _toughness: [Integer] Card's toughness.
        _image: [String] Card's image (path).
        _seticon: [String] Card's seticon (path).
        _rarity: [String] Card's rarity.
        _creator: [String] Card's creator.
        _picture: [String] Saved picture (path) of the created card
                  that shows a printable card.
    """

    def __init__(self, name):
        """ Class constructor. Creates a new card.
        Args:
            name: [String] Name of the card.
        """

        self._card_id     = str(uuid.uuid4())
        self._name        = name
        self._cubes       = []
        self._maintype    = ""
        self._legendary   = False
        self._tribal      = False
        self._subtype     = []
        self._colour      = []
        self._manacost    = ""
        self._feature     = []
        self._feature2    = []
        self._ruletext    = ""
        self._flavourtext = ""
        self._power       = 0
        self._toughness   = 0
        self._image       = ""
        self._seticon     = ""
        self._rarity      = ""
        self._creator     = ""
        self._picture     = ""

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

    def get_picture(self):
        return self._picture

    ## Set
    def set_id(self, card_id):
        """ Sets card's id.
        Args:
            card_id: [String] The id to be set.
        """

        self._card_id = card_id

    def set_name(self, name):
        """ Sets card's name.
        Args:
            name: [String] The name to be set.
        """

        self._name = name

    def set_cubes(self, cubes):
        """ Sets a list of cubes that the card is in.
        Args:
            cubes: [List or String] A list of Cube id's or a string of them to be set.
        """

        if isinstance(cubes, list):
            self._cubes = cubes
        else:
            self._cubes = cubes.split(",")

    def set_maintype(self, maintype):
        """ Sets card's maintype.
        Args:
            maintype: [String] The maintype to be set.
        """

        self._maintype = maintype

    def set_legendary(self, boolean):
        """ Sets whether the card is legendary if the card type is allowed to be legendary.
        Args:
            legendary: [Boolean] Tells if the card is legendary.
        """

        if self._legendary is not None and boolean is not None:
            self._legendary = boolean

    def set_tribal(self, boolean):
        """ Sets whether the card has tribal if the card type is allowed to have tribal.
        Args:
            tribal: [Boolean] Tells if the card has tribal.
        """

        if self._tribal is not None and boolean is not None:
            self._tribal = boolean

    def set_subtype(self, subtype):
        """ Sets card's subtypes if the card type is allowed to have subtypes.
        Args:
            subtype: [List or String] List of subtypes or a string of them to be set.
        """

        if self._subtype is not None and subtype is not None:
            if isinstance(subtype, list):
                self._subtype = subtype
            else:
                self._subtype = subtype.split(" ")

    def set_colour(self, colour):
        """ Sets colours to the card. If there are no colours,
            an empty list is set. Updates multicolour attribute.
        Args:
            colur: [List or String] List of card colours or a
                   string of card colours (from database)
        """

        if isinstance(colour, list):
            self._colour = colour
        else:
            if colour == "Väritön":
                self._colour = []
            else:
                self._colour = colour.split(", ")

    def set_manacost(self, manacost):
        """ Sets card's manacost if the card type is allowed to have manacost.
        Args:
            manacost: [String] The manacost to be set.
        """

        if self._manacost is not None and manacost is not None:
            self._manacost = manacost

    def set_power(self, power):
        """ Sets card's power if the card type is allowed to have power.
        Args:
            power: [Integer] The power to be set.
        """

        if self._power is not None and power is not None:
            self._power = power

    def set_toughness(self, toughness):
        """ Sets card's toughness if the card type is allowed to have toughness.
        Args:
            toughness: [Integer] The toughness to be set.
        """

        if self._toughness is not None and toughness is not None:
            self._toughness = toughness

    def set_feature(self, feature):
        """ Sets features to the card if the card type is allowed
            to have features.
        Args:
            feature: [List or String] List of card features or a
                     string of card features (from database)
        """

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
        """ Sets card's ruletext.
        Args:
            ruletext: [String] The ruletext to be set.
        """

        self._ruletext = ruletext

    def set_flavourtext(self, flavourtext):
        """ Sets card's flavourtext.
        Args:
            flavourtext: [String] The flavourtext to be set.
        """

        self._flavourtext = flavourtext

    def set_image(self, image):
        """ Sets card's image.
        Args:
            image: [String] The image (path) to be set.
        """

        self._image = image

    def set_seticon(self, seticon):
        """ Sets card's seticon.
        Args:
            seticon: [String] The seticon (path) to be set.
        """

        self._seticon = seticon

    def set_rarity(self, rarity):
        """ Sets card's rarity.
        Args:
            rarity: [String] The rarity to be set.
        """

        self._rarity = rarity

    def set_creator(self, creator):
        """ Sets card's creator.
        Args:
            creator: [String] The creator to be set.
        """

        self._creator = creator

    def set_picture(self, picture):
        """ Sets card picture.
        Args:
            picture: [String] The picture (path) to be set.
        """

        self._picture = picture

    ## Get print
    def get_cubes_print(self):
        """ Creates a printable string of the cube ids which the card belongs to.
        Return:
            [String] Cube ids in a string.
        """

        if not self._cubes:
            return ""
        return ', '.join(self._cubes)

    def get_colour_print(self):
        """ Creates a printable string of the card colours.
        Return:
            [String] Colours in a string.
        """

        if not self._colour:
            return "Väritön"
        return ', '.join(self._colour)

    def get_card_colour(self):
        """ Creates a printable string of the card frame colour.
        Return:
            [String] Colour of the card frame.
        """

        if self._check_if_multicolour():
            return "Kulta"
        if not self._colour:
            return "Väritön"
        return self._colour[0]

    def get_legendary_print(self):
        """ Creates a printable string of the legendary attribute.
        Return:
            [String] "Legendary" or ""
        """

        if self._legendary:
            return "Legendary "
        return ""

    def get_tribal_print(self):
        """ Creates a printable string of the tribal attribute.
        Return:
            [String] "Tribal" or ""
        """

        if self._tribal:
            return "Tribal "
        return ""

    def get_subtype_print(self):
        """ Creates a printable string of the subtypes.
        Return:
            [String] Subtypes of the card in a string.
        """

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
        """ Creates a printable string of the features.
        Return:
            [String] Features of the card in a string.
        """

        if self._feature is None:
            return ""
        return ', '.join(self._feature)

    ## Get list
    def get_feature_list(self):
        """ Creates an empty list of features if it is None.
        Return:
            [List String] Features in a list.
        """

        if self._feature is None:
            return []
        return self._feature

    ## Add
    def add_cube(self, cube_id):
        """ Adds a cube id in the cubes list.
        Args:
            cube_id: [String] The cube id to be added.
        """

        if cube_id not in self._cubes:
            self._cubes.append(cube_id)

    def add_colour(self, colour):
        """ Adds a colour in the colour list.
        Args:
            colour: [String] The colour to be added.
        """

        if colour not in self._colour:
            self._colour.append(colour)

    def add_feature(self, feature):
        """ Adds a feature in the feature list.
        Args:
            feature: [String] The feature to be added.
        """

        if feature not in self._feature:
            if not self._feature2:
                self._feature.append(feature)
            else:
                if feature in self._feature2:
                    self._feature.append(feature)

    ## Remove
    def remove_cube(self, cube_id):
        """ Removes a cube id from the cubes list.
        Args:
            cube_id: [String] The cube id to be removed.
        """

        if cube_id in self._cubes:
            self._cubes.remove(cube_id)

    def remove_colour(self, colour):
        """ Removes a colour from the colour list.
        Args:
            colour: [String] The colour to be removed.
        """

        if colour in self._colour:
            self._colour.remove(colour)

    def remove_feature(self, feature):
        """ Removes a feature from the feature list.
        Args:
            feature: [String] The feature to be removed.
        """

        if self._feature is not None:
            if feature in self._feature:
                self._feature.remove(feature)

    ## Other
    def _check_if_multicolour(self):
        """ Checks if card has multiple colours, and sets
            the _multicolour paramater accordingly.
        Returns:
            [Boolean] Tells if the card has multiple colours.
        """

        if len(self._colour) > 1:
            return True
        return False

    def copy(self, card):
        """ Copies the properties of another card to this card.
        """

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
        self.set_picture(card.get_picture())