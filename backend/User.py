from mimetypes import init


import hashlib
import re
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def check_valid_email(self, email):
        regex = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
        if re.fullmatch(regex, email):
            return True
        return False

    def check_valid_password(self, password):
        # Min 8 chars, 1 letter, 1 number
        regex = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
        if re.fullmatch(regex, password):
            return True
        return False

    # Hashes password and returns hash in hexadecimal format
    def hash_password(self, password):
        hashed_password = hashlib.sha256()
        hashed_password.update(password.encode('utf8'))
        return hashed_password.hexdigest()