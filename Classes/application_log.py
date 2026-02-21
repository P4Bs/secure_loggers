"""
    Author: Pablo Jesús Moreno Polo
    application_log Python module

    This file defines the class for the database table application_logs on the logging Database
"""

import datetime
from base import Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import Any


class ApplicationLog(Base):
    __tablename__ = "application_logs"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[str] = mapped_column(default=datetime.datetime.now())
    level: Mapped[str]
    logger_name: Mapped[str]
    file_path: Mapped[str]
    line_number: Mapped[int]
    function_name: Mapped[str]
    code_line: Mapped[str]
    process_id: Mapped[int]
    thread_name: Mapped[str]
    message: Mapped[str]

    def __init__(self, date: str, level: str, logger_name: str, file_path: str,
                 line_number: int, function_name: str, code_line: str, process_id: int,
                 thread_name: str, message: str, **kw: Any):
        super().__init__(**kw)
        self.date = date
        self.level = level
        self.logger_name = logger_name
        self.file_path = file_path
        self.line_number = line_number
        self.function_name = function_name
        self.code_line = code_line.strip()
        self.process_id = process_id
        self.thread_name = thread_name
        self.message = message
