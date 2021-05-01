import unittest
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
from entities.cube import Cube
from entities.user import User
from services.korttikube_service import KorttikubeService

class FakeCardRepository():
    def __init__(self, cards=[]):
        self.cards = cards

    def create(self, new_card):
        self.cards.append(new_card)

    def update(self, new_card):
        for card in self.cards:
            if card.get_id() == new_card.get_id():
                self.cards.remove(card)
                break
        self.cards.append(new_card)

    def save(self, new_card):
        update = False
        for card in self.cards:
            if card.get_id() == new_card.get_id():
                self.update(card)
                break
        if update == False:
            self.create(new_card)

    def delete(self, card_id):
        for card in self.cards:
            if card.get_id() == card_id:
                self.cards.remove(card)

    def find_by_cube(self, cube_id):
        cards_in_cube = []
        for card in self.cards:
            if cube_id in card.get_cubes():
                cards_in_cube.append(card)
        return cards_in_cube
        
class FakeCubeRepository():
    def __init__(self, cubes=[]):
        self.cubes = cubes

    def create(self, new_cube):
        self.cubes.append(new_cube)

    def update(self, new_cube):
        for cube in self.cubes:
            if cube.get_id() == new_cube.get_id():
                self.cubes.remove(cube)
                break
        self.cubes.append(new_cube)

    def save(self, new_cube):
        update = False
        for cube in self.cubes:
            if cube.get_id() == new_cube.get_id():
                self.update(cube)
                break
        if update == False:
            self.create(new_cube)

    def delete(self, cube_id):
        for cube in self.cubes:
            if cube.get_id() == cube_id:
                self.cubes.remove(cube)

    def find_by_user(self, username):
        cubes = []
        for cube in self.cubes:
            print(cube.get_users())
            if username in cube.get_users():
                cubes.append(cube)
        print(cubes)
        return cubes

class FakeUserRepository():
    def __init__(self, users=[]):
        self.users = users

    def create(self, new_user):
        self.users.append(new_user)

    def save(self, new_user):
        self.create(new_user)

    def delete(self, username):
        for user in self.users:
            if user.get_username() == username:
                self.users.remove(user)

    def find_by_username(self, username):
        for user in self.users:
            if username == user.get_username():
                return [(user.get_username(), user.get_password())]
        return []

    def find_all(self):
        return self.users

