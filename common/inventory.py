from common.product import Product

class Inventory:

    def __init__(self, products: list):
        self.products = products

    @staticmethod
    def check_valid_product_name(product_name: str):
        return product_name not in (None, 'undefined', 0)

    """add product to products list"""
    def add_product(self, product: Product):
        valid_name = self.check_valid_product_name(product['name'])
        exists = False
        if not valid_name:
            return "can not add product to inventory with invalid name"

        for item in self.products:
            if item['name'] == product['name']:
                item['quantity'] += product['quantity']
                exists = True
                return f"Quantity of the product is being increased."

            if exists == False:
                self.products.append(product)
                return f"product {product['name']} was added to inventory."

    """remove product from products list"""
    def remove_product(self, product_name: str):
        valid_name = self.check_valid_product_name(product_name)

        if valid_name and self.products != []:
            for item in self.products:
                  if item['name'] == product_name:
                      self.products.remove(item)
                      return f"product {item['name']} was removed from inventory"

            return f"can not remove not exist {product_name}."

        else:
            return f"can not remove product from an empty list or product_name is not valid"

    """get specific product from products list"""
    def get_product(self, product_name: str) -> Product:
        valid_name = self.check_valid_product_name(product_name)
        if valid_name and self.products != []:
            for item in self.products:
                if item['name'] == product_name:
                    return item

            return f"{product_name} is not in the list."
        else:
            return f"can not get product from an empty list or product name is not valid"

    """get total_inventory_value from products list"""
    def total_inventory_value(self) -> float:
        if self.products != []:
            return sum( item['price'] * item['quantity'] for item in self.products)
        else:
            return 0