from requests.auth import HTTPBasicAuth
import requests
import xml.etree.ElementTree as ET

basic_auth = HTTPBasicAuth('1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL', '')
basic_url = 'http://164.92.218.36:8080/api/contacts/'

def create_contact_test(): 
    headers = {'Content-Type': 'application/xml'}
    body = """
    <prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
        <contact>
            <name>
                <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">
                    aaa
                </language>
            </name>
            <description>
                <language >
                
                </language>
            </description>
        </contact>
    </prestashop>
    """

    response = requests.post(basic_url, headers=headers, data=body, auth=basic_auth)

    assert response.status_code == 201, f"Response status code was {response.status_code}"

#create_contact_test()

