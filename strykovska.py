from requests.auth import HTTPBasicAuth
import requests
import xml.etree.ElementTree as ET

basic_auth = HTTPBasicAuth('1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL', '')
basic_url = 'http://164.92.218.36:8080/api/'

def test_get_address():
    adrress_id = '9'
    expected_id = '9'
    url = basic_url + 'addresses/' + adrress_id
    response = requests.get(url, auth=basic_auth)

    print(response)
    # Перевіряємо, що статус код відповіді дорівнює 200
    assert response.status_code == 200, f"Response status code was {response.status_code}"
    
    # Отримуємо дані з відповіді та перевіряємо, що вони не порожні
    data = response.content
    assert data, "Response data was empty"
    
    # Парсимо XML та перевіряємо, що отримані дані містять очікувані значення
    root = ET.fromstring(data)

    root = ET.fromstring(data)
    id_element = root.find('address/id')
    id_value = id_element.text

    assert id_value == expected_id, f"Response data was {id_value}, expected {expected_id}"