import random
from requests.auth import HTTPBasicAuth
import requests
import xml.etree.ElementTree as ET

basic_auth = HTTPBasicAuth('1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL', '')
basic_url = 'http://164.92.218.36:8080/api/'


def test_get_currency():
    currency_id = '16'
    expected_id = '16'
    url = basic_url + 'currencies/' + currency_id
    response = requests.get(url, auth=basic_auth)

    print(response)

    assert response.status_code == 200, f"Response status code was {response.status_code}"

    data = response.content
    assert data, "Response data was empty"

    root = ET.fromstring(data)

    root = ET.fromstring(data)
    id_element = root.find('currency/id')
    id_value = id_element.text

    assert id_value == expected_id, f"Response data was {id_value}, expected {expected_id}"
