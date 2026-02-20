"""
    error_log Python module

    This module define the class for the database table ErrorLogs on the logging Database.

    These logs are stored on the ErrorLogs database table.
"""

import datetime
from Base import Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import Any


class ErrorLog(Base):
    __tablename__ = "ErrorLogs"
    id: Mapped[int] = mapped_column("ID", primary_key=True, autoincrement=True)
    date: Mapped[str] = mapped_column("Date", default=datetime.datetime.now())
    logger_name: Mapped[str] = mapped_column("LoggerName")
    type: Mapped[str] = mapped_column("Type")
    value: Mapped[str] = mapped_column("Value")
    file_path: Mapped[str] = mapped_column("FilePath")
    line_number: Mapped[str] = mapped_column("LineNumber")
    local_variables: Mapped[str] = mapped_column("LocalVariables")
    global_variables: Mapped[str] = mapped_column("GlobalVariables")
    process_id: Mapped[int] = mapped_column("PID")
    thread_name: Mapped[str] = mapped_column("ThreadName")
    message: Mapped[str] = mapped_column("Message")

    def __init__(self, date: str, logger_name: str, except_type: str, except_value: str, file_path: str,
                 line_number: str, local_variables: str, global_variables: str, process_id: int,
                 thread_name: str, message: str, **kw: Any):
        super().__init__(**kw)
        self.date = date
        self.logger_name = logger_name
        self.type = except_type
        self.value = except_value
        self.file_path = file_path
        self.line_number = line_number
        self.local_variables = local_variables
        self.global_variables = global_variables
        self.process_id = process_id
        self.thread_name = thread_name
        self.message = message
