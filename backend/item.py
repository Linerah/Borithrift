from User import User
class Item:

    def __init__(self, name, price, size, style, gender, description, image, user):
        self.name = self.valid_string_type(name)
        self.price = self.valid_float_type(price)
        self.size = self.valid_string_type(size)
        self.style = self.valid_string_type(style)
        self.gender = self.valid_string_type(gender)
        self.description = self.valid_string_type(description)
        self.image = self.valid_string_type(image)
        self.username = self.valid_user_type(user).username

    def valid_string_type(self, string_input):
        if(type(string_input) != str):
            raise TypeError('The value is not of type str')
        return string_input


    def valid_float_type(self, float_input):
        if(type(float_input) != float):
            raise TypeError('The value is not of type float')
        return float_input
    
    def valid_user_type(self, user):
        if(type(user) != User): # profile could change to user
            raise TypeError('The user is not of type User')
        return user
        
    
    def __str__(self) -> str:
        extra_hyphens = len(self.name)
        return(f'-----------------<{self.name}>-----------------\n   image url: {self.image}\n   price: {self.price}\n   size: {self.size}\n   description: {self.description}')