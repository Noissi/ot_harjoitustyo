import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv('DATABASE_FILENAME') or 'database.db'
DATABASE_FILE_PATH = os.path.join(dirname, DATABASE_FILENAME)

IMAGES_FILE_PATH      = 'img/'
CARD_IMAGES_FILE_PATH = 'imgcards/'
USER_IMAGES_FILE_PATH = 'imguser/'
USER_FILES_FILE_PATH  = 'userfiles/'

CARD_RATIO = 7/5
