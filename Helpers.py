import xml.etree.ElementTree as ET
import pandas as pd


def check_error(metadata) -> None:
    r_httpCode = metadata.find('httpCode').text
    r_errorType = metadata.find('errorType').text
    r_description = metadata.find('description').text
    if r_httpCode == '204':
        print(r_httpCode, r_errorType, r_description)
    if r_httpCode != '200':
        raise Exception('Error {} ({}): {}'.format(r_httpCode, r_errorType, r_description))


def is_xml(value):
    try:
        ET.fromstring(value)
    except ET.ParseError:
        return False
    return True


def parse_xml_response(response, path):
    root = ET.fromstring(response.text)
    parsed_response = root.find(path)

    return parsed_response


def parse_csv_response(response):
    pass


def extract_df(r_dict: dict) -> pd.DataFrame:
    pd.set_option('display.max_columns', None)
    r_body = r_dict['responseBody']
    r_items_list = r_body['responseList']['item']
    try:
        df_items = pd.DataFrame(r_items_list)
    except Exception as e:
        print("error")
        try:
            df_items = pd.DataFrame(r_items_list, index=[0])
        except Exception as e:
            print("error")
            raise e

    return df_items
