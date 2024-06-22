import logging
from logging.handlers import RotatingFileHandler
from typing import Optional

class Logger:
    _instance: Optional['Logger'] = None
    _initialized: bool = False

    def __new__(cls, *args, **kwargs) -> 'Logger':
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self, log_file: str = "conversion.log", max_bytes: int = 10485760, backup_count: int = 5):
        if not Logger._initialized:
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.INFO)

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            file_handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
            file_handler.setFormatter(formatter)

            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)
            self.logger.addHandler(stream_handler)
            
            Logger._initialized = True

    def get_logger(self) -> logging.Logger:
        return self.logger
