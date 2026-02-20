"""
    AUTHOR: PABLO JESÚS MORENO POLO

    file_logger Python module

    This module defines the class for a file logger.

    It stores every log entry in a single file.
"""

import logging

# TODO: DARLE UNA VUELTA PARA PODER LOGAR EN TRES NIVELEs: ERROR, INFO Y DEBUG
class FileLogger:
    def __init__(self):
        self.setup_file_logger()

    @property
    def file_logger(self):
        if self.file_logger is None:
            self.setup_file_logger()
        return self.file_logger


    def setup_file_logger(self):
        logger_name = "system_log"
        log_file_name = "system_logs.txt"
        formatter = logging.Formatter(
            fmt="%(asctime)s: %(levelname)-8s | %(message)s |",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler = logging.FileHandler(log_file_name, mode='a')
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        self.file_logger = logging.getLogger(logger_name)
        

        self.file_logger.setLevel(level)
        self.file_logger.addHandler(file_handler)
        self.file_logger.addHandler(stream_handler)

    def log_info(self, message: str):
        self.file_logger.info(message)

info_file_logger = FileLogger()
