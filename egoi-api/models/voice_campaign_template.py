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


class VoiceCampaignTemplate(object):
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
        'template_id': 'int',
        'template_hash': 'str',
        'internal_name': 'str',
        'created': 'datetime',
        'updated': 'datetime',
        'message': 'str',
        'sender': 'str',
        'message_type': 'str',
        'file': 'str',
        'options': 'list[object]'
    }

    attribute_map = {
        'template_id': 'template_id',
        'template_hash': 'template_hash',
        'internal_name': 'internal_name',
        'created': 'created',
        'updated': 'updated',
        'message': 'message',
        'sender': 'sender',
        'message_type': 'message_type',
        'file': 'file',
        'options': 'options'
    }

    def __init__(self, template_id=None, template_hash=None, internal_name=None, created=None, updated=None, message=None, sender=None, message_type=None, file=None, options=None, local_vars_configuration=None):  # noqa: E501
        """VoiceCampaignTemplate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._template_id = None
        self._template_hash = None
        self._internal_name = None
        self._created = None
        self._updated = None
        self._message = None
        self._sender = None
        self._message_type = None
        self._file = None
        self._options = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if template_hash is not None:
            self.template_hash = template_hash
        if internal_name is not None:
            self.internal_name = internal_name
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if message is not None:
            self.message = message
        if sender is not None:
            self.sender = sender
        if message_type is not None:
            self.message_type = message_type
        if file is not None:
            self.file = file
        if options is not None:
            self.options = options

    @property
    def template_id(self):
        """Gets the template_id of this VoiceCampaignTemplate.  # noqa: E501


        :return: The template_id of this VoiceCampaignTemplate.  # noqa: E501
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this VoiceCampaignTemplate.


        :param template_id: The template_id of this VoiceCampaignTemplate.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                template_id is not None and template_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `template_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._template_id = template_id

    @property
    def template_hash(self):
        """Gets the template_hash of this VoiceCampaignTemplate.  # noqa: E501


        :return: The template_hash of this VoiceCampaignTemplate.  # noqa: E501
        :rtype: str
        """
        return self._template_hash

    @template_hash.setter
    def template_hash(self, template_hash):
        """Sets the template_hash of this VoiceCampaignTemplate.


        :param template_hash: The template_hash of this VoiceCampaignTemplate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                template_hash is not None and not re.search(r'[a-zA-Z0-9_-]*', template_hash)):  # noqa: E501
            raise ValueError(r"Invalid value for `template_hash`, must be a follow pattern or equal to `/[a-zA-Z0-9_-]*/`")  # noqa: E501

        self._template_hash = template_hash

    @property
    def internal_name(self):
        """Gets the internal_name of this VoiceCampaignTemplate.  # noqa: E501

        Campaign internal name  # noqa: E501

        :return: The internal_name of this VoiceCampaignTemplate.  # noqa: E501
        :rtype: str
        """
        return self._internal_name

    @internal_name.setter
    def internal_name(self, internal_name):
        """Sets the internal_name of this VoiceCampaignTemplate.

        Campaign internal name  # noqa: E501

        :param internal_name: The internal_name of this VoiceCampaignTemplate.  # noqa: E501
        :type: str
        """

        self._internal_name = internal_name

    @property
    def created(self):
        """Gets the created of this VoiceCampaignTemplate.  # noqa: E501


        :return: The created of this VoiceCampaignTemplate.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this VoiceCampaignTemplate.


        :param created: The created of this VoiceCampaignTemplate.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this VoiceCampaignTemplate.  # noqa: E501


        :return: The updated of this VoiceCampaignTemplate.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this VoiceCampaignTemplate.


        :param updated: The updated of this VoiceCampaignTemplate.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def message(self):
        """Gets the message of this VoiceCampaignTemplate.  # noqa: E501

        Message  # noqa: E501

        :return: The message of this VoiceCampaignTemplate.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this VoiceCampaignTemplate.

        Message  # noqa: E501

        :param message: The message of this VoiceCampaignTemplate.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def sender(self):
        """Gets the sender of this VoiceCampaignTemplate.  # noqa: E501

        Sender number  # noqa: E501

        :return: The sender of this VoiceCampaignTemplate.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this VoiceCampaignTemplate.

        Sender number  # noqa: E501

        :param sender: The sender of this VoiceCampaignTemplate.  # noqa: E501
        :type: str
        """

        self._sender = sender

    @property
    def message_type(self):
        """Gets the message_type of this VoiceCampaignTemplate.  # noqa: E501

        Message type  # noqa: E501

        :return: The message_type of this VoiceCampaignTemplate.  # noqa: E501
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this VoiceCampaignTemplate.

        Message type  # noqa: E501

        :param message_type: The message_type of this VoiceCampaignTemplate.  # noqa: E501
        :type: str
        """
        allowed_values = ["normal", "flash"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and message_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `message_type` ({0}), must be one of {1}"  # noqa: E501
                .format(message_type, allowed_values)
            )

        self._message_type = message_type

    @property
    def file(self):
        """Gets the file of this VoiceCampaignTemplate.  # noqa: E501

        Voice template message file  # noqa: E501

        :return: The file of this VoiceCampaignTemplate.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this VoiceCampaignTemplate.

        Voice template message file  # noqa: E501

        :param file: The file of this VoiceCampaignTemplate.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def options(self):
        """Gets the options of this VoiceCampaignTemplate.  # noqa: E501

        Extra options  # noqa: E501

        :return: The options of this VoiceCampaignTemplate.  # noqa: E501
        :rtype: list[object]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this VoiceCampaignTemplate.

        Extra options  # noqa: E501

        :param options: The options of this VoiceCampaignTemplate.  # noqa: E501
        :type: list[object]
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
        if not isinstance(other, VoiceCampaignTemplate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VoiceCampaignTemplate):
            return True

        return self.to_dict() != other.to_dict()
