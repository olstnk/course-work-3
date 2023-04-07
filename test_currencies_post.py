import random
from requests.auth import HTTPBasicAuth
import requests
import xml.etree.ElementTree as ET

basic_auth = HTTPBasicAuth('1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL', '')
basic_url = 'http://164.92.218.36:8080/api/'


post_url = basic_url + 'currencies'


def test_create_currency():

    root = ET.Element('prestashop')
    currency = ET.SubElement(root, 'currency')

    ET.SubElement(currency, 'name').text = 'euro'
    ET.SubElement(currency, 'iso_code').text = 'ABC'
    ET.SubElement(currency, 'conversion_rate').text = '3.10'


root = ET.Element('prestashop')
xml_data = ET.tostring(root)

response = requests.post(post_url, data=xml_data, auth=basic_auth, headers={
                         'Content-Type': 'application/xml'})


assert response.status_code == 201, f"Response status code was {response.status_code}"


data = response.content
assert data, "Response data was empty"

root = ET.fromstring(data)
# assert root.find('currency/name').text == 'euro'
# assert root.find('currency/iso_code').text == 'ABC'
# assert root.find('currency/conversion_rate').text == '0.199'
xml_body = """
        <prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
            <currency>
                <names>
                    <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1" format="isUnsignedId"></language>
                </names>
                <name notFilterable="true" required="true" maxSize="255" format="isGenericName">euro</name>
                <symbol maxSize="255">
                    <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1" format="isUnsignedId"></language>
                </symbol>
                <iso_code required="true" maxSize="3" format="isLanguageIsoCode">ABC</iso_code>
                <conversion_rate required="true" format="isUnsignedFloat">3.10</conversion_rate>
            </currency>
        </prestashop>
    """


headers = {'Content-Type': 'application/xml'}

response = requests.post(basic_url, auth=basic_auth,
                         data=xml_body, headers=headers)

print(response.status_code)
print(data)
mod_xml = ET.fromstring(xml_data)
print(mod_xml.tag)
