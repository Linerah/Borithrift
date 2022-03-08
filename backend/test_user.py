import unittest
from User import User

# def __init__(self, email, password, username):
# data for tests
testEmail = "victorandresvega@gmail.com"
testPassword = "Annihilation1"
testUsername = "victorandresvega"

#python3 -m unittest test_user
class TestUser(unittest.TestCase):

    def test_argument_values(self):
        # rating must be an int between 0 and 5
        self.assertRaises(ValueError, User, testEmail, "yes", testUsername)
        self.assertRaises(ValueError, User, testEmail, testPassword, "fnweifuheuifbiufb32uf34if3iuh3iu4h3")
        self.assertRaises(ValueError, User, "fef34f34.com", testPassword, testUsername)
        self.assertRaises(ValueError, User, "@gm,a", testPassword, testUsername)
        self.assertRaises(ValueError, User, "@gmail.com", testPassword, testUsername)
        self.assertRaises(ValueError, User,testEmail, "123445", testUsername)
        self.assertRaises(ValueError, User,testEmail, "adewwee", testUsername)
        self.assertRaises(ValueError, User,testEmail, testPassword, "ddweueuw&3#@")
        self.assertRaises(ValueError, User,"%wfe#@@gmail.com", testPassword, testUsername)
        self.assertRaises(ValueError, User,"test@@email.com", testPassword, testUsername)

    def test_argument_types(self):
        # title, author, and genre must be strings
        self.assertRaises(TypeError, User, 0, testPassword, testUsername)
        self.assertRaises(TypeError, User, testEmail, 0, testUsername)
        self.assertRaises(TypeError, User, testEmail, testPassword, 0)
        self.assertRaises(TypeError, User, True, testPassword, testUsername)
        self.assertRaises(TypeError, User, testEmail, False, testUsername)
        self.assertRaises(TypeError, User, testEmail, testPassword, True)
        self.assertRaises(TypeError, User, None, testPassword, testUsername)
# User('victorandresvega@gmail.com', testPassword, testUsername)

