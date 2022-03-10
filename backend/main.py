from item import Item
from User import User
from Profile import Profile
import os

def clear_console():
    clear = lambda: os.system('clear')
    clear()

def greet():
    print("Hello, Welcome to Borithrift an online platform for boricuas to exchange second-hand products\n" )
    history = ""
    user = ''
    while(history != 1 and history !=2):
        try:
            history = int(input("Are you a returning user: Press 1 for yes and 2 to sign up:\n"))
            if history != 1 and history !=2:
                print("Option not available\n")
        except:
            print("Invalid type of entry")
    if(history==1):
        print("Welcome back! Please provide your username and password:")
        while(type(user) == str):
            user = login()
            if(type(user) == str):
                clear_console()
                print(user)
        return user
    elif(history==2):
        print("To an create account, Please provide the following:")
        while(type(user) == str):
            user = register()
            if(type(user) == str):
                clear_console()
                print(user)

        new_user_profile=Profile(user.username,0.0,0,"")
        all_users[user.get_username()] = user 
        all_profiles[user.get_username()] = new_user_profile
        return user


def get_user_items(current_user):
    print('Your items are:')
    for i in range(len(current_user.user_items)):
        print(f'{i+1}. {current_user.user_items[i]}')
    pass

def show_total_items(total_items,username):
    print('Items on sale are:')
    counter=0
    for i in range(len(total_items)):
        if(total_items[i].username != username.username):
            counter+=1
            print(f'{counter}. {total_items[i]}')
            user=all_profiles[total_items[i].username]
            print(f"   Sold by: {user.username} {round(user.ratings,2)} stars")

    pass

def buy_or_sell(user):
    option=input("Press Buy to see and buy items on sale or Sell to exchange your products or Exit to exit:\n")
    clear_console()
    if(option=="Buy"):
        user_profile = all_profiles[user.username]
        show_total_items(all_items,user)
        item_to_buy=-1
        while(item_to_buy<=0 or item_to_buy>len(all_items)-len(user_profile.user_items)):
                try:
                    item_to_buy= int(input("Select Item to Buy by its number on list:"))
                    if (item_to_buy<=0 or item_to_buy>len(all_items)-len(user_profile.user_items)):
                        print("Option not valid")
                except:
                    print("Option not valid")
        counter=0
        for i in range(len(all_items)):        
            if(all_items[i].username!=current_user.username):
                counter+=1
                
            if counter == item_to_buy:
                item_to_buy=i
                break
        item=all_items[item_to_buy]
        seller=all_profiles[item.username]
        seller._Remove_Item(item)
        all_items.remove(item)
        review=-1
        while(review<0 or review>5):
            try:
                review=int(input("Thank you for your purchase, please rate this user from 1 to 5:"))
            except ValueError or TypeError:
                print("Review Score not valid")
        seller._Review_Score(review)
        after=""
        while(after!="Yes" and after!="No"):
            try:
                after=input("Would you like to complete another action?")
            except:
                print("Option not valid")
        if(after=="No"):
            return
        if(after=="Yes"):
            buy_or_sell(user)

    elif(option=="Sell"):
        user_profile = all_profiles[user.username]
        get_user_items(user_profile)
        action=input("Do you wish to add or remove an item?\n Press 1 for Add 2 for Remove and 3 to exit:\n")
        clear_console()
        if(action=="1"):
            name_of_item= str(input("Name of Item:"))
            price_of_item= float(validate_float("Price of Item:"))
            size_of_item= str(input("Size of Item:"))
            style_of_item= str(input("Style of Item:"))
            item_gender= str(input("Gender of Item:"))
            description_of_item= str(input("Description of Item:"))
            item_image= input("Image URL:")
            # def __init__(self, name, price, size, style, gender, description, image, seller):
            item_to_add= Item(name_of_item,price_of_item,size_of_item,style_of_item,item_gender,description_of_item,item_image,user)
            user_profile._Add_Item_to_Sell(item_to_add)
            all_items.append(item_to_add)
            clear_console()
            get_user_items(user_profile)
            buy_or_sell(user)
        elif(action=="2"):
            item_to_remove=-1
            get_user_items(user_profile)
            while(item_to_remove<=0 or item_to_remove>len(user_profile.user_items)-1):
                try:
                    item_to_remove= int(input("Select Item to Remove by its number on list:"))
                except:
                    print("Option not valid")
            user_profile.Remove_Item(user_profile.user_items[item_to_remove-1])
            all_items.remove(user_profile.user_items[item_to_remove-1])
            clear_console()
            print('The item was removed successfully')
            get_user_items(user_profile)
            buy_or_sell(user)
        elif(action=="3"):
            return
    elif(option=="Exit"):
        return
    else:
        print("Option not valid")
        buy_or_sell(user)
    pass


