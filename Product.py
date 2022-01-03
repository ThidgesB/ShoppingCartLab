# As a developer, I want the Product class to have class properties to keep track of the Product’s name, price, and category.

# As a developer, I want the Product class’s initializer to take in the initial values for the name, price, and category via parameters

class Product:
    def __init__(self, product_name, product_price, product_category):
        self.name = product_name
        self.price = product_price
        self.category = product_category

    # def available_products():
    #     product_list = []
    #     product_list.append(Product('Mac n\' Cheese', 4.99, 'Food'))
    #     product_list.append(Product('BigTV', 0.05, 'Electronics'))
    #     product_list.append(Product('Plumbus', 139.99, 'Luxury'))
    #     return product_list