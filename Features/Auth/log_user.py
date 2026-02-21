from Constants.constants import INFO
from Loggers.TypeLoggers.log_application_event import log_application_event


@log_application_event(level=INFO)
def log_in_user(username: str, password: str):
    print(f'Login user {username} with password {password}')