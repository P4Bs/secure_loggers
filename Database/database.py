"""
    database Python module

    This file defines the class Database to manage database insertion and table entries retrieval
"""

from Classes.application_log import ApplicationLog
from Meta.singleton_meta import SingletonMeta
from sqlalchemy import create_engine, engine, select, Sequence, Row
from sqlalchemy.orm import Session


class Database(metaclass=SingletonMeta):
    engine: engine

    def __init__(self) -> None:
        db_file: str = "C:/Databases/loggers.db"
        self.engine = create_engine(f"sqlite:///{db_file}")
        print(f"Connected to database with connection string sqlite:///{db_file}")

    def insert(self, log_entry: ApplicationLog) -> None:
        with Session(self.engine) as session:
            session.add(log_entry)
            session.commit()

    def retrieve_logs_optional_date(self, oldest_date: str = None) -> Sequence[Row[ApplicationLog]]:
        with (Session(self.engine) as session):
            query = select(ApplicationLog)
            if oldest_date:
                query = query.where(ApplicationLog.date >= oldest_date)
            query = query.order_by(ApplicationLog.date.desc())
            return session.execute(query).yield_per(1000)

    # TODO: CHECK COMMENTED CODE
    # def execute_query(self, query: Select[SystemLog]) -> Sequence[Row[SystemLog]]:
    #     with (Session(self.engine) as session):
    #         return session.execute(query).yield_per(1000)
