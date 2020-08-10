# coding: utf-8

"""
    APIv3 (Beta)

     # Introduction Just a quick peek!!! This is our new version of API. Remember, it is not stable yet!!! But we invite you play with it and give us your feedback ;) # Getting Started  E-goi can be integrated with many environments and programming languages via our REST API. We've created a developer focused portal to give your organization a clear and quick overview of how to integrate with E-goi. The developer portal focuses on scenarios for integration and flow of events. We recommend familiarizing yourself with all of the content in the developer portal, before start using our rest API.   The E-goi  APIv3 is served over HTTPS. To ensure data privacy, unencrypted HTTP is not supported.  Request data is passed to the API by POSTing JSON objects to the API endpoints with the appropriate parameters.   BaseURL = api.egoiapp.com  # RESTful Services This API supports 5 HTTP methods:  * <b>GET</b>: The HTTP GET method is used to **read** (or retrieve) a representation of a resource. * <b>POST</b>: The POST verb is most-often utilized to **create** new resources. * <b>PATCH</b>: PATCH is used for **modify** capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource * <b>PUT</b>: PUT is most-often utilized for **update** capabilities, PUT-ing to a known resource URI with the request body containing the newly-updated representation of the original resource. * <b>DELETE</b>: DELETE is pretty easy to understand. It is used to **delete** a resource identified by a URI.  # Authentication   We use a custom authentication method, you will need a apikey that you can find in your account settings. Below you will see a curl example to get your account information:  #!/bin/bash  curl -X GET 'https://api.egoiapp.com/my-account' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>'  Here you can see a curl Post example with authentication:  #!/bin/bash  curl -X POST 'http://api.egoiapp.com/tags' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>' \\  -H 'Content-Type: application/json' \\  -d '{`name`:`Your custom tag`,`color`:`#FFFFFF`}'  # SDK Get started quickly with E-goi with our integration tools. Our SDK is a modern open source library that makes it easy to integrate your application with E-goi services.  * <a href='https://github.com/E-goi/sdk-java'>Java</a>  * <a href='https://github.com/E-goi/sdk-php'>PHP</a>  * <a href='https://github.com/E-goi/sdk-python'>Python</a>  * <a href='https://github.com/E-goi/sdk-ruby'>Ruby</a>  * <a href='https://github.com/E-goi/sdk-javascript'>Javascript</a>  * <a href='https://github.com/E-goi/sdk-csharp'>C#</a>  # Stream Limits Stream limits are security mesures we have to make sure our API have a fair use policy, for this reason, any request that creates or modifies data (**POST**, **PATCH** and **PUT**) is limited to a maximum of **20MB** of content length. If you arrive to this limit in one of your request, you'll receive a HTTP code **413 (Request Entity Too Large)** and the request will be ignored. To avoid this error in importation's requests, it's advised the request's division in batches that have each one less than 20MB. <security-definitions/>  # noqa: E501

    The version of the OpenAPI document: 3.0.0-beta
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from egoi-api.configuration import Configuration


class UniqueFieldInUseErrors(object):
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
        'unique_field_in_use': 'str',
        'field_id': 'str',
        'contacts': 'list[str]'
    }

    attribute_map = {
        'unique_field_in_use': 'unique_field_in_use',
        'field_id': 'field_id',
        'contacts': 'contacts'
    }

    def __init__(self, unique_field_in_use=None, field_id=None, contacts=None, local_vars_configuration=None):  # noqa: E501
        """UniqueFieldInUseErrors - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._unique_field_in_use = None
        self._field_id = None
        self._contacts = None
        self.discriminator = None

        if unique_field_in_use is not None:
            self.unique_field_in_use = unique_field_in_use
        if field_id is not None:
            self.field_id = field_id
        if contacts is not None:
            self.contacts = contacts

    @property
    def unique_field_in_use(self):
        """Gets the unique_field_in_use of this UniqueFieldInUseErrors.  # noqa: E501

        Occurs when a provided field is already in use  # noqa: E501

        :return: The unique_field_in_use of this UniqueFieldInUseErrors.  # noqa: E501
        :rtype: str
        """
        return self._unique_field_in_use

    @unique_field_in_use.setter
    def unique_field_in_use(self, unique_field_in_use):
        """Sets the unique_field_in_use of this UniqueFieldInUseErrors.

        Occurs when a provided field is already in use  # noqa: E501

        :param unique_field_in_use: The unique_field_in_use of this UniqueFieldInUseErrors.  # noqa: E501
        :type: str
        """
        allowed_values = ["A unique field is already being used"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and unique_field_in_use not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `unique_field_in_use` ({0}), must be one of {1}"  # noqa: E501
                .format(unique_field_in_use, allowed_values)
            )

        self._unique_field_in_use = unique_field_in_use

    @property
    def field_id(self):
        """Gets the field_id of this UniqueFieldInUseErrors.  # noqa: E501

        Field ID  # noqa: E501

        :return: The field_id of this UniqueFieldInUseErrors.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this UniqueFieldInUseErrors.

        Field ID  # noqa: E501

        :param field_id: The field_id of this UniqueFieldInUseErrors.  # noqa: E501
        :type: str
        """

        self._field_id = field_id

    @property
    def contacts(self):
        """Gets the contacts of this UniqueFieldInUseErrors.  # noqa: E501


        :return: The contacts of this UniqueFieldInUseErrors.  # noqa: E501
        :rtype: list[str]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this UniqueFieldInUseErrors.


        :param contacts: The contacts of this UniqueFieldInUseErrors.  # noqa: E501
        :type: list[str]
        """

        self._contacts = contacts

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
        if not isinstance(other, UniqueFieldInUseErrors):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UniqueFieldInUseErrors):
            return True

        return self.to_dict() != other.to_dict()
