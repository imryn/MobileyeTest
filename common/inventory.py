from common.product import Product

class Inventory:

    def __init__(self, products):
        self.products = products

    @staticmethod
    def check_valid_product_name(product_name):
        if product_name == None or product_name == 'undefined' or product_name == 0:
            return False
        else:
            return True;

    def add_product(self, product: Product):
        valid_name = self.check_valid_product_name(product['name'])
        if valid_name:
            for item in self.products:
                if product['name'] == item['name']:
                    item['quantity'] += product['quantity']

                else:
                    self.products.append(product)
                    return f"product {product['name']} was added to inventory."

        else:
            return "can not add product to inventory with invalid name"

    def remove_product(self, product_name):
        valid_name = self.check_valid_product_name(product_name)
        if valid_name and self.products != []:
            for item in self.products:
                  if item['name'] == product_name:
                    self.products.remove(item)
                    return f"product {item['name']} was removed from inventory"
                  else:
                    return f"can not remove not exist {product_name}."
        else:
            return f"can not remove product from an empty list or product_name is not valid"

    def get_product(self, product_name) -> Product:
        valid_name = self.check_valid_product_name(product_name)
        if valid_name and self.products != []:
            for item in self.products:
                if item['name'] == product_name:
                    return item

            return f"{product_name} is not in the list."
        else:
            return f"can not get product from an empty list or product name is not valid"

    def total_inventory_value(self) -> float:
        sum = 0
        if self.products != []:
            for item in self.products:
                sum += item['price'] * item['quantity']
            return sum
        else:
            return 0