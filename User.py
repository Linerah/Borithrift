import hashlib
import re
import time
class User:
    """
    Creates a user which stores and validates and email, a password and a username.

    Attrbibutes:
        email (str): The user's email adress. Verified to be RFC 5322 comliant.
        password (str): The user's password. Verified to be 8 chara, 1 letter and 1 number minimum length. Stored as hash from sha512.
        username (str): The user's displayed name. Verified to be 3-20 alphanum characters and can include "." and "_".
    """
    @staticMethod
    def create_new_user(email, password, username):
        return User(email, password, username)
    
    @staticMethod
    def save_user(user):
        connection = post.connect()
        mongo.save({"user", convert_to_json(user)})
        
    def __init__(self, email, password, username):
        if ((type(email) is not str) or (type(password) is not str) or 
        (type(username) is not str)):
            raise TypeError("email, password and username parameters must be strings")

        if (not self.check_valid_email(email)):
            raise ValueError("Invalid email")
        if (not self.check_valid_password(password)):
            raise ValueError("Invalid password")
        if (not self.check_valid_username(username)):
            raise ValueError("Invalid username")
    
        self.email = email
        self.password = self.hash_password(password)
        self.username = username
        self.usr_id = self.generate_user_ID()
    
    # Setters
    def set_email(self, email):
        if (not self.check_valid_email(email)):
            raise ValueError("Invalid email")
        self.email = email
    def set_password(self, password):
        if (not self.check_valid_password(password)):
            raise ValueError("Invalid password")
        self.password = self.hash_password(password)
    def set_username(self, username):
        if (not self.check_valid_username(username)):
            raise ValueError("Invalid username")
        self.username = username
    # Getters
    def get_email(self):
        return self.email
    def get_password(self):
        return self.password
    def get_username(self):
        return self.username

    # Validity checks
    def check_valid_email(self, email):
        # Uses RFC 5322 email standard to check if an email is valid
        regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        if (re.fullmatch(regex, email)):
            return True
        return False
    def check_valid_password(self, password):
        # Min 8 chars, 1 letter, 1 number
        time.sleep(1)  # Make password verification slower to prevent brute force attack
        regex = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
        if (re.fullmatch(regex, password)):
            return True
        return False
    def check_valid_username(self, username):
        # 3-20 alphanum chars and "." "_"
        regex = re.compile(r"[a-zA-Z0-9._]{3,20}$")
        if (re.fullmatch(regex, username)):
            return True
        return False

    # Generators
    def hash_password(self, password):
        # Hashes password and returns hash in hexadecimal format
        hashed_password = hashlib.sha512()
        hashed_password.update(password.encode("utf8"))
        return hashed_password.hexdigest()
    def generate_user_ID(self):
        # Generate unique user ID
        cur_time = str(time.time())
        hashed_time = hashlib.sha1()
        hashed_time.update(cur_time.encode("utf8"))
        return hashed_time.hexdigest()
    def to_json(self):
        # Returns a dictionary of the user's attributes
        return {
            "email": self.email,
            "password": self.password,
            "username": self.username,
            "usr_id": self.usr_id
        }

    # Compare
    def compare_password(self, password):
        # Checks if input password matches stored password
        if (self.password == self.hash_password(password)):
            return True
        return False

    # MongoDb 
    @staticmethod
    def create_user(email, password, username, database):
        # Creates and returns a user object which is also stores in mongoDB database
        user = User(email, password, username)
        user_document = user.to_json()
        collection = database.db.items
        print(user_document)
        collection.insert_one(user_document)
        return user
    @staticmethod
    def get_user(username, database):
        # Returns a user object from mongoDB database if user if found. Returns None otherwise
        collection = database.db.items
        user_document = collection.find_one({"username": username})
        if (user_document is None):
            return None
        return User(user_document["email"], user_document["password"], user_document["username"])