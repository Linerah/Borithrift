class Item:
    def __init__(self, name, price, size, style, gender, description, image, seller):
        self.name = name
        self.price = price
        self.size = size
        self.style = style
        self.gender = gender
        self.description = description
        self.image = image
        self.seller = seller

    def __str__(self) -> str:
        extra_hyphens = len(self.name)
        print(f'-----------------<{self.name}>-----------------')
        print(f'image url: {self.image}')
        print(f'price: {self.price}')
        print(f'size: {self.size}')
        print(f'description: {self.description}')
        print(extra_hyphens*'-' + '------------------------------------')