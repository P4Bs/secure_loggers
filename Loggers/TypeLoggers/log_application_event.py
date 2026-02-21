"""

    The secure_log function is a function wrapper that provides the functionality to log function calls to the function
    to which the wrapper is applied to.
"""

import datetime
import functools
import inspect
import os
import threading
from Classes.application_log import ApplicationLog
from inspect import Traceback
from Loggers.database_logger import db_logger


def log_application_event(level: str, message: str = None):
    def log_to_database(func):
        @functools.wraps(func)
        def func_wrapper(*args, **kwargs):
            caller_traceback: Traceback = inspect.getframeinfo(inspect.currentframe().f_back)
            system_log = ApplicationLog(
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
            db_logger.insert(system_log)
            return func(*args, **kwargs)

        return func_wrapper

    return log_to_database
