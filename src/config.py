import os

dirname = os.path.dirname(__file__)

IMAGES_FILE_PATH      = 'img/'
CARD_IMAGES_FILE_PATH = 'imgcards/'
USER_IMAGES_FILE_PATH = 'imguser/'
USER_FILES_FILE_PATH = 'userfiles/'

DATABASE_FILENAME = "database.db"
DATABASE_FILE_PATH = os.path.join(dirname, DATABASE_FILENAME)

CARD_RATIO = 7/5
