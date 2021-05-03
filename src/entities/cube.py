import uuid
#import User

class Cube:
    """ Class that represents a single cube. Cube can
        belong to some users and they can add cards in a cube.
    Attributes:
        _cube_id: [String] Cube's unique id.
        _name: [String] Cube's name.
        _users: [List String] List of (unique) usernames that
                has an access to the cube.
        _seticon: [String] Cube's seticon (path).
    """

    def __init__(self, name):
        """ Class constructor. Creates a new cube.

        Args:
            name: [String] Name of the cube.
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
        """ Creates a printable string of the usernames.
        Return:
            [String] Usernames in a string or "Ei käyttäjiä" if there are none.
        """

        if not self._users:
            return "Ei käyttäjiä"
        return ', '.join(self._users)

    ## Set
    def set_id(self, cube_id):
        """ Sets cube's id.
        Args:
            card_id: [String] The id to be set.
        """

        self._cube_id = cube_id

    def set_name(self, name):
        """ Sets cube's name.
        Args:
            name: [String] The name to be set.
        """

        self._name = name

    def set_users(self, users):
        """ Sets a list of users that has the cube.
        Args:
            users: [List or String] A list of usernames or
                   a string of them to be set.
        """

        if isinstance(users, list):
            self._users = users
        else:
            self._users = users.split(",")

    def set_image(self, image):
        """ Sets cube's image.
        Args:
            image: [String] The image (path) to be set.
        """

        self._image = image

    def set_seticon(self, seticon):
        """ Sets cube's seticon.
        Args:
            seticon: [String] The seticon (path) to be set.
        """

        self._seticon = seticon

    ## Add
    def add_user(self, username):
        """ Adds a username in the users list.
        Args:
            username: [String] The username to be added.
        """

        if username not in self._users:
            self._users.append(username)

    ## Remove
    def remove_user(self, username):
        """ Removes a username from the users list.
        Args:
            username: [String] The username to be removed.
        """

        if username is not None:
            if username in self._users:
                self._users.remove(username)