def validate_float(output_val):
    value = input(output_val)
    while(not is_float(value)):
        print('Input value should be of type float')
        value = input(output_val)
    return value

def is_float(values):
    count = 0
    for value in values:
        if(value == '.'):
            count += 1
        elif(value not in '0123456789'):
            return False
    return count <= 1

def register():
    new_username=""
    new_pass=""
    new_email=""
    
    while(not new_username):
        try:
            new_username=input("Select a username:\n")
            if(new_username in all_users):
                new_username=""
                print("Username already exists")
            new_user=User("validemail@gmail.com","ValidPassword1",new_username)
        except:
            print("Invalid entry! username has to be unique and must be between 3-20 characters long and not contain any special characters")
            new_username=""
            
    
    while(not new_pass):
        try:
            new_pass=input("Select a password:\n")
            new_user=User("validemail@gmail.com",new_pass,new_username)
        except:
            print("Invalid entry! Password must be at least 8 characters long and must contain at least 1 letter and 1 number")
            new_pass=""
    while(not new_email):
        try:
            new_email=input("Email:\n")
            new_user=User(new_email,new_pass,new_username)
        except:
            print("Invalid format for email")
            new_email=""      
    return User(new_email, new_pass, new_username)
def login():
    current_user=input("Username:")
    current_pass=input("Password:")
    return validate_user(current_user, current_pass)

def validate_user(username, password):
    if(username in all_users):
        user = all_users[username]
        if(user.compare_password(password)):
            return user
        else:
            return 'Password is incorrect'
    else:
        return 'User does not exist'

def add_items_to_corresponding_profiles(items):
    for item in items:
        username = item.username
        if(username in all_profiles):
            all_profiles[username]._Add_Item_to_Sell(item)

def valid_input_int_type(integer_input):
    if(type(integer_input) != int):
        raise TypeError("Your response has to be an integer")
    return integer_input

def valid_input_int_value(integer_input):
    if(integer_input <1 or integer_input>2):
        raise ValueError("Your response has to be either 1 or 2")
    return integer_input


# All users
victor = User("victor@whereever.com", "a12341231", "victorandresvega")
josue = User("josue@whereever.com", "b5678567857", "josueestr")
kevin = User("kevin@whereever.com", "c0000000000", "kevilin")

# All profiles -- profile is linked with user, through username 
victor_profile = Profile(victor.get_username(),4.25,27,"../flag.png")
josue_profile = Profile(josue.get_username(),3.75,15,"../flag.png")
kevin_profile = Profile(kevin.get_username(),4.45,38,"../flag.png")

# All items -- item is linked with user, through username
victor_item1 = Item("Yosemite Tee",15.00,"L","Sportswear","Men","Basic T-shirt for everyday use","../images/yosemite_tee.png", victor)
victor_item2 = Item("Japan Tee",25.00,"M","Casual","Men","Basic T-shirt for everyday use","../images/japan_tee.png", victor)
victor_item3 = Item("Blue Shirt",10.00,"S","Casual","Men","Basic T-shirt for everyday use","../images/blue_shirt.png", victor)
josue_item1 = Item("Black Running Jacket",25.00,"L","Sportswear","Men","Basic T-shirt for everyday use","../images/running_jacket_black.png", josue)
josue_item2 = Item("Spread Positive Energy Shirt",15.00,"L","Casual","Men","Basic T-shirt for everyday use","../images/spreed_energy_tee.png", josue)
kevin_item1 = Item("White Tee",10.00,"S","Casual","Men","Basic T-shirt for everyday use","../images/white_shirt.png", kevin)
kevin_item2 = Item("Green Running Jacket",35.00,"M","Casual","Men","Basic T-shirt for everyday use","../images/running_jacket_green.png", kevin)

# Fake DB of items 
all_items= [victor_item1,victor_item2,victor_item3,josue_item1,josue_item2,kevin_item1,kevin_item2]
# Fake DB of users 
all_users= {"victorandresvega": victor,"josueestr": josue,"kevilin": kevin}
# Fake DB of profiles
all_profiles = {"victorandresvega": victor_profile, "josueestr": josue_profile, "kevilin": kevin_profile}

# adding items to the corresponding user's profile
add_items_to_corresponding_profiles(all_items)

# start program
current_user=greet()
clear_console()
buy_or_sell(current_user)
     

# boricuas API
'''
all_users = []
all_profiles = []

def create_user(username, password):
    user = User(username, password)
    profile = Profile(..., username)

   all_profile.add(profile)
   all_users.add(user)
   '''


