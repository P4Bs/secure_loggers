import datetime
import os
import sys
import threading
from error_log import ErrorLog
from log_to_database import db_logger


def log_error(message: str = None) -> None:
    except_type, except_value, traceback = sys.exc_info()
    error_log = ErrorLog(
        date=datetime.datetime.now().isoformat(),
        logger_name=db_logger.__class__.__name__,
        except_type=except_type,
        except_value=except_value,
        file_path=traceback.f_code.co_filenime,
        line_number=traceback.f_lineno,
        local_variables=traceback.f_locals,
        global_variables=traceback.f_globals,
        process_id=os.getpid(),
        thread_name=threading.current_thread().name,
        message=message
    )
    db_logger.log_error(error_log)
    return None
