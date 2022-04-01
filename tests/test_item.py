from typing import Type
import unittest
from item import Item
from User import User

class testItem(unittest.TestCase):

    def setUp(self):
        self.user = User("josue@techexchange.in", "Password123", "josue237")

        self.item1 = Item("Yosemite Tee",15.00,"L","Sportswear","Men","Basic T-shirt for everyday use","../images/yosemite_tee.png", self.user)
        self.item2 = Item("Japan Tee",25.00,"M","Casual","Men","Basic T-shirt for everyday use","../images/japan_tee.png", self.user)
        self.item3 = Item("Blue Shirt",10.00,"S","Casual","Men","Basic T-shirt for everyday use","../images/blue_shirt.png", self.user)
        self.item4 = Item("Black Running Jacket",25.00,"L","Sportswear","Men","Basic T-shirt for everyday use","../images/running_jacket_black.png", self.user)
        self.item5 = Item("Spread Positive Energy Shirt",15.00,"L","Casual","Men","Basic T-shirt for everyday use","../images/spreed_energy_tee.png", self.user)
        self.item6 = Item("White Tee",10.00,"S","Casual","Men","Basic T-shirt for everyday use","../images/white_shirt.png", self.user)
        self.item7 = Item("Green Running Jacket",35.00,"M","Casual","Men","Basic T-shirt for everyday use","../images/running_jacket_green.png", self.user)

    def test00_init(self):
        self.assertEqual(self.item1.name, "Yosemite Tee")
        self.assertEqual(self.item2.price, 25.00)
        self.assertEqual(self.item3.size, "S")
        self.assertEqual(self.item4.style, "Sportswear")
        self.assertEqual(self.item5.gender, "Men")
        self.assertEqual(self.item6.description, "Basic T-shirt for everyday use")
        self.assertEqual(self.item7.image, "../images/running_jacket_green.png")
        self.assertEqual(self.item7.username, self.user.get_username())
    def test01_init_types(self):
        self.assertRaises(TypeError, Item, False,0.00,"XXS","aa","Men","aa","aa",self.user)
        self.assertRaises(TypeError, Item, "aa",0,"XS","aa","aa","Women","aa",self.user)
        self.assertRaises(TypeError, Item, "aa",0.00,False,"aa","Men","aa","aa",self.user)
        self.assertRaises(TypeError, Item, "aa",0.00,"S",False,"Women","aa","aa",self.user)
        self.assertRaises(TypeError, Item, "aa",0.00,"M","aa",False,"aa","aa",self.user)
        self.assertRaises(TypeError, Item, "aa",0.00,"L","aa","Men",False,"aa",self.user)
        self.assertRaises(TypeError, Item, "aa",0.00,"XL","aa","Women","aa",False,self.user)
        self.assertRaises(TypeError, Item, "aa",0.00,"XXL","aa","Men","aa","aa",False)
    def test02_init_values(self):
        self.assertRaises(ValueError, Item, "",0.00,"XXS","aa","Men","aa","aa",self.user)  # String len
        self.assertRaises(ValueError, Item, "aa",-1337.00,"XS","aa","Women","aa","aa",self.user)  # Negative number
        self.assertRaises(ValueError, Item, "aa",0.00,"S","aa","chair","aa","aa",self.user)  # Gender
        self.assertRaises(ValueError, Item, "aa",0.00,"plant","aa","Men","aa","aa",self.user)  # Size