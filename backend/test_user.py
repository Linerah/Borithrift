import unittest
from User import User

# def __init__(self, email, password, username, user_type):
# data for tests
testEmail = "victorandresvega@gmail.com"
testPassword = "Annihilation"
testUsername = "victorandresvega"
testUserType= "seller"

#python3 -m unittest test_User
class TestUser(unittest.TestCase):

    def test_argument_values(self):
        # rating must be an int between 0 and 5
        self.assertRaises(ValueError, User, testEmail, testPassword, testUsername, testUserType)
        self.assertRaises(ValueError, User, testEmail, testPassword, testUsername, "Neither")
        self.assertRaises(ValueError, User, testEmail, testPassword, testUsername, 0)
        self.assertRaises(ValueError, User, testEmail, testPassword, testUsername, testUserType)

    def test_argument_types(self):
        # title, author, and genre must be strings
        self.assertRaises(TypeError, User, 0, testPassword, testUsername, testUserType)
        self.assertRaises(TypeError, User, testEmail, 0, testUsername, testUserType)
        self.assertRaises(TypeError, User, testEmail, testPassword, 0, testUserType)
        self.assertRaises(TypeError, User, testEmail, testPassword, testUsername, 0)
        self.assertRaises(TypeError, User, testEmail, testPassword, testUsername, testUserType)
        self.assertRaises(TypeError, User, testEmail, testPassword, testUsername, testUserType)
        self.assertRaises(TypeError, User, testEmail, testPassword, testUsername, testUserType)

    def test_updateRating(self):
        # rating must be an int
        self.assertRaises(TypeError, User.Review_Score, self, 3.5)
        self.assertRaises(TypeError, User.Review_Score, self, "5")
        # rating must be an int between 0 and 5
        self.assertRaises(ValueError, User.Review_Score, self, -1)
        self.assertRaises(ValueError, User.Review_Score, self, 6)
        # method successfully updates the rating property
        testUser = User(testEmail, testPassword, testUsername, testUserType)
        testUser.updateRating(3)
        self.assertEqual(testUser.Review_Score, 3)
User('victorandresvega@gmail.com', testPassword, testUsername, "seller")
