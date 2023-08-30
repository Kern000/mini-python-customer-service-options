import pytest
from unittest.mock import patch
from pythonProject import add_new_customer, customer_list

@patch('builtins.input', side_effect=["y","Ah meow", "ahmeow@gmail.com", '62353535', 'y', '8', 'y'])

def test_add_new_customer(mock_input):
    global customer_list
    add_new_customer()
# check for successful or not
    assert customer_list[0]['name'] == 'Ah meow'
    assert customer_list[0]['email'] == "ahmeow@gmail.com"
    assert customer_list[0]['phone_number'] == 62353535

