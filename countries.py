from requests.auth import HTTPBasicAuth
import requests
import xml.etree.ElementTree as ET

basic_auth = HTTPBasicAuth('1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL', '')
basic_url = 'http://164.92.218.36:8080/api/countries/'

def get_country_test():
    country_id = '388'
    expected_country_name = 'Portuguese'
    response = requests.get(basic_url + country_id, auth=basic_auth)

    assert response.status_code == 200, f"Response status code was {response.status_code}"

    data = response.content
    parsed_data = ET.fromstring(data)
    country_name = parsed_data.find('country/name/language').text

    assert country_name == expected_country_name, f"Response country name was {country_name}, expected {expected_country_name}"

def create_country_test():
    headers = {'Content-Type': 'application/xml'}
    body = """
    <prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
        <country>
            <id_zone required="true" format="isUnsignedId">4</id_zone>
            <iso_code required="true" maxSize="3" format="isLanguageIsoCode">BRA</iso_code>
            <contains_states required="true" format="isBool">0</contains_states>
            <need_identification_number required="true" format="isBool">0</need_identification_number>
            <display_tax_label required="true" format="isBool">1</display_tax_label>
            <name required="true" maxSize="64" format="isGenericName">
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1" format="isUnsignedId">
            Brazil
            </language>
            </name>
        </country>
    </prestashop>
    """

    response = requests.post(basic_url, headers=headers, data=body, auth=basic_auth)
    print(response.content)

    assert response.status_code == 201, f"Response status code was {response.status_code}"


get_country_test()
create_country_test()


