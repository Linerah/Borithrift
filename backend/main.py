from item import Item
from User import User
from profile import Profile
# def __init__(self, name, price, size, style, gender, description, image, seller):
item1=Item("Yosemite Tee",15.00,"L","Sportswear","Men","Basic T-shirt for everyday use","../images/yosemite_tee.png","victorandres")
item2=Item("Japan Tee",25.00,"M","Casual","Men","Basic T-shirt for everyday use","../images/japan_tee.png","josuestr")
item3=Item("Blue Shirt",10.00,"S","Casual","Men","Basic T-shirt for everyday use","../images/blue_shirt.png","victorandres")
item4=Item("Black Running Jacket",25.00,"L","Sportswear","Men","Basic T-shirt for everyday use","../images/running_jacket_black.png","victorandres")
item5=Item("Spread Positive Energy Shirt",15.00,"L","Casual","Men","Basic T-shirt for everyday use","../images/spreed_energy_tee.png","victorandres")
item6=Item("White Tee",10.00,"S","Casual","Men","Basic T-shirt for everyday use","../images/white_shirt.png","victorandres")
item7=Item("Green Running Jacket",35.00,"M","Casual","Men","Basic T-shirt for everyday use","../images/running_jacket_green.png","victorandres")
#def __init__(self, user_items, reviews,reviewers_total, profile_image):
    # def __init__(self, email, password,username,user_type):
Victor_items=[item1,item2,item3]
Victor=Profile("victorvegaward@techexchange.in","12345678","victorandres","Seller",Victor_items,4.25,27,"../flag.png")
Josue_items=[item4,item5]
Josue=Profile("josue@techexchange.in","GoogleTech","josuestr","Seller",Victor_items,3.75,15,"../flag.png")
Kevin_items=[item6,item7]
Kevin=Profile("kevinlinera@techexchange.in","HotDog","kevilin","Seller",Victor_items,4.45,38,"../flag.png")
total_items=[item1,item2,item3,item4,item5,item6,item7]

def greet():
    print("Hello, Welcome to Borithrift an online platform for boricuas to exchange second-hand products" )
    History=input("Are you a returning user: Press 1 for yes and 2 to sign up:")
    History=int(History)
    if(type(History) is not int):
        raise TypeError("Your response has to be an integer")
    if(History <1 or History>2):
        raise ValueError("Your response has to be either 1 or 2")
    if(History==1):
        print("Welcome back! Please give your username")
        current_user=input("Username:")
        current_pass=input("Password:")
        # validate_user(current_user,current_pass)
    pass
greet()
