import pytest
from common.inventory import Inventory
from common.product import Product

@pytest.fixture()
def get_inventory():
    inventory = Inventory([{"name": "Iphone 14", "product_id": "162243XZ", "price": 320, "quantity": 1},
                           {"name": "Iphone 15", "product_id": "163243XZ", "price": 450.5, "quantity": 2}])
    return inventory
