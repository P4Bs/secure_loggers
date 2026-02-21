from Constants.constants import EVENT_LOGS
from Loggers.file_logger_factory import log_call, FileLoggerFactory

@log_call(FileLoggerFactory.get_logger(EVENT_LOGS))
def modify_username(username):
    print(f"Username changed to: {username}")
