"""
    Author: Pablo Jesús Moreno Polo
    error_log Python module

    This file defines the class for the database table error_logs on the logging Database.
"""

import datetime
from base import Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import Any


class ErrorLog(Base):
    __tablename__ = "error_logs"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[str] = mapped_column(default=datetime.datetime.now())
    logger_name: Mapped[str]
    exception_type: Mapped[str]
    exception_value: Mapped[str]
    file_path: Mapped[str]
    line_number: Mapped[int]
    function_name: Mapped[str]
    code_line: Mapped[str]
    pid: Mapped[int]
    thread_name: Mapped[str]
    message: Mapped[str]

    def __init__(self, date: str, logger_name: str, exception_type: str, exception_value: str, file_path: str,
                 line_number: int, function_name: str, code_line: str, pid: int, thread_name: str,
                 message: str, **kw: Any):
        super().__init__(**kw)
        self.date = date
        self.logger_name = logger_name
        self.exception_type = exception_type
        self.exception_value = exception_value
        self.file_path = file_path
        self.line_number = line_number
        self.function_name = function_name
        self.code_line = code_line
        self.pid = pid
        self.thread_name = thread_name
        self.message = message