class TestKorttikubeService(unittest.TestCase):
    def setUp(self):
        self.kks = KorttikubeService(FakeCardRepository([]), FakeCubeRepository([]), FakeUserRepository([]))
        self.card = Card("Testi")
        self.cube = Cube("Testikube")
        self.user = User("Testaaja", "testo")
        self.card_db = ('ac9a8253-5b78-4010-9aab-516dd1b00879', 'Peruna', \
                          '7132ac94-3e63-4fc8-9d33-5b8e7a2280cd', 'Instant', \
                          1, 0, 'Pottu', 'Valkoinen', '2U', None, \
                          'Peruna on pyöreä.', 'Peruna on soikea.', \
                          None, None, 'kuva', 'tunnus', 'rare', 'Tekijä')
        self.cube_db = ('ac9a8253-5b78-4010-9aab-516dd1b00879', 'Kube', \
                        '7132ac94-3e63-4fc8-9d33-5b8e7a2280cd', 'kuva', \
                        'tunnus')
        self.user_db = ('Käyttäjä', 'salasana')
        
    def set_user_and_cube(self):
        user = self.kks.create_user("Testuri", "sana")
        self.kks.save_to_database(user, "user")
        cube = self.kks.create_cube_entity("Testikube2")
        self.kks.save_to_database(cube, "cube")
        return user, cube
    
    # GET
    def test_get(self):
        self.assertEqual(self.kks.get_card(), None)
        self.assertEqual(self.kks.get_cube(), None)
        self.assertEqual(self.kks.get_user(), None)
    # SET
    def test_set(self):
        self.kks.set_card(self.card)
        self.assertEqual(self.kks.get_card(), self.card)
        self.kks.set_cube(self.cube)
        self.assertEqual(self.kks.get_cube(), self.cube)
        self.kks.set_user(self.user)
        self.assertEqual(self.kks.get_user(), self.user)        

    # LOGIN AND LOGOUT
    def test_login_logout(self):
        user = self.kks.login("Testaaja", "testo")
        self.assertEqual(user, False)
        self.kks.save_to_database(self.user, "user")
        user = self.kks.login("Testaaja", "testo")
        self.assertEqual(user.get_username(), "Testaaja")
        self.assertEqual(self.kks.get_user().get_username(), "Testaaja")
        self.kks.logout()
        self.assertEqual(self.kks.get_user(), None)

    # SET ENTITIES
    def test_set_card_entity(self):
        db_row = self.card_db
        card = self.kks.set_card_entity(db_row)
        self.assertEqual(card.get_id(), db_row[0])
        self.assertEqual(card.get_name(), db_row[1])
        self.assertEqual(card.get_cubes(), [db_row[2]])
        self.assertEqual(card.get_maintype(), db_row[3])
        self.assertEqual(card.get_legendary(), db_row[4])
        self.assertEqual(card.get_tribal(), db_row[5])
        self.assertEqual(card.get_subtype(), [db_row[6]])
        self.assertEqual(card.get_colour(), [db_row[7]])
        self.assertEqual(card.get_manacost(), db_row[8])
        self.assertEqual(card.get_feature(), db_row[9])
        self.assertEqual(card.get_ruletext(), db_row[10])
        self.assertEqual(card.get_flavourtext(), db_row[11])
        self.assertEqual(card.get_power(), db_row[12])
        self.assertEqual(card.get_toughness(), db_row[13])
        self.assertEqual(card.get_image(), db_row[14])
        self.assertEqual(card.get_seticon(), db_row[15])
        self.assertEqual(card.get_rarity(), db_row[16])
        self.assertEqual(card.get_creator(), db_row[17])

    def test_set_card_entity_types(self):
        db_row = list(self.card_db)
        db_row[3] = ""
        card = self.kks.set_card_entity(tuple(db_row))
        self.assertEqual(card.get_maintype(), "")
        db_row[3] = "Creature"
        card = self.kks.set_card_entity(tuple(db_row))
        self.assertEqual(card.get_maintype(), "Creature")
        db_row[3] = "Artifact"
        card = self.kks.set_card_entity(tuple(db_row))
        self.assertEqual(card.get_maintype(), "Artifact")
        db_row[3] = "Enchantment"
        card = self.kks.set_card_entity(tuple(db_row))
        self.assertEqual(card.get_maintype(), "Enchantment")
        db_row[3] = "Land"
        card = self.kks.set_card_entity(tuple(db_row))
        self.assertEqual(card.get_maintype(), "Land")
        db_row[3] = "Sorcery"
        card = self.kks.set_card_entity(tuple(db_row))
        self.assertEqual(card.get_maintype(), "Sorcery")
        db_row[3] = "Planeswalker"
        card = self.kks.set_card_entity(tuple(db_row))
        self.assertEqual(card.get_maintype(), "Planeswalker")
        db_row[3] = "Artifact Creature"
        card = self.kks.set_card_entity(tuple(db_row))
        self.assertEqual(card.get_maintype(), "Artifact Creature")
        db_row[3] = "Enchantment Creature"
        card = self.kks.set_card_entity(tuple(db_row))
        self.assertEqual(card.get_maintype(), "Enchantment Creature")

    def test_set_cube_entity(self):
        db_row = self.cube_db
        cube = self.kks.set_cube_entity(db_row)
        self.assertEqual(cube.get_id(), db_row[0])
        self.assertEqual(cube.get_name(), db_row[1])
        self.assertEqual(cube.get_users(), [db_row[2]])
        self.assertEqual(cube.get_image(), db_row[3])
        self.assertEqual(cube.get_seticon(), db_row[4])

    def test_set_user_entity(self):
        db_row = self.user_db
        user = self.kks.set_user_entity(db_row)
        self.assertEqual(user.get_username(), db_row[0])
        self.assertEqual(user.get_password(), db_row[1])

    # ENTER AND EXIT
    def test_enter_exit_card(self):
        self.kks.enter_card(self.card_db)
        print(self.kks.get_card())
        self.assertEqual(self.kks.get_card().get_name(), "Peruna")
        self.kks.exit_card()
        self.assertEqual(self.kks.get_card(), None)

    def test_enter_exit_cube(self):
        self.kks.enter_cube(self.cube_db)
        self.assertEqual(self.kks.get_cube().get_name(), "Kube")
        self.kks.exit_cube()
        self.assertEqual(self.kks.get_cube(), None)

    # CREATE ENTITIES
    def test_create_card_entity(self):
        self.kks.set_user(self.user)
        self.kks.set_cube(self.cube)
        card = self.kks.create_card_entity("Kortti")
        self.assertEqual(card.get_name(), "Kortti")
        self.assertEqual(card.get_cubes(), [self.cube.get_id()])

    def test_create_cube_entity(self):
        self.kks.set_user(self.user)
        cube = self.kks.create_cube_entity("Kube2")
        self.assertEqual(cube.get_name(), "Kube2")
        self.assertEqual(cube.get_users(), [self.user.get_username()])

    def test_create_user(self):
        user = self.kks.create_user("Kana", "sana")
        self.assertEqual(user.get_username(), "Kana")
        self.assertEqual(user.get_password(), "sana")

    def test_create_user_exists(self):
        user = self.kks.create_user("Kana", "sana2")
        self.kks.save_to_database(user, "user")
        user = self.kks.create_user("Kana", "sana")
        self.assertEqual(user, False)

    # OTHER
    def test_change_card_type(self):
        self.assertEqual(self.card.get_name(), "Testi")
        self.assertEqual(self.card.get_maintype(), "")
        self.assertEqual(self.card.get_power(), 0)
        new_card = self.kks.change_card_type(self.card, "Land")
        self.assertEqual(new_card.get_name(), "Testi")
        self.assertEqual(new_card.get_maintype(), "Land")
        self.assertEqual(new_card.get_power(), None)

    def test_change_card_type_all(self):
        new_card = self.kks.change_card_type(self.card, "Creature")
        self.assertEqual(new_card.get_maintype(), "Creature")
        new_card = self.kks.change_card_type(self.card, "Artifact")
        self.assertEqual(new_card.get_maintype(), "Artifact")
        new_card = self.kks.change_card_type(self.card, "Enchantment")
        self.assertEqual(new_card.get_maintype(), "Enchantment")
        new_card = self.kks.change_card_type(self.card, "Instant")
        self.assertEqual(new_card.get_maintype(), "Instant")
        new_card = self.kks.change_card_type(self.card, "Sorcery")
        self.assertEqual(new_card.get_maintype(), "Sorcery")
        new_card = self.kks.change_card_type(self.card, "Planeswalker")
        self.assertEqual(new_card.get_maintype(), "Planeswalker")
        new_card = self.kks.change_card_type(self.card, "Artifact Creature")
        self.assertEqual(new_card.get_maintype(), "Artifact Creature")
        new_card = self.kks.change_card_type(self.card, "Enchantment Creature")
        self.assertEqual(new_card.get_maintype(), "Enchantment Creature")

    def test_update_card(self):
        self.assertEqual(self.card.get_name(), "Testi")
        self.assertEqual(self.card.get_maintype(), "")
        self.assertEqual(self.card.get_colour(), [])
        self.assertEqual(self.card.get_feature(), [])
        self.assertEqual(self.card.get_power(), 0)
        self.kks.update_card(self.card, "Uusi", "name")
        self.assertEqual(self.card.get_name(), "Uusi")
        self.assertEqual(self.card.get_maintype(), "")
        self.assertEqual(self.card.get_colour(), [])
        self.assertEqual(self.card.get_feature(), [])
        self.assertEqual(self.card.get_power(), 0)
        self.kks.update_card(self.card, "Vihreä", "colour", True)
        self.assertEqual(self.card.get_name(), "Uusi")
        self.assertEqual(self.card.get_maintype(), "")
        self.assertEqual(self.card.get_colour(), ["Vihreä"])
        self.assertEqual(self.card.get_feature(), [])
        self.assertEqual(self.card.get_power(), 0)
        self.kks.update_card(self.card, 5, "power")
        self.assertEqual(self.card.get_name(), "Uusi")
        self.assertEqual(self.card.get_maintype(), "")
        self.assertEqual(self.card.get_colour(), ["Vihreä"])
        self.assertEqual(self.card.get_feature(), [])
        self.assertEqual(self.card.get_power(), 5)
        self.kks.update_card(self.card, "Haste", "feature", True)
        self.assertEqual(self.card.get_name(), "Uusi")
        self.assertEqual(self.card.get_maintype(), "")
        self.assertEqual(self.card.get_colour(), ["Vihreä"])
        self.assertEqual(self.card.get_feature(), ["Haste"])
        self.assertEqual(self.card.get_power(), 5)
        self.kks.update_card(self.card, "Flying", "feature", True)
        self.assertEqual(self.card.get_name(), "Uusi")
        self.assertEqual(self.card.get_maintype(), "")
        self.assertEqual(self.card.get_colour(), ["Vihreä"])
        self.assertEqual(self.card.get_feature(), ["Haste", "Flying"])
        self.assertEqual(self.card.get_power(), 5)
        self.kks.update_card(self.card, "Firststike", "feature", False)
        self.assertEqual(self.card.get_name(), "Uusi")
        self.assertEqual(self.card.get_maintype(), "")
        self.assertEqual(self.card.get_colour(), ["Vihreä"])
        self.assertEqual(self.card.get_feature(), ["Haste", "Flying"])
        self.assertEqual(self.card.get_power(), 5)
        self.kks.update_card(self.card, "Haste", "feature", False)
        self.assertEqual(self.card.get_name(), "Uusi")
        self.assertEqual(self.card.get_maintype(), "")
        self.assertEqual(self.card.get_colour(), ["Vihreä"])
        self.assertEqual(self.card.get_feature(), ["Flying"])
        self.assertEqual(self.card.get_power(), 5)

    def test_update_card_all(self):
        self.kks.update_card(self.card, "000", "cubes")
        self.assertEqual(self.card.get_cubes(), ["000"])
        self.kks.update_card(self.card, 1, "legendary")
        self.assertEqual(self.card.get_legendary(), 1)
        self.kks.update_card(self.card, 1, "tribal")
        self.assertEqual(self.card.get_tribal(), 1)
        self.kks.update_card(self.card, "Lintu", "subtype")
        self.assertEqual(self.card.get_subtype(), ["Lintu"])
        self.kks.update_card(self.card, "Vihreä", "colour", False)
        self.assertEqual(self.card.get_colour(), [])
        self.kks.update_card(self.card, "2U", "manacost")
        self.assertEqual(self.card.get_manacost(), "2U")
        self.kks.update_card(self.card, "teksti", "ruletext")
        self.assertEqual(self.card.get_ruletext(), "teksti")
        self.kks.update_card(self.card, "tarina", "flavourtext")
        self.assertEqual(self.card.get_flavourtext(), "tarina")
        self.kks.update_card(self.card, 2, "toughness")
        self.assertEqual(self.card.get_toughness(), 2)
        self.kks.update_card(self.card, "kuva", "image")
        self.assertEqual(self.card.get_image(), "kuva")
        self.kks.update_card(self.card, "xx", "seticon")
        self.assertEqual(self.card.get_seticon(), "xx")
        self.kks.update_card(self.card, "ei rare", "rarity")
        self.assertEqual(self.card.get_rarity(), "ei rare")
        self.kks.update_card(self.card, "Peruna", "creator")
        self.assertEqual(self.card.get_creator(), "Peruna")

    def test_set_card_frame(self):
        card_frame_image = self.kks.set_card_frame(self.card_db)
        self.assertEqual(card_frame_image, "img/whitecard.png")
        self.card.set_colour(["Punainen"])
        card_frame_image = self.kks.set_card_frame(self.card)
        self.assertEqual(card_frame_image, "img/redcard.png")
        self.card.set_colour(["Sininen"])
        card_frame_image = self.kks.set_card_frame(self.card)
        self.assertEqual(card_frame_image, "img/bluecard.png")
        self.card.set_colour(["Vihreä"])
        card_frame_image = self.kks.set_card_frame(self.card)
        self.assertEqual(card_frame_image, "img/greencard.png")
        self.card.set_colour(["Musta"])
        card_frame_image = self.kks.set_card_frame(self.card)
        self.assertEqual(card_frame_image, "img/blackcard.png")
        self.card.set_colour([])
        card_frame_image = self.kks.set_card_frame(self.card)
        self.assertEqual(card_frame_image, "img/colourlesscard.png")
        self.card.set_colour(["Punainen", "Valkoinen"])
        card_frame_image = self.kks.set_card_frame(self.card)
        self.assertEqual(card_frame_image, "img/goldcard.png")

    # DATABASE
    def test_get_cards_in_cube(self):
        self.set_user_and_cube()
        cards = self.kks.get_cards_in_cube()
        self.assertEqual(cards, [])
        card = self.kks.create_card_entity("uusi kortti")
        self.kks.save_to_database(card, "card")
        cards = self.kks.get_cards_in_cube()
        self.assertEqual(cards, [card])

    def test_get_cubes_from_user(self):
        suser, cube = self.set_user_and_cube()
        cubes = self.kks.get_cubes_from_user()
        self.assertEqual(cubes, [cube])

    def test_get_users_in_cube(self):
        self.set_user_and_cube()
        users = self.kks.get_users_in_cube()
        self.assertEqual(users, ["Testuri"])

    def test_get_users(self):
        users = self.kks.get_users()
        self.assertEqual(users, [])
        self.kks.save_to_database(self.user, "user")
        users = self.kks.get_users()
        self.assertEqual(users, [self.user])

    def test_delete_card(self):
        self.set_user_and_cube()
        cards = self.kks.get_cards_in_cube()
        self.assertEqual(cards, [])
        self.kks.delete_card(self.card)
        cards = self.kks.get_cards_in_cube()
        self.assertEqual(cards, [])
        card = self.kks.create_card_entity("Eka")
        self.kks.save_to_database(card, "card")
        cards = self.kks.get_cards_in_cube()
        self.assertEqual(cards, [card])
        self.kks.delete_card(card)
        cards = self.kks.get_cards_in_cube()
        self.assertEqual(cards, [])