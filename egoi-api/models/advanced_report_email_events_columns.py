# coding: utf-8

"""
    APIv3 (Beta)

     # Introduction Just a quick pick!!! This is our new version of API. Remember, it is not stable yet!!! But we invite you play with it and give us your feedback ;) # Getting Started  E-goi can be integrated with many environments and programming languages via our REST API. We've created a developer focused portal to give your organization a clear and quick overview of how to integrate with E-goi. The developer portal focuses on scenarios for integration and flow of events. We recommend familiarizing yourself with all of the content in the developer portal, before start using our rest API.   The E-goi  APIv3 is served over HTTPS. To ensure data privacy, unencrypted HTTP is not supported.  Request data is passed to the API by POSTing JSON objects to the API endpoints with the appropriate parameters.   BaseURL = api.egoiapp.com  # HTTP Methods for RESTful Services This API supports 5 HTTP methods:  * <b>GET</b>: The HTTP GET method is used to **read** (or retrieve) a representation of a resource. * <b>POST</b>: The POST verb is most-often utilized to **create** new resources. * <b>PATCH</b>: PATCH is used for **modify** capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource * <b>PUT</b>: PUT is most-often utilized for **update** capabilities, PUT-ing to a known resource URI with the request body containing the newly-updated representation of the original resource. * <b>DELETE</b>: DELETE is pretty easy to understand. It is used to **delete** a resource identified by a URI.  # Authentication   We use a custom authentication method, you will need a apikey that you can find in your account settings. Below you will see a curl example to get your account information:  #!/bin/bash  curl -X GET 'https://api.egoiapp.com/my-account' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>'  Here you can see a curl Post example with authentication:  #!/bin/bash  curl -X POST 'http://api.egoiapp.com/tags' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>' \\  -H 'Content-Type: application/json' \\  -d '{`name`:`Your custom tag`,`color`:`#FFFFFF`}'  <security-definitions/>  # noqa: E501

    The version of the OpenAPI document: 3.0.0-beta
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from egoi-api.configuration import Configuration


class AdvancedReportEmailEventsColumns(object):
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
        'list_base_fields': 'list[str]',
        'list_extra_fields': 'list[object]',
        'list_stats_fields': 'EmailEventsListStatsFields',
        'campaign_fields': 'EmailEventsCampaignFields'
    }

    attribute_map = {
        'list_base_fields': 'list_base_fields',
        'list_extra_fields': 'list_extra_fields',
        'list_stats_fields': 'list_stats_fields',
        'campaign_fields': 'campaign_fields'
    }

    def __init__(self, list_base_fields=None, list_extra_fields=None, list_stats_fields=None, campaign_fields=None, local_vars_configuration=None):  # noqa: E501
        """AdvancedReportEmailEventsColumns - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._list_base_fields = None
        self._list_extra_fields = None
        self._list_stats_fields = None
        self._campaign_fields = None
        self.discriminator = None

        self.list_base_fields = list_base_fields
        self.list_extra_fields = list_extra_fields
        self.list_stats_fields = list_stats_fields
        self.campaign_fields = campaign_fields

    @property
    def list_base_fields(self):
        """Gets the list_base_fields of this AdvancedReportEmailEventsColumns.  # noqa: E501

        Array of base fields  # noqa: E501

        :return: The list_base_fields of this AdvancedReportEmailEventsColumns.  # noqa: E501
        :rtype: list[str]
        """
        return self._list_base_fields

    @list_base_fields.setter
    def list_base_fields(self, list_base_fields):
        """Sets the list_base_fields of this AdvancedReportEmailEventsColumns.

        Array of base fields  # noqa: E501

        :param list_base_fields: The list_base_fields of this AdvancedReportEmailEventsColumns.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and list_base_fields is None:  # noqa: E501
            raise ValueError("Invalid value for `list_base_fields`, must not be `None`")  # noqa: E501

        self._list_base_fields = list_base_fields

    @property
    def list_extra_fields(self):
        """Gets the list_extra_fields of this AdvancedReportEmailEventsColumns.  # noqa: E501


        :return: The list_extra_fields of this AdvancedReportEmailEventsColumns.  # noqa: E501
        :rtype: list[object]
        """
        return self._list_extra_fields

    @list_extra_fields.setter
    def list_extra_fields(self, list_extra_fields):
        """Sets the list_extra_fields of this AdvancedReportEmailEventsColumns.


        :param list_extra_fields: The list_extra_fields of this AdvancedReportEmailEventsColumns.  # noqa: E501
        :type: list[object]
        """
        if self.local_vars_configuration.client_side_validation and list_extra_fields is None:  # noqa: E501
            raise ValueError("Invalid value for `list_extra_fields`, must not be `None`")  # noqa: E501

        self._list_extra_fields = list_extra_fields

    @property
    def list_stats_fields(self):
        """Gets the list_stats_fields of this AdvancedReportEmailEventsColumns.  # noqa: E501


        :return: The list_stats_fields of this AdvancedReportEmailEventsColumns.  # noqa: E501
        :rtype: EmailEventsListStatsFields
        """
        return self._list_stats_fields

    @list_stats_fields.setter
    def list_stats_fields(self, list_stats_fields):
        """Sets the list_stats_fields of this AdvancedReportEmailEventsColumns.


        :param list_stats_fields: The list_stats_fields of this AdvancedReportEmailEventsColumns.  # noqa: E501
        :type: EmailEventsListStatsFields
        """
        if self.local_vars_configuration.client_side_validation and list_stats_fields is None:  # noqa: E501
            raise ValueError("Invalid value for `list_stats_fields`, must not be `None`")  # noqa: E501

        self._list_stats_fields = list_stats_fields

    @property
    def campaign_fields(self):
        """Gets the campaign_fields of this AdvancedReportEmailEventsColumns.  # noqa: E501


        :return: The campaign_fields of this AdvancedReportEmailEventsColumns.  # noqa: E501
        :rtype: EmailEventsCampaignFields
        """
        return self._campaign_fields

    @campaign_fields.setter
    def campaign_fields(self, campaign_fields):
        """Sets the campaign_fields of this AdvancedReportEmailEventsColumns.


        :param campaign_fields: The campaign_fields of this AdvancedReportEmailEventsColumns.  # noqa: E501
        :type: EmailEventsCampaignFields
        """
        if self.local_vars_configuration.client_side_validation and campaign_fields is None:  # noqa: E501
            raise ValueError("Invalid value for `campaign_fields`, must not be `None`")  # noqa: E501

        self._campaign_fields = campaign_fields

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
        if not isinstance(other, AdvancedReportEmailEventsColumns):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdvancedReportEmailEventsColumns):
            return True

        return self.to_dict() != other.to_dict()
