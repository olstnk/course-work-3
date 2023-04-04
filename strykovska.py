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


post_url = basic_url + 'addresses'

def test_create_address():
    # створення елементу ХМЛ з даними адреси
    root = ET.Element('prestashop')
    address = ET.SubElement(root, 'address')
    
    ET.SubElement(address, 'id_country').text = '14'
    ET.SubElement(address, 'alias').text = '14'
    ET.SubElement(address, 'lastname').text = 'Doe'
    ET.SubElement(address, 'firstname').text = 'John'
    ET.SubElement(address, 'address1').text = '123 Main St'
    ET.SubElement(address, 'city').text = 'Anytown'

    # перетворення елементу ХМЛ до рядку
    xml_data = ET.tostring(root)

    # відправлення POST запиту
    response = requests.post(post_url, data=xml_data, auth=basic_auth, headers={'Content-Type': 'application/xml'})

    # Перевіряємо, що статус код відповіді дорівнює 201 (створено)
    assert response.status_code == 201, f"Response status code was {response.status_code}"

    # отримання створеної адреси у форматі ХМЛ
    data = response.content
    assert data, "Response data was empty"

    # Парсимо ХМЛ та перевіряємо, що отримані дані містять очікувані значення
    root = ET.fromstring(data)
    assert root.find('address/alias').text == '14'
    assert root.find('address/id_country').text == '14'
    assert root.find('address/lastname').text == 'Doe'
    assert root.find('address/firstname').text == 'John'
    assert root.find('address/address1').text == '123 Main St'
    assert root.find('address/city').text == 'Anytown'

    # виведення результату
    print(response.status_code)
    print(data)


def update_address():
    updated_id = '4256'

    # Отримуємо ID ресурсу
    url = basic_url + 'addresses/' + updated_id
    
    response = requests.get(url, auth=basic_auth)
    data = response.content
    root = ET.fromstring(data)

    address_id = root.find('.address/id').text
    
    print(address_id)

    # Підготовка даних для відправки
    headers = {'Content-Type': 'application/xml'}
    payload = """
<prestashop>
    <address>
        <id required="true" format="isUnsignedId">""" + updated_id + """</id>
        <id_country required="true" format="isUnsignedId">5</id_country>
        <alias required="true" maxSize="32" format="isGenericName">
            testA
        </alias>
        <lastname required="true" maxSize="255" format="isName">
            testA
        </lastname>
        <firstname required="true" maxSize="255" format="isName">
            testA
        </firstname>
        <address1 required="true" maxSize="128" format="isAddress">
            testA
        </address1>
        <city required="true" maxSize="64" format="isCityName">
            testA
        </city>
    </address>
</prestashop>
    """

    # Відправляємо запит PUT
    response = requests.put(post_url, headers=headers, data=payload, auth=basic_auth)
    
    # Перевіряємо відповідь сервера
    assert response.status_code == 200, f"Response status code was {response.status_code}."
    print(response.content)


def delete_address():
    url = basic_url + 'addresses/39'
    response = requests.delete(url, auth=basic_auth)

    # Перевіряємо, що статус код відповіді дорівнює 200
    assert response.status_code == 200, f"Response status code was {response.status_code}"
    print("Address was deleted successfully")