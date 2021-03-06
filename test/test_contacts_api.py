# coding: utf-8

"""
    APIv3 (New)

     # Introduction This is our new version of API. We invite you to start using it and give us your feedback # Getting Started  E-goi can be integrated with many environments and programming languages via our REST API. We've created a developer focused portal to give your organization a clear and quick overview of how to integrate with E-goi. The developer portal focuses on scenarios for integration and flow of events. We recommend familiarizing yourself with all of the content in the developer portal, before start using our rest API.   The E-goi  APIv3 is served over HTTPS. To ensure data privacy, unencrypted HTTP is not supported.  Request data is passed to the API by POSTing JSON objects to the API endpoints with the appropriate parameters.   BaseURL = api.egoiapp.com  # RESTful Services This API supports 5 HTTP methods:  * <b>GET</b>: The HTTP GET method is used to **read** (or retrieve) a representation of a resource. * <b>POST</b>: The POST verb is most-often utilized to **create** new resources. * <b>PATCH</b>: PATCH is used for **modify** capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource * <b>PUT</b>: PUT is most-often utilized for **update** capabilities, PUT-ing to a known resource URI with the request body containing the newly-updated representation of the original resource. * <b>DELETE</b>: DELETE is pretty easy to understand. It is used to **delete** a resource identified by a URI.  # Authentication   We use a custom authentication method, you will need a apikey that you can find in your account settings. Below you will see a curl example to get your account information:  #!/bin/bash  curl -X GET 'https://api.egoiapp.com/my-account' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>'  Here you can see a curl Post example with authentication:  #!/bin/bash  curl -X POST 'http://api.egoiapp.com/tags' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>' \\  -H 'Content-Type: application/json' \\  -d '{`name`:`Your custom tag`,`color`:`#FFFFFF`}'  # SDK Get started quickly with E-goi with our integration tools. Our SDK is a modern open source library that makes it easy to integrate your application with E-goi services.  * <a href='https://github.com/E-goi/sdk-java'>Java</a>  * <a href='https://github.com/E-goi/sdk-php'>PHP</a>  * <a href='https://github.com/E-goi/sdk-python'>Python</a>  * <a href='https://github.com/E-goi/sdk-ruby'>Ruby</a>  * <a href='https://github.com/E-goi/sdk-javascript'>Javascript</a>  * <a href='https://github.com/E-goi/sdk-csharp'>C#</a>  # Stream Limits Stream limits are security mesures we have to make sure our API have a fair use policy, for this reason, any request that creates or modifies data (**POST**, **PATCH** and **PUT**) is limited to a maximum of **20MB** of content length. If you arrive to this limit in one of your request, you'll receive a HTTP code **413 (Request Entity Too Large)** and the request will be ignored. To avoid this error in importation's requests, it's advised the request's division in batches that have each one less than 20MB.  # Timeouts Timeouts set a maximum waiting time on a request's response. Our API, sets a default timeout for each request and when breached, you'll receive an HTTP **408 (Request Timeout)** error code. You should take into consideration that response times can vary widely based on the complexity of the request, amount of data being analyzed, and the load on the system and workspace at the time of the query. When dealing with such errors, you should first attempt to reduce the complexity and amount of data under analysis, and only then, if problems are still occurring ask for support.  For all these reasons, the default timeout for each request is **10 Seconds** and any request that creates or modifies data (**POST**, **PATCH** and **PUT**) will have a timeout of **60 Seconds**. Specific timeouts may exist for specific requests, these can be found in the request's documentation.  <security-definitions/>  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import egoi_api
from egoi_api.api.contacts_api import ContactsApi  # noqa: E501
from egoi_api.rest import ApiException


class TestContactsApi(unittest.TestCase):
    """ContactsApi unit test stubs"""

    def setUp(self):
        self.api = egoi_api.api.contacts_api.ContactsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_action_activate_contacts(self):
        """Test case for action_activate_contacts

        Activate contacts  # noqa: E501
        """
        pass

    def test_action_attach_tag(self):
        """Test case for action_attach_tag

        Attach tag to contact  # noqa: E501
        """
        pass

    def test_action_deactivate_contacts(self):
        """Test case for action_deactivate_contacts

        Deactivate contacts  # noqa: E501
        """
        pass

    def test_action_detach_tag(self):
        """Test case for action_detach_tag

        Detach tag to contact  # noqa: E501
        """
        pass

    def test_action_export_contacts(self):
        """Test case for action_export_contacts

        Exports a list of contacts  # noqa: E501
        """
        pass

    def test_action_forget_contacts(self):
        """Test case for action_forget_contacts

        Forget contacts  # noqa: E501
        """
        pass

    def test_action_import_bulk(self):
        """Test case for action_import_bulk

        Import collection of contacts  # noqa: E501
        """
        pass

    def test_action_start_automation(self):
        """Test case for action_start_automation

        Start automation  # noqa: E501
        """
        pass

    def test_action_unsubscribe_contact(self):
        """Test case for action_unsubscribe_contact

        Unsubscribes contacts  # noqa: E501
        """
        pass

    def test_create_contact(self):
        """Test case for create_contact

        Create new contact  # noqa: E501
        """
        pass

    def test_get_all_contact_activities(self):
        """Test case for get_all_contact_activities

        Get all contact activities  # noqa: E501
        """
        pass

    def test_get_all_contacts(self):
        """Test case for get_all_contacts

        Get all contacts  # noqa: E501
        """
        pass

    def test_get_all_contacts_by_segment(self):
        """Test case for get_all_contacts_by_segment

        Get all contacts by Segment Id  # noqa: E501
        """
        pass

    def test_get_contact(self):
        """Test case for get_contact

        Get contact  # noqa: E501
        """
        pass

    def test_patch_contact(self):
        """Test case for patch_contact

        Update a specific contact  # noqa: E501
        """
        pass

    def test_search_contacts(self):
        """Test case for search_contacts

        Search contact  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
