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


class ComplexContactAllOfEmailStats(object):
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
        'sent': 'int',
        'opens': 'int',
        'clicks': 'int',
        'soft_bounces': 'int',
        'hard_bounces': 'int',
        'forwards': 'int',
        'conversions': 'int',
        'social_actions': 'int',
        'last_send_date': 'datetime',
        'last_open_date': 'datetime',
        'last_click_date': 'datetime',
        'last_open_country': 'str',
        'last_open_region': 'str',
        'last_open_city': 'str'
    }

    attribute_map = {
        'sent': 'sent',
        'opens': 'opens',
        'clicks': 'clicks',
        'soft_bounces': 'soft_bounces',
        'hard_bounces': 'hard_bounces',
        'forwards': 'forwards',
        'conversions': 'conversions',
        'social_actions': 'social_actions',
        'last_send_date': 'last_send_date',
        'last_open_date': 'last_open_date',
        'last_click_date': 'last_click_date',
        'last_open_country': 'last_open_country',
        'last_open_region': 'last_open_region',
        'last_open_city': 'last_open_city'
    }

    def __init__(self, sent=None, opens=None, clicks=None, soft_bounces=None, hard_bounces=None, forwards=None, conversions=None, social_actions=None, last_send_date=None, last_open_date=None, last_click_date=None, last_open_country=None, last_open_region=None, last_open_city=None, local_vars_configuration=None):  # noqa: E501
        """ComplexContactAllOfEmailStats - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sent = None
        self._opens = None
        self._clicks = None
        self._soft_bounces = None
        self._hard_bounces = None
        self._forwards = None
        self._conversions = None
        self._social_actions = None
        self._last_send_date = None
        self._last_open_date = None
        self._last_click_date = None
        self._last_open_country = None
        self._last_open_region = None
        self._last_open_city = None
        self.discriminator = None

        if sent is not None:
            self.sent = sent
        if opens is not None:
            self.opens = opens
        if clicks is not None:
            self.clicks = clicks
        if soft_bounces is not None:
            self.soft_bounces = soft_bounces
        if hard_bounces is not None:
            self.hard_bounces = hard_bounces
        if forwards is not None:
            self.forwards = forwards
        if conversions is not None:
            self.conversions = conversions
        if social_actions is not None:
            self.social_actions = social_actions
        self.last_send_date = last_send_date
        self.last_open_date = last_open_date
        self.last_click_date = last_click_date
        self.last_open_country = last_open_country
        self.last_open_region = last_open_region
        self.last_open_city = last_open_city

    @property
    def sent(self):
        """Gets the sent of this ComplexContactAllOfEmailStats.  # noqa: E501

        Emails sent to the contact  # noqa: E501

        :return: The sent of this ComplexContactAllOfEmailStats.  # noqa: E501
        :rtype: int
        """
        return self._sent

    @sent.setter
    def sent(self, sent):
        """Sets the sent of this ComplexContactAllOfEmailStats.

        Emails sent to the contact  # noqa: E501

        :param sent: The sent of this ComplexContactAllOfEmailStats.  # noqa: E501
        :type: int
        """

        self._sent = sent

    @property
    def opens(self):
        """Gets the opens of this ComplexContactAllOfEmailStats.  # noqa: E501

        Emails opened by the contact  # noqa: E501

        :return: The opens of this ComplexContactAllOfEmailStats.  # noqa: E501
        :rtype: int
        """
        return self._opens

    @opens.setter
    def opens(self, opens):
        """Sets the opens of this ComplexContactAllOfEmailStats.

        Emails opened by the contact  # noqa: E501

        :param opens: The opens of this ComplexContactAllOfEmailStats.  # noqa: E501
        :type: int
        """

        self._opens = opens

    @property
    def clicks(self):
        """Gets the clicks of this ComplexContactAllOfEmailStats.  # noqa: E501

        Total number of clicks made by the contact  # noqa: E501

        :return: The clicks of this ComplexContactAllOfEmailStats.  # noqa: E501
        :rtype: int
        """
        return self._clicks

    @clicks.setter
    def clicks(self, clicks):
        """Sets the clicks of this ComplexContactAllOfEmailStats.

        Total number of clicks made by the contact  # noqa: E501

        :param clicks: The clicks of this ComplexContactAllOfEmailStats.  # noqa: E501
        :type: int
        """

        self._clicks = clicks

    @property
    def soft_bounces(self):
        """Gets the soft_bounces of this ComplexContactAllOfEmailStats.  # noqa: E501

        Soft bounces for the contact  # noqa: E501

        :return: The soft_bounces of this ComplexContactAllOfEmailStats.  # noqa: E501
        :rtype: int
        """
        return self._soft_bounces

    @soft_bounces.setter
    def soft_bounces(self, soft_bounces):
        """Sets the soft_bounces of this ComplexContactAllOfEmailStats.

        Soft bounces for the contact  # noqa: E501

        :param soft_bounces: The soft_bounces of this ComplexContactAllOfEmailStats.  # noqa: E501
        :type: int
        """

        self._soft_bounces = soft_bounces

    @property
    def hard_bounces(self):
        """Gets the hard_bounces of this ComplexContactAllOfEmailStats.  # noqa: E501

        Hard bounces for the contact  # noqa: E501

        :return: The hard_bounces of this ComplexContactAllOfEmailStats.  # noqa: E501
        :rtype: int
        """
        return self._hard_bounces

    @hard_bounces.setter
    def hard_bounces(self, hard_bounces):
        """Sets the hard_bounces of this ComplexContactAllOfEmailStats.

        Hard bounces for the contact  # noqa: E501

        :param hard_bounces: The hard_bounces of this ComplexContactAllOfEmailStats.  # noqa: E501
        :type: int
        """

        self._hard_bounces = hard_bounces

    @property
    def forwards(self):
        """Gets the forwards of this ComplexContactAllOfEmailStats.  # noqa: E501

        Emails forwarded by the contact  # noqa: E501

        :return: The forwards of this ComplexContactAllOfEmailStats.  # noqa: E501
        :rtype: int
        """
        return self._forwards

    @forwards.setter
    def forwards(self, forwards):
        """Sets the forwards of this ComplexContactAllOfEmailStats.

        Emails forwarded by the contact  # noqa: E501

        :param forwards: The forwards of this ComplexContactAllOfEmailStats.  # noqa: E501
        :type: int
        """

        self._forwards = forwards

    @property
    def conversions(self):
        """Gets the conversions of this ComplexContactAllOfEmailStats.  # noqa: E501

        Total of conversions  # noqa: E501

        :return: The conversions of this ComplexContactAllOfEmailStats.  # noqa: E501
        :rtype: int
        """
        return self._conversions

    @conversions.setter
    def conversions(self, conversions):
        """Sets the conversions of this ComplexContactAllOfEmailStats.

        Total of conversions  # noqa: E501

        :param conversions: The conversions of this ComplexContactAllOfEmailStats.  # noqa: E501
        :type: int
        """

        self._conversions = conversions

    @property
    def social_actions(self):
        """Gets the social_actions of this ComplexContactAllOfEmailStats.  # noqa: E501

        Total of social actions for the contact  # noqa: E501

        :return: The social_actions of this ComplexContactAllOfEmailStats.  # noqa: E501
        :rtype: int
        """
        return self._social_actions

    @social_actions.setter
    def social_actions(self, social_actions):
        """Sets the social_actions of this ComplexContactAllOfEmailStats.

        Total of social actions for the contact  # noqa: E501

        :param social_actions: The social_actions of this ComplexContactAllOfEmailStats.  # noqa: E501
        :type: int
        """

        self._social_actions = social_actions

    @property
    def last_send_date(self):
        """Gets the last_send_date of this ComplexContactAllOfEmailStats.  # noqa: E501

        Date of the last email sent to the contact  # noqa: E501

        :return: The last_send_date of this ComplexContactAllOfEmailStats.  # noqa: E501
        :rtype: datetime
        """
        return self._last_send_date

    @last_send_date.setter
    def last_send_date(self, last_send_date):
        """Sets the last_send_date of this ComplexContactAllOfEmailStats.

        Date of the last email sent to the contact  # noqa: E501

        :param last_send_date: The last_send_date of this ComplexContactAllOfEmailStats.  # noqa: E501
        :type: datetime
        """

        self._last_send_date = last_send_date

    @property
    def last_open_date(self):
        """Gets the last_open_date of this ComplexContactAllOfEmailStats.  # noqa: E501

        Date of the last email open of the contact  # noqa: E501

        :return: The last_open_date of this ComplexContactAllOfEmailStats.  # noqa: E501
        :rtype: datetime
        """
        return self._last_open_date

    @last_open_date.setter
    def last_open_date(self, last_open_date):
        """Sets the last_open_date of this ComplexContactAllOfEmailStats.

        Date of the last email open of the contact  # noqa: E501

        :param last_open_date: The last_open_date of this ComplexContactAllOfEmailStats.  # noqa: E501
        :type: datetime
        """

        self._last_open_date = last_open_date

    @property
    def last_click_date(self):
        """Gets the last_click_date of this ComplexContactAllOfEmailStats.  # noqa: E501

        Date of the last email click of the contact  # noqa: E501

        :return: The last_click_date of this ComplexContactAllOfEmailStats.  # noqa: E501
        :rtype: datetime
        """
        return self._last_click_date

    @last_click_date.setter
    def last_click_date(self, last_click_date):
        """Sets the last_click_date of this ComplexContactAllOfEmailStats.

        Date of the last email click of the contact  # noqa: E501

        :param last_click_date: The last_click_date of this ComplexContactAllOfEmailStats.  # noqa: E501
        :type: datetime
        """

        self._last_click_date = last_click_date

    @property
    def last_open_country(self):
        """Gets the last_open_country of this ComplexContactAllOfEmailStats.  # noqa: E501

        Country where the last email for that contact was opened  # noqa: E501

        :return: The last_open_country of this ComplexContactAllOfEmailStats.  # noqa: E501
        :rtype: str
        """
        return self._last_open_country

    @last_open_country.setter
    def last_open_country(self, last_open_country):
        """Sets the last_open_country of this ComplexContactAllOfEmailStats.

        Country where the last email for that contact was opened  # noqa: E501

        :param last_open_country: The last_open_country of this ComplexContactAllOfEmailStats.  # noqa: E501
        :type: str
        """

        self._last_open_country = last_open_country

    @property
    def last_open_region(self):
        """Gets the last_open_region of this ComplexContactAllOfEmailStats.  # noqa: E501

        Region where the last email for that contact was opened  # noqa: E501

        :return: The last_open_region of this ComplexContactAllOfEmailStats.  # noqa: E501
        :rtype: str
        """
        return self._last_open_region

    @last_open_region.setter
    def last_open_region(self, last_open_region):
        """Sets the last_open_region of this ComplexContactAllOfEmailStats.

        Region where the last email for that contact was opened  # noqa: E501

        :param last_open_region: The last_open_region of this ComplexContactAllOfEmailStats.  # noqa: E501
        :type: str
        """

        self._last_open_region = last_open_region

    @property
    def last_open_city(self):
        """Gets the last_open_city of this ComplexContactAllOfEmailStats.  # noqa: E501

        City where the last email for that contact was opened  # noqa: E501

        :return: The last_open_city of this ComplexContactAllOfEmailStats.  # noqa: E501
        :rtype: str
        """
        return self._last_open_city

    @last_open_city.setter
    def last_open_city(self, last_open_city):
        """Sets the last_open_city of this ComplexContactAllOfEmailStats.

        City where the last email for that contact was opened  # noqa: E501

        :param last_open_city: The last_open_city of this ComplexContactAllOfEmailStats.  # noqa: E501
        :type: str
        """

        self._last_open_city = last_open_city

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
        if not isinstance(other, ComplexContactAllOfEmailStats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComplexContactAllOfEmailStats):
            return True

        return self.to_dict() != other.to_dict()
