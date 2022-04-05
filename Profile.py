from User import User
from item import Item
"""
    Class is in charge of managing and creating user profiles which contains their username, ratings, 
    the amount of raters that have reviewed this user and the profile image URL. It also contains the items
    the user is currently selling 


    Attrbibutes:
        username (str): username of user
        ratings(float): is the average rating given by all the raters that have reviewed this user
        raters_amount (int): amount of raters that have reviewed this user upon buying from them.
        profile_image (str): Contains the URL of the profile picture of the user.
        """
class Profile():
    def __init__(self,username, ratings,raters_amount, profile_image):
        # super().__init__(email, password,username,user_type)
        if (type(ratings) is not float):
            raise TypeError("review must be a float")
        if (ratings<0) or (ratings>5):
            raise ValueError("ratings must be between 0 and 5")
        if(type(raters_amount) != int):
            raise TypeError("raters amount must be and integer")
        if (raters_amount<0):
            raise ValueError("raters total must be higher or equal to 0")
        if(type(profile_image) != str):
            raise TypeError("URL must be of type string")
        
        self.username=username
        self.raters_amount=raters_amount
        self.user_items = []
        self.ratings = ratings
        self.profile_image=profile_image
    '''
    function that takes in a new rating for the seller from which the item was bought and updates that user's rating
    taking into account the number of their previous raters and rating. It then returns the updated rating of that seller
    in two decimal places
    '''
    @staticmethod
    def create_profile(username, rating, raters_amount, profile_image,database):
        profile = Profile(username, rating, raters_amount, profile_image)
        profile_document = profile.to_json()
        collection = database.db.profiles
        print(profile)
        collection.insert_one(profile_document)
        return profile

    @staticmethod
    def get_user_items(username,database):
        collection = database.db.items
        # Items=collection.find( { "username": username}, { "_id": 0, "name": 0, "size": 0,"price":0,"style":0,"gender":0,"description":0,"image":1,"username":0} )
        Items=collection.find({"username":"kevilin"})
        # Items = collection.find_one({"username": username}).project({"user_items":1})
        return Items

    @staticmethod
    def get_profile(username,database):
        collection=database.db.profiles
        profile=collection.find_one({"username":username})
        return profile
        
    def to_json(self):
        return {'username': self.username, 'ratings': self.ratings , 'raters_amount': self.raters_amount, 'user_items': self.user_items, 'profile_image': self.profile_image}

    def _Review_Score(self, new_review):
        if(type(self.ratings)==None):
            raise ValueError
        if(type(new_review)==None):
            raise ValueError("Cannot be type None")
        if (type(new_review) != int):
            raise TypeError("ratings must be an integer")
        if (new_review<0) or (new_review>5):
            raise ValueError("ratings must be between 0 and 5")
        total_ratings=self.raters_amount*self.ratings
        self.raters_amount=self.raters_amount+1
        self.ratings=(total_ratings+new_review)/self.raters_amount
        return round(self.ratings,2)
    '''
    Function that takes an Item that the user wants to add to the items they are currently selling and updates their list of items
    '''
    
    def Add_Item_to_Sell(self,item):
        
        if(type(item)==None):
            raise ValueError("Cannot be type None")
        if(type(item) != Item):
            raise TypeError("object has to be of type Item")
        if(self.username != item.username):
            raise ValueError("Incorrect Owner")
        self.user_items.append(item)
    @staticmethod
    def Add_Item_to_SellDb(username,item,database):
        collection = database.db.profiles
        collection.update({'username':username},{'$push':{'user_items':item.to_json()}})
        if(type(item)==None):
            raise ValueError("Cannot be type None")
        if(type(item) != Item):
            raise TypeError("object has to be of type Item")
        if(username != item.username):
            raise ValueError("Incorrect Owner")
    @staticmethod
    def get_user_items(username,database):
        collection = database.db.items
        items = collection.find_one({'username':username})
        return items
    @staticmethod
    def get_profile(username,database):
        collection = database.db.profiles
        profile = collection.find_one({'username':username})
        return profile

    '''
    Function that takes in an Item and deletes it from the user's list of items on sale, this is done when a 
    user chooses to stop selling and item or when an item is bought
    '''
    def Remove_Item(self,item):
        if(type(item)==None):
            raise ValueError("Cannot be type None")
        if(type(item) != Item):
            raise TypeError("object has to be of type Item")
        if(item not in self.user_items):
            raise ValueError("user is not owner of item")
        self.user_items.remove(item)