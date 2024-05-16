import boto3
import os
from urllib.parse import parse_qsl, urlencode, urljoin, urlparse, urlsplit, urlunsplit

import requests
from requests import RequestException
from requests.auth import AuthBase, HTTPBasicAuth

from elastalert.auth import RefeshableAWSRequestsAuth
from elastalert.util import EAException

class OpensearchExternalUrlFormatter:
    '''Interface for formatting external Opensearch urls'''

    def format(self, relative_url: str) -> str:
        raise NotImplementedError()

class AbsoluteOpensearchExternalUrlFormatter(OpensearchExternalUrlFormatter):
    '''Formats absolute external Opensearch urls'''

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def format(self, relative_url: str) -> str:
        url = urljoin(self.base_url, relative_url)
        return url

def create_opensearch_external_url_formatter(
    rule
) -> OpensearchExternalUrlFormatter:
    '''Creates a Opensearch external url formatter'''

    base_url = rule.get('opensearch_url')

    return AbsoluteOpensearchExternalUrlFormatter(base_url)
