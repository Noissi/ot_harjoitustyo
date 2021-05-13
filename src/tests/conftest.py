from initialise_database import initialise_database


def pytest_configure():
    initialise_database()