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


class AdvancedReportEmailBouncesOptions(object):
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
        'include_unopens': 'bool',
        'notify': 'list[int]',
        'grouping': 'str'
    }

    attribute_map = {
        'include_unopens': 'include_unopens',
        'notify': 'notify',
        'grouping': 'grouping'
    }

    def __init__(self, include_unopens=None, notify=None, grouping='by_campaign', local_vars_configuration=None):  # noqa: E501
        """AdvancedReportEmailBouncesOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._include_unopens = None
        self._notify = None
        self._grouping = None
        self.discriminator = None

        self.include_unopens = include_unopens
        if notify is not None:
            self.notify = notify
        if grouping is not None:
            self.grouping = grouping

    @property
    def include_unopens(self):
        """Gets the include_unopens of this AdvancedReportEmailBouncesOptions.  # noqa: E501

        True to include info for not opened campaigns, false otherwise  # noqa: E501

        :return: The include_unopens of this AdvancedReportEmailBouncesOptions.  # noqa: E501
        :rtype: bool
        """
        return self._include_unopens

    @include_unopens.setter
    def include_unopens(self, include_unopens):
        """Sets the include_unopens of this AdvancedReportEmailBouncesOptions.

        True to include info for not opened campaigns, false otherwise  # noqa: E501

        :param include_unopens: The include_unopens of this AdvancedReportEmailBouncesOptions.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and include_unopens is None:  # noqa: E501
            raise ValueError("Invalid value for `include_unopens`, must not be `None`")  # noqa: E501

        self._include_unopens = include_unopens

    @property
    def notify(self):
        """Gets the notify of this AdvancedReportEmailBouncesOptions.  # noqa: E501

        Array of user IDs to notify  # noqa: E501

        :return: The notify of this AdvancedReportEmailBouncesOptions.  # noqa: E501
        :rtype: list[int]
        """
        return self._notify

    @notify.setter
    def notify(self, notify):
        """Sets the notify of this AdvancedReportEmailBouncesOptions.

        Array of user IDs to notify  # noqa: E501

        :param notify: The notify of this AdvancedReportEmailBouncesOptions.  # noqa: E501
        :type: list[int]
        """

        self._notify = notify

    @property
    def grouping(self):
        """Gets the grouping of this AdvancedReportEmailBouncesOptions.  # noqa: E501

        Field to group data  # noqa: E501

        :return: The grouping of this AdvancedReportEmailBouncesOptions.  # noqa: E501
        :rtype: str
        """
        return self._grouping

    @grouping.setter
    def grouping(self, grouping):
        """Sets the grouping of this AdvancedReportEmailBouncesOptions.

        Field to group data  # noqa: E501

        :param grouping: The grouping of this AdvancedReportEmailBouncesOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["by_contact", "by_campaign"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and grouping not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `grouping` ({0}), must be one of {1}"  # noqa: E501
                .format(grouping, allowed_values)
            )

        self._grouping = grouping

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
        if not isinstance(other, AdvancedReportEmailBouncesOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdvancedReportEmailBouncesOptions):
            return True

        return self.to_dict() != other.to_dict()
