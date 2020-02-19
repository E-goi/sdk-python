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


class Form(object):
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
        'form_id': 'int',
        'internal_title': 'str',
        'title': 'str',
        'language': 'Language',
        'list_id': 'int',
        'default': 'bool',
        'owner': 'int',
        'status': 'str',
        'created': 'datetime',
        'updated': 'datetime'
    }

    attribute_map = {
        'form_id': 'form_id',
        'internal_title': 'internal_title',
        'title': 'title',
        'language': 'language',
        'list_id': 'list_id',
        'default': 'default',
        'owner': 'owner',
        'status': 'status',
        'created': 'created',
        'updated': 'updated'
    }

    def __init__(self, form_id=None, internal_title='$request.body#/title', title=None, language=None, list_id=None, default=None, owner=None, status=None, created=None, updated=None, local_vars_configuration=None):  # noqa: E501
        """Form - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._form_id = None
        self._internal_title = None
        self._title = None
        self._language = None
        self._list_id = None
        self._default = None
        self._owner = None
        self._status = None
        self._created = None
        self._updated = None
        self.discriminator = None

        if form_id is not None:
            self.form_id = form_id
        if internal_title is not None:
            self.internal_title = internal_title
        self.title = title
        if language is not None:
            self.language = language
        if list_id is not None:
            self.list_id = list_id
        if default is not None:
            self.default = default
        if owner is not None:
            self.owner = owner
        if status is not None:
            self.status = status
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated

    @property
    def form_id(self):
        """Gets the form_id of this Form.  # noqa: E501


        :return: The form_id of this Form.  # noqa: E501
        :rtype: int
        """
        return self._form_id

    @form_id.setter
    def form_id(self, form_id):
        """Sets the form_id of this Form.


        :param form_id: The form_id of this Form.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                form_id is not None and form_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `form_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._form_id = form_id

    @property
    def internal_title(self):
        """Gets the internal_title of this Form.  # noqa: E501

        Internal title of the form  # noqa: E501

        :return: The internal_title of this Form.  # noqa: E501
        :rtype: str
        """
        return self._internal_title

    @internal_title.setter
    def internal_title(self, internal_title):
        """Sets the internal_title of this Form.

        Internal title of the form  # noqa: E501

        :param internal_title: The internal_title of this Form.  # noqa: E501
        :type: str
        """

        self._internal_title = internal_title

    @property
    def title(self):
        """Gets the title of this Form.  # noqa: E501

        Title of the form  # noqa: E501

        :return: The title of this Form.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Form.

        Title of the form  # noqa: E501

        :param title: The title of this Form.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def language(self):
        """Gets the language of this Form.  # noqa: E501


        :return: The language of this Form.  # noqa: E501
        :rtype: Language
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Form.


        :param language: The language of this Form.  # noqa: E501
        :type: Language
        """

        self._language = language

    @property
    def list_id(self):
        """Gets the list_id of this Form.  # noqa: E501


        :return: The list_id of this Form.  # noqa: E501
        :rtype: int
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this Form.


        :param list_id: The list_id of this Form.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                list_id is not None and list_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `list_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._list_id = list_id

    @property
    def default(self):
        """Gets the default of this Form.  # noqa: E501

        True if this is the default form in the list, false otherwise  # noqa: E501

        :return: The default of this Form.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this Form.

        True if this is the default form in the list, false otherwise  # noqa: E501

        :param default: The default of this Form.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def owner(self):
        """Gets the owner of this Form.  # noqa: E501


        :return: The owner of this Form.  # noqa: E501
        :rtype: int
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Form.


        :param owner: The owner of this Form.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                owner is not None and owner < 1):  # noqa: E501
            raise ValueError("Invalid value for `owner`, must be a value greater than or equal to `1`")  # noqa: E501

        self._owner = owner

    @property
    def status(self):
        """Gets the status of this Form.  # noqa: E501

        Status of the form  # noqa: E501

        :return: The status of this Form.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Form.

        Status of the form  # noqa: E501

        :param status: The status of this Form.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "unpublished", "cloned", "deleted"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created(self):
        """Gets the created of this Form.  # noqa: E501

        The date and time  # noqa: E501

        :return: The created of this Form.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Form.

        The date and time  # noqa: E501

        :param created: The created of this Form.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this Form.  # noqa: E501

        The date and time  # noqa: E501

        :return: The updated of this Form.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Form.

        The date and time  # noqa: E501

        :param updated: The updated of this Form.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

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
        if not isinstance(other, Form):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Form):
            return True

        return self.to_dict() != other.to_dict()
