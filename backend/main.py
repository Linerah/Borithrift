from item import Item
from User import User
from Profile import Profile
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
Victor=Profile("victorandresvega",Victor_items,4.25,27,"../flag.png")
Josue_items=[item4,item5]
Josue=Profile("josueestr",Josue_items,3.75,15,"../flag.png")
Kevin_items=[item6,item7]
Kevin=Profile("kevilin",Kevin_items,4.45,38,"../flag.png")
total_items=[item1,item2,item3,item4,item5,item6,item7]
all_users={"victorandresvega":Victor,"josueestr":Josue,"kevilin":Kevin}
# all_users = []
# all_profiles = []
# all_items = [kevins, victors]


def greet():
    print("Hello, Welcome to Borithrift an online platform for boricuas to exchange second-hand products\n" )
    History=input("Are you a returning user: Press 1 for yes and 2 to sign up:\n")
    History=int(History)
    if(type(History) is not int):
        raise TypeError("Your response has to be an integer")
    if(History <1 or History>2):
        raise ValueError("Your response has to be either 1 or 2")
    if(History==1):
        print("Welcome back! Please provide your username and password:")
        current_user=input("Username:")
        current_pass=input("Password:")
        # validate_user(current_user,current_pass)
        return all_users[current_user]
#      if input == "add_user":
#         password=
#         username=
#         all_users.add(User())
    elif(History==2):
        new_user=input("Select a username:\n")
        new_pass=input("Select a password:\n")
        new_email=input("Email:\n")
        type_of_client=input("Seller or Buyer:\n")
        # def __init__(self, email, password, username, user_type):
        # new_user_to_add=User(new_email,new_pass,new_user,type_of_client)
        # all_users.append(new_user_to_add)
        new_user_profile=Profile(new_user,[],0.0,0,"")
        all_users[new_user]=(new_user_profile)
        return new_user_profile

def get_user_items(current_user):
    print('Your items are:')
    for i in range(len(current_user.user_items)):
        print(f'{i+1}. {current_user.user_items[i]}')
    pass
def show_total_items(total_items):
    print('Items on sale are:')
    for i in range(len(total_items)):
        print(f'{i+1}. {total_items[i]}')
    pass
def buy_or_sell(user):
    option=input("Press Buy to see and buy items on sale or Sell to exchange your products:\n")
    if(option=="Buy"):
        show_total_items(total_items)
    elif(option=="Sell"):
        get_user_items(user)
        action=input("Do you wish to add or remove an item?\n Press 1 for Add 2 for Remove and 3 to exit:\n")
        if(action=="1"):
            name_of_item=input("Name of Item:")
            name_of_item=str(name_of_item)
            price_of_item=input("Price of Item:")
            price_of_item=float(price_of_item)
            size_of_item=input("Size of Item:")
            size_of_item=str(size_of_item)
            style_of_item=input("Style of Item:")
            item_gender=input("Gender of Item:")
            description_of_item=input("Description of Item:") 

            item_image=input("Image URL:")
            # def __init__(self, name, price, size, style, gender, description, image, seller):
            item_to_add=Item(name_of_item,price_of_item,size_of_item,style_of_item,item_gender,description_of_item,item_image,user)
            user.Add_Item_to_Sell(item_to_add)
            total_items.append(item_to_add)
            get_user_items(user)
            buy_or_sell(user)
        elif(action=="2"):
            get_user_items(user)
            item_to_remove=input("Select Item to Remove by its number on list:")
            item_to_remove=int(item_to_remove)
            user.Remove_Item(user.user_items[item_to_remove-1])
            total_items.remove(user.user_items[item_to_remove-1])
            get_user_items(user)
            buy_or_sell(user)
        elif(action=="3"):
            return
    pass
current_user=greet()
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


