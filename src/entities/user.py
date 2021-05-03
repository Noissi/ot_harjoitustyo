class User:
    """ Class that represents a single user. """

    def __init__(self, username, password):
        """ Class constructor. Creates a new user.
        Attributes:
            _username: [String] Unique identifier of the user.
            _password: [String] Password of the user profile.
            _cubes: [List String] List of cube ids that the user has created.
            _shared_cubes: [List String] List of cube ids that are shared with the user.
        """

        self._username     = username
        self._password     = password
        self._cubes        = []
        self._shared_cubes = []

    ## Get
    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_cubes(self):
        return self._cubes

    def get_shared_cubes(self):
        return self._shared_cubes

    ## Set
    def set_username(self, username):
        """ Sets username.
        Args:
            username: [String] The username to be set.
        """

        self._username = username

    def set_password(self, password):
        """ Sets user's password.
        Args:
            password: [String] The password to be set.
        """

        self._password = password

    def set_cubes(self, cubes):
        """ Sets a list of cubes that the user has created.
        Args:
            cubes: [List or String] A list of Cube id's or a string of them to be set.
        """

        if isinstance(cubes, list):
            self._cubes = cubes
        else:
            self._cubes = cubes.split(",")

    def set_shared_cubes(self, shared_cubes):
        """ Sets a list of shared cubes that the user has.
        Args:
            shared_cubes: [List or String] A list of Cube id's or a string of them to be set.
        """

        if isinstance(shared_cubes, list):
            self._shared_cubes = shared_cubes
        else:
            self._shared_cubes = shared_cubes.split(",")

    ## Get print
    def get_cubes_print(self):
        """ Creates a printable string of the cube ids.
        Return:
            [String] Cube ids in a string.
        """

        if not self._cubes:
            return ""
        return ', '.join(self._cubes)

    def get_shared_cubes_print(self):
        """ Creates a printable string of the shared cube ids.
        Return:
            [String] Shared cube ids in a string.
        """

        if not self._shared_cubes:
            return ""
        return ', '.join(self._shared_cubes)

    ## Add
    def add_cube(self, cube_id):
        """ Adds a cube id in the cubes list.
        Args:
            cube_id: [String] The cube id to be added.
        """

        if cube_id not in self._cubes:
            self._cubes.append(cube_id)

    def add_shared_cube(self, cube_id):
        """ Adds a cube id in the shared cubes list.
        Args:
            cube_id: [String] The cube id to be added.
        """

        if cube_id not in self._shared_cubes:
            self._shared_cubes.append(cube_id)

    ## Remove
    def remove_cube(self, cube_id):
        """ Removes a cube id from the cubes list.
        Args:
            cube_id: [String] The cube id to be removed.
        """

        if cube_id in self._cubes:
            self._cubes.remove(cube_id)

    def remove_shared_cube(self, cube_id):
        """ Removes a cube id from the shared cubes list.
        Args:
            cube_id: [String] The cube id to be removed.
        """

        if cube_id in self._shared_cubes:
            self._shared_cubes.remove(cube_id)
