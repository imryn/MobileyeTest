import pytest

def test_add_new_product_to_inventory(get_inventory):
    product = {"name": "Samsung Galaxy 21", "product_id": "3543XZ", "price": 450, "quantity": 1}

    product_added = get_inventory.add_product(product)
    if product['name'] not in product_added:
         raise Exception("product was not added to the inventory")

    res = get_inventory.get_product(product['name'])
    assert res == product, f"product is not in inventory. look at {res}."

def test_add_product_that_already_exists_in_inventory(get_inventory):
    product = {"name": "Iphone 14", "product_id": "162243XZ", "price": 320, "quantity": 2}
    product_added = get_inventory.add_product(product)

    assert product_added == 'Quantity of the product is being increased.'


@pytest.mark.parametrize('product_with_invalid_name',[{"name": None, "product_id": "3243XZ", "price": 450, "quantity": 1},
                                                 {"name": 0, "product_id": "3243XZ", "price": 450, "quantity": 1},
                                                 {"name": "undefined", "product_id": "3243XZ", "price": 450, "quantity": 1}])
def test_add_product_with_invalid_name(get_inventory, product_with_invalid_name):
    product_added = get_inventory.add_product(product_with_invalid_name)
    assert 'can not add product to inventory with invalid name' == product_added, "get another error or wrong status or product was added."
