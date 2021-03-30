import os
#from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

'''
try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except FileNotFoundError:
    pass
'''

#IMAGES_FILE_PATH = os.path.join(dirname, '..', 'data')

DATABASE_FILENAME = "database.db"
DATABASE_FILE_PATH = os.path.join(dirname, DATABASE_FILENAME)
