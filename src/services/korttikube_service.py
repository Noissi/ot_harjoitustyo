from entities.user import User
from entities.cube import Cube
from entities.card import Card

from entities.card_creature import Creature
from entities.card_land import Land
from entities.card_instant import Instant
from entities.card_sorcery import Sorcery
from entities.card_enchantment import Enchantment
from entities.card_planeswalker import Planeswalker
from entities.card_artifact import Artifact
from entities.card_enchantment_creature import EnchantmentCreature
from entities.card_artifact_creature import ArtifactCreature

from repositories.user_repository import user_repository as default_user_repository
from repositories.cube_repository import cube_repository as default_cube_repository
from repositories.card_repository import card_repository as default_card_repository

from config import IMAGES_FILE_PATH

class KorttikubeService:
    """ Class responsible for application logic. """

    def __init__(
        self,
        card_repository = default_card_repository,
        cube_repository = default_cube_repository,
        user_repository = default_user_repository
    ):
        """ Class constructor. Create a new application servise.
        Args:
            card_repository:
                Optional. CardRepository entity.
            cube_repository:
                Optional. CubeRepository entity.
            user_repository:
                Optional. UserRepository entity.
        """

        self._user = None
        self._cube = None
        self._card = None

        self._card_repository = card_repository
        self._cube_repository = cube_repository
        self._user_repository = user_repository

    # GET
    def get_card(self):
        return self._card

    def get_cube(self):
        return self._cube

    def get_user(self):
        """ Returns the current user.
        Returns:
            [User] User entity of the current user.
        """
        return self._user

    #SET
    def set_card(self, card):
        self._card = card

    def set_cube(self, cube):
        self._cube = cube

    def set_user(self, user):
        self._user = user

    # ENTER AND EXIT
    def enter_card(self, card_db):
        card_entity = self.set_card_entity(card_db)
        self._card = card_entity

    def exit_card(self):
        self._card = None

    def enter_cube(self, cube_db):
        cube_entity = self.set_cube_entity(cube_db)
        self._cube = cube_entity

    def exit_cube(self):
        self._cube = None

    # LOGIN AND LOGOUT
    def login(self, username, password):
        """ Log in user.
        Args:
            username: [String] Username of the user.
            password: [String] Password of the user.
        Returns:
            [User] User entity that is logged in.
        Raises:
            InvalidCredentialsError:
                Invalid username and/or password.
        """

        user_list = self._user_repository.find_by_username(username)
        if not user_list or user_list[0][1] != password:
            return False

        user = self.set_user_entity(user_list[0])
        self._user = user

        return user

    def logout(self):
        self._user = None

    # CREATE
    def create_card_entity(self, cardname):
        """ Create a new card.
        Args:
            cardname: [String] The name of the card.
        Returns:
            [Card] Created Card entity.
        """

        card = Card(cardname)
        card.add_cube(self._cube.get_id())
        return card

    def create_cube_entity(self, cubename):
        """ Create a new cube.
        Args:
            cubename: [String] The name of the cube.
        Returns:
            [Cube] Created Cube entity.
        """

        cube = Cube(cubename)
        cube.add_user(self._user.get_username())
        return cube

    def create_user(self, username, password):
        """ Creates a new user.
        Args:
            username: [String] Username of the user.
            password: [String] Password of the user.
        Returns:
            [User] Created User entity.
        Raises:
            UsernameExistsError:
                Cannot use the selected username. Username already exists.
        """

        existing_user = self._user_repository.find_by_username(username)
        if existing_user:
            return False

        user = User(username, password)
        self._user_repository.create(user)

        return user

    # SET ENTITIES
    def set_card_entity(self, card_row):
        """ Create a Card entity from the given database row.
        Args:
            card_row: [List Tuple] List of tuples including the parameters
                       of one card in database.
        Returns:
            [Card] Created Card entity.
        """

        name = card_row[1]
        maintype = card_row[3]
        if maintype == "":
            card = Card(name)
        elif maintype == "Creature":
            card = Creature(name)
        elif maintype == "Artifact":
            card = Artifact(name)
        elif maintype == "Enchantment":
            card = Enchantment(name)
        elif maintype == "Land":
            card = Land(name)
        elif maintype == "Instant":
            card = Instant(name)
        elif maintype == "Sorcery":
            card = Sorcery(name)
        elif maintype == "Planeswalker":
            card = Planeswalker(name)
        elif maintype == "Artifact Creature":
            card = ArtifactCreature(name)
        elif maintype == "Enchantment Creature":
            card = EnchantmentCreature(name)

        card.set_id(card_row[0])
        card.set_cubes(card_row[2])
        card.set_legendary(card_row[4])
        card.set_tribal(card_row[5])
        card.set_subtype(card_row[6])
        card.set_colour(card_row[7])
        card.set_manacost(card_row[8])
        card.set_feature(card_row[9])
        card.set_ruletext(card_row[10])
        card.set_flavourtext(card_row[11])
        card.set_power(card_row[12])
        card.set_toughness(card_row[13])
        card.set_image(card_row[14])
        card.set_seticon(card_row[15])
        card.set_rarity(card_row[16])
        card.set_creator(card_row[17])
        card.set_picture(card_row[18])

        return card

    def set_cube_entity(self, cube_row):
        """ Create a Cube entity from the given database row.
        Args:
            cube_row: [List Tuple] List of tuples including the parameters
                       of one cube in database.
        Returns:
            [Cube] Created Cube entity.
        """

        name = cube_row[1]
        cube = Cube(name)

        cube.set_id(cube_row[0])
        cube.set_users(cube_row[2])
        cube.set_image(cube_row[3])
        cube.set_seticon(cube_row[4])

        return cube

    def set_user_entity(self, user_row):
        """ Create a User entity from the given database row.
        Args:
            user_row: [List Tuple] List of tuples including the parameters
                       of one user in database.
        Returns:
            [User] Created User entity.
        """

        username = user_row[0]
        password = user_row[1]
        user = User(username, password)

        #user.set_id(cube_row[0])

        return user

    # OTHER
    def change_card_type(self, card, maintype):
        """ Modifies card's maintype. (Creates a new Card entity that
            copies the properties from the old one.)
        Args:
            card: [Card] Card entity that needs to be changed.
            maintype: [String] New maintype for the card.
        """

        if maintype == "Creature":
            new_card = Creature(card.get_name())
        elif maintype == "Artifact":
            new_card = Artifact(card.get_name())
        elif maintype == "Enchantment":
            new_card = Enchantment(card.get_name())
        elif maintype == "Land":
            new_card = Land(card.get_name())
        elif maintype == "Instant":
            new_card = Instant(card.get_name())
        elif maintype == "Sorcery":
            new_card = Sorcery(card.get_name())
        elif maintype == "Planeswalker":
            new_card = Planeswalker(card.get_name())
        elif maintype == "Artifact Creature":
            new_card = ArtifactCreature(card.get_name())
        elif maintype == "Enchantment Creature":
            new_card = EnchantmentCreature(card.get_name())
        new_card.copy(card)

        return new_card

    def update_card(self, card, prop, prop_name, add=None):
        """ Modifies card's property that is specified as a parameter.
        Args:
            card: [Card] Card that needs to be modified.
            prop: [String, Boolean] New property text/boolean to replace the current one.
                           (e.g. a new name or ruletext for the card).
            prop_name: [String] Property type (e.g. "name", "ruletext").
            add: [Boolean] Optional. Defines which method to do for
                           properties with multiple check boxes.
        """

        if prop_name == 'name':
            card.set_name(prop)
        elif prop_name == "cubes":
            card.set_cubes(prop)
        elif prop_name == 'legendary':
            card.set_legendary(prop)
        elif prop_name == 'tribal':
            card.set_tribal(prop)
        elif prop_name == 'subtype':
            card.set_subtype(prop)
        elif prop_name == 'colour':
            if add:
                card.add_colour(prop)
            else:
                card.remove_colour(prop)
        elif prop_name == 'manacost':
            card.set_manacost(prop)
        elif prop_name == 'feature':
            if add:
                card.add_feature(prop)
            else:
                card.remove_feature(prop)
        elif prop_name == 'ruletext':
            card.set_ruletext(prop)
        elif prop_name == 'flavourtext':
            card.set_flavourtext(prop)
        elif prop_name == 'power':
            card.set_power(prop)
        elif prop_name == 'toughness':
            card.set_toughness(prop)
        elif prop_name == 'image':
            card.set_image(prop)
        elif prop_name == 'seticon':
            card.set_seticon(prop)
        elif prop_name == 'rarity':
            card.set_rarity(prop)
        elif prop_name == 'creator':
            card.set_creator(prop)
        elif prop_name == 'picture':
            card.set_picture(prop)

    # DATABASE SEARCH
    def get_cards_in_cube(self):
        """ Returns list of cards in cube.
        Args:
            cube_id: [String] Cude entity id.
        Returns:
            [List Card] List of Card entities in cube.
        """

        cube_id = self._cube.get_id()
        cards = self._card_repository.find_by_cube(cube_id)

        return list(cards)

    def get_cards_by_name_that_contains(self, text):
        """ Returns list of cards (in cube) which name includes the given text.
            Not case sensitive.
        Args:
            text: [String] Given search parameter.
        Returns:
            [List Card] List of Card entities in cube that match the criteria.
        """

        cards = self._card_repository.find_by_name_that_contains(text)

        return cards

    def get_cubes_from_user(self):
        """ Returns list of all cubes from current user.
        Returns:
            [List Cube] List of Cube entities.
        """

        username = self._user.get_username()
        cubes = list(self._cube_repository.find_by_user(username))
        return cubes

    def set_card_frame(self, card):
        """ Selects and returns corresponding card frame image.
        Args:
            card: [Card] Card entity.
        Returns:
            [String] Path to the card frame image.
        """

        if isinstance(card, tuple):
            card = self.set_card_entity(card)

        if card.get_card_colour() == "Punainen":
            card_frame_image = IMAGES_FILE_PATH + "redcard.png"
        elif card.get_card_colour() == "Sininen":
            card_frame_image = IMAGES_FILE_PATH + "bluecard.png"
        elif card.get_card_colour() == "Vihreä":
            card_frame_image = IMAGES_FILE_PATH + "greencard.png"
        elif card.get_card_colour() == "Valkoinen":
            card_frame_image = IMAGES_FILE_PATH + "whitecard.png"
        elif card.get_card_colour() == "Musta":
            card_frame_image = IMAGES_FILE_PATH + "blackcard.png"
        elif card.get_card_colour() == "Väritön":
            card_frame_image = IMAGES_FILE_PATH + "colourlesscard.png"
        elif card.get_card_colour() == "Kulta":
            card_frame_image = IMAGES_FILE_PATH + "goldcard.png"
        return card_frame_image

    def get_users_in_cube(self):
        """ Returns list of users in cube.
        Args:
            cube_id: [String] Cude entity id.
        Returns:
            [List User] List of User entities in cube.
        """

        return self._cube.get_users()

    def get_users(self):
        """ Returns list of all users.
        Returns:
            [List User] List of all User entities.
        """

        return self._user_repository.find_all()

    def delete_card(self, card):
        """ Delete an existing card.
        Args:
            card: [Card] The Card entity to be deleted from the database.
        """

        self._card_repository.delete(card.get_id())

    def save_to_database(self, obj, obj_type):
        """ Save an object to the database.
        Args:
            obj: [Card/Cube/User] Entity to be saved to the database.
            obj_type: [String] Object type ("card", "cube" or "user")
        """

        if obj_type == "card":
            self._card = obj
            self._card_repository.save(obj)
        elif obj_type == "cube":
            self._cube = obj
            self._cube_repository.save(obj)
        elif obj_type == "user":
            self._user = obj
            self._user_repository.save(obj)

korttikube_service = KorttikubeService()
