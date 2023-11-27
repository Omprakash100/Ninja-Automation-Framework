import os
from dotenv import load_dotenv

class CredentialsManager:
    def __init__(self):
        load_dotenv()
        self.valid_email = os.getenv("valid_email")
        self.valid_password = os.getenv("valid_password")

    def get_valid_email(self):
        return self.valid_email

    def get_valid_password(self):
        return self.valid_password