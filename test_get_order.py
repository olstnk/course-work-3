from requests.auth import HTTPBasicAuth
import requests
import xml.etree.ElementTree as ET

basic_auth = HTTPBasicAuth('1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL', '')
basic_url = 'http://164.92.218.36:8080/api/'


def test_get_order():
    order_id = '16'
    expected_id = '16'
    url = basic_url + 'orders/' + order_id
    response = requests.get(url, auth=basic_auth)

    print(response)

    assert response.status_code == 200, f"Response status code was {response.status_code}"

    data = response.content
    assert data, "Response data was empty"

    root = ET.fromstring(data)

    root = ET.fromstring(data)
    id_element = root.find('order/id')
    id_value = id_element.text

    assert id_value == expected_id, f"Response data was {id_value}, expected {expected_id}"


post_url = basic_url + 'orders'


# def test_create_order():

#     root = ET.Element('prestashop')
#     order = ET.SubElement(root, 'order')

#     ET.SubElement(order, 'id_address_delivery').text = '3'
#     ET.SubElement(order, 'id_customer').text = '1'
#     ET.SubElement(order, 'id_cart').text = '1'
#     ET.SubElement(order, 'payment').text = 'payment by card'
#     ET.SubElement(order, 'total_paid').text = '100'

#     xml_data = ET.tostring(root)

#     response = requests.post(post_url, data=xml_data, auth=basic_auth, headers={
#                              'Content-Type': 'application/xml'})

#     assert response.status_code == 201, f"Response status code was {response.status_code}"

#     data = response.content
#     assert data, "Response data was empty"

#     root = ET.fromstring(data)
#     assert root.find('order/id_address_delivery').text == '3'
#     assert root.find('order/id_customer').text == '1'
#     assert root.find('order/id_cart').text == '1'
#     assert root.find('order/payment').text == 'payment by card'
#     assert root.find('order/total_paid').text == '100'

#     print(response.status_code)
#     print(data)
