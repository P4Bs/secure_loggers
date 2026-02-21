"""
    log_to_database Python module

    This file defines the class for the database logger utility.
"""

from Database.database import Database
from sqlalchemy import Sequence, Row
from Classes.application_log import ApplicationLog


class DatabaseLogger:
    def __init__(self):
        self.database: Database = Database()

    def insert(self, log: ApplicationLog) -> None:
        self.database.insert(log)

    def retrieve_logs(self, oldest_date: str = None) -> Sequence[Row[ApplicationLog]]:
        if oldest_date:
            return self.database.retrieve_logs_optional_date(oldest_date)
        return self.database.retrieve_logs_optional_date()


db_logger = DatabaseLogger()
