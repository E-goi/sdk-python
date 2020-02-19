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


class UnsubscriptionObject(object):
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
        'unsubscription_method': 'str',
        'unsubscription_reason': 'str',
        'unsubscription_observation': 'str'
    }

    attribute_map = {
        'unsubscription_method': 'unsubscription_method',
        'unsubscription_reason': 'unsubscription_reason',
        'unsubscription_observation': 'unsubscription_observation'
    }

    def __init__(self, unsubscription_method=None, unsubscription_reason=None, unsubscription_observation=None, local_vars_configuration=None):  # noqa: E501
        """UnsubscriptionObject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._unsubscription_method = None
        self._unsubscription_reason = None
        self._unsubscription_observation = None
        self.discriminator = None

        if unsubscription_method is not None:
            self.unsubscription_method = unsubscription_method
        if unsubscription_reason is not None:
            self.unsubscription_reason = unsubscription_reason
        if unsubscription_observation is not None:
            self.unsubscription_observation = unsubscription_observation

    @property
    def unsubscription_method(self):
        """Gets the unsubscription_method of this UnsubscriptionObject.  # noqa: E501

        Unsubcription Method  # noqa: E501

        :return: The unsubscription_method of this UnsubscriptionObject.  # noqa: E501
        :rtype: str
        """
        return self._unsubscription_method

    @unsubscription_method.setter
    def unsubscription_method(self, unsubscription_method):
        """Sets the unsubscription_method of this UnsubscriptionObject.

        Unsubcription Method  # noqa: E501

        :param unsubscription_method: The unsubscription_method of this UnsubscriptionObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["manual", "form", "unsubscribe_link", "bounce", "api"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and unsubscription_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `unsubscription_method` ({0}), must be one of {1}"  # noqa: E501
                .format(unsubscription_method, allowed_values)
            )

        self._unsubscription_method = unsubscription_method

    @property
    def unsubscription_reason(self):
        """Gets the unsubscription_reason of this UnsubscriptionObject.  # noqa: E501

        Unsubcription Reason  # noqa: E501

        :return: The unsubscription_reason of this UnsubscriptionObject.  # noqa: E501
        :rtype: str
        """
        return self._unsubscription_reason

    @unsubscription_reason.setter
    def unsubscription_reason(self, unsubscription_reason):
        """Sets the unsubscription_reason of this UnsubscriptionObject.

        Unsubcription Reason  # noqa: E501

        :param unsubscription_reason: The unsubscription_reason of this UnsubscriptionObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["not_interested", "lack_of_time", "email_address_change", "spam", "other"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and unsubscription_reason not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `unsubscription_reason` ({0}), must be one of {1}"  # noqa: E501
                .format(unsubscription_reason, allowed_values)
            )

        self._unsubscription_reason = unsubscription_reason

    @property
    def unsubscription_observation(self):
        """Gets the unsubscription_observation of this UnsubscriptionObject.  # noqa: E501

        Unsubcription Observation  # noqa: E501

        :return: The unsubscription_observation of this UnsubscriptionObject.  # noqa: E501
        :rtype: str
        """
        return self._unsubscription_observation

    @unsubscription_observation.setter
    def unsubscription_observation(self, unsubscription_observation):
        """Sets the unsubscription_observation of this UnsubscriptionObject.

        Unsubcription Observation  # noqa: E501

        :param unsubscription_observation: The unsubscription_observation of this UnsubscriptionObject.  # noqa: E501
        :type: str
        """

        self._unsubscription_observation = unsubscription_observation

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
        if not isinstance(other, UnsubscriptionObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UnsubscriptionObject):
            return True

        return self.to_dict() != other.to_dict()
