# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import egoi_api
from egoi_api.paths.catalogs_catalog_id_products import get  # noqa: E501
from egoi_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestCatalogsCatalogIdProducts(ApiTestMixin, unittest.TestCase):
    """
    CatalogsCatalogIdProducts unit test stubs
        Get all products  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
