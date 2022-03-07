from User import User
class Item:

    def __init__(self, name, price, size, style, gender, description, image, seller):
        self.name = self.valid_string_type(name)
        self.price = self.valid_float_type(price)
        self.size = self.valid_string_type(size)
        self.style = self.valid_string_type(style)
        self.gender = self.valid_string_type(gender)
        self.description = self.valid_string_type(description)
        self.image = self.valid_string_type(image)
        self.seller_username = self.valid_user_type(seller).username

    def valid_string_type(self, string_input):
        if(type(string_input) != str):
            raise TypeError('The value is not of type str')
        return string_input


    def valid_float_type(self, float_input):
        if(type(float_input) != float):
            raise TypeError('The value is not of type float')
        return float_input
    
    def valid_user_type(self, seller_input):
        if(type(seller_input) != User): # profile could change to user
            raise TypeError('The user is not of type User')
        return seller_input
        
    
    def __str__(self) -> str:
        extra_hyphens = len(self.name)
        return(f'-----------------<{self.name}>-----------------\nimage url: {self.image}\nprice: {self.price}\nsize: {self.size}\ndescription: {self.description}\n' + extra_hyphens*'-' + '------------------------------------')
        # print(f'image url: {self.image}')
        # print(f'price: {self.price}')
        # print(f'size: {self.size}')
        # print(f'description: {self.description}')
        # print(extra_hyphens*'-' + '------------------------------------')