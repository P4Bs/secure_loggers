"""
    main Python module

    This is the entry point of the Python project. It serves as a showcase of both the file logger and the database
    logger.
"""
from Features.Auth.log_user import log_in_user
from Loggers.TypeLoggers.log_error_event import log_error_event

def test_log_to_database():
    log_in_user('test_user', 'this_password_does_not_matter')

def function_that_produces_exception():
    value: float
    try:
        value = 1 / 0.0
    except ZeroDivisionError:
        log_error_event("Se ha producido una excepcion al dividir entre cero")
        raise

    print(value)


function_that_produces_exception()
