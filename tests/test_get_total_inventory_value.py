import pytest

def test_get_total_inventory_value(get_inventory):
    total_inventory_value = get_inventory.total_inventory_value()

    assert total_inventory_value == 1221.0, f"wrong value for total_inventory_value. look at {total_inventory_value}"