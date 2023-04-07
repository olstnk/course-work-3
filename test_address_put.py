import random
from requests.auth import HTTPBasicAuth
import requests
import xml.etree.ElementTree as ET
basic_auth = HTTPBasicAuth('1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL', '')
basic_url = 'http://164.92.218.36:8080/api/'


def test_update_address():
    updated_id = '88'
    url = basic_url + 'addresses/' + updated_id
    response = requests.get(url, auth=basic_auth)
    data = response.content
    root = ET.fromstring(data)
    address_id = root.find('address/id').text
    print(address_id)

    headers = {'Content-Type': 'application/xml'}
    payload = f"""
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <address>
        <id> """ + updated_id + """ </id>
        <id_country required="true" format="isUnsignedId">1</id_country>
        <alias required="true" maxSize="32" format="isGenericName">pytest</alias>
        <lastname required="true" maxSize="255" format="isName">Len</lastname>
        <firstname required="true" maxSize="255" format="isName">Vik</firstname>
        <address1 required="true" maxSize="128" format="isAddress">Address 678</address1>
        <city required="true" maxSize="64" format="isCityName">Plt</city>
    </address>
</prestashop>"""

    response = requests.put(url, headers=headers,
                            data=payload, auth=basic_auth)
    assert response.status_code == 200, f"Response status code was {response.status_code}."
    print(response.content)
