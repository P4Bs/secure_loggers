"""
    system_log Python module

    This module define the class for the database table SystemLogs on the logging Database
"""

import datetime
from Base import Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import Any



class SystemLog(Base):
    __tablename__ = "SystemLogs"
    id: Mapped[int] = mapped_column("ID", primary_key=True, autoincrement=True)
    date: Mapped[str] = mapped_column("Date", default=datetime.datetime.now())
    level: Mapped[str] = mapped_column("Level")
    logger_name: Mapped[str] = mapped_column("LoggerName")
    file_path: Mapped[str] = mapped_column("FilePath")
    line_number: Mapped[int] = mapped_column("LineNumber")
    function_name: Mapped[str] = mapped_column("FunctionName")
    code_line: Mapped[str] = mapped_column("CodeLine")
    process_id: Mapped[int] = mapped_column("PID")
    thread_name: Mapped[str] = mapped_column("ThreadName")
    message: Mapped[str] = mapped_column("Message")

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
