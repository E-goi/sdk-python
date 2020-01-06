# coding: utf-8

"""
    APIv3 (Beta)

     # Introduction Just a quick pick!!! This is our new version of API. Remember, it is not stable yet!!! But we invite you play with it and give us your feedback ;) # Getting Started  E-goi can be integrated with many environments and programming languages via our REST API. We've created a developer focused portal to give your organization a clear and quick overview of how to integrate with E-goi. The developer portal focuses on scenarios for integration and flow of events. We recommend familiarizing yourself with all of the content in the developer portal, before start using our rest API.   The E-goi  APIv3 is served over HTTPS. To ensure data privacy, unencrypted HTTP is not supported.  Request data is passed to the API by POSTing JSON objects to the API endpoints with the appropriate parameters.   BaseURL = api.egoiapp.com  # HTTP Methods for RESTful Services This API supports 5 HTTP methods:  * <b>GET</b>: The HTTP GET method is used to **read** (or retrieve) a representation of a resource. * <b>POST</b>: The POST verb is most-often utilized to **create** new resources. * <b>PATCH</b>: PATCH is used for **modify** capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource * <b>PUT</b>: PUT is most-often utilized for **update** capabilities, PUT-ing to a known resource URI with the request body containing the newly-updated representation of the original resource. * <b>DELETE</b>: DELETE is pretty easy to understand. It is used to **delete** a resource identified by a URI.  # Authentication   We use a custom authentication method, you will need a apikey that you can find in your account settings. Below you will see a curl example to get your account information:  #!/bin/bash  curl -X GET 'https://api.egoiapp.com/my-account' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>'  Here you can see a curl Post example with authentication:  #!/bin/bash  curl -X POST 'http://api.egoiapp.com/tags' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>' \\  -H 'Content-Type: application/json' \\  -d '{`name`:`Your custom tag`,`color`:`#FFFFFF`}'  <security-definitions/>  # noqa: E501

    The version of the OpenAPI document: 3.0.0-beta
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from egoi-api.configuration import Configuration


class PushCampaignPostRequest(object):
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
        'app_id': 'int',
        'title': 'str',
        'content': 'CampaignPushContent',
        'actions': 'list[PushCampaignPostRequestActions]',
        'geo_options': 'PushCampaignPostRequestGeoOptions',
        'notification_options': 'PushCampaignPostRequestNotificationOptions'
    }

    attribute_map = {
        'app_id': 'app_id',
        'title': 'title',
        'content': 'content',
        'actions': 'actions',
        'geo_options': 'geo_options',
        'notification_options': 'notification_options'
    }

    def __init__(self, app_id=None, title=None, content=None, actions=None, geo_options=None, notification_options=None, local_vars_configuration=None):  # noqa: E501
        """PushCampaignPostRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._app_id = None
        self._title = None
        self._content = None
        self._actions = None
        self._geo_options = None
        self._notification_options = None
        self.discriminator = None

        self.app_id = app_id
        self.title = title
        self.content = content
        if actions is not None:
            self.actions = actions
        if geo_options is not None:
            self.geo_options = geo_options
        if notification_options is not None:
            self.notification_options = notification_options

    @property
    def app_id(self):
        """Gets the app_id of this PushCampaignPostRequest.  # noqa: E501


        :return: The app_id of this PushCampaignPostRequest.  # noqa: E501
        :rtype: int
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this PushCampaignPostRequest.


        :param app_id: The app_id of this PushCampaignPostRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and app_id is None:  # noqa: E501
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                app_id is not None and app_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `app_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._app_id = app_id

    @property
    def title(self):
        """Gets the title of this PushCampaignPostRequest.  # noqa: E501

        Push campaign subject  # noqa: E501

        :return: The title of this PushCampaignPostRequest.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PushCampaignPostRequest.

        Push campaign subject  # noqa: E501

        :param title: The title of this PushCampaignPostRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def content(self):
        """Gets the content of this PushCampaignPostRequest.  # noqa: E501


        :return: The content of this PushCampaignPostRequest.  # noqa: E501
        :rtype: CampaignPushContent
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this PushCampaignPostRequest.


        :param content: The content of this PushCampaignPostRequest.  # noqa: E501
        :type: CampaignPushContent
        """
        if self.local_vars_configuration.client_side_validation and content is None:  # noqa: E501
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def actions(self):
        """Gets the actions of this PushCampaignPostRequest.  # noqa: E501

        Actions for push campaign  # noqa: E501

        :return: The actions of this PushCampaignPostRequest.  # noqa: E501
        :rtype: list[PushCampaignPostRequestActions]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this PushCampaignPostRequest.

        Actions for push campaign  # noqa: E501

        :param actions: The actions of this PushCampaignPostRequest.  # noqa: E501
        :type: list[PushCampaignPostRequestActions]
        """

        self._actions = actions

    @property
    def geo_options(self):
        """Gets the geo_options of this PushCampaignPostRequest.  # noqa: E501


        :return: The geo_options of this PushCampaignPostRequest.  # noqa: E501
        :rtype: PushCampaignPostRequestGeoOptions
        """
        return self._geo_options

    @geo_options.setter
    def geo_options(self, geo_options):
        """Sets the geo_options of this PushCampaignPostRequest.


        :param geo_options: The geo_options of this PushCampaignPostRequest.  # noqa: E501
        :type: PushCampaignPostRequestGeoOptions
        """

        self._geo_options = geo_options

    @property
    def notification_options(self):
        """Gets the notification_options of this PushCampaignPostRequest.  # noqa: E501


        :return: The notification_options of this PushCampaignPostRequest.  # noqa: E501
        :rtype: PushCampaignPostRequestNotificationOptions
        """
        return self._notification_options

    @notification_options.setter
    def notification_options(self, notification_options):
        """Sets the notification_options of this PushCampaignPostRequest.


        :param notification_options: The notification_options of this PushCampaignPostRequest.  # noqa: E501
        :type: PushCampaignPostRequestNotificationOptions
        """

        self._notification_options = notification_options

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
        if not isinstance(other, PushCampaignPostRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PushCampaignPostRequest):
            return True

        return self.to_dict() != other.to_dict()
