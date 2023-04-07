from requests.auth import HTTPBasicAuth
import requests
import xml.etree.ElementTree as ET

basic_auth = HTTPBasicAuth('1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL', '')
basic_url = 'http://164.92.218.36:8080/api/'


def test_delete_address():
    url = basic_url + 'address/46'
    response = requests.delete(url, auth=basic_auth)

    assert response.status_code == 200, f"Response status code was {response.status_code}"
    print("Address was deleted successfully")
