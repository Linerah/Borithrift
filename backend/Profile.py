
class Profile():
    def __init__(self, username, userItems, reviews,reviewesTotal, profileImage):
        if (type(username) is not str or type(profileImage) is not str): 
            raise TypeError("username and profile URL must be a string")
        if (type(userItems) is not dict):
            raise TypeError("user items must be a dictionary")
        if (type(reviews) is not int):
            raise TypeError("review must be an integer")
        if (reviews<0) or (reviews>5):
            raise ValueError("reviews must be between 0 and 5")
        self.reviewersTotal=reviewesTotal
        self.username = username
        self.userItems = userItems
        self.reviews = reviews
        self.profileImage=profileImage
    def ReviewScore(self, newReview):
        if (type(newReview) is not int):
            raise TypeError("reviews must be an integer")
        if (newReview<0) or (newReview>5):
            raise ValueError("reviews must be between 0 and 5")
        totalreviews=self.reviewersTotal*self.reviews
        self.reviewersTotal=self.reviewersTotal+1
        self.reviews=(totalreviews+newReview)/self.reviewersTotal
        