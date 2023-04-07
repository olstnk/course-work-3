from requests.auth import HTTPBasicAuth
import requests
import xml.etree.ElementTree as ET

basic_auth = HTTPBasicAuth('1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL', '')
basic_url = 'http://164.92.218.36:8080/api/products/'

def get_product_test():
    product_id = '14'
    expected_reference = 'demo_20'
    response = requests.get(basic_url + product_id, auth=basic_auth)

    assert response.status_code == 200, f"Response status code was {response.status_code}"

    data = response.content
    parsed_data = ET.fromstring(data)
    reference = parsed_data.find('product/reference').text

    assert reference == expected_reference, f"Response reference was {reference}, expected {expected_reference}"

def delete_product_test():
    product_id = '12'
    response = requests.delete(basic_url + product_id, auth=basic_auth)

    assert response.status_code == 200, f"Response status code was {response.status_code}"


#get_product_test()
#delete_product_test()
