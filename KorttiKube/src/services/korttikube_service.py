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


class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class KorttikubeService:
    """Sovelluslogiikasta vastaava luokka."""

    def __init__(
        self,
        card_repository = default_card_repository,
        cube_repository = default_cube_repository,
        user_repository = default_user_repository
    ):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun.
        Args:
            card_repository:
                Vapaaehtoinen, oletusarvoltaan CardRepository-olio.
                Olio, jolla on CardRepository-luokkaa vastaavat metodit.
            user_repository:
                Vapaaehtoinen, oletusarvoltaan UserRepository-olio.
                Olio, jolla on UserRepository-luokkaa vastaavat metodit.
        """
        self._user = None
        self._card_repository = card_repository
        self._cube_repository = cube_repository
        self._user_repository = user_repository

    def create_card(self, cardname):
        """ Create a new card.
        Args:
            cardname: [String] The name of the card.
        Returns:
            Created Card entity.
        """

        card = Card(cardname)

        return self._card_repository.create(card)
        
    def delete_card(self, card):
        print('delete')
        
    def save_to_database(self, card):
        self._card_repository.save(card)
        
    def change_card_type(self, card, maintype):
        """ Modifies card's maintype. (Creates a new sub card entity.)
        Args:
            card: [card entity] Card that needs to be changed.
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
            card: [Card entity] Card that needs to be modified.
            prop: [String] New property text to replace the current one.
                           (e.g. a new name or ruletext for the card)
            prop_name: [String] Property type (e.g. "name", "ruletext")
            add: [Boolean] Optional. Defines which method to do for 
                           properties with multiple check boxes.
        """
        if prop_name == 'name':
            card.set_name(prop)
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
        elif prop_name == 'power':
            card.set_power(prop)
        elif prop_name == 'toughness':
            card.set_toughness(prop)
        elif prop_name == 'feature':
            if add:
                card.add_feature(prop)
            else:
                card.remove_feature(prop)
        elif prop_name == 'ruletext':
            card.set_ruletext(prop)
        elif prop_name == 'flavourtext':
            card.set_flavourtext(prop)
        elif prop_name == 'creator':
            card.set_creator(prop)
        elif prop_name == 'seticon':
            card.set_seticon(prop)
        elif prop_name == 'rarity':
            card.set_rarity(prop)
            
    def get_cards_in_cube(self, cube):
        """ Returns cards in a given collection.
        Returns:
            [List Card] List of card entities.
        """
        if not cube:
            return []

        cards = self._card_repository.find_by_cube(cube)

        return list(cards)
        
    '''
    def get_undone_todos(self):
        """Palauttaa kirjautuneen käyttäjän tekemättömät tehtävät.
        Returns:
            Palauttaa kirjautuneen käyttäjän tekemättömät tehtävät Todo-olioden listana.
            Jos kirjautunutta käyttäjää ei ole, palauttaa tyhjän listan.
        """

        if not self._user:
            return []

        todos = self._todo_repository.find_by_username(self._user.username)
        undone_todos = filter(lambda todo: not todo.done, todos)

        return list(undone_todos)

    

    def login(self, username, password):
        """Kirjaa käyttäjän sisään.
        Args:
            username: Merkkijonoarvo, joka kuvaa kirjautuvan käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvaa kirjautuvan käyttäjän salasanaa.
        Returns:
            Kirjautunut käyttäjä User-olion muodossa.
        Raises:
            InvalidCredentialsError:
                Virhe, joka tapahtuu, kun käyttäjätunnus ja salasana eivät täsmää.
        """

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError('Invalid username or password')

        self._user = user

        return user

    def get_current_user(self):
        """Paluttaa kirjautuunen käyttäjän.
        Returns:
            Kirjautunut käyttäjä User-olion muodossa.
        """
        return self._user

    def get_users(self):
        """Palauttaa kaikki käyttäjät.
        Returns:
            User-oliota sisältä lista kaikista käyttäjistä.
        """
        return self._user_repository.find_all()

    def logout(self):
        """Kirjaa nykyisen käyttäjän ulos.
        """
        self._user = None

    def create_user(self, username, password, login=True):
        """Luo uuden käyttäjän ja tarvittaessa kirjaa sen sisään.
        Args:
            username: Merkkijonoarvo, joka kuvastaa käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvastaa käyttäjän salasanaa.
            login:
                Vapaahtoinen, oletusarvo True.
                Boolean-arvo, joka kertoo kirjataanko käyttäjä sisään onnistuneen luonnin jälkeen.
        Raises:
            UsernameExistsError: Virhe, joka tapahtuu, kun käyttäjätunnus on jo käytössä.
        Returns:
            Luotu käyttäjä User-olion muodossa.
        """

        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError(f'Username {username} already exists')

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user
    '''

korttikube_service = KorttikubeService()