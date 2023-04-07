import random
from requests.auth import HTTPBasicAuth
import requests
import xml.etree.ElementTree as ET
basic_auth = HTTPBasicAuth('1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL', '')
basic_url = 'http://164.92.218.36:8080/api/'


def test_update_contact():
    updated_id = '4'
    url = basic_url + 'contacts/' + updated_id
    response = requests.get(url, auth=basic_auth)
    data = response.content
    root = ET.fromstring(data)
    contact_id = root.find('contact/id').text
    print(contact_id)

    headers = {'Content-Type': 'application/xml'}
    payload = f"""<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
             <contact>
<id> """ + updated_id + """ </id>
<name>
<language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">
testTesttest
</language>
</name>
</contact>
</prestashop>"""

    response = requests.put(url, headers=headers,
                            data=payload, auth=basic_auth)
    assert response.status_code == 200, f"Response status code was {response.status_code}."
    print(response.content)
