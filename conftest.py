import pytest
from common.inventory import Inventory
from common.product import Product

@pytest.fixture()
def get_inventory():
    inventory = Inventory([{"name": "Iphone 15", "product_id": "163243XZ", "price": 450, "quantity": 1}])
    return inventory
