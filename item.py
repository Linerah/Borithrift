from User import User
class Item:
    """
    Creates an item that stores its values, like name, price, size, stype, gender, 
    description, image, and the user that owns it.

    Attrbibutes:
        name (str): The name of the item. The name should be 1-35 characters in length.
        price (float): The price of the item. The price should be greater or equal to 0. 
        size (str): The size of the item. Size should be of a valid value like: 'S', 'M'...
        style (str): The style category that the item falls into. The style should be 1-16 characters in length.
        gender (str): The gender category that the item falls into. Gender should be of a valid value like: 'Men', 'Women'
        description (str): The description of the item. The description should be 1-150 characters in length.
        image (str): The url link for the image of the item. The name should be 1-150 characters in length.
        user (User): The user that is selling the item. The user must me of type User.
    """
    def __init__(self, name, price, size, style, gender, description, image, user):
        self.name = self.valid_string_length(self.valid_string_type(name), 1, 35)
        self.price = self.valid_price_value(self.valid_float_type(price))
        self.size = self.valid_size_value(self.valid_string_type(size))
        self.style = self.valid_string_length(self.valid_string_type(style), 1, 16)
        self.gender = self.valid_gender_value(self.valid_string_type(gender))
        self.description = self.valid_string_length(self.valid_string_type(description), 1, 150)
        self.image = self.valid_string_length(self.valid_string_type(image), 1, 150)
        self.username = self.valid_user_type(user).username # to avoid testing if the username is real

    def valid_string_type(self, string_input):
        # checking to see if input is a string
        if(type(string_input) != str):
            raise TypeError('The value is not of type str')
        return string_input

    def valid_float_type(self, float_input):
        # checking to see if input is a float
        if(type(float_input) != float):
            raise TypeError('The value is not of type float')
        return float_input
    
    def valid_user_type(self, user):
        # checking to see if input is a User
        if(type(user) != User): # profile could change to user
            raise TypeError('The user is not of type User')
        return user
    
    def valid_string_length(self, string_input, min, max):  
        # checking to see if input string is a valid length
        string_length = len(string_input)
        if(string_length < min or string_length > max):
            raise ValueError(f'The input should have more than {min} characters and less than {max} characters')
        return string_input
    
    def valid_size_value(self, size_input):
        # checking to see if the size of the item is a valid size.
        size_list = ['XXS','XS','S', 'M', 'L', 'XL', 'XXL']
        for size in size_list:
            if(size == size_input):
                return size_input
        raise ValueError(f'{size_input} is not a valid size. (Ex. sizes: ..., L, XL, XXL)')

    def valid_gender_value(self, gender_input):
         # checking to see if the gender department of the item is valid.
        gender_list = ['Men','Women']
        for gender in gender_list:
            if(gender == gender_input):
                return gender_input
        raise ValueError(f'{gender} is not a valid gender department. (Ex. gender: Men, Women)')
    
    def valid_price_value(self, price_input):
         # checking to see if the price is bigger than -1.0.
        if(price_input < 0.0):
             raise ValueError('the price should be greater or equally to 0.0')
        return price_input
        
    def __str__(self) -> str:
        extra_hyphens = len(self.name)
        return(f'-----------------<{self.name}>-----------------\n   image url: {self.image}\n   price: {self.price}\n   size: {self.size}\n   description: {self.description}')