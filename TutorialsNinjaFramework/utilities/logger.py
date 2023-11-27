import logging
import os

class CustomLogger:
    def __init__(self, logger_name, log_file_path):
        if os.path.exists(log_file_path):
            os.remove(log_file_path)
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        self._configure_file_handler(log_file_path, formatter)
        # self._configure_console_handler(formatter)

    def _configure_file_handler(self, log_file_path, formatter):
        if os.path.exists(log_file_path):
            os.remove(log_file_path)

        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def _configure_console_handler(self, formatter):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger
