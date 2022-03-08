from User import User
class Profile():
    def __init__(self,username, reviews,reviewers_total, profile_image):
        # super().__init__(email, password,username,user_type)
        if (type(reviews) is not float):
            raise TypeError("review must be a float")
        if (reviews<0) or (reviews>5):
            raise ValueError("reviews must be between 0 and 5")
        self.username=username
        self.reviewers_total=reviewers_total
        self.user_items = []
        self.reviews = reviews
        self.profile_image=profile_image
    def _Review_Score(self, new_review):
        if (type(new_review) is not int):
            raise TypeError("reviews must be an integer")
        if (new_review<0) or (new_review>5):
            raise ValueError("reviews must be between 0 and 5")
        total_reviews=self.reviewers_total*self.reviews
        self.reviewers_total=self.reviewers_total+1
        self.reviews=(total_reviews+new_review)/self.reviewers_total
    def _Add_Item_to_Sell(self,item):
        self.user_items.append(item)
    def _Remove_Item(self,item):
        self.user_items.remove(item)
