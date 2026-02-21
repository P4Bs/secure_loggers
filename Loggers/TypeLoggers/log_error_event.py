"""

"""

import datetime
import linecache
import os
import sys
import threading
from Classes.error_log import ErrorLog
from Loggers.database_logger import db_logger


def log_error_event(message: str = None) -> None:
    except_type, except_value, traceback = sys.exc_info()
    file_path: str = traceback.tb_frame.f_code.co_filename
    line_number: int = traceback.tb_lineno
    error_log = ErrorLog(
        date=datetime.datetime.now().isoformat(),
        logger_name=db_logger.__class__.__name__,
        exception_type=except_type.__name__,
        exception_value=str(except_value),
        file_path=file_path,
        line_number=line_number,
        function_name=sys._getframe().f_back.f_code.co_name,
        code_line=linecache.getline(file_path, line_number).strip(),
        pid=os.getpid(),
        thread_name=threading.current_thread().name,
        message=message
    )
    db_logger.insert(error_log)
    return None
