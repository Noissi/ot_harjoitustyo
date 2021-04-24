import uuid
#import User

class Cube:
    """ Class that represents a single cube. """

    def __init__(self, name):
        """ Class constructor. Create a new cube.

        Args:
            cube_id:
                [String] Cube id
            name:
                [String] Name of the cube
            users:
                [List String] List of users who can access the cube.
            seticon:
                [String] Path to a seticon image
        """

        self._cube_id = str(uuid.uuid4())
        self._name    = name
        self._users   = []
        self._image   = ""
        self._seticon = ""

    ## Get
    def get_id(self):
        return self._cube_id

    def get_name(self):
        return self._name

    def get_users(self):
        return self._users

    def get_image(self):
        return self._image

    def get_seticon(self):
        return self._seticon

    ## Get print
    def get_users_print(self):
        if not self._users:
            return "Ei käyttäjiä"
        return ', '.join(self._users)

    ## Set
    def set_id(self, cube_id):
        self._cube_id = cube_id

    def set_name(self, name):
        self._name = name

    def set_users(self, users):
        if isinstance(users, list):
            self._users = users
        else:
            self._users = users.split(",")

    def set_image(self, image):
        self._image = image

    def set_seticon(self, seticon):
        self._seticon = seticon

    ## Add
    def add_user(self, user_id):
        if user_id not in self._users:
            self._users.append(user_id)

    ## Remove
    def remove_user(self, user_id):
        if user_id is not None:
            if user_id in self._users:
                self._users.remove(user_id)
