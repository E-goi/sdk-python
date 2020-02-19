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


class CampaignSmartSmsOptions(object):
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
        'encoding': 'str',
        'max_messages': 'int'
    }

    attribute_map = {
        'encoding': 'encoding',
        'max_messages': 'max_messages'
    }

    def __init__(self, encoding=None, max_messages=None, local_vars_configuration=None):  # noqa: E501
        """CampaignSmartSmsOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._encoding = None
        self._max_messages = None
        self.discriminator = None

        if encoding is not None:
            self.encoding = encoding
        if max_messages is not None:
            self.max_messages = max_messages

    @property
    def encoding(self):
        """Gets the encoding of this CampaignSmartSmsOptions.  # noqa: E501


        :return: The encoding of this CampaignSmartSmsOptions.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this CampaignSmartSmsOptions.


        :param encoding: The encoding of this CampaignSmartSmsOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["gsm", "unicode"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and encoding not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `encoding` ({0}), must be one of {1}"  # noqa: E501
                .format(encoding, allowed_values)
            )

        self._encoding = encoding

    @property
    def max_messages(self):
        """Gets the max_messages of this CampaignSmartSmsOptions.  # noqa: E501


        :return: The max_messages of this CampaignSmartSmsOptions.  # noqa: E501
        :rtype: int
        """
        return self._max_messages

    @max_messages.setter
    def max_messages(self, max_messages):
        """Sets the max_messages of this CampaignSmartSmsOptions.


        :param max_messages: The max_messages of this CampaignSmartSmsOptions.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_messages is not None and max_messages > 9):  # noqa: E501
            raise ValueError("Invalid value for `max_messages`, must be a value less than or equal to `9`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_messages is not None and max_messages < 1):  # noqa: E501
            raise ValueError("Invalid value for `max_messages`, must be a value greater than or equal to `1`")  # noqa: E501

        self._max_messages = max_messages

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
        if not isinstance(other, CampaignSmartSmsOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampaignSmartSmsOptions):
            return True

        return self.to_dict() != other.to_dict()
