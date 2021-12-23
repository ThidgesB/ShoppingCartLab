from customer import Customer
from shopping_cart import ShoppingCart 
from product import Product

user_input = Customer(input('Please enter your name.'))

my_cart = ShoppingCart()


big_tv = Product("BigTV", 0.05, 'Electronics')
mac_n_cheese = Product("Mac and Cheese", 4.99, "Pasta")

my_cart.add_item_to_cart(mac_n_cheese)
my_cart.add_item_to_cart(big_tv)


my_cart.display_items_in_cart()

print(f'Total price of all items in cart: {my_cart.total_price}')