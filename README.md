![E-goi](https://www.e-goi.com/wp-content/themes/egoi2019/imgs/svg/logo-egoi.svg)

Almost anything you can do in E-goi, you can do with our API.

The API describes each available method. Learn about parameters, errors, and how to format your requests. That means you can easily call on E-goi actions for your integration.
**API** Full documentation at https://developers.e-goi.com/api/v3/

If you find a bug or something worth fixing, create an issue.

### Changelog
#### 1.1.2RC1
## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/E-goi/sdk-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/E-goi/sdk-python.git`)

Then import the package:
```python
import egoi_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import egoi_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import egoi_api
from pprint import pprint
from egoi_api.apis.tags import advanced_reports_api
from egoi_api.model.accepted_response import AcceptedResponse
from egoi_api.model.advanced_report import AdvancedReport
from egoi_api.model.bad_request import BadRequest
from egoi_api.model.forbidden import Forbidden
from egoi_api.model.generate_email_bounces_report import GenerateEmailBouncesReport
from egoi_api.model.generate_email_clicks_by_contact_report import GenerateEmailClicksByContactReport
from egoi_api.model.generate_email_clicks_by_url_report import GenerateEmailClicksByUrlReport
from egoi_api.model.generate_email_events_report import GenerateEmailEventsReport
from egoi_api.model.generate_email_unsubscriptions_report import GenerateEmailUnsubscriptionsReport
from egoi_api.model.generate_form_answers_report import GenerateFormAnswersReport
from egoi_api.model.generate_sends_report import GenerateSendsReport
from egoi_api.model.generate_sms_bounces_report import GenerateSmsBouncesReport
from egoi_api.model.generate_sms_events_report import GenerateSmsEventsReport
from egoi_api.model.generate_subscriptions_report import GenerateSubscriptionsReport
from egoi_api.model.generate_unsubscriptions_report import GenerateUnsubscriptionsReport
from egoi_api.model.internal_server_error import InternalServerError
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.too_many_requests import TooManyRequests
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.unprocessable_entity import UnprocessableEntity
## Documentation for API Endpoints

All URIs are relative to *https://api.egoiapp.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdvancedReportsApi* | [**generate_email_bounces_report**](docs/apis/tags/AdvancedReportsApi.md#generate_email_bounces_report) | **post** /reports/advanced/email-bounces | Generate email bounces report
*AdvancedReportsApi* | [**generate_email_clicks_by_contact_report**](docs/apis/tags/AdvancedReportsApi.md#generate_email_clicks_by_contact_report) | **post** /reports/advanced/email-clicks-by-contact | Generate email clicks by contact report
*AdvancedReportsApi* | [**generate_email_clicks_by_url_report**](docs/apis/tags/AdvancedReportsApi.md#generate_email_clicks_by_url_report) | **post** /reports/advanced/email-clicks-by-url | Generate email clicks by URL report
*AdvancedReportsApi* | [**generate_email_events_report**](docs/apis/tags/AdvancedReportsApi.md#generate_email_events_report) | **post** /reports/advanced/email-events | Generate email events report
*AdvancedReportsApi* | [**generate_email_sms_report**](docs/apis/tags/AdvancedReportsApi.md#generate_email_sms_report) | **post** /reports/advanced/sms-bounces | Generate SMS bounces report
*AdvancedReportsApi* | [**generate_email_unsubscriptions_report**](docs/apis/tags/AdvancedReportsApi.md#generate_email_unsubscriptions_report) | **post** /reports/advanced/email-unsubscriptions | Generate email unsubscriptions report
*AdvancedReportsApi* | [**generate_form_answers_report**](docs/apis/tags/AdvancedReportsApi.md#generate_form_answers_report) | **post** /reports/advanced/form-answers | Generate form answers report
*AdvancedReportsApi* | [**generate_sends_report**](docs/apis/tags/AdvancedReportsApi.md#generate_sends_report) | **post** /reports/advanced/sends | Generate sends report
*AdvancedReportsApi* | [**generate_sms_events_report**](docs/apis/tags/AdvancedReportsApi.md#generate_sms_events_report) | **post** /reports/advanced/sms-events | Generate SMS events report
*AdvancedReportsApi* | [**generate_subscriptions_report**](docs/apis/tags/AdvancedReportsApi.md#generate_subscriptions_report) | **post** /reports/advanced/subscriptions | Generate subscriptions report
*AdvancedReportsApi* | [**generate_unsubscriptions_report**](docs/apis/tags/AdvancedReportsApi.md#generate_unsubscriptions_report) | **post** /reports/advanced/unsubscriptions | Generate unsubscriptions report
*AdvancedReportsApi* | [**get_all_advanced_reports**](docs/apis/tags/AdvancedReportsApi.md#get_all_advanced_reports) | **get** /reports/advanced | Get all advanced reports
*AutomationsApi* | [**delete_automation**](docs/apis/tags/AutomationsApi.md#delete_automation) | **delete** /automations/{automation_id} | Remove automation
*AutomationsApi* | [**get_all_automations**](docs/apis/tags/AutomationsApi.md#get_all_automations) | **get** /automations | Get all automations
*CNamesApi* | [**create_c_name**](docs/apis/tags/CNamesApi.md#create_c_name) | **post** /cnames | Create cname
*CNamesApi* | [**get_all_c_names**](docs/apis/tags/CNamesApi.md#get_all_c_names) | **get** /cnames | Get All CNames
*CampaignGroupsApi* | [**create_campaign_group**](docs/apis/tags/CampaignGroupsApi.md#create_campaign_group) | **post** /campaign-groups | Create new campaign group
*CampaignGroupsApi* | [**delete_campaign_group**](docs/apis/tags/CampaignGroupsApi.md#delete_campaign_group) | **delete** /campaign-groups/{group_id} | Remove Campaign Group
*CampaignGroupsApi* | [**get_all_campaign_groups**](docs/apis/tags/CampaignGroupsApi.md#get_all_campaign_groups) | **get** /campaign-groups | Get all campaign groups
*CampaignGroupsApi* | [**update_campaign_group**](docs/apis/tags/CampaignGroupsApi.md#update_campaign_group) | **put** /campaign-groups/{group_id} | Update a specific campaign group
*CampaignsApi* | [**delete_campaigns**](docs/apis/tags/CampaignsApi.md#delete_campaigns) | **delete** /campaigns/{campaign_hash} | Remove Campaign
*CampaignsApi* | [**get_all_campaigns**](docs/apis/tags/CampaignsApi.md#get_all_campaigns) | **get** /campaigns | Get all Campaigns
*ConnectedSitesApi* | [**create_connected_sites**](docs/apis/tags/ConnectedSitesApi.md#create_connected_sites) | **post** /connectedsites | Creates a Connected Site
*ConnectedSitesApi* | [**delete_connected_sites**](docs/apis/tags/ConnectedSitesApi.md#delete_connected_sites) | **delete** /connectedsites/{domain} | Deletes a Connected Site
*ConnectedSitesApi* | [**get_all_connected_sites**](docs/apis/tags/ConnectedSitesApi.md#get_all_connected_sites) | **get** /connectedsites | Get all Connected Sites
*ConnectedSitesApi* | [**get_connected_sites**](docs/apis/tags/ConnectedSitesApi.md#get_connected_sites) | **get** /connectedsites/{domain} | Get a Connected Site
*ContactsApi* | [**action_activate_contacts**](docs/apis/tags/ContactsApi.md#action_activate_contacts) | **post** /lists/{list_id}/contacts/actions/activate | Activate contacts
*ContactsApi* | [**action_attach_tag**](docs/apis/tags/ContactsApi.md#action_attach_tag) | **post** /lists/{list_id}/contacts/actions/attach-tag | Attach tag to contact
*ContactsApi* | [**action_deactivate_contacts**](docs/apis/tags/ContactsApi.md#action_deactivate_contacts) | **post** /lists/{list_id}/contacts/actions/deactivate | Deactivate contacts
*ContactsApi* | [**action_detach_tag**](docs/apis/tags/ContactsApi.md#action_detach_tag) | **post** /lists/{list_id}/contacts/actions/detach-tag | Detach tag to contact
*ContactsApi* | [**action_export_contacts**](docs/apis/tags/ContactsApi.md#action_export_contacts) | **post** /lists/{list_id}/contacts/actions/export | Exports a list of contacts
*ContactsApi* | [**action_forget_contacts**](docs/apis/tags/ContactsApi.md#action_forget_contacts) | **post** /lists/{list_id}/contacts/actions/forget | Forget contacts
*ContactsApi* | [**action_import_bulk**](docs/apis/tags/ContactsApi.md#action_import_bulk) | **post** /lists/{list_id}/contacts/actions/import-bulk | Import collection of contacts
*ContactsApi* | [**action_start_automation**](docs/apis/tags/ContactsApi.md#action_start_automation) | **post** /lists/{list_id}/contacts/actions/start-automation | Start automation
*ContactsApi* | [**action_unsubscribe_contact**](docs/apis/tags/ContactsApi.md#action_unsubscribe_contact) | **post** /lists/{list_id}/contacts/actions/unsubscribe | Unsubscribes contacts
*ContactsApi* | [**action_update_contacts**](docs/apis/tags/ContactsApi.md#action_update_contacts) | **post** /lists/{list_id}/contacts/actions/update | Updates contacts
*ContactsApi* | [**create_contact**](docs/apis/tags/ContactsApi.md#create_contact) | **post** /lists/{list_id}/contacts | Create new contact
*ContactsApi* | [**get_all_contact_activities**](docs/apis/tags/ContactsApi.md#get_all_contact_activities) | **get** /lists/{list_id}/contacts/{contact_id}/activities | Get all contact activities
*ContactsApi* | [**get_all_contacts**](docs/apis/tags/ContactsApi.md#get_all_contacts) | **get** /lists/{list_id}/contacts | Get all contacts
*ContactsApi* | [**get_all_contacts_by_segment**](docs/apis/tags/ContactsApi.md#get_all_contacts_by_segment) | **get** /lists/{list_id}/contacts/segment/{segment_id} | Get all contacts by Segment Id
*ContactsApi* | [**get_contact**](docs/apis/tags/ContactsApi.md#get_contact) | **get** /lists/{list_id}/contacts/{contact_id} | Get contact
*ContactsApi* | [**patch_contact**](docs/apis/tags/ContactsApi.md#patch_contact) | **patch** /lists/{list_id}/contacts/{contact_id} | Update a specific contact
*ContactsApi* | [**search_contacts**](docs/apis/tags/ContactsApi.md#search_contacts) | **get** /contacts/search | Search contact
*EcommerceApi* | [**create_cart**](docs/apis/tags/EcommerceApi.md#create_cart) | **post** /{domain}/carts | Create cart
*EcommerceApi* | [**create_catalog**](docs/apis/tags/EcommerceApi.md#create_catalog) | **post** /catalogs | Create new catalog
*EcommerceApi* | [**create_order**](docs/apis/tags/EcommerceApi.md#create_order) | **post** /{domain}/orders | Create order
*EcommerceApi* | [**create_product**](docs/apis/tags/EcommerceApi.md#create_product) | **post** /catalogs/{catalog_id}/products | Create new product
*EcommerceApi* | [**delete_catalog**](docs/apis/tags/EcommerceApi.md#delete_catalog) | **delete** /catalogs/{catalog_id} | Remove catalog
*EcommerceApi* | [**delete_product**](docs/apis/tags/EcommerceApi.md#delete_product) | **delete** /catalogs/{catalog_id}/products/{product_identifier} | Remove product
*EcommerceApi* | [**get_all_catalogs**](docs/apis/tags/EcommerceApi.md#get_all_catalogs) | **get** /catalogs | Get all catalogs
*EcommerceApi* | [**get_all_products**](docs/apis/tags/EcommerceApi.md#get_all_products) | **get** /catalogs/{catalog_id}/products | Get all products
*EcommerceApi* | [**get_product**](docs/apis/tags/EcommerceApi.md#get_product) | **get** /catalogs/{catalog_id}/products/{product_identifier} | Get product
*EcommerceApi* | [**import_products**](docs/apis/tags/EcommerceApi.md#import_products) | **post** /catalogs/{catalog_id}/products/actions/import | Import products
*EcommerceApi* | [**update_product**](docs/apis/tags/EcommerceApi.md#update_product) | **patch** /catalogs/{catalog_id}/products/{product_identifier} | Update product
*EcommerceActivityApi* | [**import_orders_bulk**](docs/apis/tags/EcommerceActivityApi.md#import_orders_bulk) | **post** /lists/{list_id}/orders | Orders import bulk request
*EmailApi* | [**action_enable_email_rss**](docs/apis/tags/EmailApi.md#action_enable_email_rss) | **post** /campaigns/email/rss/{campaign_hash}/actions/enable | Enables a rss email campaign
*EmailApi* | [**action_send_email**](docs/apis/tags/EmailApi.md#action_send_email) | **post** /campaigns/email/{campaign_hash}/actions/send | Send email message
*EmailApi* | [**create_email_campaign**](docs/apis/tags/EmailApi.md#create_email_campaign) | **post** /campaigns/email | Create new email campaign
*EmailApi* | [**create_email_rss_campaign**](docs/apis/tags/EmailApi.md#create_email_rss_campaign) | **post** /campaigns/email/rss | Create new email rss campaign
*EmailApi* | [**patch_email_campaign**](docs/apis/tags/EmailApi.md#patch_email_campaign) | **patch** /campaigns/email/{campaign_hash} | Update a specific email campaign
*FieldsApi* | [**create_extra_field**](docs/apis/tags/FieldsApi.md#create_extra_field) | **post** /lists/{list_id}/fields/extra | Create extra field
*FieldsApi* | [**create_field_option**](docs/apis/tags/FieldsApi.md#create_field_option) | **post** /lists/{list_id}/fields/extra/{field_id}/options | Create new field option
*FieldsApi* | [**delete_extra_field**](docs/apis/tags/FieldsApi.md#delete_extra_field) | **delete** /lists/{list_id}/fields/extra/{field_id} | Remove extra field
*FieldsApi* | [**delete_field_option**](docs/apis/tags/FieldsApi.md#delete_field_option) | **delete** /lists/{list_id}/fields/extra/{field_id}/options/{option_id} | Deletes an option
*FieldsApi* | [**get_all_field_options**](docs/apis/tags/FieldsApi.md#get_all_field_options) | **get** /lists/{list_id}/fields/extra/{field_id}/options | Get all field options
*FieldsApi* | [**get_all_fields**](docs/apis/tags/FieldsApi.md#get_all_fields) | **get** /lists/{list_id}/fields | Get all fields
*FieldsApi* | [**patch_base_field**](docs/apis/tags/FieldsApi.md#patch_base_field) | **patch** /lists/{list_id}/fields/base/{field_id} | Update base field
*FieldsApi* | [**patch_extra_field**](docs/apis/tags/FieldsApi.md#patch_extra_field) | **patch** /lists/{list_id}/fields/extra/{field_id} | Update extra field
*FieldsApi* | [**update_field_option**](docs/apis/tags/FieldsApi.md#update_field_option) | **patch** /lists/{list_id}/fields/extra/{field_id}/options/{option_id} | Update field option
*ListsApi* | [**create_list**](docs/apis/tags/ListsApi.md#create_list) | **post** /lists | Create new list
*ListsApi* | [**delete_list**](docs/apis/tags/ListsApi.md#delete_list) | **delete** /lists/{list_id} | Remove list
*ListsApi* | [**get_all_lists**](docs/apis/tags/ListsApi.md#get_all_lists) | **get** /lists | Get all lists
*ListsApi* | [**update_list**](docs/apis/tags/ListsApi.md#update_list) | **patch** /lists/{list_id} | Update a specific list
*MyAccountApi* | [**enable_te**](docs/apis/tags/MyAccountApi.md#enable_te) | **post** /my-account/actions/enable-te | Enable Track&amp;Engage
*MyAccountApi* | [**enable_transactional**](docs/apis/tags/MyAccountApi.md#enable_transactional) | **post** /my-account/actions/enable-transactional | Enable Transactional
*MyAccountApi* | [**get_my_account**](docs/apis/tags/MyAccountApi.md#get_my_account) | **get** /my-account | Get My Account Info
*OperationsApi* | [**action_approve_operation**](docs/apis/tags/OperationsApi.md#action_approve_operation) | **post** /operations/actions/approve | Approve operation
*OperationsApi* | [**action_cancel_operation**](docs/apis/tags/OperationsApi.md#action_cancel_operation) | **post** /operations/actions/cancel | Cancel operation
*OperationsApi* | [**action_pause_operation**](docs/apis/tags/OperationsApi.md#action_pause_operation) | **post** /operations/actions/pause | Pause operation
*OperationsApi* | [**action_resume_operation**](docs/apis/tags/OperationsApi.md#action_resume_operation) | **post** /operations/actions/resume | Resume operation
*OperationsApi* | [**get_all_operations**](docs/apis/tags/OperationsApi.md#get_all_operations) | **get** /operations | Get all queued operations
*PingApi* | [**ping**](docs/apis/tags/PingApi.md#ping) | **post** /ping | Pings the API
*PushApi* | [**action_send_push**](docs/apis/tags/PushApi.md#action_send_push) | **post** /campaigns/push/{campaign_hash}/actions/send | Send push message
*PushApi* | [**create_push_campaign**](docs/apis/tags/PushApi.md#create_push_campaign) | **post** /campaigns/push | Create new push campaign
*PushApi* | [**get_push_app**](docs/apis/tags/PushApi.md#get_push_app) | **get** /push/apps/{app_id} | Get a Push application from E-goi
*PushApi* | [**get_push_apps**](docs/apis/tags/PushApi.md#get_push_apps) | **get** /push/apps | Get all Push applications from E-goi
*PushApi* | [**patch_push_campaign**](docs/apis/tags/PushApi.md#patch_push_campaign) | **patch** /campaigns/push/{campaign_hash} | Update a specific push campaign
*PushApi* | [**register_push_event**](docs/apis/tags/PushApi.md#register_push_event) | **post** /push/apps/{app_id}/event | Registers an event from the push notification.
*PushApi* | [**register_push_token**](docs/apis/tags/PushApi.md#register_push_token) | **post** /push/apps/{app_id}/token | Registers a Firebase token
*ReportsApi* | [**get_email_report**](docs/apis/tags/ReportsApi.md#get_email_report) | **get** /reports/email/{campaign_hash} | Get email report
*ReportsApi* | [**get_sms_report**](docs/apis/tags/ReportsApi.md#get_sms_report) | **get** /reports/sms/{campaign_hash} | Get sms report
*ReportsApi* | [**get_voice_report**](docs/apis/tags/ReportsApi.md#get_voice_report) | **get** /reports/voice/{campaign_hash} | Get voice report
*ReportsApi* | [**get_web_push_report**](docs/apis/tags/ReportsApi.md#get_web_push_report) | **get** /reports/web-push/{campaign_hash} | Get webpush report
*SegmentsApi* | [**delete_segment**](docs/apis/tags/SegmentsApi.md#delete_segment) | **delete** /lists/{list_id}/segments/{segment_id} | Remove segment
*SegmentsApi* | [**get_all_segments**](docs/apis/tags/SegmentsApi.md#get_all_segments) | **get** /lists/{list_id}/segments | Get all segments
*SendersApi* | [**create_cellphone_sender**](docs/apis/tags/SendersApi.md#create_cellphone_sender) | **post** /senders/cellphone | Create cellphone sender
*SendersApi* | [**create_email_sender**](docs/apis/tags/SendersApi.md#create_email_sender) | **post** /senders/email | Create email sender
*SendersApi* | [**create_phone_sender**](docs/apis/tags/SendersApi.md#create_phone_sender) | **post** /senders/phone | Create phone sender
*SendersApi* | [**delete_cellphone_sender**](docs/apis/tags/SendersApi.md#delete_cellphone_sender) | **delete** /senders/cellphone/{sender_id} | Remove cellphone sender
*SendersApi* | [**delete_email_sender**](docs/apis/tags/SendersApi.md#delete_email_sender) | **delete** /senders/email/{sender_id} | Remove email sender
*SendersApi* | [**delete_phone_sender**](docs/apis/tags/SendersApi.md#delete_phone_sender) | **delete** /senders/phone/{sender_id} | Remove phone sender
*SendersApi* | [**get_all_cellphone_senders**](docs/apis/tags/SendersApi.md#get_all_cellphone_senders) | **get** /senders/cellphone | Get all cellphone senders
*SendersApi* | [**get_all_email_senders**](docs/apis/tags/SendersApi.md#get_all_email_senders) | **get** /senders/email | Get all email senders
*SendersApi* | [**get_all_phone_senders**](docs/apis/tags/SendersApi.md#get_all_phone_senders) | **get** /senders/phone | Get all phone senders
*SendersApi* | [**put_email_sender**](docs/apis/tags/SendersApi.md#put_email_sender) | **put** /senders/email/{sender_id} | Update email sender
*SmartSmsApi* | [**action_send_smart_sms**](docs/apis/tags/SmartSmsApi.md#action_send_smart_sms) | **post** /campaigns/smart-sms/{campaign_hash}/actions/send | Send smart sms message
*SmartSmsApi* | [**create_smart_sms_campaign**](docs/apis/tags/SmartSmsApi.md#create_smart_sms_campaign) | **post** /campaigns/smart-sms | Create new smart sms campaign
*SmartSmsApi* | [**patch_smart_sms_campaign**](docs/apis/tags/SmartSmsApi.md#patch_smart_sms_campaign) | **patch** /campaigns/smart-sms/{campaign_hash} | Update a specific smart sms campaign
*SmsApi* | [**action_send_sms**](docs/apis/tags/SmsApi.md#action_send_sms) | **post** /campaigns/sms/{campaign_hash}/actions/send | Send sms message
*SmsApi* | [**create_sms_campaign**](docs/apis/tags/SmsApi.md#create_sms_campaign) | **post** /campaigns/sms | Create new sms campaign
*SmsApi* | [**patch_sms_campaign**](docs/apis/tags/SmsApi.md#patch_sms_campaign) | **patch** /campaigns/sms/{campaign_hash} | Update a specific sms campaign
*SuppressionListApi* | [**create_suppression_list**](docs/apis/tags/SuppressionListApi.md#create_suppression_list) | **post** /suppression-list | Add to suppression list
*SuppressionListApi* | [**delete_suppression_list**](docs/apis/tags/SuppressionListApi.md#delete_suppression_list) | **delete** /suppression-list/{suppression_id} | Delete from suppression list
*SuppressionListApi* | [**get_all_suppression_list**](docs/apis/tags/SuppressionListApi.md#get_all_suppression_list) | **get** /suppression-list | Get the suppression list
*TagsApi* | [**create_tag**](docs/apis/tags/TagsApi.md#create_tag) | **post** /tags | Create new tag
*TagsApi* | [**delete_tag**](docs/apis/tags/TagsApi.md#delete_tag) | **delete** /tags/{tag_id} | Remove tag
*TagsApi* | [**get_all_tags**](docs/apis/tags/TagsApi.md#get_all_tags) | **get** /tags | Get all tags
*TagsApi* | [**update_tag**](docs/apis/tags/TagsApi.md#update_tag) | **put** /tags/{tag_id} | Update a specific tag
*TrackEngageApi* | [**get_all_domains**](docs/apis/tags/TrackEngageApi.md#get_all_domains) | **get** /trackengage/domains | Get all domains
*TrackEngageApi* | [**get_all_goals**](docs/apis/tags/TrackEngageApi.md#get_all_goals) | **get** /trackengage/goals | Get all goals
*UsersApi* | [**delete_user**](docs/apis/tags/UsersApi.md#delete_user) | **delete** /users/{user_id} | Remove user
*UsersApi* | [**get_all_users**](docs/apis/tags/UsersApi.md#get_all_users) | **get** /users | Get all users
*UtilitiesApi* | [**get_all_countries**](docs/apis/tags/UtilitiesApi.md#get_all_countries) | **get** /utilities/countries | Get all countries
*VoiceApi* | [**action_send_voice**](docs/apis/tags/VoiceApi.md#action_send_voice) | **post** /campaigns/voice/{campaign_hash}/actions/send | Send voice message
*VoiceApi* | [**create_voice_campaign**](docs/apis/tags/VoiceApi.md#create_voice_campaign) | **post** /campaigns/voice | Create new voice campaign
*VoiceApi* | [**patch_voice_campaign**](docs/apis/tags/VoiceApi.md#patch_voice_campaign) | **patch** /campaigns/voice/{campaign_hash} | Update a specific voice campaign
*WebHooksApi* | [**create_webhook**](docs/apis/tags/WebHooksApi.md#create_webhook) | **post** /webhooks | Create new webhook
*WebHooksApi* | [**delete_webhook**](docs/apis/tags/WebHooksApi.md#delete_webhook) | **delete** /webhooks/{webhook_id} | Remove webhook
*WebHooksApi* | [**get_all_webhooks**](docs/apis/tags/WebHooksApi.md#get_all_webhooks) | **get** /webhooks | Get all webhooks
*WebpushApi* | [**action_enable_web_push_rss**](docs/apis/tags/WebpushApi.md#action_enable_web_push_rss) | **post** /campaigns/webpush/rss/{campaign_hash}/actions/enable | Enable a rss webpush campaign
*WebpushApi* | [**action_send_web_push**](docs/apis/tags/WebpushApi.md#action_send_web_push) | **post** /campaigns/web-push/{campaign_hash}/actions/send | Send webpush message
*WebpushApi* | [**create_web_push_campaign**](docs/apis/tags/WebpushApi.md#create_web_push_campaign) | **post** /campaigns/web-push | Create new webpush campaign
*WebpushApi* | [**create_web_push_rss_campaign**](docs/apis/tags/WebpushApi.md#create_web_push_rss_campaign) | **post** /campaigns/webpush/rss | Create new webpush rss campaign
*WebpushApi* | [**create_webpush_site**](docs/apis/tags/WebpushApi.md#create_webpush_site) | **post** /webpush/sites | Creates a webpush site
*WebpushApi* | [**get_all_web_push_sites**](docs/apis/tags/WebpushApi.md#get_all_web_push_sites) | **get** /webpush/sites | Get all webpush sites
*WebpushApi* | [**patch_web_push_campaign**](docs/apis/tags/WebpushApi.md#patch_web_push_campaign) | **patch** /campaigns/web-push/{campaign_hash} | Update a specific webpush campaign

## Documentation For Models

 - [AbstractCampaignSendRequest](docs/models/AbstractCampaignSendRequest.md)
 - [AbstractCampaignTemplate](docs/models/AbstractCampaignTemplate.md)
 - [AbstractCellphoneSender](docs/models/AbstractCellphoneSender.md)
 - [AbstractSegment](docs/models/AbstractSegment.md)
 - [AbstractSendEmail](docs/models/AbstractSendEmail.md)
 - [AbstractSendVoice](docs/models/AbstractSendVoice.md)
 - [AbstractSuppresionList](docs/models/AbstractSuppresionList.md)
 - [AcceptedResponse](docs/models/AcceptedResponse.md)
 - [ActivateContactsAll](docs/models/ActivateContactsAll.md)
 - [ActivateContactsMany](docs/models/ActivateContactsMany.md)
 - [ActivateContactsRequest](docs/models/ActivateContactsRequest.md)
 - [AdvancedReport](docs/models/AdvancedReport.md)
 - [AdvancedReportCampaigns](docs/models/AdvancedReportCampaigns.md)
 - [AdvancedReportCampaignsObject](docs/models/AdvancedReportCampaignsObject.md)
 - [AdvancedReportEmailBouncesColumns](docs/models/AdvancedReportEmailBouncesColumns.md)
 - [AdvancedReportEmailBouncesOptions](docs/models/AdvancedReportEmailBouncesOptions.md)
 - [AdvancedReportEmailClicksByContactColumns](docs/models/AdvancedReportEmailClicksByContactColumns.md)
 - [AdvancedReportEmailClicksByContactOptions](docs/models/AdvancedReportEmailClicksByContactOptions.md)
 - [AdvancedReportEmailClicksByUrlColumns](docs/models/AdvancedReportEmailClicksByUrlColumns.md)
 - [AdvancedReportEmailClicksByUrlOptions](docs/models/AdvancedReportEmailClicksByUrlOptions.md)
 - [AdvancedReportEmailEventsColumns](docs/models/AdvancedReportEmailEventsColumns.md)
 - [AdvancedReportEmailEventsOptions](docs/models/AdvancedReportEmailEventsOptions.md)
 - [AdvancedReportEmailUnsubscriptionsColumns](docs/models/AdvancedReportEmailUnsubscriptionsColumns.md)
 - [AdvancedReportEmailUnsubscriptionsOptions](docs/models/AdvancedReportEmailUnsubscriptionsOptions.md)
 - [AdvancedReportForms](docs/models/AdvancedReportForms.md)
 - [AdvancedReportListExtraFields](docs/models/AdvancedReportListExtraFields.md)
 - [AdvancedReportRange](docs/models/AdvancedReportRange.md)
 - [AdvancedReportSendsColumns](docs/models/AdvancedReportSendsColumns.md)
 - [AdvancedReportSendsOptions](docs/models/AdvancedReportSendsOptions.md)
 - [AdvancedReportSmsBouncesColumns](docs/models/AdvancedReportSmsBouncesColumns.md)
 - [AdvancedReportSmsBouncesOptions](docs/models/AdvancedReportSmsBouncesOptions.md)
 - [AdvancedReportSmsEventsColumns](docs/models/AdvancedReportSmsEventsColumns.md)
 - [AdvancedReportSmsEventsOptions](docs/models/AdvancedReportSmsEventsOptions.md)
 - [AdvancedReportSubscriptionsColumns](docs/models/AdvancedReportSubscriptionsColumns.md)
 - [AdvancedReportSubscriptionsOptions](docs/models/AdvancedReportSubscriptionsOptions.md)
 - [AdvancedReportUnsubscriptionsColumns](docs/models/AdvancedReportUnsubscriptionsColumns.md)
 - [AdvancedReportUnsubscriptionsOptions](docs/models/AdvancedReportUnsubscriptionsOptions.md)
 - [AlphanumericCellphoneSender](docs/models/AlphanumericCellphoneSender.md)
 - [AlphanumericCellphoneSenderPost](docs/models/AlphanumericCellphoneSenderPost.md)
 - [AppStructure](docs/models/AppStructure.md)
 - [AttachTagRequest](docs/models/AttachTagRequest.md)
 - [AttachTagResponse](docs/models/AttachTagResponse.md)
 - [AutomaticSegment](docs/models/AutomaticSegment.md)
 - [Automation](docs/models/Automation.md)
 - [AutomationPost](docs/models/AutomationPost.md)
 - [BadRequest](docs/models/BadRequest.md)
 - [BalanceInfo](docs/models/BalanceInfo.md)
 - [BaseConflict](docs/models/BaseConflict.md)
 - [BasicProduct](docs/models/BasicProduct.md)
 - [BasicSender](docs/models/BasicSender.md)
 - [BillingInfo](docs/models/BillingInfo.md)
 - [BulkActionResponse](docs/models/BulkActionResponse.md)
 - [CName](docs/models/CName.md)
 - [CNamePost](docs/models/CNamePost.md)
 - [Campaign](docs/models/Campaign.md)
 - [CampaignEmailBaseContent](docs/models/CampaignEmailBaseContent.md)
 - [CampaignEmailContent](docs/models/CampaignEmailContent.md)
 - [CampaignEmailContentFile](docs/models/CampaignEmailContentFile.md)
 - [CampaignEmailContentHtml](docs/models/CampaignEmailContentHtml.md)
 - [CampaignEmailContentHtmlPatch](docs/models/CampaignEmailContentHtmlPatch.md)
 - [CampaignEmailContentTemplate](docs/models/CampaignEmailContentTemplate.md)
 - [CampaignEmailContentWebPage](docs/models/CampaignEmailContentWebPage.md)
 - [CampaignEmailRssContent](docs/models/CampaignEmailRssContent.md)
 - [CampaignEmailRssContentHtml](docs/models/CampaignEmailRssContentHtml.md)
 - [CampaignEmailScheduleRequest](docs/models/CampaignEmailScheduleRequest.md)
 - [CampaignEmailSendNowRequest](docs/models/CampaignEmailSendNowRequest.md)
 - [CampaignEmailSendRequest](docs/models/CampaignEmailSendRequest.md)
 - [CampaignGroup](docs/models/CampaignGroup.md)
 - [CampaignGroupPost](docs/models/CampaignGroupPost.md)
 - [CampaignPushContent](docs/models/CampaignPushContent.md)
 - [CampaignPushContentTemplate](docs/models/CampaignPushContentTemplate.md)
 - [CampaignPushContentText](docs/models/CampaignPushContentText.md)
 - [CampaignPushScheduleRequest](docs/models/CampaignPushScheduleRequest.md)
 - [CampaignPushSendRequest](docs/models/CampaignPushSendRequest.md)
 - [CampaignSentLast30Days](docs/models/CampaignSentLast30Days.md)
 - [CampaignSmartSmsHtml](docs/models/CampaignSmartSmsHtml.md)
 - [CampaignSmartSmsImport](docs/models/CampaignSmartSmsImport.md)
 - [CampaignSmartSmsOptions](docs/models/CampaignSmartSmsOptions.md)
 - [CampaignSmartSmsPageContent](docs/models/CampaignSmartSmsPageContent.md)
 - [CampaignSmartSmsRedirect](docs/models/CampaignSmartSmsRedirect.md)
 - [CampaignSmartSmsScheduleRequest](docs/models/CampaignSmartSmsScheduleRequest.md)
 - [CampaignSmartSmsSendRequest](docs/models/CampaignSmartSmsSendRequest.md)
 - [CampaignSmsContent](docs/models/CampaignSmsContent.md)
 - [CampaignSmsContentTemplate](docs/models/CampaignSmsContentTemplate.md)
 - [CampaignSmsContentText](docs/models/CampaignSmsContentText.md)
 - [CampaignSmsOptions](docs/models/CampaignSmsOptions.md)
 - [CampaignSmsScheduleRequest](docs/models/CampaignSmsScheduleRequest.md)
 - [CampaignSmsSendRequest](docs/models/CampaignSmsSendRequest.md)
 - [CampaignVoiceScheduleRequest](docs/models/CampaignVoiceScheduleRequest.md)
 - [CampaignVoiceSendRequest](docs/models/CampaignVoiceSendRequest.md)
 - [CampaignWebPushScheduleRequest](docs/models/CampaignWebPushScheduleRequest.md)
 - [CampaignWebPushSendRequest](docs/models/CampaignWebPushSendRequest.md)
 - [Cart](docs/models/Cart.md)
 - [CartId](docs/models/CartId.md)
 - [CartPatchRequest](docs/models/CartPatchRequest.md)
 - [Catalog](docs/models/Catalog.md)
 - [CatalogPost](docs/models/CatalogPost.md)
 - [CatalogPostRequest](docs/models/CatalogPostRequest.md)
 - [CellphoneSender](docs/models/CellphoneSender.md)
 - [CellphoneSenderPost](docs/models/CellphoneSenderPost.md)
 - [ClientAlreadyEnabled](docs/models/ClientAlreadyEnabled.md)
 - [ClientIsBeingEnabled](docs/models/ClientIsBeingEnabled.md)
 - [CnameExists](docs/models/CnameExists.md)
 - [ComplexContact](docs/models/ComplexContact.md)
 - [ComplexField](docs/models/ComplexField.md)
 - [ComplexList](docs/models/ComplexList.md)
 - [ComplexUser](docs/models/ComplexUser.md)
 - [ComplexUserPost](docs/models/ComplexUserPost.md)
 - [Conflict](docs/models/Conflict.md)
 - [ConnectedSitesDomain](docs/models/ConnectedSitesDomain.md)
 - [ConnectedSitesDomainDetail](docs/models/ConnectedSitesDomainDetail.md)
 - [ConnectedSitesEmbedForm](docs/models/ConnectedSitesEmbedForm.md)
 - [ConnectedSitesGeneralProductAppDetail](docs/models/ConnectedSitesGeneralProductAppDetail.md)
 - [ConnectedSitesGeneralProductAppDetailGlobal](docs/models/ConnectedSitesGeneralProductAppDetailGlobal.md)
 - [ConnectedSitesGeneralProductFormDetail](docs/models/ConnectedSitesGeneralProductFormDetail.md)
 - [ConnectedSitesGeneralProductFormDetailGlobal](docs/models/ConnectedSitesGeneralProductFormDetailGlobal.md)
 - [ConnectedSitesGeneralProductTEDetailGlobal](docs/models/ConnectedSitesGeneralProductTEDetailGlobal.md)
 - [ConnectedSitesProductEmbedFormDetail](docs/models/ConnectedSitesProductEmbedFormDetail.md)
 - [ConnectedSitesProducts](docs/models/ConnectedSitesProducts.md)
 - [Contact](docs/models/Contact.md)
 - [ContactActivity](docs/models/ContactActivity.md)
 - [ContactActivityAbstractActionsWithData](docs/models/ContactActivityAbstractActionsWithData.md)
 - [ContactActivityClick](docs/models/ContactActivityClick.md)
 - [ContactBaseExtra](docs/models/ContactBaseExtra.md)
 - [ContactBaseExtraBulk](docs/models/ContactBaseExtraBulk.md)
 - [ContactBaseExtraFull](docs/models/ContactBaseExtraFull.md)
 - [ContactBaseExtraPost](docs/models/ContactBaseExtraPost.md)
 - [ContactBaseFieldsBulkSchema](docs/models/ContactBaseFieldsBulkSchema.md)
 - [ContactBaseFieldsPostSchema](docs/models/ContactBaseFieldsPostSchema.md)
 - [ContactBaseFieldsSchema](docs/models/ContactBaseFieldsSchema.md)
 - [ContactBaseFieldsWithIdSchema](docs/models/ContactBaseFieldsWithIdSchema.md)
 - [ContactBaseStatusExtra](docs/models/ContactBaseStatusExtra.md)
 - [ContactBaseStatusExtraBulk](docs/models/ContactBaseStatusExtraBulk.md)
 - [ContactBaseStatusExtraNoRemoved](docs/models/ContactBaseStatusExtraNoRemoved.md)
 - [ContactBaseWithStatusFieldsBulkSchema](docs/models/ContactBaseWithStatusFieldsBulkSchema.md)
 - [ContactBaseWithStatusFieldsNoTokensSchema](docs/models/ContactBaseWithStatusFieldsNoTokensSchema.md)
 - [ContactBaseWithStatusFieldsSchema](docs/models/ContactBaseWithStatusFieldsSchema.md)
 - [ContactBaseWithStatusNoRemovedFieldsSchema](docs/models/ContactBaseWithStatusNoRemovedFieldsSchema.md)
 - [ContactBodyId](docs/models/ContactBodyId.md)
 - [ContactBulk](docs/models/ContactBulk.md)
 - [ContactBulkFile](docs/models/ContactBulkFile.md)
 - [ContactExportRequest](docs/models/ContactExportRequest.md)
 - [ContactExtraFieldCellphone](docs/models/ContactExtraFieldCellphone.md)
 - [ContactExtraFieldCellphoneBulk](docs/models/ContactExtraFieldCellphoneBulk.md)
 - [ContactExtraFieldDate](docs/models/ContactExtraFieldDate.md)
 - [ContactExtraFieldEmail](docs/models/ContactExtraFieldEmail.md)
 - [ContactExtraFieldEmailBulk](docs/models/ContactExtraFieldEmailBulk.md)
 - [ContactExtraFieldNumber](docs/models/ContactExtraFieldNumber.md)
 - [ContactExtraFieldOptions](docs/models/ContactExtraFieldOptions.md)
 - [ContactExtraFieldPhone](docs/models/ContactExtraFieldPhone.md)
 - [ContactExtraFieldPhoneBulk](docs/models/ContactExtraFieldPhoneBulk.md)
 - [ContactExtraFieldText](docs/models/ContactExtraFieldText.md)
 - [ContactExtraFields](docs/models/ContactExtraFields.md)
 - [ContactExtraFieldsBulk](docs/models/ContactExtraFieldsBulk.md)
 - [ContactExtraFieldsBulkSchema](docs/models/ContactExtraFieldsBulkSchema.md)
 - [ContactExtraFieldsSchema](docs/models/ContactExtraFieldsSchema.md)
 - [ContactFieldMappingFileBulkSchema](docs/models/ContactFieldMappingFileBulkSchema.md)
 - [ContactForgetRequest](docs/models/ContactForgetRequest.md)
 - [ContactId](docs/models/ContactId.md)
 - [ContactInsideBase](docs/models/ContactInsideBase.md)
 - [ContactInsideBaseBulk](docs/models/ContactInsideBaseBulk.md)
 - [ContactInsideBasePost](docs/models/ContactInsideBasePost.md)
 - [ContactInsideBaseWithId](docs/models/ContactInsideBaseWithId.md)
 - [ContactOtherActivity](docs/models/ContactOtherActivity.md)
 - [ContactQueryId](docs/models/ContactQueryId.md)
 - [ContactSearchResponse](docs/models/ContactSearchResponse.md)
 - [ContactStatusFieldsBulkSchema](docs/models/ContactStatusFieldsBulkSchema.md)
 - [ContactStatusFieldsSchema](docs/models/ContactStatusFieldsSchema.md)
 - [ContactTags](docs/models/ContactTags.md)
 - [ContactTagsBulk](docs/models/ContactTagsBulk.md)
 - [ContactsActionUpdateContactsSchema](docs/models/ContactsActionUpdateContactsSchema.md)
 - [ContentVoice](docs/models/ContentVoice.md)
 - [ContentVoiceAudio](docs/models/ContentVoiceAudio.md)
 - [ContentVoicePatch](docs/models/ContentVoicePatch.md)
 - [ContentVoiceTemplate](docs/models/ContentVoiceTemplate.md)
 - [Country](docs/models/Country.md)
 - [CreateCartResponse](docs/models/CreateCartResponse.md)
 - [CreateContactResponse](docs/models/CreateContactResponse.md)
 - [CreateOrder](docs/models/CreateOrder.md)
 - [CreateOrderResponse](docs/models/CreateOrderResponse.md)
 - [CreateSuppressionListRequest](docs/models/CreateSuppressionListRequest.md)
 - [Date](docs/models/Date.md)
 - [DateTime](docs/models/DateTime.md)
 - [DeactivateContactsAll](docs/models/DeactivateContactsAll.md)
 - [DeactivateContactsMany](docs/models/DeactivateContactsMany.md)
 - [DeactivateContactsRequest](docs/models/DeactivateContactsRequest.md)
 - [DeleteCampaignsConflict](docs/models/DeleteCampaignsConflict.md)
 - [DeleteFieldsConflict](docs/models/DeleteFieldsConflict.md)
 - [DeleteListsConflict](docs/models/DeleteListsConflict.md)
 - [DeleteListsConflictsErrors](docs/models/DeleteListsConflictsErrors.md)
 - [DeleteSegmentsConflict](docs/models/DeleteSegmentsConflict.md)
 - [DeleteSegmentsConflictsErrors](docs/models/DeleteSegmentsConflictsErrors.md)
 - [DeleteSuppressionListConflictsErrors](docs/models/DeleteSuppressionListConflictsErrors.md)
 - [DetachTagRequest](docs/models/DetachTagRequest.md)
 - [Domain](docs/models/Domain.md)
 - [DomainAlreadyDefined](docs/models/DomainAlreadyDefined.md)
 - [DomainListRequired](docs/models/DomainListRequired.md)
 - [EmailBouncesCampaignFields](docs/models/EmailBouncesCampaignFields.md)
 - [EmailBouncesListStatsFields](docs/models/EmailBouncesListStatsFields.md)
 - [EmailCampaignCreate](docs/models/EmailCampaignCreate.md)
 - [EmailCampaignPatch](docs/models/EmailCampaignPatch.md)
 - [EmailCampaignTemplate](docs/models/EmailCampaignTemplate.md)
 - [EmailClicksByContactCampaignFields](docs/models/EmailClicksByContactCampaignFields.md)
 - [EmailClicksByContactListStatsFields](docs/models/EmailClicksByContactListStatsFields.md)
 - [EmailClicksByUrlCampaignFields](docs/models/EmailClicksByUrlCampaignFields.md)
 - [EmailClicksByUrlListStatsFields](docs/models/EmailClicksByUrlListStatsFields.md)
 - [EmailEventsCampaignFields](docs/models/EmailEventsCampaignFields.md)
 - [EmailEventsListStatsFields](docs/models/EmailEventsListStatsFields.md)
 - [EmailReport](docs/models/EmailReport.md)
 - [EmailReportByDate](docs/models/EmailReportByDate.md)
 - [EmailReportByDomain](docs/models/EmailReportByDomain.md)
 - [EmailReportByEcommerce](docs/models/EmailReportByEcommerce.md)
 - [EmailReportByHour](docs/models/EmailReportByHour.md)
 - [EmailReportByLocation](docs/models/EmailReportByLocation.md)
 - [EmailReportByReader](docs/models/EmailReportByReader.md)
 - [EmailReportByUrl](docs/models/EmailReportByUrl.md)
 - [EmailReportByWeekday](docs/models/EmailReportByWeekday.md)
 - [EmailReportOverall](docs/models/EmailReportOverall.md)
 - [EmailRssCampaignCreate](docs/models/EmailRssCampaignCreate.md)
 - [EmailSendSegment](docs/models/EmailSendSegment.md)
 - [EmailSender](docs/models/EmailSender.md)
 - [EmailSenderPost](docs/models/EmailSenderPost.md)
 - [EmailSenderPutRequest](docs/models/EmailSenderPutRequest.md)
 - [EmailUnsubscriptionsCampaignFields](docs/models/EmailUnsubscriptionsCampaignFields.md)
 - [EmailUnsubscriptionsListStatsFields](docs/models/EmailUnsubscriptionsListStatsFields.md)
 - [EnableTeConflict](docs/models/EnableTeConflict.md)
 - [EnableTeConflictsErrors](docs/models/EnableTeConflictsErrors.md)
 - [EnableTransactionalConflict](docs/models/EnableTransactionalConflict.md)
 - [EnableTransactionalConflictsErrors](docs/models/EnableTransactionalConflictsErrors.md)
 - [ExportContactsWebhookData](docs/models/ExportContactsWebhookData.md)
 - [Field](docs/models/Field.md)
 - [FieldId](docs/models/FieldId.md)
 - [FieldInUse](docs/models/FieldInUse.md)
 - [FieldOption](docs/models/FieldOption.md)
 - [FieldOptionPost](docs/models/FieldOptionPost.md)
 - [Forbidden](docs/models/Forbidden.md)
 - [Form](docs/models/Form.md)
 - [GeneralInfo](docs/models/GeneralInfo.md)
 - [GenerateEmailBouncesReport](docs/models/GenerateEmailBouncesReport.md)
 - [GenerateEmailClicksByContactReport](docs/models/GenerateEmailClicksByContactReport.md)
 - [GenerateEmailClicksByUrlReport](docs/models/GenerateEmailClicksByUrlReport.md)
 - [GenerateEmailEventsReport](docs/models/GenerateEmailEventsReport.md)
 - [GenerateEmailUnsubscriptionsReport](docs/models/GenerateEmailUnsubscriptionsReport.md)
 - [GenerateFormAnswersReport](docs/models/GenerateFormAnswersReport.md)
 - [GenerateSendsReport](docs/models/GenerateSendsReport.md)
 - [GenerateSmsBouncesReport](docs/models/GenerateSmsBouncesReport.md)
 - [GenerateSmsEventsReport](docs/models/GenerateSmsEventsReport.md)
 - [GenerateSubscriptionsReport](docs/models/GenerateSubscriptionsReport.md)
 - [GenerateUnsubscriptionsReport](docs/models/GenerateUnsubscriptionsReport.md)
 - [Goal](docs/models/Goal.md)
 - [GoalAutommaticInfo](docs/models/GoalAutommaticInfo.md)
 - [GoalInfo](docs/models/GoalInfo.md)
 - [GoalManualInfo](docs/models/GoalManualInfo.md)
 - [GoalTimeInfo](docs/models/GoalTimeInfo.md)
 - [HasAutomations](docs/models/HasAutomations.md)
 - [HasCampaignsLastThirtyDays](docs/models/HasCampaignsLastThirtyDays.md)
 - [HasPushApp](docs/models/HasPushApp.md)
 - [HasQueuedCampaigns](docs/models/HasQueuedCampaigns.md)
 - [HasQueuedOperations](docs/models/HasQueuedOperations.md)
 - [HasWebPushSite](docs/models/HasWebPushSite.md)
 - [Hash](docs/models/Hash.md)
 - [HashcodeCampaign](docs/models/HashcodeCampaign.md)
 - [HeaderFooter](docs/models/HeaderFooter.md)
 - [HeaderFooterTemplate](docs/models/HeaderFooterTemplate.md)
 - [Id](docs/models/Id.md)
 - [ImportBulkFileRequest](docs/models/ImportBulkFileRequest.md)
 - [ImportBulkFileRequestSchema](docs/models/ImportBulkFileRequestSchema.md)
 - [ImportBulkRequest](docs/models/ImportBulkRequest.md)
 - [ImportOrdersBulk](docs/models/ImportOrdersBulk.md)
 - [ImportOrdersBulkBulkRequest](docs/models/ImportOrdersBulkBulkRequest.md)
 - [ImportOrdersBulkBulkRequestItems](docs/models/ImportOrdersBulkBulkRequestItems.md)
 - [InternalServerError](docs/models/InternalServerError.md)
 - [InvalidSegmentType](docs/models/InvalidSegmentType.md)
 - [Language](docs/models/Language.md)
 - [LimitContactsActionSend](docs/models/LimitContactsActionSend.md)
 - [LimitContactsPercentActionSend](docs/models/LimitContactsPercentActionSend.md)
 - [LimitContactsValueActionSend](docs/models/LimitContactsValueActionSend.md)
 - [LimitHourActionSend](docs/models/LimitHourActionSend.md)
 - [LimitSpeedActionSend](docs/models/LimitSpeedActionSend.md)
 - [ListLimitReached](docs/models/ListLimitReached.md)
 - [MessageWebPush](docs/models/MessageWebPush.md)
 - [MessageWebPushPost](docs/models/MessageWebPushPost.md)
 - [MessageWebPushRss](docs/models/MessageWebPushRss.md)
 - [ModelList](docs/models/ModelList.md)
 - [ModuleInfo](docs/models/ModuleInfo.md)
 - [MyAccount](docs/models/MyAccount.md)
 - [NameAlreadyExists](docs/models/NameAlreadyExists.md)
 - [NotFound](docs/models/NotFound.md)
 - [NotifyUserIdArrayActionSend](docs/models/NotifyUserIdArrayActionSend.md)
 - [Now](docs/models/Now.md)
 - [NumericCellphoneSender](docs/models/NumericCellphoneSender.md)
 - [NumericCellphoneSenderPost](docs/models/NumericCellphoneSenderPost.md)
 - [OLimitContactsActionSend](docs/models/OLimitContactsActionSend.md)
 - [OSegmentsActionSend](docs/models/OSegmentsActionSend.md)
 - [OSegmentsWithoutContactActionSend](docs/models/OSegmentsWithoutContactActionSend.md)
 - [Operation](docs/models/Operation.md)
 - [OperationActionRequest](docs/models/OperationActionRequest.md)
 - [OperationActionResponse](docs/models/OperationActionResponse.md)
 - [Order](docs/models/Order.md)
 - [OrderPatchRequest](docs/models/OrderPatchRequest.md)
 - [Overall](docs/models/Overall.md)
 - [PatchRequestBaseField](docs/models/PatchRequestBaseField.md)
 - [PatchRequestField](docs/models/PatchRequestField.md)
 - [PatchRequestList](docs/models/PatchRequestList.md)
 - [PayloadTooLarge](docs/models/PayloadTooLarge.md)
 - [PhoneCampaignTemplate](docs/models/PhoneCampaignTemplate.md)
 - [PhoneReport](docs/models/PhoneReport.md)
 - [PhoneSender](docs/models/PhoneSender.md)
 - [PhoneSenderPost](docs/models/PhoneSenderPost.md)
 - [Ping](docs/models/Ping.md)
 - [PlanInfo](docs/models/PlanInfo.md)
 - [PostCNameConflict](docs/models/PostCNameConflict.md)
 - [PostContactsConflict](docs/models/PostContactsConflict.md)
 - [PostListsConflict](docs/models/PostListsConflict.md)
 - [PostProductsConflict](docs/models/PostProductsConflict.md)
 - [PostRequestList](docs/models/PostRequestList.md)
 - [PostWebpushSiteConflict](docs/models/PostWebpushSiteConflict.md)
 - [Product](docs/models/Product.md)
 - [ProductAlreadyExists](docs/models/ProductAlreadyExists.md)
 - [ProductBulkRequest](docs/models/ProductBulkRequest.md)
 - [ProductCustomAttributes](docs/models/ProductCustomAttributes.md)
 - [ProductPatchRequest](docs/models/ProductPatchRequest.md)
 - [ProductPostRequest](docs/models/ProductPostRequest.md)
 - [PushAppId](docs/models/PushAppId.md)
 - [PushCampaignPatchRequest](docs/models/PushCampaignPatchRequest.md)
 - [PushCampaignPostRequest](docs/models/PushCampaignPostRequest.md)
 - [PushEvent](docs/models/PushEvent.md)
 - [PushNotificationSoundSchema](docs/models/PushNotificationSoundSchema.md)
 - [PushNotificationSoundSchemaDefault](docs/models/PushNotificationSoundSchemaDefault.md)
 - [PushNotificationSoundSchemaNone](docs/models/PushNotificationSoundSchemaNone.md)
 - [PushNotificationSoundSchemaUrl](docs/models/PushNotificationSoundSchemaUrl.md)
 - [PushReport](docs/models/PushReport.md)
 - [PushResponse](docs/models/PushResponse.md)
 - [PushToken](docs/models/PushToken.md)
 - [PushVersions](docs/models/PushVersions.md)
 - [QueryId](docs/models/QueryId.md)
 - [RemoveRequest](docs/models/RemoveRequest.md)
 - [RemoveResponse](docs/models/RemoveResponse.md)
 - [ReportCampaignsAll](docs/models/ReportCampaignsAll.md)
 - [ReportCampaignsGroup](docs/models/ReportCampaignsGroup.md)
 - [ReportCampaignsLast](docs/models/ReportCampaignsLast.md)
 - [ReportCampaignsSpecific](docs/models/ReportCampaignsSpecific.md)
 - [RequestEntityTooLarge](docs/models/RequestEntityTooLarge.md)
 - [RequestItemsUnsubscribe](docs/models/RequestItemsUnsubscribe.md)
 - [RequestTimeout](docs/models/RequestTimeout.md)
 - [SavedSegment](docs/models/SavedSegment.md)
 - [Segment](docs/models/Segment.md)
 - [SegmentsActionSend](docs/models/SegmentsActionSend.md)
 - [SegmentsWithoutContactActionSend](docs/models/SegmentsWithoutContactActionSend.md)
 - [SendContact](docs/models/SendContact.md)
 - [SendContactCellphone](docs/models/SendContactCellphone.md)
 - [SendEmailContact](docs/models/SendEmailContact.md)
 - [SendNone](docs/models/SendNone.md)
 - [SendPush](docs/models/SendPush.md)
 - [SendSegment](docs/models/SendSegment.md)
 - [SendSmartSms](docs/models/SendSmartSms.md)
 - [SendSms](docs/models/SendSms.md)
 - [SendWebPush](docs/models/SendWebPush.md)
 - [SendsCampaignFields](docs/models/SendsCampaignFields.md)
 - [ServiceUnavailable](docs/models/ServiceUnavailable.md)
 - [ShowRemoved](docs/models/ShowRemoved.md)
 - [SingleCartObject](docs/models/SingleCartObject.md)
 - [SingleOrderObject](docs/models/SingleOrderObject.md)
 - [SmartSmsCampaign](docs/models/SmartSmsCampaign.md)
 - [SmartSmsCampaignPatchRequest](docs/models/SmartSmsCampaignPatchRequest.md)
 - [SmartSmsSegmentsActionSend](docs/models/SmartSmsSegmentsActionSend.md)
 - [SmsBouncesCampaignFields](docs/models/SmsBouncesCampaignFields.md)
 - [SmsBouncesListStatsFields](docs/models/SmsBouncesListStatsFields.md)
 - [SmsCampaign](docs/models/SmsCampaign.md)
 - [SmsCampaignPatchRequest](docs/models/SmsCampaignPatchRequest.md)
 - [SmsCampaignTemplate](docs/models/SmsCampaignTemplate.md)
 - [SmsEventsCampaignFields](docs/models/SmsEventsCampaignFields.md)
 - [SmsEventsListStatsFields](docs/models/SmsEventsListStatsFields.md)
 - [SmsSegmentsActionSend](docs/models/SmsSegmentsActionSend.md)
 - [StartAutomationRequest](docs/models/StartAutomationRequest.md)
 - [StartAutomationResponse](docs/models/StartAutomationResponse.md)
 - [SubscriptionsListStatsFields](docs/models/SubscriptionsListStatsFields.md)
 - [SuppressionList](docs/models/SuppressionList.md)
 - [SuppressionTypeCellphone](docs/models/SuppressionTypeCellphone.md)
 - [SuppressionTypeEmail](docs/models/SuppressionTypeEmail.md)
 - [SuppressionTypeEmailDomain](docs/models/SuppressionTypeEmailDomain.md)
 - [SuppressionTypePhone](docs/models/SuppressionTypePhone.md)
 - [SuppressionTypeUserEmail](docs/models/SuppressionTypeUserEmail.md)
 - [Tag](docs/models/Tag.md)
 - [TagRequest](docs/models/TagRequest.md)
 - [TagSegment](docs/models/TagSegment.md)
 - [TeResponse](docs/models/TeResponse.md)
 - [TooManyRequests](docs/models/TooManyRequests.md)
 - [Unauthorized](docs/models/Unauthorized.md)
 - [UniqueFieldInUse](docs/models/UniqueFieldInUse.md)
 - [UnprocessableEntity](docs/models/UnprocessableEntity.md)
 - [UnremovableEntry](docs/models/UnremovableEntry.md)
 - [UnsubscriptionObject](docs/models/UnsubscriptionObject.md)
 - [UnsubscriptionsListStatsFields](docs/models/UnsubscriptionsListStatsFields.md)
 - [UpdateContactsRequest](docs/models/UpdateContactsRequest.md)
 - [UsedInAutomations](docs/models/UsedInAutomations.md)
 - [UsedInRecurringMessages](docs/models/UsedInRecurringMessages.md)
 - [User](docs/models/User.md)
 - [UserPost](docs/models/UserPost.md)
 - [UserPostRequest](docs/models/UserPostRequest.md)
 - [VoiceCampaign](docs/models/VoiceCampaign.md)
 - [VoiceCampaignTemplate](docs/models/VoiceCampaignTemplate.md)
 - [VoicePatchCampaign](docs/models/VoicePatchCampaign.md)
 - [WebPushCampaign](docs/models/WebPushCampaign.md)
 - [WebPushPatchCampaign](docs/models/WebPushPatchCampaign.md)
 - [WebPushReport](docs/models/WebPushReport.md)
 - [WebPushRssCampaign](docs/models/WebPushRssCampaign.md)
 - [WebPushSite](docs/models/WebPushSite.md)
 - [WebPushStats](docs/models/WebPushStats.md)
 - [Webhook](docs/models/Webhook.md)
 - [WebhookActionSchema](docs/models/WebhookActionSchema.md)
 - [WebpushActions](docs/models/WebpushActions.md)

## Documentation For Authorization

 Authentication schemes defined for the API:
## Apikey

- **Type**: API key
- **API key parameter name**: Apikey
- **Location**: HTTP header


## Author































## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in egoi_api.apis and egoi_api.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from egoi_api.apis.default_api import DefaultApi`
- `from egoi_api.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import egoi_api
from egoi_api.apis import *
from egoi_api.models import *
```
