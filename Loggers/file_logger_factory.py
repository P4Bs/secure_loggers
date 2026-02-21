import logging
import os
from typing import Optional

from Constants.constants import INFO
from Loggers.TableLoggers.log_application_event import log_application_event


class FileLoggerFactory:
    _loggers: dict[str, logging.Logger] = {}

    @classmethod
    def get_logger(
            cls,
            logger_name: str,
            log_file: Optional[str] = None,
            level: int = logging.INFO
    ) -> logging.Logger:
        """
        Returns an existing logger by name or creates a new one.
        If no log_file is provided, defaults to '<logger_name>.log'.
        """
        if logger_name not in cls._loggers:
            log_file = log_file or f"./Logs/{logger_name}.log"
            create_log_file(log_file)
            cls._loggers[logger_name] = setup_logger(logger_name, log_file, level)

        return cls._loggers[logger_name]

    @classmethod
    def list_loggers(cls) -> list[str]:
        """Returns the names of all registered loggers."""
        return list(cls._loggers.keys())

    @classmethod
    def remove_logger(cls, logger_name: str) -> None:
        """Removes a logger and closes its handlers."""
        if logger_name in cls._loggers:
            logger = cls._loggers.pop(logger_name)
            for handler in logger.handlers[:]:
                handler.close()
                logger.removeHandler(handler)


def setup_logger(logger_name, log_file, level=logging.INFO) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    formatter = logging.Formatter(
        fmt="%(asctime)s: %(levelname)-8s | %(message)s |",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler = logging.FileHandler(log_file, mode='a')
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger

@log_application_event(level=INFO, message="A new log file has been created")
def create_log_file(file_name: str) -> None:
    if not os.path.exists(file_name):
        with open(file_name, "w"):
            # Just create the file
            pass
        print(f"Log file {file_name} created")

    return None

def log_call(logger: logging.Logger):
    def log_function_call(func):
        def func_wrapper(*args, **kwargs):
            logger.info(f'Function {func.__name__} called with args: {args}, kwargs: {kwargs}')
            return func(*args, **kwargs)

        return func_wrapper

    return log_function_call
