from User import User
from item import Item
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
    def _Review_Score(self, new_review):
        if (type(new_review) != int):
            raise TypeError("ratings must be an integer")
        if (new_review<0) or (new_review>5):
            raise ValueError("ratings must be between 0 and 5")
        total_ratings=self.raters_amount*self.ratings
        self.raters_amount=self.raters_amount+1
        self.ratings=(total_ratings+new_review)/self.raters_amount
    def _Add_Item_to_Sell(self,item):
        if(type(item) != Item):
            raise TypeError("object has to be of type Item")
        self.user_items.append(item)
    def _Remove_Item(self,item):
        if(type(item) != Item):
            raise TypeError("object has to be of type Item")
        if(item not in self.user_items):
            raise ValueError("user is not owner of item")
        self.user_items.remove(item)
