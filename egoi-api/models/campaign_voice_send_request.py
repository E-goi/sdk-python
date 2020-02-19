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


class CampaignVoiceSendRequest(object):
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
        'segments': 'OSegmentsActionSend',
        'notify': 'list[int]',
        'destination_field': 'str',
        'limit_contacts': 'OLimitContactsActionSend',
        'limit_hour': 'LimitHourActionSendLimitHour',
        'limit_speed': 'int',
        'schedule_date': 'datetime'
    }

    attribute_map = {
        'list_id': 'list_id',
        'segments': 'segments',
        'notify': 'notify',
        'destination_field': 'destination_field',
        'limit_contacts': 'limit_contacts',
        'limit_hour': 'limit_hour',
        'limit_speed': 'limit_speed',
        'schedule_date': 'schedule_date'
    }

    def __init__(self, list_id=None, segments=None, notify=None, destination_field=None, limit_contacts=None, limit_hour=None, limit_speed=None, schedule_date=None, local_vars_configuration=None):  # noqa: E501
        """CampaignVoiceSendRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._list_id = None
        self._segments = None
        self._notify = None
        self._destination_field = None
        self._limit_contacts = None
        self._limit_hour = None
        self._limit_speed = None
        self._schedule_date = None
        self.discriminator = None

        self.list_id = list_id
        self.segments = segments
        if notify is not None:
            self.notify = notify
        self.destination_field = destination_field
        if limit_contacts is not None:
            self.limit_contacts = limit_contacts
        if limit_hour is not None:
            self.limit_hour = limit_hour
        if limit_speed is not None:
            self.limit_speed = limit_speed
        if schedule_date is not None:
            self.schedule_date = schedule_date

    @property
    def list_id(self):
        """Gets the list_id of this CampaignVoiceSendRequest.  # noqa: E501


        :return: The list_id of this CampaignVoiceSendRequest.  # noqa: E501
        :rtype: int
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this CampaignVoiceSendRequest.


        :param list_id: The list_id of this CampaignVoiceSendRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and list_id is None:  # noqa: E501
            raise ValueError("Invalid value for `list_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                list_id is not None and list_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `list_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._list_id = list_id

    @property
    def segments(self):
        """Gets the segments of this CampaignVoiceSendRequest.  # noqa: E501


        :return: The segments of this CampaignVoiceSendRequest.  # noqa: E501
        :rtype: OSegmentsActionSend
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """Sets the segments of this CampaignVoiceSendRequest.


        :param segments: The segments of this CampaignVoiceSendRequest.  # noqa: E501
        :type: OSegmentsActionSend
        """
        if self.local_vars_configuration.client_side_validation and segments is None:  # noqa: E501
            raise ValueError("Invalid value for `segments`, must not be `None`")  # noqa: E501

        self._segments = segments

    @property
    def notify(self):
        """Gets the notify of this CampaignVoiceSendRequest.  # noqa: E501

        Array of IDs of the users to notify  # noqa: E501

        :return: The notify of this CampaignVoiceSendRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._notify

    @notify.setter
    def notify(self, notify):
        """Sets the notify of this CampaignVoiceSendRequest.

        Array of IDs of the users to notify  # noqa: E501

        :param notify: The notify of this CampaignVoiceSendRequest.  # noqa: E501
        :type: list[int]
        """

        self._notify = notify

    @property
    def destination_field(self):
        """Gets the destination_field of this CampaignVoiceSendRequest.  # noqa: E501

        Destination field of this campaign  # noqa: E501

        :return: The destination_field of this CampaignVoiceSendRequest.  # noqa: E501
        :rtype: str
        """
        return self._destination_field

    @destination_field.setter
    def destination_field(self, destination_field):
        """Sets the destination_field of this CampaignVoiceSendRequest.

        Destination field of this campaign  # noqa: E501

        :param destination_field: The destination_field of this CampaignVoiceSendRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and destination_field is None:  # noqa: E501
            raise ValueError("Invalid value for `destination_field`, must not be `None`")  # noqa: E501
        allowed_values = ["phone", "cellphone", "phone_failsafe_cellphone", "cellphone_failsafe_phone", "cellphone_phone"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and destination_field not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `destination_field` ({0}), must be one of {1}"  # noqa: E501
                .format(destination_field, allowed_values)
            )

        self._destination_field = destination_field

    @property
    def limit_contacts(self):
        """Gets the limit_contacts of this CampaignVoiceSendRequest.  # noqa: E501


        :return: The limit_contacts of this CampaignVoiceSendRequest.  # noqa: E501
        :rtype: OLimitContactsActionSend
        """
        return self._limit_contacts

    @limit_contacts.setter
    def limit_contacts(self, limit_contacts):
        """Sets the limit_contacts of this CampaignVoiceSendRequest.


        :param limit_contacts: The limit_contacts of this CampaignVoiceSendRequest.  # noqa: E501
        :type: OLimitContactsActionSend
        """

        self._limit_contacts = limit_contacts

    @property
    def limit_hour(self):
        """Gets the limit_hour of this CampaignVoiceSendRequest.  # noqa: E501


        :return: The limit_hour of this CampaignVoiceSendRequest.  # noqa: E501
        :rtype: LimitHourActionSendLimitHour
        """
        return self._limit_hour

    @limit_hour.setter
    def limit_hour(self, limit_hour):
        """Sets the limit_hour of this CampaignVoiceSendRequest.


        :param limit_hour: The limit_hour of this CampaignVoiceSendRequest.  # noqa: E501
        :type: LimitHourActionSendLimitHour
        """

        self._limit_hour = limit_hour

    @property
    def limit_speed(self):
        """Gets the limit_speed of this CampaignVoiceSendRequest.  # noqa: E501

        Speed limit to send the campaign  # noqa: E501

        :return: The limit_speed of this CampaignVoiceSendRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit_speed

    @limit_speed.setter
    def limit_speed(self, limit_speed):
        """Sets the limit_speed of this CampaignVoiceSendRequest.

        Speed limit to send the campaign  # noqa: E501

        :param limit_speed: The limit_speed of this CampaignVoiceSendRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                limit_speed is not None and limit_speed > 10):  # noqa: E501
            raise ValueError("Invalid value for `limit_speed`, must be a value less than or equal to `10`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                limit_speed is not None and limit_speed < 1):  # noqa: E501
            raise ValueError("Invalid value for `limit_speed`, must be a value greater than or equal to `1`")  # noqa: E501

        self._limit_speed = limit_speed

    @property
    def schedule_date(self):
        """Gets the schedule_date of this CampaignVoiceSendRequest.  # noqa: E501

        The date and time  # noqa: E501

        :return: The schedule_date of this CampaignVoiceSendRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._schedule_date

    @schedule_date.setter
    def schedule_date(self, schedule_date):
        """Sets the schedule_date of this CampaignVoiceSendRequest.

        The date and time  # noqa: E501

        :param schedule_date: The schedule_date of this CampaignVoiceSendRequest.  # noqa: E501
        :type: datetime
        """

        self._schedule_date = schedule_date

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
        if not isinstance(other, CampaignVoiceSendRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampaignVoiceSendRequest):
            return True

        return self.to_dict() != other.to_dict()
