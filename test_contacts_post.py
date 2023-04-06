import random
from requests.auth import HTTPBasicAuth
import requests
import xml.etree.ElementTree as ET

basic_auth = HTTPBasicAuth('1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL', '')
basic_url = 'http://164.92.218.36:8080/api/'


post_url = basic_url + 'contacts'


def test_create_contacts():

    root = ET.Element('prestashop')
    contact = ET.SubElement(root, 'contacts')

    ET.SubElement(contact, 'name').text = 'testTesttest_test'


root = ET.Element('prestashop')
xml_data = ET.tostring(root)

response = requests.post(post_url, data=xml_data, auth=basic_auth, headers={
                         'Content-Type': 'application/xml'})


assert response.status_code == 201, f"Response status code was {response.status_code}"


data = response.content
assert data, "Response data was empty"

root = ET.fromstring(data)

xml_body = """<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
             <contact>
<name>
<language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">
testTesttest_test
</language>
</name>
</contact>
</prestashop>"""


headers = {'Content-Type': 'application/xml'}

response = requests.post(basic_url, auth=basic_auth,
                         data=xml_body, headers=headers)

print(response.status_code)
print(data)
mod_xml = ET.fromstring(xml_data)
print(mod_xml.tag)
