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


class EmailCampaignCreate(object):
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
        'subject': 'str',
        'content': 'CampaignEmailContent',
        'sender_id': 'int',
        'reply_to': 'int',
        'header_footer': 'HeaderFooter'
    }

    attribute_map = {
        'list_id': 'list_id',
        'internal_name': 'internal_name',
        'subject': 'subject',
        'content': 'content',
        'sender_id': 'sender_id',
        'reply_to': 'reply_to',
        'header_footer': 'header_footer'
    }

    def __init__(self, list_id=None, internal_name=None, subject=None, content=None, sender_id=None, reply_to=None, header_footer=None, local_vars_configuration=None):  # noqa: E501
        """EmailCampaignCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._list_id = None
        self._internal_name = None
        self._subject = None
        self._content = None
        self._sender_id = None
        self._reply_to = None
        self._header_footer = None
        self.discriminator = None

        self.list_id = list_id
        self.internal_name = internal_name
        if subject is not None:
            self.subject = subject
        self.content = content
        self.sender_id = sender_id
        if reply_to is not None:
            self.reply_to = reply_to
        if header_footer is not None:
            self.header_footer = header_footer

    @property
    def list_id(self):
        """Gets the list_id of this EmailCampaignCreate.  # noqa: E501


        :return: The list_id of this EmailCampaignCreate.  # noqa: E501
        :rtype: int
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this EmailCampaignCreate.


        :param list_id: The list_id of this EmailCampaignCreate.  # noqa: E501
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
        """Gets the internal_name of this EmailCampaignCreate.  # noqa: E501

        Campaign internal name  # noqa: E501

        :return: The internal_name of this EmailCampaignCreate.  # noqa: E501
        :rtype: str
        """
        return self._internal_name

    @internal_name.setter
    def internal_name(self, internal_name):
        """Sets the internal_name of this EmailCampaignCreate.

        Campaign internal name  # noqa: E501

        :param internal_name: The internal_name of this EmailCampaignCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and internal_name is None:  # noqa: E501
            raise ValueError("Invalid value for `internal_name`, must not be `None`")  # noqa: E501

        self._internal_name = internal_name

    @property
    def subject(self):
        """Gets the subject of this EmailCampaignCreate.  # noqa: E501

        Campaign subject. If no value is sent, defaults to 'internal_name' property value  # noqa: E501

        :return: The subject of this EmailCampaignCreate.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this EmailCampaignCreate.

        Campaign subject. If no value is sent, defaults to 'internal_name' property value  # noqa: E501

        :param subject: The subject of this EmailCampaignCreate.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def content(self):
        """Gets the content of this EmailCampaignCreate.  # noqa: E501


        :return: The content of this EmailCampaignCreate.  # noqa: E501
        :rtype: CampaignEmailContent
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this EmailCampaignCreate.


        :param content: The content of this EmailCampaignCreate.  # noqa: E501
        :type: CampaignEmailContent
        """
        if self.local_vars_configuration.client_side_validation and content is None:  # noqa: E501
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def sender_id(self):
        """Gets the sender_id of this EmailCampaignCreate.  # noqa: E501


        :return: The sender_id of this EmailCampaignCreate.  # noqa: E501
        :rtype: int
        """
        return self._sender_id

    @sender_id.setter
    def sender_id(self, sender_id):
        """Sets the sender_id of this EmailCampaignCreate.


        :param sender_id: The sender_id of this EmailCampaignCreate.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and sender_id is None:  # noqa: E501
            raise ValueError("Invalid value for `sender_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sender_id is not None and sender_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `sender_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._sender_id = sender_id

    @property
    def reply_to(self):
        """Gets the reply_to of this EmailCampaignCreate.  # noqa: E501


        :return: The reply_to of this EmailCampaignCreate.  # noqa: E501
        :rtype: int
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """Sets the reply_to of this EmailCampaignCreate.


        :param reply_to: The reply_to of this EmailCampaignCreate.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                reply_to is not None and reply_to < 1):  # noqa: E501
            raise ValueError("Invalid value for `reply_to`, must be a value greater than or equal to `1`")  # noqa: E501

        self._reply_to = reply_to

    @property
    def header_footer(self):
        """Gets the header_footer of this EmailCampaignCreate.  # noqa: E501


        :return: The header_footer of this EmailCampaignCreate.  # noqa: E501
        :rtype: HeaderFooter
        """
        return self._header_footer

    @header_footer.setter
    def header_footer(self, header_footer):
        """Sets the header_footer of this EmailCampaignCreate.


        :param header_footer: The header_footer of this EmailCampaignCreate.  # noqa: E501
        :type: HeaderFooter
        """

        self._header_footer = header_footer

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
        if not isinstance(other, EmailCampaignCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailCampaignCreate):
            return True

        return self.to_dict() != other.to_dict()
