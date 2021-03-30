from database_connection import get_database_connection

class CardRepository:
    def __init__(self, connection):
        self._connection = connection
        
    def create(self, card):
        """
        Create a new card into the cards table.
        """
        card_sql = (card.get_id(), card.get_name(), card.get_image(), \
                    card.get_maintype(), card.get_legendary(), card.get_tribal(), \
                    card.get_subtype_print(), card.get_colour_print(), card.get_manacost(), \
                    card.get_power(), card.get_toughness(), card.get_feature_print(), \
                    card.get_ruletext(), card.get_flavourtext(), card.get_creator(), \
                    card.get_seticon(), card.get_rarity());
            
        sql = ''' INSERT INTO cards(id, name, image, maintype, legendary,
                  tribal, subtype, colour, manacost, power, toughness, feature,
                  ruletext, flavourtext, creator, seticon, rarity)
                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?); '''
        
        cursor = self._connection.cursor()
        cursor.execute(sql, card_sql)
        self._connection.commit()
        
    def update(self, card):
        card_sql = (card.get_name(), card.get_image(), card.get_maintype(), \
                    card.get_legendary(), card.get_tribal(), card.get_subtype_print(), \
                    card.get_colour_print(), card.get_manacost(), card.get_power(), \
                    card.get_toughness(), card.get_feature_print(), card.get_ruletext(), \
                    card.get_flavourtext(), card.get_creator(), card.get_seticon(), \
                    card.get_rarity(), card.get_id());
                    
        sql = ''' UPDATE cards
                  SET name = ?,
                      image = ?,
                      maintype = ?,
                      legendary = ?,
                      tribal = ?,
                      subtype = ?,
                      colour = ?,
                      manacost = ?,
                      power = ?,
                      toughness = ?,
                      feature = ?,
                      ruletext = ?,
                      flavourtext = ?,
                      creator = ?,
                      seticon = ?,
                      rarity = ?
                   WHERE id = ?; '''
                   
        cursor = self._connection.cursor()
        cursor.execute(sql, card_sql)
        self._connection.commit()        
        
    def save(self, card):
        card_sql = (card.get_id(),);
        sql = """ SELECT 1 FROM cards WHERE id = ?; """
        cursor = self._connection.cursor()
        cursor.execute(sql, card_sql)
        if cursor.fetchone() == None:
            self.create(card)
        else:
            self.update(card)
        
    def delete(self, card):
        cursor = self._connection.cursor()
        cursor.execute('DELETE card FROM cards') # Fix this
        self._connection.commit()
        
    def find_by_cube(self, cube):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM cards')
        rows = cursor.fetchall()
        return rows

card_repository = CardRepository(get_database_connection())
        
    
