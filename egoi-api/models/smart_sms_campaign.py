# coding: utf-8

"""
    APIv3 (Beta)

     # Introduction Just a quick peek!!! This is our new version of API. Remember, it is not stable yet!!! But we invite you play with it and give us your feedback ;) # Getting Started  E-goi can be integrated with many environments and programming languages via our REST API. We've created a developer focused portal to give your organization a clear and quick overview of how to integrate with E-goi. The developer portal focuses on scenarios for integration and flow of events. We recommend familiarizing yourself with all of the content in the developer portal, before start using our rest API.   The E-goi  APIv3 is served over HTTPS. To ensure data privacy, unencrypted HTTP is not supported.  Request data is passed to the API by POSTing JSON objects to the API endpoints with the appropriate parameters.   BaseURL = api.egoiapp.com  # RESTful Services This API supports 5 HTTP methods:  * <b>GET</b>: The HTTP GET method is used to **read** (or retrieve) a representation of a resource. * <b>POST</b>: The POST verb is most-often utilized to **create** new resources. * <b>PATCH</b>: PATCH is used for **modify** capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource * <b>PUT</b>: PUT is most-often utilized for **update** capabilities, PUT-ing to a known resource URI with the request body containing the newly-updated representation of the original resource. * <b>DELETE</b>: DELETE is pretty easy to understand. It is used to **delete** a resource identified by a URI.  # Authentication   We use a custom authentication method, you will need a apikey that you can find in your account settings. Below you will see a curl example to get your account information:  #!/bin/bash  curl -X GET 'https://api.egoiapp.com/my-account' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>'  Here you can see a curl Post example with authentication:  #!/bin/bash  curl -X POST 'http://api.egoiapp.com/tags' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>' \\  -H 'Content-Type: application/json' \\  -d '{`name`:`Your custom tag`,`color`:`#FFFFFF`}'  # SDK Get started quickly with E-goi with our integration tools. Our SDK is a modern open source library that makes it easy to integrate your application with E-goi services. * <b><a href='https://github.com/E-goi/sdk-java'>Java</a></b> * <b><a href='https://github.com/E-goi/sdk-php'>PHP</a></b> * <b><a href='https://github.com/E-goi/sdk-python'>Python</a></b>  <security-definitions/>  # noqa: E501

    The version of the OpenAPI document: 3.0.0-beta
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from egoi-api.configuration import Configuration


class SmartSmsCampaign(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'list_id': 'int',
        'internal_name': 'str',
        'campaign_content': 'SmartSmsCampaignCampaignContent',
        'page_content': 'CampaignSmartSmsPageContent',
        'sender_id': 'int',
        'cname_id': 'int',
        'options': 'CampaignSmartSmsOptions'
    }

    attribute_map = {
        'list_id': 'list_id',
        'internal_name': 'internal_name',
        'campaign_content': 'campaign_content',
        'page_content': 'page_content',
        'sender_id': 'sender_id',
        'cname_id': 'cname_id',
        'options': 'options'
    }

    def __init__(self, list_id=None, internal_name=None, campaign_content=None, page_content=None, sender_id=None, cname_id=None, options=None, local_vars_configuration=None):  # noqa: E501
        """SmartSmsCampaign - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._list_id = None
        self._internal_name = None
        self._campaign_content = None
        self._page_content = None
        self._sender_id = None
        self._cname_id = None
        self._options = None
        self.discriminator = None

        self.list_id = list_id
        self.internal_name = internal_name
        self.campaign_content = campaign_content
        self.page_content = page_content
        if sender_id is not None:
            self.sender_id = sender_id
        if cname_id is not None:
            self.cname_id = cname_id
        if options is not None:
            self.options = options

    @property
    def list_id(self):
        """Gets the list_id of this SmartSmsCampaign.  # noqa: E501


        :return: The list_id of this SmartSmsCampaign.  # noqa: E501
        :rtype: int
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this SmartSmsCampaign.


        :param list_id: The list_id of this SmartSmsCampaign.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and list_id is None:  # noqa: E501
            raise ValueError("Invalid value for `list_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                list_id is not None and list_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `list_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._list_id = list_id

    @property
    def internal_name(self):
        """Gets the internal_name of this SmartSmsCampaign.  # noqa: E501

        Smart SMS campaign internal name  # noqa: E501

        :return: The internal_name of this SmartSmsCampaign.  # noqa: E501
        :rtype: str
        """
        return self._internal_name

    @internal_name.setter
    def internal_name(self, internal_name):
        """Sets the internal_name of this SmartSmsCampaign.

        Smart SMS campaign internal name  # noqa: E501

        :param internal_name: The internal_name of this SmartSmsCampaign.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and internal_name is None:  # noqa: E501
            raise ValueError("Invalid value for `internal_name`, must not be `None`")  # noqa: E501

        self._internal_name = internal_name

    @property
    def campaign_content(self):
        """Gets the campaign_content of this SmartSmsCampaign.  # noqa: E501


        :return: The campaign_content of this SmartSmsCampaign.  # noqa: E501
        :rtype: SmartSmsCampaignCampaignContent
        """
        return self._campaign_content

    @campaign_content.setter
    def campaign_content(self, campaign_content):
        """Sets the campaign_content of this SmartSmsCampaign.


        :param campaign_content: The campaign_content of this SmartSmsCampaign.  # noqa: E501
        :type: SmartSmsCampaignCampaignContent
        """
        if self.local_vars_configuration.client_side_validation and campaign_content is None:  # noqa: E501
            raise ValueError("Invalid value for `campaign_content`, must not be `None`")  # noqa: E501

        self._campaign_content = campaign_content

    @property
    def page_content(self):
        """Gets the page_content of this SmartSmsCampaign.  # noqa: E501


        :return: The page_content of this SmartSmsCampaign.  # noqa: E501
        :rtype: CampaignSmartSmsPageContent
        """
        return self._page_content

    @page_content.setter
    def page_content(self, page_content):
        """Sets the page_content of this SmartSmsCampaign.


        :param page_content: The page_content of this SmartSmsCampaign.  # noqa: E501
        :type: CampaignSmartSmsPageContent
        """
        if self.local_vars_configuration.client_side_validation and page_content is None:  # noqa: E501
            raise ValueError("Invalid value for `page_content`, must not be `None`")  # noqa: E501

        self._page_content = page_content

    @property
    def sender_id(self):
        """Gets the sender_id of this SmartSmsCampaign.  # noqa: E501


        :return: The sender_id of this SmartSmsCampaign.  # noqa: E501
        :rtype: int
        """
        return self._sender_id

    @sender_id.setter
    def sender_id(self, sender_id):
        """Sets the sender_id of this SmartSmsCampaign.


        :param sender_id: The sender_id of this SmartSmsCampaign.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                sender_id is not None and sender_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `sender_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._sender_id = sender_id

    @property
    def cname_id(self):
        """Gets the cname_id of this SmartSmsCampaign.  # noqa: E501


        :return: The cname_id of this SmartSmsCampaign.  # noqa: E501
        :rtype: int
        """
        return self._cname_id

    @cname_id.setter
    def cname_id(self, cname_id):
        """Sets the cname_id of this SmartSmsCampaign.


        :param cname_id: The cname_id of this SmartSmsCampaign.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                cname_id is not None and cname_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `cname_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._cname_id = cname_id

    @property
    def options(self):
        """Gets the options of this SmartSmsCampaign.  # noqa: E501


        :return: The options of this SmartSmsCampaign.  # noqa: E501
        :rtype: CampaignSmartSmsOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this SmartSmsCampaign.


        :param options: The options of this SmartSmsCampaign.  # noqa: E501
        :type: CampaignSmartSmsOptions
        """

        self._options = options

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SmartSmsCampaign):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmartSmsCampaign):
            return True

        return self.to_dict() != other.to_dict()
