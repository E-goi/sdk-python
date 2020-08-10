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


class ContactInsideBaseBulk(object):
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
        'contact_id': 'str',
        'status': 'str',
        'consent': 'str',
        'consent_date': 'datetime',
        'subscription_method': 'str',
        'subscription_date': 'datetime',
        'subscription_form': 'int',
        'unsubscription_method': 'str',
        'unsubscription_reason': 'str',
        'unsubscription_observation': 'str',
        'unsubscription_date': 'datetime',
        'change_date': 'date',
        'first_name': 'str',
        'last_name': 'str',
        'birth_date': 'date',
        'language': 'Language',
        'email': 'str',
        'email_status': 'str',
        'cellphone': 'str',
        'cellphone_status': 'str',
        'phone': 'str',
        'phone_status': 'str',
        'push_token_android': 'list[ContactBaseWithStatusFieldsSchemaBasePushTokenAndroid]',
        'push_token_ios': 'list[ContactBaseWithStatusFieldsSchemaBasePushTokenIos]'
    }

    attribute_map = {
        'contact_id': 'contact_id',
        'status': 'status',
        'consent': 'consent',
        'consent_date': 'consent_date',
        'subscription_method': 'subscription_method',
        'subscription_date': 'subscription_date',
        'subscription_form': 'subscription_form',
        'unsubscription_method': 'unsubscription_method',
        'unsubscription_reason': 'unsubscription_reason',
        'unsubscription_observation': 'unsubscription_observation',
        'unsubscription_date': 'unsubscription_date',
        'change_date': 'change_date',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'birth_date': 'birth_date',
        'language': 'language',
        'email': 'email',
        'email_status': 'email_status',
        'cellphone': 'cellphone',
        'cellphone_status': 'cellphone_status',
        'phone': 'phone',
        'phone_status': 'phone_status',
        'push_token_android': 'push_token_android',
        'push_token_ios': 'push_token_ios'
    }

    def __init__(self, contact_id=None, status='active', consent='consent', consent_date=None, subscription_method=None, subscription_date=None, subscription_form=None, unsubscription_method=None, unsubscription_reason=None, unsubscription_observation=None, unsubscription_date=None, change_date=None, first_name=None, last_name=None, birth_date=None, language=None, email=None, email_status='active', cellphone=None, cellphone_status='active', phone=None, phone_status='active', push_token_android=None, push_token_ios=None, local_vars_configuration=None):  # noqa: E501
        """ContactInsideBaseBulk - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._contact_id = None
        self._status = None
        self._consent = None
        self._consent_date = None
        self._subscription_method = None
        self._subscription_date = None
        self._subscription_form = None
        self._unsubscription_method = None
        self._unsubscription_reason = None
        self._unsubscription_observation = None
        self._unsubscription_date = None
        self._change_date = None
        self._first_name = None
        self._last_name = None
        self._birth_date = None
        self._language = None
        self._email = None
        self._email_status = None
        self._cellphone = None
        self._cellphone_status = None
        self._phone = None
        self._phone_status = None
        self._push_token_android = None
        self._push_token_ios = None
        self.discriminator = None

        if contact_id is not None:
            self.contact_id = contact_id
        if status is not None:
            self.status = status
        if consent is not None:
            self.consent = consent
        if consent_date is not None:
            self.consent_date = consent_date
        if subscription_method is not None:
            self.subscription_method = subscription_method
        if subscription_date is not None:
            self.subscription_date = subscription_date
        if subscription_form is not None:
            self.subscription_form = subscription_form
        if unsubscription_method is not None:
            self.unsubscription_method = unsubscription_method
        if unsubscription_reason is not None:
            self.unsubscription_reason = unsubscription_reason
        if unsubscription_observation is not None:
            self.unsubscription_observation = unsubscription_observation
        if unsubscription_date is not None:
            self.unsubscription_date = unsubscription_date
        if change_date is not None:
            self.change_date = change_date
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if birth_date is not None:
            self.birth_date = birth_date
        if language is not None:
            self.language = language
        if email is not None:
            self.email = email
        if email_status is not None:
            self.email_status = email_status
        if cellphone is not None:
            self.cellphone = cellphone
        if cellphone_status is not None:
            self.cellphone_status = cellphone_status
        if phone is not None:
            self.phone = phone
        if phone_status is not None:
            self.phone_status = phone_status
        if push_token_android is not None:
            self.push_token_android = push_token_android
        if push_token_ios is not None:
            self.push_token_ios = push_token_ios

    @property
    def contact_id(self):
        """Gets the contact_id of this ContactInsideBaseBulk.  # noqa: E501


        :return: The contact_id of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this ContactInsideBaseBulk.


        :param contact_id: The contact_id of this ContactInsideBaseBulk.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                contact_id is not None and not re.search(r'[a-fA-F\d]{10}', contact_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `contact_id`, must be a follow pattern or equal to `/[a-fA-F\d]{10}/`")  # noqa: E501

        self._contact_id = contact_id

    @property
    def status(self):
        """Gets the status of this ContactInsideBaseBulk.  # noqa: E501

        Status of the contact  # noqa: E501

        :return: The status of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ContactInsideBaseBulk.

        Status of the contact  # noqa: E501

        :param status: The status of this ContactInsideBaseBulk.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "inactive", "removed", "unconfirmed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def consent(self):
        """Gets the consent of this ContactInsideBaseBulk.  # noqa: E501

        Contact consent  # noqa: E501

        :return: The consent of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: str
        """
        return self._consent

    @consent.setter
    def consent(self, consent):
        """Sets the consent of this ContactInsideBaseBulk.

        Contact consent  # noqa: E501

        :param consent: The consent of this ContactInsideBaseBulk.  # noqa: E501
        :type: str
        """
        allowed_values = ["any", "consent", "contract", "legitimate_interest", "none", "protect_vital_interests", "public_interests", "required_by_law", "withdrawn"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and consent not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `consent` ({0}), must be one of {1}"  # noqa: E501
                .format(consent, allowed_values)
            )

        self._consent = consent

    @property
    def consent_date(self):
        """Gets the consent_date of this ContactInsideBaseBulk.  # noqa: E501

        Date and hour of the contact consent  # noqa: E501

        :return: The consent_date of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: datetime
        """
        return self._consent_date

    @consent_date.setter
    def consent_date(self, consent_date):
        """Sets the consent_date of this ContactInsideBaseBulk.

        Date and hour of the contact consent  # noqa: E501

        :param consent_date: The consent_date of this ContactInsideBaseBulk.  # noqa: E501
        :type: datetime
        """

        self._consent_date = consent_date

    @property
    def subscription_method(self):
        """Gets the subscription_method of this ContactInsideBaseBulk.  # noqa: E501

        Contact subscription method  # noqa: E501

        :return: The subscription_method of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: str
        """
        return self._subscription_method

    @subscription_method.setter
    def subscription_method(self, subscription_method):
        """Sets the subscription_method of this ContactInsideBaseBulk.

        Contact subscription method  # noqa: E501

        :param subscription_method: The subscription_method of this ContactInsideBaseBulk.  # noqa: E501
        :type: str
        """
        allowed_values = ["manual", "form", "imported", "referral", "api"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and subscription_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `subscription_method` ({0}), must be one of {1}"  # noqa: E501
                .format(subscription_method, allowed_values)
            )

        self._subscription_method = subscription_method

    @property
    def subscription_date(self):
        """Gets the subscription_date of this ContactInsideBaseBulk.  # noqa: E501

        Date and hour of the contact subscription  # noqa: E501

        :return: The subscription_date of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: datetime
        """
        return self._subscription_date

    @subscription_date.setter
    def subscription_date(self, subscription_date):
        """Sets the subscription_date of this ContactInsideBaseBulk.

        Date and hour of the contact subscription  # noqa: E501

        :param subscription_date: The subscription_date of this ContactInsideBaseBulk.  # noqa: E501
        :type: datetime
        """

        self._subscription_date = subscription_date

    @property
    def subscription_form(self):
        """Gets the subscription_form of this ContactInsideBaseBulk.  # noqa: E501

        Contact subscription form  # noqa: E501

        :return: The subscription_form of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: int
        """
        return self._subscription_form

    @subscription_form.setter
    def subscription_form(self, subscription_form):
        """Sets the subscription_form of this ContactInsideBaseBulk.

        Contact subscription form  # noqa: E501

        :param subscription_form: The subscription_form of this ContactInsideBaseBulk.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                subscription_form is not None and subscription_form < 0):  # noqa: E501
            raise ValueError("Invalid value for `subscription_form`, must be a value greater than or equal to `0`")  # noqa: E501

        self._subscription_form = subscription_form

    @property
    def unsubscription_method(self):
        """Gets the unsubscription_method of this ContactInsideBaseBulk.  # noqa: E501

        Contact unsubscription method  # noqa: E501

        :return: The unsubscription_method of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: str
        """
        return self._unsubscription_method

    @unsubscription_method.setter
    def unsubscription_method(self, unsubscription_method):
        """Sets the unsubscription_method of this ContactInsideBaseBulk.

        Contact unsubscription method  # noqa: E501

        :param unsubscription_method: The unsubscription_method of this ContactInsideBaseBulk.  # noqa: E501
        :type: str
        """
        allowed_values = ["manual", "form", "unsubscribe_link", "bounce", "api", ""]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and unsubscription_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `unsubscription_method` ({0}), must be one of {1}"  # noqa: E501
                .format(unsubscription_method, allowed_values)
            )

        self._unsubscription_method = unsubscription_method

    @property
    def unsubscription_reason(self):
        """Gets the unsubscription_reason of this ContactInsideBaseBulk.  # noqa: E501

        Contact unsubscription reason  # noqa: E501

        :return: The unsubscription_reason of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: str
        """
        return self._unsubscription_reason

    @unsubscription_reason.setter
    def unsubscription_reason(self, unsubscription_reason):
        """Sets the unsubscription_reason of this ContactInsideBaseBulk.

        Contact unsubscription reason  # noqa: E501

        :param unsubscription_reason: The unsubscription_reason of this ContactInsideBaseBulk.  # noqa: E501
        :type: str
        """
        allowed_values = ["not_interested", "lack_of_time", "email_address_change", "spam", "other", ""]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and unsubscription_reason not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `unsubscription_reason` ({0}), must be one of {1}"  # noqa: E501
                .format(unsubscription_reason, allowed_values)
            )

        self._unsubscription_reason = unsubscription_reason

    @property
    def unsubscription_observation(self):
        """Gets the unsubscription_observation of this ContactInsideBaseBulk.  # noqa: E501

        Contact unsubscription observation  # noqa: E501

        :return: The unsubscription_observation of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: str
        """
        return self._unsubscription_observation

    @unsubscription_observation.setter
    def unsubscription_observation(self, unsubscription_observation):
        """Sets the unsubscription_observation of this ContactInsideBaseBulk.

        Contact unsubscription observation  # noqa: E501

        :param unsubscription_observation: The unsubscription_observation of this ContactInsideBaseBulk.  # noqa: E501
        :type: str
        """

        self._unsubscription_observation = unsubscription_observation

    @property
    def unsubscription_date(self):
        """Gets the unsubscription_date of this ContactInsideBaseBulk.  # noqa: E501

        Contact unsubscription date  # noqa: E501

        :return: The unsubscription_date of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: datetime
        """
        return self._unsubscription_date

    @unsubscription_date.setter
    def unsubscription_date(self, unsubscription_date):
        """Sets the unsubscription_date of this ContactInsideBaseBulk.

        Contact unsubscription date  # noqa: E501

        :param unsubscription_date: The unsubscription_date of this ContactInsideBaseBulk.  # noqa: E501
        :type: datetime
        """

        self._unsubscription_date = unsubscription_date

    @property
    def change_date(self):
        """Gets the change_date of this ContactInsideBaseBulk.  # noqa: E501

        Last modification date of the contact  # noqa: E501

        :return: The change_date of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: date
        """
        return self._change_date

    @change_date.setter
    def change_date(self, change_date):
        """Sets the change_date of this ContactInsideBaseBulk.

        Last modification date of the contact  # noqa: E501

        :param change_date: The change_date of this ContactInsideBaseBulk.  # noqa: E501
        :type: date
        """

        self._change_date = change_date

    @property
    def first_name(self):
        """Gets the first_name of this ContactInsideBaseBulk.  # noqa: E501

        First name of the contact  # noqa: E501

        :return: The first_name of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ContactInsideBaseBulk.

        First name of the contact  # noqa: E501

        :param first_name: The first_name of this ContactInsideBaseBulk.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this ContactInsideBaseBulk.  # noqa: E501

        Last name of the contact  # noqa: E501

        :return: The last_name of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ContactInsideBaseBulk.

        Last name of the contact  # noqa: E501

        :param last_name: The last_name of this ContactInsideBaseBulk.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def birth_date(self):
        """Gets the birth_date of this ContactInsideBaseBulk.  # noqa: E501

        Birth date of the contact  # noqa: E501

        :return: The birth_date of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: date
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this ContactInsideBaseBulk.

        Birth date of the contact  # noqa: E501

        :param birth_date: The birth_date of this ContactInsideBaseBulk.  # noqa: E501
        :type: date
        """

        self._birth_date = birth_date

    @property
    def language(self):
        """Gets the language of this ContactInsideBaseBulk.  # noqa: E501


        :return: The language of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: Language
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ContactInsideBaseBulk.


        :param language: The language of this ContactInsideBaseBulk.  # noqa: E501
        :type: Language
        """

        self._language = language

    @property
    def email(self):
        """Gets the email of this ContactInsideBaseBulk.  # noqa: E501

        Email of the contact  # noqa: E501

        :return: The email of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ContactInsideBaseBulk.

        Email of the contact  # noqa: E501

        :param email: The email of this ContactInsideBaseBulk.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def email_status(self):
        """Gets the email_status of this ContactInsideBaseBulk.  # noqa: E501

        Email channel status  # noqa: E501

        :return: The email_status of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: str
        """
        return self._email_status

    @email_status.setter
    def email_status(self, email_status):
        """Sets the email_status of this ContactInsideBaseBulk.

        Email channel status  # noqa: E501

        :param email_status: The email_status of this ContactInsideBaseBulk.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "inactive"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and email_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `email_status` ({0}), must be one of {1}"  # noqa: E501
                .format(email_status, allowed_values)
            )

        self._email_status = email_status

    @property
    def cellphone(self):
        """Gets the cellphone of this ContactInsideBaseBulk.  # noqa: E501

        Cellphone of the contact  # noqa: E501

        :return: The cellphone of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: str
        """
        return self._cellphone

    @cellphone.setter
    def cellphone(self, cellphone):
        """Sets the cellphone of this ContactInsideBaseBulk.

        Cellphone of the contact  # noqa: E501

        :param cellphone: The cellphone of this ContactInsideBaseBulk.  # noqa: E501
        :type: str
        """

        self._cellphone = cellphone

    @property
    def cellphone_status(self):
        """Gets the cellphone_status of this ContactInsideBaseBulk.  # noqa: E501

        Cellphone channel status  # noqa: E501

        :return: The cellphone_status of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: str
        """
        return self._cellphone_status

    @cellphone_status.setter
    def cellphone_status(self, cellphone_status):
        """Sets the cellphone_status of this ContactInsideBaseBulk.

        Cellphone channel status  # noqa: E501

        :param cellphone_status: The cellphone_status of this ContactInsideBaseBulk.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "inactive"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and cellphone_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `cellphone_status` ({0}), must be one of {1}"  # noqa: E501
                .format(cellphone_status, allowed_values)
            )

        self._cellphone_status = cellphone_status

    @property
    def phone(self):
        """Gets the phone of this ContactInsideBaseBulk.  # noqa: E501

        Phone of the contact  # noqa: E501

        :return: The phone of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ContactInsideBaseBulk.

        Phone of the contact  # noqa: E501

        :param phone: The phone of this ContactInsideBaseBulk.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def phone_status(self):
        """Gets the phone_status of this ContactInsideBaseBulk.  # noqa: E501

        Phone channel status  # noqa: E501

        :return: The phone_status of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: str
        """
        return self._phone_status

    @phone_status.setter
    def phone_status(self, phone_status):
        """Sets the phone_status of this ContactInsideBaseBulk.

        Phone channel status  # noqa: E501

        :param phone_status: The phone_status of this ContactInsideBaseBulk.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "inactive"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and phone_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `phone_status` ({0}), must be one of {1}"  # noqa: E501
                .format(phone_status, allowed_values)
            )

        self._phone_status = phone_status

    @property
    def push_token_android(self):
        """Gets the push_token_android of this ContactInsideBaseBulk.  # noqa: E501

        Android push token of the contact  # noqa: E501

        :return: The push_token_android of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: list[ContactBaseWithStatusFieldsSchemaBasePushTokenAndroid]
        """
        return self._push_token_android

    @push_token_android.setter
    def push_token_android(self, push_token_android):
        """Sets the push_token_android of this ContactInsideBaseBulk.

        Android push token of the contact  # noqa: E501

        :param push_token_android: The push_token_android of this ContactInsideBaseBulk.  # noqa: E501
        :type: list[ContactBaseWithStatusFieldsSchemaBasePushTokenAndroid]
        """

        self._push_token_android = push_token_android

    @property
    def push_token_ios(self):
        """Gets the push_token_ios of this ContactInsideBaseBulk.  # noqa: E501

        IOS push token of the contact  # noqa: E501

        :return: The push_token_ios of this ContactInsideBaseBulk.  # noqa: E501
        :rtype: list[ContactBaseWithStatusFieldsSchemaBasePushTokenIos]
        """
        return self._push_token_ios

    @push_token_ios.setter
    def push_token_ios(self, push_token_ios):
        """Sets the push_token_ios of this ContactInsideBaseBulk.

        IOS push token of the contact  # noqa: E501

        :param push_token_ios: The push_token_ios of this ContactInsideBaseBulk.  # noqa: E501
        :type: list[ContactBaseWithStatusFieldsSchemaBasePushTokenIos]
        """

        self._push_token_ios = push_token_ios

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
        if not isinstance(other, ContactInsideBaseBulk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContactInsideBaseBulk):
            return True

        return self.to_dict() != other.to_dict()
