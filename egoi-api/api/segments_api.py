# coding: utf-8

"""
    APIv3 (Beta)

     # Introduction Just a quick pick!!! This is our new version of API. Remember, it is not stable yet!!! But we invite you play with it and give us your feedback ;) # Getting Started  E-goi can be integrated with many environments and programming languages via our REST API. We've created a developer focused portal to give your organization a clear and quick overview of how to integrate with E-goi. The developer portal focuses on scenarios for integration and flow of events. We recommend familiarizing yourself with all of the content in the developer portal, before start using our rest API.   The E-goi  APIv3 is served over HTTPS. To ensure data privacy, unencrypted HTTP is not supported.  Request data is passed to the API by POSTing JSON objects to the API endpoints with the appropriate parameters.   BaseURL = api.egoiapp.com  # HTTP Methods for RESTful Services This API supports 5 HTTP methods:  * <b>GET</b>: The HTTP GET method is used to **read** (or retrieve) a representation of a resource. * <b>POST</b>: The POST verb is most-often utilized to **create** new resources. * <b>PATCH</b>: PATCH is used for **modify** capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource * <b>PUT</b>: PUT is most-often utilized for **update** capabilities, PUT-ing to a known resource URI with the request body containing the newly-updated representation of the original resource. * <b>DELETE</b>: DELETE is pretty easy to understand. It is used to **delete** a resource identified by a URI.  # Authentication   We use a custom authentication method, you will need a apikey that you can find in your account settings. Below you will see a curl example to get your account information:  #!/bin/bash  curl -X GET 'https://api.egoiapp.com/my-account' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>'  Here you can see a curl Post example with authentication:  #!/bin/bash  curl -X POST 'http://api.egoiapp.com/tags' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>' \\  -H 'Content-Type: application/json' \\  -d '{`name`:`Your custom tag`,`color`:`#FFFFFF`}'  <security-definitions/>  # noqa: E501

    The version of the OpenAPI document: 3.0.0-beta
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from egoi-api.api_client import ApiClient
from egoi-api.exceptions import (
    ApiTypeError,
    ApiValueError
)


class SegmentsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_segment(self, segment_id, list_id, **kwargs):  # noqa: E501
        """Remove segment  # noqa: E501

        Remove segment information given its ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_segment(segment_id, list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str segment_id: ID of the Segment (required)
        :param int list_id: ID of the List (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_segment_with_http_info(segment_id, list_id, **kwargs)  # noqa: E501

    def delete_segment_with_http_info(self, segment_id, list_id, **kwargs):  # noqa: E501
        """Remove segment  # noqa: E501

        Remove segment information given its ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_segment_with_http_info(segment_id, list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str segment_id: ID of the Segment (required)
        :param int list_id: ID of the List (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['segment_id', 'list_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_segment" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'segment_id' is set
        if self.api_client.client_side_validation and ('segment_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['segment_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `segment_id` when calling `delete_segment`")  # noqa: E501
        # verify the required parameter 'list_id' is set
        if self.api_client.client_side_validation and ('list_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['list_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `list_id` when calling `delete_segment`")  # noqa: E501

        if self.api_client.client_side_validation and 'list_id' in local_var_params and local_var_params['list_id'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `list_id` when calling `delete_segment`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'segment_id' in local_var_params:
            path_params['segment_id'] = local_var_params['segment_id']  # noqa: E501
        if 'list_id' in local_var_params:
            path_params['list_id'] = local_var_params['list_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/lists/{list_id}/segments/{segment_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_segments(self, list_id, **kwargs):  # noqa: E501
        """Get all segments  # noqa: E501

        Returns all segments  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_segments(list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int list_id: ID of the List (required)
        :param str type: Type of segment
        :param str name: Segment name
        :param int offset: Element offset (starting at zero for the first element)
        :param int limit: Number of items to return
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SegmentCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_all_segments_with_http_info(list_id, **kwargs)  # noqa: E501

    def get_all_segments_with_http_info(self, list_id, **kwargs):  # noqa: E501
        """Get all segments  # noqa: E501

        Returns all segments  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_segments_with_http_info(list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int list_id: ID of the List (required)
        :param str type: Type of segment
        :param str name: Segment name
        :param int offset: Element offset (starting at zero for the first element)
        :param int limit: Number of items to return
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SegmentCollection, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['list_id', 'type', 'name', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_segments" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'list_id' is set
        if self.api_client.client_side_validation and ('list_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['list_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `list_id` when calling `get_all_segments`")  # noqa: E501

        if self.api_client.client_side_validation and 'list_id' in local_var_params and local_var_params['list_id'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `list_id` when calling `get_all_segments`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `get_all_segments`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_all_segments`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `get_all_segments`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'list_id' in local_var_params:
            path_params['list_id'] = local_var_params['list_id']  # noqa: E501

        query_params = []
        if 'type' in local_var_params and local_var_params['type'] is not None:  # noqa: E501
            query_params.append(('type', local_var_params['type']))  # noqa: E501
        if 'name' in local_var_params and local_var_params['name'] is not None:  # noqa: E501
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Apikey']  # noqa: E501

        return self.api_client.call_api(
            '/lists/{list_id}/segments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SegmentCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
