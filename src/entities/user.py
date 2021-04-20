class User:
    """ Class that represents a single user. """

    def __init__(self, username, password):
        """ Class constructor. Create a new user.
        Args:
            username: [String] Unique identifier of the user.
            password: [String] Password of the user profile.
        """

        self._username = username
        self._password = password
        self._cubes = []
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
        self._username = username

    def set_password(self, password):
        self._password = password

    def set_cubes(self, cubes):
        if type(cubes) is list:
            self._cubes = cubes
        else:
            self._cubes = cubes.split(",")

    def set_shared_cubes(self, shared_cubes):
        if type(shared_cubes) is list:
            self._shared_cubes = shared_cubes
        else:
            self._shared_cubes = shared_cubes.split(",")

    ## Get print
    def get_cubes_print(self):
        if not self._cubes:
            return ""
        return ', '.join(self._cubes)

    def get_shared_cubes_print(self):
        if not self._shared_cubes:
            return ""
        return ', '.join(self._shared_cubes)

    ## Add
    def add_cube(self, cube_id):
        if cube_id not in self._cubes:
            self._cubes.append(cube_id)

    def add_shared_cube(self, cube_id):
        if cube_id not in self._shared_cubes:
            self._shared_cubes.append(cube_id)

    ## Remove
    def remove_cube(self, cube_id):
        if cube_id in self._cubes:
            self._cubes.remove(cube_id)

    def remove_shared_cube(self, cube_id):
        if cube_id in self._shared_cubes:
            self._shared_cubes.remove(cube_id)
