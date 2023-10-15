import json
import logging
import xml.etree.ElementTree as ET
import csv
import xmltodict
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from Helpers import check_error, is_xml, extract_df

ELEXON_URL = 'https://api.bmreports.com/BMRS'


class ElexonClientBase:

    def __init__(self, api_key: str = None, api_version: str = "v1", api_service_type: str = 'xml',
                 session: requests.Session = None, retry_count: int = 2,
                 proxies: dict = None):
        if api_key is None:
            raise TypeError('API key is missing')
        self.api_key = api_key
        self.api_version = api_version
        self.api_service_type = api_service_type
        self.retry_count = retry_count
        if session is None:
            self._init_session()
        else:
            self.session = session
        self.proxies = proxies

    def _init_session(self) -> requests.Session:
        self.session = requests.session()
        

    def _get_request_kwargs(self, report_name, **kwargs):

        # check params: TO DO -> check that mandatory param are here

        # add base params: TO DO -> do it one time instead of each time
        base_args = {
            'APIKey': self.api_key,
            'ServiceType': self.api_service_type
        }
        kwargs.update(base_args)
        return kwargs

    def _request(self, report_name: str, args: dict) -> requests.Response:

        url = self._get_url(report_name)

        try:
            response = self.session.get(url=url, params=args, proxies=self.proxies)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            logging.debug(f'URL: {response.url}')
            raise e
        else:
            return response.content.decode()

    def request(self, report_name: str, **kwargs):

        args = self._get_request_kwargs(report_name, **kwargs)
        response = self._request(report_name, args)

        return self._parse_response(response)

    def _get_url(self, report_name: str) -> str:
        return f"{ELEXON_URL}/{report_name.upper()}/{self.api_version}"

    def _parse_response(self, response: requests.Response):

        if self.api_service_type == 'xml':
            root = ET.fromstring(response)
            r_metadata = root.find('./responseMetadata')
            r_header = root.find('./responseHeader')
            r_body = root.find('./responseBody')
            check_error(r_metadata)

            return ET.tostring(r_body, encoding='unicode')

        elif self.api_service_type == 'csv':
            if is_xml(response):
                root = ET.fromstring(response)
                r_metadata = root.find('./responseMetadata')
                check_error(r_metadata)
            else:
                return response
        else:
            raise RuntimeError('Invalid service_type specified.')


class ElexonClient(ElexonClientBase):

    def __init__(self, api_key: str, api_version: str = "v1", api_service_type: str = 'xml',
                 session: requests.Session = None, retry_count: int = 1,
                 proxies: dict = None):
        super().__init__(api_key, api_version, api_service_type, session, retry_count, proxies)


class ElexonPandasClient(ElexonClientBase):
    pass


if __name__ == '__main__':
    pass
