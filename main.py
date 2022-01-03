import customer
from shopping_cart import ShoppingCart 
from product import Product

customer_cart = ShoppingCart()
customer_name = input('NAME PLEASE: ')
current_user = customer.Customer(customer_name)
mac_food = Product('Mac n\' cheese', 4.99, 'Food')
big_tv = Product('BigTV', 300, 'Electronics')
plumbus = Product('Plumbus', 139.99, 'Luxury')
current_products = plumbus, big_tv, mac_food

def welcome_user():
    print(F'WELCOME {customer_name.upper()}, WE HOPE YOU HAVE A PLEASANT SHOPPING EXPERIENCE.')
    

def present_choices():
    print('Our current stock is:')
    for item in current_products:
        print(f'{item.category}: {item.name}, ${str(item.price)}')

def add_items(product):
    input_flag = False
    while input_flag == False:
        user_input = input(f'Would you like to add {product.name} to your cart? ').lower().strip()
        if user_input == 'yes':
            customer_cart.add_item_to_cart(product)
            input_flag = True
        elif user_input == 'no':
                input_flag = True
        else:
            print('Unrecognized input')
            input_flag = False

def view_cart():
    customer_cart.display_items_in_cart()

def cart_total_price():
    customer_cart.total_price_of_cart()

def empty_cart():
    customer_cart.empty_cart()

welcome_user()
present_choices()
add_items(mac_food)
add_items(big_tv)
add_items(plumbus)
view_cart()
cart_total_price()
empty_cart()
view_cart()
cart_total_price()