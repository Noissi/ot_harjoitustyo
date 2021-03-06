from database_connection import get_database_connection

class CardRepository:
    """ Class responsible for card database logic.

    Attributes:
        connection: A databse connection object.
    """

    def __init__(self, connection):
        """ Class constructor. Creates a new card repository.

        Args:
            connection: A databse connection object.
        """

        self._connection = connection

    def create(self, card):
        """ Creates a new card into the cards table.
        Args:
            card: [Card] The Card entity to be saved.
        """

        card_sql = (card.get_id(), card.get_name(), card.get_cubes_print(),  \
                    card.get_maintype(), card.get_legendary(), card.get_tribal(), \
                    card.get_subtype_print(), card.get_colour_print(), card.get_manacost(), \
                    card.get_feature_print(), card.get_ruletext(), card.get_flavourtext(), \
                    card.get_power(), card.get_toughness(), card.get_image(), \
                    card.get_seticon(), card.get_rarity(), card.get_creator(), \
                    card.get_picture())

        sql = ''' INSERT INTO cards(id, name, cube_id, maintype, legendary,
                  tribal, subtype, colour, manacost, feature, ruletext, flavourtext,
                  power, toughness, image, seticon, rarity, creator, picture)
                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?); '''

        cursor = self._connection.cursor()
        cursor.execute(sql, card_sql)
        self._connection.commit()

    def update(self, card):
        """ Updates an existing card in the cards table.
        Args:
            card: [Card] The Card entity to be updated.
        """

        card_sql = (card.get_name(), card.get_cubes_print(),  \
                    card.get_maintype(), card.get_legendary(), card.get_tribal(), \
                    card.get_subtype_print(), card.get_colour_print(), card.get_manacost(), \
                    card.get_feature_print(), card.get_ruletext(), card.get_flavourtext(), \
                    card.get_power(), card.get_toughness(), card.get_image(), \
                    card.get_seticon(), card.get_rarity(), card.get_creator(), card.get_picture(), \
                    card.get_id())

        sql = ''' UPDATE cards
                  SET name = ?,
                      cube_id = ?,
                      maintype = ?,
                      legendary = ?,
                      tribal = ?,
                      subtype = ?,
                      colour = ?,
                      manacost = ?,
                      feature = ?,
                      ruletext = ?,
                      flavourtext = ?,
                      power = ?,
                      toughness = ?,
                      image = ?,
                      seticon = ?,
                      rarity = ?,
                      creator = ?,
                      picture = ?
                   WHERE id = ?; '''

        cursor = self._connection.cursor()
        cursor.execute(sql, card_sql)
        self._connection.commit()

    def save(self, card):
        """ Saves the card into the cards table.
        Args:
            card: [Card] The Card entity to be saved.
        """

        card_sql = (card.get_id(),)
        sql = """ SELECT 1 FROM cards WHERE id = ?; """
        cursor = self._connection.cursor()
        cursor.execute(sql, card_sql)
        if cursor.fetchone() is None:
            self.create(card)
        else:
            self.update(card)

    def delete(self, card_id):
        """ Removes the card from the cards table.
        Args:
            card_id: [String] The id of the card to be removed from the database.
        """

        card_sql = (card_id,)
        sql = """ DELETE FROM cards WHERE id = ?; """
        cursor = self._connection.cursor()
        cursor.execute(sql, card_sql)
        self._connection.commit()

    def delete_all(self):
        """ Removes all the cards from the cards table.
        """

        sql = """ DELETE FROM cards; """
        cursor = self._connection.cursor()
        cursor.execute(sql)
        self._connection.commit()

    def find_all(self):
        """ Selects all cards in database.
        Return:
            rows: [List Tuple] List of tuples including the cards.
        """

        sql = """ SELECT * FROM cards; """
        cursor = self._connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows

    def find_by_cube(self, cube_id):
        """ Selects the cards belonging to the given cube.
        Args:
            cube_id: [String] The id of the cube.
        Return:
            rows: [List Tuple] List of tuples including the cards.
        """

        cube_sql = (cube_id,)
        sql = """ SELECT * FROM cards WHERE cube_id = ?; """
        cursor = self._connection.cursor()
        cursor.execute(sql, cube_sql)
        rows = cursor.fetchall()
        return rows

    def find_by_name_from_cube(self, cube_id, name):
        """ Selects the card with given cube id and name.
        Args:
            cube_id: [String] The id of the cube.
            name: [String] The name of the card.
        Return:
            row: [Tuple] Card tuple.
        """

        text_sql = (cube_id, name)
        sql = """ SELECT * FROM cards WHERE cube_id = ? AND lower(name) = ?; """
        cursor = self._connection.cursor()
        cursor.execute(sql, text_sql)
        row = cursor.fetchall()
        return row

    def find_cards_from_cube_that_contains(self, cube_id, name_part, maintype, colour, order):
        """ Selects the cards belonging to the given cube that has given
            maintype and card frame colour and which name includes name_part.
        Args:
            cube_id: [String] The id of the cube.
            name_part: [String] String to be matched with the name.
            maintype: [String] Maintype that the cards should be.
            colour: [String] Card frame colour that the cards should have.
            order: [List String] Desired order parameter and direction of the cards.
        Return:
            rows: [List Tuple] List of tuples including the cards.
        """

        insert_sql = (cube_id, '%'+maintype+'%', '%'+colour+'%', '%'+name_part+'%')
        sql = """ SELECT * FROM cards WHERE cube_id = ? AND maintype LIKE ? AND colour LIKE ?
                  AND name LIKE ? COLLATE NOCASE ORDER BY {}; """.format(order[0] + " " + order[1])
        cursor = self._connection.cursor()
        cursor.execute(sql, insert_sql)
        rows = cursor.fetchall()
        return rows

    def create_csv_file(self, cube_id):
        """ Creates a csv-file from cards in selected cubr.
        Args:
            cube: [Cube] The Cube entity from where the cards are selected.
        Return:
            data: cursor data
        """

        cube_sql = (cube_id,)
        sql = """ SELECT * FROM cards WHERE cube_id = ?; """
        cursor = self._connection.cursor()
        cursor.execute(sql, cube_sql)

        return cursor

card_repository = CardRepository(get_database_connection())
