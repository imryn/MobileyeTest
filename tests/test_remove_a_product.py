import pytest

def test_remove_exist_product_from_inventory(get_inventory):
    product_name = "Iphone 15"
    product_removed = get_inventory.remove_product(product_name)
    assert product_removed == f"product {product_name} was removed from inventory", "product was not removed"

    res = get_inventory.get_product(product_name)

    assert res == f"{product_name} is not in the list.", "product is in the list"

def test_remove_unexist_product_from_inventory(get_inventory):
    product_name = "Samsung Galaxy 3"
    product_removed = get_inventory.remove_product(product_name)

    assert product_removed == f"can not remove not exist {product_name}."


