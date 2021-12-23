class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_item_to_cart(self, object):
        self.items.append(object)
        print(f"{object.name} was added to the cart")

    def display_items_in_cart(self):
        for item in self.items:
            print(item.name)
            print(item.price)
            print(item.category)
            self.total_price = self.total_price + item.price
