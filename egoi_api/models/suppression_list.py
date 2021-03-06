# coding: utf-8

"""
    APIv3 (New)

     # Introduction This is our new version of API. We invite you to start using it and give us your feedback # Getting Started  E-goi can be integrated with many environments and programming languages via our REST API. We've created a developer focused portal to give your organization a clear and quick overview of how to integrate with E-goi. The developer portal focuses on scenarios for integration and flow of events. We recommend familiarizing yourself with all of the content in the developer portal, before start using our rest API.   The E-goi  APIv3 is served over HTTPS. To ensure data privacy, unencrypted HTTP is not supported.  Request data is passed to the API by POSTing JSON objects to the API endpoints with the appropriate parameters.   BaseURL = api.egoiapp.com  # RESTful Services This API supports 5 HTTP methods:  * <b>GET</b>: The HTTP GET method is used to **read** (or retrieve) a representation of a resource. * <b>POST</b>: The POST verb is most-often utilized to **create** new resources. * <b>PATCH</b>: PATCH is used for **modify** capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource * <b>PUT</b>: PUT is most-often utilized for **update** capabilities, PUT-ing to a known resource URI with the request body containing the newly-updated representation of the original resource. * <b>DELETE</b>: DELETE is pretty easy to understand. It is used to **delete** a resource identified by a URI.  # Authentication   We use a custom authentication method, you will need a apikey that you can find in your account settings. Below you will see a curl example to get your account information:  #!/bin/bash  curl -X GET 'https://api.egoiapp.com/my-account' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>'  Here you can see a curl Post example with authentication:  #!/bin/bash  curl -X POST 'http://api.egoiapp.com/tags' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>' \\  -H 'Content-Type: application/json' \\  -d '{`name`:`Your custom tag`,`color`:`#FFFFFF`}'  # SDK Get started quickly with E-goi with our integration tools. Our SDK is a modern open source library that makes it easy to integrate your application with E-goi services.  * <a href='https://github.com/E-goi/sdk-java'>Java</a>  * <a href='https://github.com/E-goi/sdk-php'>PHP</a>  * <a href='https://github.com/E-goi/sdk-python'>Python</a>  * <a href='https://github.com/E-goi/sdk-ruby'>Ruby</a>  * <a href='https://github.com/E-goi/sdk-javascript'>Javascript</a>  * <a href='https://github.com/E-goi/sdk-csharp'>C#</a>  # Stream Limits Stream limits are security mesures we have to make sure our API have a fair use policy, for this reason, any request that creates or modifies data (**POST**, **PATCH** and **PUT**) is limited to a maximum of **20MB** of content length. If you arrive to this limit in one of your request, you'll receive a HTTP code **413 (Request Entity Too Large)** and the request will be ignored. To avoid this error in importation's requests, it's advised the request's division in batches that have each one less than 20MB.  # Timeouts Timeouts set a maximum waiting time on a request's response. Our API, sets a default timeout for each request and when breached, you'll receive an HTTP **408 (Request Timeout)** error code. You should take into consideration that response times can vary widely based on the complexity of the request, amount of data being analyzed, and the load on the system and workspace at the time of the query. When dealing with such errors, you should first attempt to reduce the complexity and amount of data under analysis, and only then, if problems are still occurring ask for support.  For all these reasons, the default timeout for each request is **10 Seconds** and any request that creates or modifies data (**POST**, **PATCH** and **PUT**) will have a timeout of **60 Seconds**. Specific timeouts may exist for specific requests, these can be found in the request's documentation.  <security-definitions/>  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from egoi_api.configuration import Configuration


class SuppressionList(object):
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
        'id': 'int',
        'value': 'str',
        'type': 'str',
        'method': 'str',
        'campaign_hash': 'str',
        'created': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'value': 'value',
        'type': 'type',
        'method': 'method',
        'campaign_hash': 'campaign_hash',
        'created': 'created'
    }

    def __init__(self, id=None, value=None, type=None, method=None, campaign_hash=None, created=None, local_vars_configuration=None):  # noqa: E501
        """SuppressionList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._value = None
        self._type = None
        self._method = None
        self._campaign_hash = None
        self._created = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if value is not None:
            self.value = value
        if type is not None:
            self.type = type
        if method is not None:
            self.method = method
        if campaign_hash is not None:
            self.campaign_hash = campaign_hash
        if created is not None:
            self.created = created

    @property
    def id(self):
        """Gets the id of this SuppressionList.  # noqa: E501


        :return: The id of this SuppressionList.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SuppressionList.


        :param id: The id of this SuppressionList.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                id is not None and id < 1):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def value(self):
        """Gets the value of this SuppressionList.  # noqa: E501

        Suppressed value  # noqa: E501

        :return: The value of this SuppressionList.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SuppressionList.

        Suppressed value  # noqa: E501

        :param value: The value of this SuppressionList.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def type(self):
        """Gets the type of this SuppressionList.  # noqa: E501

        Suppression type  # noqa: E501

        :return: The type of this SuppressionList.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SuppressionList.

        Suppression type  # noqa: E501

        :param type: The type of this SuppressionList.  # noqa: E501
        :type: str
        """
        allowed_values = ["email", "email_domain", "email_user", "cellphone", "phone"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def method(self):
        """Gets the method of this SuppressionList.  # noqa: E501

        Suppression method  # noqa: E501

        :return: The method of this SuppressionList.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this SuppressionList.

        Suppression method  # noqa: E501

        :param method: The method of this SuppressionList.  # noqa: E501
        :type: str
        """
        allowed_values = ["unsubscribe", "bounce", "manual", "other", "forgotten"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def campaign_hash(self):
        """Gets the campaign_hash of this SuppressionList.  # noqa: E501


        :return: The campaign_hash of this SuppressionList.  # noqa: E501
        :rtype: str
        """
        return self._campaign_hash

    @campaign_hash.setter
    def campaign_hash(self, campaign_hash):
        """Sets the campaign_hash of this SuppressionList.


        :param campaign_hash: The campaign_hash of this SuppressionList.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                campaign_hash is not None and not re.search(r'[a-zA-Z0-9_-]*', campaign_hash)):  # noqa: E501
            raise ValueError(r"Invalid value for `campaign_hash`, must be a follow pattern or equal to `/[a-zA-Z0-9_-]*/`")  # noqa: E501

        self._campaign_hash = campaign_hash

    @property
    def created(self):
        """Gets the created of this SuppressionList.  # noqa: E501


        :return: The created of this SuppressionList.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SuppressionList.


        :param created: The created of this SuppressionList.  # noqa: E501
        :type: datetime
        """

        self._created = created

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
        if not isinstance(other, SuppressionList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SuppressionList):
            return True

        return self.to_dict() != other.to_dict()
