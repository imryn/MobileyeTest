import pytest

def test_get_product_from_inventory(get_inventory):
    product_name = "Iphone 15"
    exist_product =  get_inventory.get_product(product_name)

    assert exist_product['name'] == product_name, "the product does not exist in inventory"

def test_get_not_exist_product_name(get_inventory):
    product_name = "test"
    product =  get_inventory.get_product(product_name)

    assert product == f"{product_name} is not in the list.", "the product does exist in inventory"

@pytest.mark.parametrize("product_name_value", [None, "undefined", 0])
def test_get_not_valid_product_name(get_inventory, product_name_value):
    product = get_inventory.get_product(product_name_value)

    assert product == 'can not get product from an empty list or product name is not valid', "the inventory has invalid product name."