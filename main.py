"""
    main Python module

    This is the entry point of the Python project. It serves as a showcase of both the file logger and the database
    logger.
"""

from logger import log_in_user, log_user_login_to_file


def test_log_to_database():
    log_in_user('test_user', 'this_password_does_not_matter')


# test_log_to_database()

def test_log_to_file():
    log_user_login_to_file('test_user', 'this_password_does_not_matter')


test_log_to_file()