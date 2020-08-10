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


class GenerateSubscriptionsReport(object):
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
        'title': 'str',
        'range': 'AdvancedReportRange',
        'lists': 'int',
        'columns': 'AdvancedReportSubscriptionsColumns',
        'options': 'AdvancedReportSubscriptionsOptions',
        'callback_url': 'str'
    }

    attribute_map = {
        'title': 'title',
        'range': 'range',
        'lists': 'lists',
        'columns': 'columns',
        'options': 'options',
        'callback_url': 'callback_url'
    }

    def __init__(self, title=None, range=None, lists=None, columns=None, options=None, callback_url=None, local_vars_configuration=None):  # noqa: E501
        """GenerateSubscriptionsReport - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._range = None
        self._lists = None
        self._columns = None
        self._options = None
        self._callback_url = None
        self.discriminator = None

        self.title = title
        self.range = range
        self.lists = lists
        self.columns = columns
        self.options = options
        if callback_url is not None:
            self.callback_url = callback_url

    @property
    def title(self):
        """Gets the title of this GenerateSubscriptionsReport.  # noqa: E501

        Advanced report title  # noqa: E501

        :return: The title of this GenerateSubscriptionsReport.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GenerateSubscriptionsReport.

        Advanced report title  # noqa: E501

        :param title: The title of this GenerateSubscriptionsReport.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def range(self):
        """Gets the range of this GenerateSubscriptionsReport.  # noqa: E501


        :return: The range of this GenerateSubscriptionsReport.  # noqa: E501
        :rtype: AdvancedReportRange
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this GenerateSubscriptionsReport.


        :param range: The range of this GenerateSubscriptionsReport.  # noqa: E501
        :type: AdvancedReportRange
        """
        if self.local_vars_configuration.client_side_validation and range is None:  # noqa: E501
            raise ValueError("Invalid value for `range`, must not be `None`")  # noqa: E501

        self._range = range

    @property
    def lists(self):
        """Gets the lists of this GenerateSubscriptionsReport.  # noqa: E501


        :return: The lists of this GenerateSubscriptionsReport.  # noqa: E501
        :rtype: int
        """
        return self._lists

    @lists.setter
    def lists(self, lists):
        """Sets the lists of this GenerateSubscriptionsReport.


        :param lists: The lists of this GenerateSubscriptionsReport.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and lists is None:  # noqa: E501
            raise ValueError("Invalid value for `lists`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                lists is not None and lists < 1):  # noqa: E501
            raise ValueError("Invalid value for `lists`, must be a value greater than or equal to `1`")  # noqa: E501

        self._lists = lists

    @property
    def columns(self):
        """Gets the columns of this GenerateSubscriptionsReport.  # noqa: E501


        :return: The columns of this GenerateSubscriptionsReport.  # noqa: E501
        :rtype: AdvancedReportSubscriptionsColumns
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this GenerateSubscriptionsReport.


        :param columns: The columns of this GenerateSubscriptionsReport.  # noqa: E501
        :type: AdvancedReportSubscriptionsColumns
        """
        if self.local_vars_configuration.client_side_validation and columns is None:  # noqa: E501
            raise ValueError("Invalid value for `columns`, must not be `None`")  # noqa: E501

        self._columns = columns

    @property
    def options(self):
        """Gets the options of this GenerateSubscriptionsReport.  # noqa: E501


        :return: The options of this GenerateSubscriptionsReport.  # noqa: E501
        :rtype: AdvancedReportSubscriptionsOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this GenerateSubscriptionsReport.


        :param options: The options of this GenerateSubscriptionsReport.  # noqa: E501
        :type: AdvancedReportSubscriptionsOptions
        """
        if self.local_vars_configuration.client_side_validation and options is None:  # noqa: E501
            raise ValueError("Invalid value for `options`, must not be `None`")  # noqa: E501

        self._options = options

    @property
    def callback_url(self):
        """Gets the callback_url of this GenerateSubscriptionsReport.  # noqa: E501

        URL which will receive the information of the report  # noqa: E501

        :return: The callback_url of this GenerateSubscriptionsReport.  # noqa: E501
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """Sets the callback_url of this GenerateSubscriptionsReport.

        URL which will receive the information of the report  # noqa: E501

        :param callback_url: The callback_url of this GenerateSubscriptionsReport.  # noqa: E501
        :type: str
        """

        self._callback_url = callback_url

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
        if not isinstance(other, GenerateSubscriptionsReport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GenerateSubscriptionsReport):
            return True

        return self.to_dict() != other.to_dict()
