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


class Operation(object):
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
        'operation_id': 'int',
        'operation_data': 'OperationOperationData',
        'type': 'str',
        'status': 'str',
        'created_by': 'int',
        'created': 'datetime',
        'start_date': 'datetime'
    }

    attribute_map = {
        'operation_id': 'operation_id',
        'operation_data': 'operation_data',
        'type': 'type',
        'status': 'status',
        'created_by': 'created_by',
        'created': 'created',
        'start_date': 'start_date'
    }

    def __init__(self, operation_id=None, operation_data=None, type=None, status=None, created_by=None, created=None, start_date=None, local_vars_configuration=None):  # noqa: E501
        """Operation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._operation_id = None
        self._operation_data = None
        self._type = None
        self._status = None
        self._created_by = None
        self._created = None
        self._start_date = None
        self.discriminator = None

        if operation_id is not None:
            self.operation_id = operation_id
        if operation_data is not None:
            self.operation_data = operation_data
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if created_by is not None:
            self.created_by = created_by
        if created is not None:
            self.created = created
        if start_date is not None:
            self.start_date = start_date

    @property
    def operation_id(self):
        """Gets the operation_id of this Operation.  # noqa: E501


        :return: The operation_id of this Operation.  # noqa: E501
        :rtype: int
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        """Sets the operation_id of this Operation.


        :param operation_id: The operation_id of this Operation.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                operation_id is not None and operation_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `operation_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._operation_id = operation_id

    @property
    def operation_data(self):
        """Gets the operation_data of this Operation.  # noqa: E501


        :return: The operation_data of this Operation.  # noqa: E501
        :rtype: OperationOperationData
        """
        return self._operation_data

    @operation_data.setter
    def operation_data(self, operation_data):
        """Sets the operation_data of this Operation.


        :param operation_data: The operation_data of this Operation.  # noqa: E501
        :type: OperationOperationData
        """

        self._operation_data = operation_data

    @property
    def type(self):
        """Gets the type of this Operation.  # noqa: E501

        Type of operation  # noqa: E501

        :return: The type of this Operation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Operation.

        Type of operation  # noqa: E501

        :param type: The type of this Operation.  # noqa: E501
        :type: str
        """
        allowed_values = ["import_contacts", "export_contacts", "export_reports", "advanced_report", "email", "sms", "smart_sms", "voice", "push", "webpush", "ads", "segment_generation", "mass_operation", "unify"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def status(self):
        """Gets the status of this Operation.  # noqa: E501

        State of the operation  # noqa: E501

        :return: The status of this Operation.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Operation.

        State of the operation  # noqa: E501

        :param status: The status of this Operation.  # noqa: E501
        :type: str
        """
        allowed_values = ["queued", "processing", "executing", "paused"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created_by(self):
        """Gets the created_by of this Operation.  # noqa: E501


        :return: The created_by of this Operation.  # noqa: E501
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Operation.


        :param created_by: The created_by of this Operation.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                created_by is not None and created_by < 1):  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must be a value greater than or equal to `1`")  # noqa: E501

        self._created_by = created_by

    @property
    def created(self):
        """Gets the created of this Operation.  # noqa: E501


        :return: The created of this Operation.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Operation.


        :param created: The created of this Operation.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def start_date(self):
        """Gets the start_date of this Operation.  # noqa: E501


        :return: The start_date of this Operation.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Operation.


        :param start_date: The start_date of this Operation.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

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
        if not isinstance(other, Operation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Operation):
            return True

        return self.to_dict() != other.to_dict()
