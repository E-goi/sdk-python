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


class ComplexListAllOfStats(object):
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
        'total_contacts': 'int',
        'total_active': 'int',
        'total_inactive': 'int',
        'total_removed': 'int',
        'total_unconfirmed': 'int',
        'total_waiting_new_confirmation': 'int'
    }

    attribute_map = {
        'total_contacts': 'total_contacts',
        'total_active': 'total_active',
        'total_inactive': 'total_inactive',
        'total_removed': 'total_removed',
        'total_unconfirmed': 'total_unconfirmed',
        'total_waiting_new_confirmation': 'total_waiting_new_confirmation'
    }

    def __init__(self, total_contacts=None, total_active=None, total_inactive=None, total_removed=None, total_unconfirmed=None, total_waiting_new_confirmation=None, local_vars_configuration=None):  # noqa: E501
        """ComplexListAllOfStats - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total_contacts = None
        self._total_active = None
        self._total_inactive = None
        self._total_removed = None
        self._total_unconfirmed = None
        self._total_waiting_new_confirmation = None
        self.discriminator = None

        if total_contacts is not None:
            self.total_contacts = total_contacts
        if total_active is not None:
            self.total_active = total_active
        if total_inactive is not None:
            self.total_inactive = total_inactive
        if total_removed is not None:
            self.total_removed = total_removed
        if total_unconfirmed is not None:
            self.total_unconfirmed = total_unconfirmed
        if total_waiting_new_confirmation is not None:
            self.total_waiting_new_confirmation = total_waiting_new_confirmation

    @property
    def total_contacts(self):
        """Gets the total_contacts of this ComplexListAllOfStats.  # noqa: E501

        Number of total contacts in the list  # noqa: E501

        :return: The total_contacts of this ComplexListAllOfStats.  # noqa: E501
        :rtype: int
        """
        return self._total_contacts

    @total_contacts.setter
    def total_contacts(self, total_contacts):
        """Sets the total_contacts of this ComplexListAllOfStats.

        Number of total contacts in the list  # noqa: E501

        :param total_contacts: The total_contacts of this ComplexListAllOfStats.  # noqa: E501
        :type: int
        """

        self._total_contacts = total_contacts

    @property
    def total_active(self):
        """Gets the total_active of this ComplexListAllOfStats.  # noqa: E501

        Number of total active contacts in the list  # noqa: E501

        :return: The total_active of this ComplexListAllOfStats.  # noqa: E501
        :rtype: int
        """
        return self._total_active

    @total_active.setter
    def total_active(self, total_active):
        """Sets the total_active of this ComplexListAllOfStats.

        Number of total active contacts in the list  # noqa: E501

        :param total_active: The total_active of this ComplexListAllOfStats.  # noqa: E501
        :type: int
        """

        self._total_active = total_active

    @property
    def total_inactive(self):
        """Gets the total_inactive of this ComplexListAllOfStats.  # noqa: E501

        Number of total inactive contacts in the list  # noqa: E501

        :return: The total_inactive of this ComplexListAllOfStats.  # noqa: E501
        :rtype: int
        """
        return self._total_inactive

    @total_inactive.setter
    def total_inactive(self, total_inactive):
        """Sets the total_inactive of this ComplexListAllOfStats.

        Number of total inactive contacts in the list  # noqa: E501

        :param total_inactive: The total_inactive of this ComplexListAllOfStats.  # noqa: E501
        :type: int
        """

        self._total_inactive = total_inactive

    @property
    def total_removed(self):
        """Gets the total_removed of this ComplexListAllOfStats.  # noqa: E501

        Number of total removed contacts in the list  # noqa: E501

        :return: The total_removed of this ComplexListAllOfStats.  # noqa: E501
        :rtype: int
        """
        return self._total_removed

    @total_removed.setter
    def total_removed(self, total_removed):
        """Sets the total_removed of this ComplexListAllOfStats.

        Number of total removed contacts in the list  # noqa: E501

        :param total_removed: The total_removed of this ComplexListAllOfStats.  # noqa: E501
        :type: int
        """

        self._total_removed = total_removed

    @property
    def total_unconfirmed(self):
        """Gets the total_unconfirmed of this ComplexListAllOfStats.  # noqa: E501

        Number of total unconfirmed contacts in the list  # noqa: E501

        :return: The total_unconfirmed of this ComplexListAllOfStats.  # noqa: E501
        :rtype: int
        """
        return self._total_unconfirmed

    @total_unconfirmed.setter
    def total_unconfirmed(self, total_unconfirmed):
        """Sets the total_unconfirmed of this ComplexListAllOfStats.

        Number of total unconfirmed contacts in the list  # noqa: E501

        :param total_unconfirmed: The total_unconfirmed of this ComplexListAllOfStats.  # noqa: E501
        :type: int
        """

        self._total_unconfirmed = total_unconfirmed

    @property
    def total_waiting_new_confirmation(self):
        """Gets the total_waiting_new_confirmation of this ComplexListAllOfStats.  # noqa: E501

        Number of total contacts waiting for new confirmation in the list  # noqa: E501

        :return: The total_waiting_new_confirmation of this ComplexListAllOfStats.  # noqa: E501
        :rtype: int
        """
        return self._total_waiting_new_confirmation

    @total_waiting_new_confirmation.setter
    def total_waiting_new_confirmation(self, total_waiting_new_confirmation):
        """Sets the total_waiting_new_confirmation of this ComplexListAllOfStats.

        Number of total contacts waiting for new confirmation in the list  # noqa: E501

        :param total_waiting_new_confirmation: The total_waiting_new_confirmation of this ComplexListAllOfStats.  # noqa: E501
        :type: int
        """

        self._total_waiting_new_confirmation = total_waiting_new_confirmation

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
        if not isinstance(other, ComplexListAllOfStats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComplexListAllOfStats):
            return True

        return self.to_dict() != other.to_dict()
