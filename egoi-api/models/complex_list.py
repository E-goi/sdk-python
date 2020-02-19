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


class ComplexList(object):
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
        'public_name': 'str',
        'status': 'str',
        'group_id': 'int',
        'created': 'datetime',
        'updated': 'datetime',
        'language': 'Language',
        'stats': 'ComplexListAllOfStats'
    }

    attribute_map = {
        'list_id': 'list_id',
        'internal_name': 'internal_name',
        'public_name': 'public_name',
        'status': 'status',
        'group_id': 'group_id',
        'created': 'created',
        'updated': 'updated',
        'language': 'language',
        'stats': 'stats'
    }

    def __init__(self, list_id=None, internal_name=None, public_name=None, status=None, group_id=None, created=None, updated=None, language=None, stats=None, local_vars_configuration=None):  # noqa: E501
        """ComplexList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._list_id = None
        self._internal_name = None
        self._public_name = None
        self._status = None
        self._group_id = None
        self._created = None
        self._updated = None
        self._language = None
        self._stats = None
        self.discriminator = None

        if list_id is not None:
            self.list_id = list_id
        if internal_name is not None:
            self.internal_name = internal_name
        self.public_name = public_name
        if status is not None:
            self.status = status
        if group_id is not None:
            self.group_id = group_id
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        self.language = language
        if stats is not None:
            self.stats = stats

    @property
    def list_id(self):
        """Gets the list_id of this ComplexList.  # noqa: E501


        :return: The list_id of this ComplexList.  # noqa: E501
        :rtype: int
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this ComplexList.


        :param list_id: The list_id of this ComplexList.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                list_id is not None and list_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `list_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._list_id = list_id

    @property
    def internal_name(self):
        """Gets the internal_name of this ComplexList.  # noqa: E501

        Internal name of the list  # noqa: E501

        :return: The internal_name of this ComplexList.  # noqa: E501
        :rtype: str
        """
        return self._internal_name

    @internal_name.setter
    def internal_name(self, internal_name):
        """Sets the internal_name of this ComplexList.

        Internal name of the list  # noqa: E501

        :param internal_name: The internal_name of this ComplexList.  # noqa: E501
        :type: str
        """

        self._internal_name = internal_name

    @property
    def public_name(self):
        """Gets the public_name of this ComplexList.  # noqa: E501

        Public name of the list  # noqa: E501

        :return: The public_name of this ComplexList.  # noqa: E501
        :rtype: str
        """
        return self._public_name

    @public_name.setter
    def public_name(self, public_name):
        """Sets the public_name of this ComplexList.

        Public name of the list  # noqa: E501

        :param public_name: The public_name of this ComplexList.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and public_name is None:  # noqa: E501
            raise ValueError("Invalid value for `public_name`, must not be `None`")  # noqa: E501

        self._public_name = public_name

    @property
    def status(self):
        """Gets the status of this ComplexList.  # noqa: E501

        Status of the list  # noqa: E501

        :return: The status of this ComplexList.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ComplexList.

        Status of the list  # noqa: E501

        :param status: The status of this ComplexList.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "blocked"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def group_id(self):
        """Gets the group_id of this ComplexList.  # noqa: E501

        ID of the list group  # noqa: E501

        :return: The group_id of this ComplexList.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ComplexList.

        ID of the list group  # noqa: E501

        :param group_id: The group_id of this ComplexList.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def created(self):
        """Gets the created of this ComplexList.  # noqa: E501


        :return: The created of this ComplexList.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ComplexList.


        :param created: The created of this ComplexList.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ComplexList.  # noqa: E501


        :return: The updated of this ComplexList.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ComplexList.


        :param updated: The updated of this ComplexList.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def language(self):
        """Gets the language of this ComplexList.  # noqa: E501


        :return: The language of this ComplexList.  # noqa: E501
        :rtype: Language
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ComplexList.


        :param language: The language of this ComplexList.  # noqa: E501
        :type: Language
        """
        if self.local_vars_configuration.client_side_validation and language is None:  # noqa: E501
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def stats(self):
        """Gets the stats of this ComplexList.  # noqa: E501


        :return: The stats of this ComplexList.  # noqa: E501
        :rtype: ComplexListAllOfStats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this ComplexList.


        :param stats: The stats of this ComplexList.  # noqa: E501
        :type: ComplexListAllOfStats
        """

        self._stats = stats

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
        if not isinstance(other, ComplexList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComplexList):
            return True

        return self.to_dict() != other.to_dict()
