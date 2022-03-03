import hashlib
import re
class User:
    def __init__(self, email, password,username,Usertype):
        self.email = email
        self.password = password
        self.username =username
        self.type=type
        if type(username) is not str or type(Usertype) is not str :
            raise TypeError("username and Usertype must be a string")
    # Setters
    def set_password(self, password):
        self.password = password
    def set_email(self, email):
        self.email = email
    # Getters
    def get_email(self):
        return self.email

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
        hashed_password = hashlib.sha512()
        hashed_password.update(password.encode('utf8'))
        return hashed_password.hexdigest()

#! Make password attempts slow to prevent brute force attacks (done outside class)