import hashlib
import re
import time
class User:
    def __init__(self, email, password, username):
        if ((type(email) is not str) or (type(password) is not str) or 
        (type(username) is not str)):
            raise TypeError("email, password, username and user_type parameters must be strings")

        if (not self.check_valid_email(email)):
            raise ValueError("Invalid email")
        if (not self.check_valid_password(password)):
            raise ValueError("Invalid password")
        if (not self.check_valid_username(username)):
            raise ValueError("Invalid username")
    
        self.email = email
        self.password = password
        self.username = username
        self.usr_id = self.generate_user_ID()
    
    # Setters
    def set_password(self, password):
        if (not self.check_valid_password(password)):
            raise ValueError("Invalid password")
        self.password = password
    def set_email(self, email):
        if (not self.check_valid_email(email)):
            raise ValueError("Invalid email")
        self.email = email
    def set_username(self, username):
        if (not self.check_valid_username(username)):
            raise ValueError("Invalid username")
        self.username = username
    # Getters
    def get_email(self):
        return self.email
    def get_username(self):
        return self.username

    # Check validity
    def check_valid_email(self, email):
        # RFC 5322 email standard
        regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        if (re.fullmatch(regex, email)):
            return True
        return False
    def check_valid_password(self, password):
        # Min 8 chars, 1 letter, 1 number
        regex = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
        if (re.fullmatch(regex, password)):
            return True
        return False
    def check_valid_username(self, username):
        # 3-20 alphanum cahrs and "." "_"
        regex = re.compile(r"[a-zA-Z0-9._]{3,20}$")
        if (re.fullmatch(regex, username)):
            return True
        return False

    # Hashes password and returns hash in hexadecimal format
    def hash_password(self, password):
        hashed_password = hashlib.sha512()
        hashed_password.update(password.encode("utf8"))
        return hashed_password.hexdigest()
    
    # Generate unique user ID
    def generate_user_ID(self):
        cur_time = str(time.time())
        hashed_time = hashlib.sha1()
        hashed_time.update(cur_time.encode("utf8"))
        return hashed_time.hexdigest()

#! Make password attempts slow to prevent brute force attacks (done outside class)