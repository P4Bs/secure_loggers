"""
    log_to_database Python module

    This module defines the class for the database logger utility.

    The instance of this database logger utility in this file is the object db_logger

    The secure_log function is a function wrapper that provides the functionality to log function calls to the function
    to which the wrapper is applied to.
"""

import datetime
import functools
import inspect
import os
import threading
from database import Database
from inspect import Traceback
from sqlalchemy import Sequence, Row
from system_log import SystemLog


class DatabaseLogger:
    def __init__(self):
        self.database: Database = Database()

    def log_to_table(self, log: SystemLog) -> None:
        self.database.add_log_entry(log)

    def retrieve_logs(self, oldest_date: str = None) -> Sequence[Row[SystemLog]]:
        if oldest_date:
            return self.database.retrieve_logs_optional_date(oldest_date)
        return self.database.retrieve_logs_optional_date()


db_logger = DatabaseLogger()


def secure_log_function_call(level: str, message: str = None):
    def log_to_database(func):
        @functools.wraps(func)
        def func_wrapper(*args, **kwargs):
            caller_traceback: Traceback = inspect.getframeinfo(inspect.currentframe().f_back)
            system_log = SystemLog(
                date=datetime.datetime.now().isoformat(),
                level=level,
                logger_name=db_logger.__class__.__name__,
                file_path=caller_traceback.filename,
                line_number=caller_traceback.lineno,
                function_name=caller_traceback.function,
                code_line=caller_traceback.code_context[0] if caller_traceback.code_context else None,
                process_id=os.getpid(),
                thread_name=threading.current_thread().name,
                message=message
            )
            db_logger.log_to_table(system_log)
            return func(*args, **kwargs)

        return func_wrapper

    return log_to_database
