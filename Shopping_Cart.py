# As a developer, I want the ShoppingCart class to have class properties to keep track of the shoppingcarts products (list)

# As a developer, I want the ShoppingCart class to have a method to calculate and return the current total of all products in the cart.

# As a developer, I want the ShoppingCart class to have a method to add a new product to the cart [Appending products to the list]
 
# As a developer, I want the ShoppingCart class to have a method to empty all products from the shopping cart

# from product import Product



class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_item_to_cart(self, object):
        self.items.append(object)
        print(f"{object.name} was added to the cart")

    def display_items_in_cart(self):
        if self.items == []:
            print('Cart is empty.' )
        else:
            print('Current cart contains: ')
            for item in self.items:
                print(item.name)
                print(f'${item.price}')
               #print(item.category)

    def total_price_of_cart(self):
        self.total_price = 0
        for item in self.items:
            self.total_price = self.total_price + item.price
        print(f'Total price of items in cart is: ${(self.total_price)}')

    def print_total_price_of_cart(self):
        print(f'Your cart total is: {self.total_price_of_cart}')

    def empty_cart(self):
        valid_input = False
        while valid_input == False:
            user_check_empty = input('Are you sure you want to empty your cart? Yes or No ').strip().lower()
            if user_check_empty == 'no':
                print(f'Cart was not emptied.')
                valid_input = True
            elif user_check_empty == 'yes':
                self.items.clear()
                print('All items have been removed.')
                valid_input = True
            else:
                print('Unrecognized input. Please enter yes or no.')
                valid_input = False
