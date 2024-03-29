# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import egoi_api
from egoi_api.paths.lists_list_id_segments_segment_id import delete  # noqa: E501
from egoi_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestListsListIdSegmentsSegmentId(ApiTestMixin, unittest.TestCase):
    """
    ListsListIdSegmentsSegmentId unit test stubs
        Remove segment  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
