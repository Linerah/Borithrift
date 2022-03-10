import  unittest
from Profile import Profile
from User import User
from item import Item

class TestProfile(unittest.TestCase):
    def setUp(self):
        print('Running setUp...')
        self.victor_profile = Profile("victorandresvega", 4.25,27,"../flag.png")
        self.josue_profile = Profile("josueestr", 3.75, 15,"../flag.png")
        self.kevin_profile = Profile("kevilin", 4.45, 38,"../flag.png")
        self.victor = User("victor@whereever.com", "a12341231", "victorandresvega")
        self.victor_item1 = Item("Yosemite Tee",15.00,"L","Sportswear","Men","Basic T-shirt for everyday use","../images/yosemite_tee.png", self.victor)

    
    # Tear Down will run even if a method succeeded or not
    # TODO: we could remove the tear dow, because we are not actually disposing
    def tearDown(self): 
        print('Running Teardown...')

    
    def test_init(self):
        test_usernames = [(self.victor_profile.username,"victorandresvega"), (self.josue_profile.username, "josueestr"), (self.kevin_profile.username, "kevilin")]
        for test_username, username in test_usernames:
            with self.subTest():
                self.assertEqual(test_username, username)

        test_reviews = [(self.victor_profile.reviews, 4.25), (self.josue_profile.reviews, 3.75), (self.kevin_profile.reviews, 4.45)]
        for test_review, review in test_reviews:
            with self.subTest():
                self.assertEqual(test_review, review)
        
        test_reviewers_total = [(self.victor_profile.reviewers_total, 27), (self.josue_profile.reviewers_total, 15), (self.kevin_profile.reviewers_total, 38)]
        for test_reviewer_total, reviewer_total in test_reviewers_total:
            with self.subTest():
                self.assertEqual(test_reviewer_total, reviewer_total)

        test_profile_images = [self.victor_profile.profile_image, self.kevin_profile.profile_image, self.josue_profile.profile_image]
        for profile_image in test_profile_images:
            with self.subTest():
                self.assertEqual(profile_image, "../flag.png")

    # TODO: This test suit fails 
    def test_init_types(self):

        # reviews - should be of type float
        test_review = [ 1, True, 'hello',[], (), {}] 
        for reviews in test_review:
             with self.subTest():
                self.assertRaises(TypeError, Profile, 'someone', reviews, 27, "../flag.png")

        # total reviewers - should be of type int
        test_total_reviewers = [ 1.0, True, 'hello',[], (), {}] 
        for total_reviewers in test_total_reviewers:
             with self.subTest():
                self.assertRaises(TypeError, Profile, 'someone', 4.25, total_reviewers, "../flag.png")

        # profile image - should be of type string
        test_profile_images = [1.0, 1, True, [], (), {}] 
        for profile_image in test_profile_images:
             with self.subTest():
                self.assertRaises(TypeError, Profile, 'someone', 4.25, 27, profile_image)

    def test_init_values(self):
        # TODO: items - could add test to it, if we add a limit to the amount of items in the list
        # TODO: profile image - could add test to it, if we add a regex to the image address

        # reviews - must be between 0.0 and 5.0
        test_review = [ -1.0, 5.1] 
        for reviews in test_review:
             with self.subTest():
                self.assertRaises(ValueError, Profile, 'someone', reviews, 27, "../flag.png")

        # TODO: the test below fails
        # total reviewers - must be greater or equal to 0
        self.assertRaises(ValueError, Profile, 'someone', 4.25, -1, "../flag.png")

        
    def test_add_item_to_sell(self):
        #item should be of type Item
        test_items = [1.0, 1, True, 'hello', [], (), {}] 
        for item in test_items: 
             with self.subTest():
                 with self.assertRaises(TypeError):
                    self.victor_profile._Add_Item_to_Sell(item)

        # TODO: the test below fails
        # should not add item if it is owned by another user
        with self.assertRaises(ValueError):
            self.kevin_profile._Add_Item_to_Sell(self.victor_item1)
        pass

    def test_remove_item(self):
        #item should be of type Item
        test_items = [1.0, 1, True, 'hello', [], (), {}] 
        for item in test_items: 
             with self.subTest():
                with self.assertRaises(TypeError):
                    self.victor_profile._Remove_Item(item)

        # TODO: the test below fails
        # should not remove an item if it is owned by another user
        with self.assertRaises(ValueError):
            self.kevin_profile._Remove_Item(self.victor_item1)

        # TODO: the test below fails
        # should not remove an item if it is not part of items 
        with self.assertRaises(ValueError):
            self.kevin_profile._Remove_Item(self.victor_item1)

    def test_review_score(self):
        # new_review should be of type integer
        test_new_reviews = [ 1.0, True, 'hello',[], (), {}] 
        for new_review in test_new_reviews:
             with self.subTest():
                 with self.assertRaises(TypeError):
                    self.josue_profile._Review_Score(new_review)

        # reviews - must be between 0 and 5
        test_new_reviews = [ -1, 6] 
        for new_review in test_new_reviews:
             with self.subTest():
                with self.assertRaises(ValueError):
                    self.josue_profile._Review_Score(new_review)

     
        # checking values: victor -> (4) -> (4.241) kevin -> (0) -> (4.335)
        test_new_reviews = [(self.victor_profile, 4, 4.241), (self.kevin_profile, 0, 4.335)]
        for profile, new_review, result in test_new_reviews:
            with self.subTest():
                self.assertAlmostEqual(profile._Review_Score(new_review), result)