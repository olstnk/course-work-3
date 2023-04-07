from products import get_product_test, delete_product_test
from contacts import create_contact_test
from countries import get_country_test, create_country_test
from strykovska import test_get_address, test_create_address, update_address, delete_address
from test_address_delete import test_delete_address
from test_address_put import test_update_address
from test_contacts_put import test_update_contact
from test_contacts_post import test_create_contacts
from test_currencies_get import test_get_currency
from test_currencies_post import test_create_currency
from test_get_order import test_get_order
from test_order_delete import test_delete_order
from test_states_get import test_get_state
from test_zones_get import test_get_zone

if __name__ == "__main__":
    # product
    get_product_test()
    delete_product_test()
    # contact
    create_contact_test()
    test_update_contact()
    test_create_contacts()
    # country
    get_country_test()
    create_country_test()
    # address
    test_get_address() 
    test_create_address() 
    update_address() 
    delete_address()
    test_update_address()
    test_delete_address()
    # currency
    test_get_currency()
    test_create_currency()
    # order 
    test_get_order()
    test_delete_order()
    # state 
    test_get_state()
    # zones
    test_get_zone()