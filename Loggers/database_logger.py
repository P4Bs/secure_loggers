from Classes.application_log import ApplicationLog
from Database.database import Database
from sqlalchemy import Sequence, Row


class DatabaseLogger:
    def __init__(self):
        self.database: Database = Database()

    def insert(self, log: ApplicationLog) -> None:
        self.database.insert(log)

    def retrieve_logs(self, oldest_date: str = None) -> Sequence[Row[ApplicationLog]]:
        if oldest_date:
            return self.database.retrieve_application_logs(oldest_date)
        return self.database.retrieve_application_logs()


db_logger = DatabaseLogger()
