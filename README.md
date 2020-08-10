![E-goi](https://www.e-goi.com/wp-content/themes/egoi2019/imgs/svg/logo-egoi.svg)

Almost anything you can do in E-goi, you can do with our API.

The API describes each available method. Learn about parameters, errors, and how to format your requests. That means you can easily call on E-goi actions for your integration.
**API** Full documentation at https://developers.e-goi.com/api/v3/

If you find a bug or something worth fixing, create an issue.

### Changelog
#### 1.1.0RC2
## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/E-goi/sdk-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/E-goi/sdk-python.git`)

Then import the package:
```python
import egoi-api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import egoi-api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import egoi-api
from egoi-api.rest import ApiException
from pprint import pprint

configuration = egoi-api.Configuration()
## Documentation for API Endpoints

All URIs are relative to *https://api.egoiapp.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdvancedReportsApi* | [**generate_email_bounces_report**](docs/AdvancedReportsApi.md#generate_email_bounces_report) | **POST** /reports/advanced/email-bounces | Generate email bounces report
*AdvancedReportsApi* | [**generate_email_clicks_by_contact_report**](docs/AdvancedReportsApi.md#generate_email_clicks_by_contact_report) | **POST** /reports/advanced/email-clicks-by-contact | Generate email clicks by contact report
*AdvancedReportsApi* | [**generate_email_clicks_by_url_report**](docs/AdvancedReportsApi.md#generate_email_clicks_by_url_report) | **POST** /reports/advanced/email-clicks-by-url | Generate email clicks by URL report
*AdvancedReportsApi* | [**generate_email_events_report**](docs/AdvancedReportsApi.md#generate_email_events_report) | **POST** /reports/advanced/email-events | Generate email events report
*AdvancedReportsApi* | [**generate_email_sms_report**](docs/AdvancedReportsApi.md#generate_email_sms_report) | **POST** /reports/advanced/sms-bounces | Generate SMS bounces report
*AdvancedReportsApi* | [**generate_email_unsubscriptions_report**](docs/AdvancedReportsApi.md#generate_email_unsubscriptions_report) | **POST** /reports/advanced/email-unsubscriptions | Generate email unsubscriptions report
*AdvancedReportsApi* | [**generate_form_answers_report**](docs/AdvancedReportsApi.md#generate_form_answers_report) | **POST** /reports/advanced/form-answers | Generate form answers report
*AdvancedReportsApi* | [**generate_sends_report**](docs/AdvancedReportsApi.md#generate_sends_report) | **POST** /reports/advanced/sends | Generate sends report
*AdvancedReportsApi* | [**generate_sms_events_report**](docs/AdvancedReportsApi.md#generate_sms_events_report) | **POST** /reports/advanced/sms-events | Generate SMS events report
*AdvancedReportsApi* | [**generate_subscriptions_report**](docs/AdvancedReportsApi.md#generate_subscriptions_report) | **POST** /reports/advanced/subscriptions | Generate subscriptions report
*AdvancedReportsApi* | [**generate_unsubscriptions_report**](docs/AdvancedReportsApi.md#generate_unsubscriptions_report) | **POST** /reports/advanced/unsubscriptions | Generate unsubscriptions report
*AdvancedReportsApi* | [**get_all_advanced_reports**](docs/AdvancedReportsApi.md#get_all_advanced_reports) | **GET** /reports/advanced | Get all advanced reports
*AutomationsApi* | [**delete_automation**](docs/AutomationsApi.md#delete_automation) | **DELETE** /automations/{automation_id} | Remove automation
*AutomationsApi* | [**get_all_automations**](docs/AutomationsApi.md#get_all_automations) | **GET** /automations | Get all automations
*CNamesApi* | [**create_c_name**](docs/CNamesApi.md#create_c_name) | **POST** /cnames | Create cname
*CNamesApi* | [**get_all_c_names**](docs/CNamesApi.md#get_all_c_names) | **GET** /cnames | Get All CNames
*CampaignGroupsApi* | [**create_campaign_group**](docs/CampaignGroupsApi.md#create_campaign_group) | **POST** /campaign-groups | Create new campaign group
*CampaignGroupsApi* | [**delete_campaign_group**](docs/CampaignGroupsApi.md#delete_campaign_group) | **DELETE** /campaign-groups/{group_id} | Remove Campaign Group
*CampaignGroupsApi* | [**get_all_campaign_groups**](docs/CampaignGroupsApi.md#get_all_campaign_groups) | **GET** /campaign-groups | Get all campaign groups
*CampaignGroupsApi* | [**update_campaign_group**](docs/CampaignGroupsApi.md#update_campaign_group) | **PUT** /campaign-groups/{group_id} | Update a specific campaign group
*CampaignsApi* | [**delete_campaigns**](docs/CampaignsApi.md#delete_campaigns) | **DELETE** /campaigns/{campaign_hash} | Remove Campaign
*CampaignsApi* | [**get_all_campaigns**](docs/CampaignsApi.md#get_all_campaigns) | **GET** /campaigns | Get all Campaigns
*ContactsApi* | [**action_activate_contacts**](docs/ContactsApi.md#action_activate_contacts) | **POST** /lists/{list_id}/contacts/actions/activate | Activate contacts
*ContactsApi* | [**action_attach_tag**](docs/ContactsApi.md#action_attach_tag) | **POST** /lists/{list_id}/contacts/actions/attach-tag | Attach tag to contact
*ContactsApi* | [**action_deactivate_contacts**](docs/ContactsApi.md#action_deactivate_contacts) | **POST** /lists/{list_id}/contacts/actions/deactivate | Deactivate contacts
*ContactsApi* | [**action_detach_tag**](docs/ContactsApi.md#action_detach_tag) | **POST** /lists/{list_id}/contacts/actions/detach-tag | Detach tag to contact
*ContactsApi* | [**action_export_contacts**](docs/ContactsApi.md#action_export_contacts) | **POST** /lists/{list_id}/contacts/actions/export | Exports a list of contacts
*ContactsApi* | [**action_forget_contacts**](docs/ContactsApi.md#action_forget_contacts) | **POST** /lists/{list_id}/contacts/actions/forget | Forget contacts
*ContactsApi* | [**action_import_bulk**](docs/ContactsApi.md#action_import_bulk) | **POST** /lists/{list_id}/contacts/actions/import-bulk | Import collection of contacts
*ContactsApi* | [**action_start_automation**](docs/ContactsApi.md#action_start_automation) | **POST** /lists/{list_id}/contacts/actions/start-automation | Start automation
*ContactsApi* | [**action_unsubscribe_contact**](docs/ContactsApi.md#action_unsubscribe_contact) | **POST** /lists/{list_id}/contacts/actions/unsubscribe | Unsubscribes contacts
*ContactsApi* | [**create_contact**](docs/ContactsApi.md#create_contact) | **POST** /lists/{list_id}/contacts | Create new contact
*ContactsApi* | [**get_all_contact_activities**](docs/ContactsApi.md#get_all_contact_activities) | **GET** /lists/{list_id}/contacts/{contact_id}/activities | Get all contact activities
*ContactsApi* | [**get_all_contacts**](docs/ContactsApi.md#get_all_contacts) | **GET** /lists/{list_id}/contacts | Get all contacts
*ContactsApi* | [**get_contact**](docs/ContactsApi.md#get_contact) | **GET** /lists/{list_id}/contacts/{contact_id} | Get contact
*ContactsApi* | [**patch_contact**](docs/ContactsApi.md#patch_contact) | **PATCH** /lists/{list_id}/contacts/{contact_id} | Update a specific contact
*ContactsApi* | [**search_contacts**](docs/ContactsApi.md#search_contacts) | **GET** /contacts/search | Search contact
*EcommerceApi* | [**create_catalog**](docs/EcommerceApi.md#create_catalog) | **POST** /catalogs | Create new catalog
*EcommerceApi* | [**create_product**](docs/EcommerceApi.md#create_product) | **POST** /catalogs/{catalog_id}/products | Create new product
*EcommerceApi* | [**delete_catalog**](docs/EcommerceApi.md#delete_catalog) | **DELETE** /catalogs/{catalog_id} | Remove catalog
*EcommerceApi* | [**delete_product**](docs/EcommerceApi.md#delete_product) | **DELETE** /catalogs/{catalog_id}/products/{product_identifier} | Remove product
*EcommerceApi* | [**get_all_catalogs**](docs/EcommerceApi.md#get_all_catalogs) | **GET** /catalogs | Get all catalogs
*EcommerceApi* | [**get_all_products**](docs/EcommerceApi.md#get_all_products) | **GET** /catalogs/{catalog_id}/products | Get all products
*EcommerceApi* | [**get_product**](docs/EcommerceApi.md#get_product) | **GET** /catalogs/{catalog_id}/products/{product_identifier} | Get product
*EcommerceApi* | [**import_orders_bulk**](docs/EcommerceApi.md#import_orders_bulk) | **POST** /lists/{list_id}/orders | Orders import bulk request
*EcommerceApi* | [**import_products**](docs/EcommerceApi.md#import_products) | **POST** /catalogs/{catalog_id}/products/actions/import | Import products
*EcommerceApi* | [**update_product**](docs/EcommerceApi.md#update_product) | **PATCH** /catalogs/{catalog_id}/products/{product_identifier} | Update product
*EmailApi* | [**action_enable_email_rss**](docs/EmailApi.md#action_enable_email_rss) | **POST** /campaigns/email/rss/{campaign_hash}/actions/enable | Enables a rss email campaign
*EmailApi* | [**action_send_email**](docs/EmailApi.md#action_send_email) | **POST** /campaigns/email/{campaign_hash}/actions/send | Send email message
*EmailApi* | [**create_email_campaign**](docs/EmailApi.md#create_email_campaign) | **POST** /campaigns/email | Create new email campaign
*EmailApi* | [**create_email_rss_campaign**](docs/EmailApi.md#create_email_rss_campaign) | **POST** /campaigns/email/rss | Create new email rss campaign
*EmailApi* | [**patch_email_campaign**](docs/EmailApi.md#patch_email_campaign) | **PATCH** /campaigns/email/{campaign_hash} | Update a specific email campaign
*FieldsApi* | [**create_extra_field**](docs/FieldsApi.md#create_extra_field) | **POST** /lists/{list_id}/fields/extra | Create extra field
*FieldsApi* | [**create_field_option**](docs/FieldsApi.md#create_field_option) | **POST** /lists/{list_id}/fields/extra/{field_id}/options | Create new field option
*FieldsApi* | [**delete_extra_field**](docs/FieldsApi.md#delete_extra_field) | **DELETE** /lists/{list_id}/fields/extra/{field_id} | Remove extra field
*FieldsApi* | [**delete_field_option**](docs/FieldsApi.md#delete_field_option) | **DELETE** /lists/{list_id}/fields/extra/{field_id}/options/{option_id} | Deletes an option
*FieldsApi* | [**get_all_field_options**](docs/FieldsApi.md#get_all_field_options) | **GET** /lists/{list_id}/fields/extra/{field_id}/options | Get all field options
*FieldsApi* | [**get_all_fields**](docs/FieldsApi.md#get_all_fields) | **GET** /lists/{list_id}/fields | Get all fields
*FieldsApi* | [**patch_base_field**](docs/FieldsApi.md#patch_base_field) | **PATCH** /lists/{list_id}/fields/base/{field_id} | Update base field
*FieldsApi* | [**patch_extra_field**](docs/FieldsApi.md#patch_extra_field) | **PATCH** /lists/{list_id}/fields/extra/{field_id} | Update extra field
*FieldsApi* | [**update_field_option**](docs/FieldsApi.md#update_field_option) | **PATCH** /lists/{list_id}/fields/extra/{field_id}/options/{option_id} | Update field option
*ListsApi* | [**create_list**](docs/ListsApi.md#create_list) | **POST** /lists | Create new list
*ListsApi* | [**delete_list**](docs/ListsApi.md#delete_list) | **DELETE** /lists/{list_id} | Remove list
*ListsApi* | [**get_all_lists**](docs/ListsApi.md#get_all_lists) | **GET** /lists | Get all lists
*ListsApi* | [**update_list**](docs/ListsApi.md#update_list) | **PATCH** /lists/{list_id} | Update a specific list
*MyAccountApi* | [**enable_te**](docs/MyAccountApi.md#enable_te) | **POST** /my-account/actions/enable-te | Enable Track&amp;Engage
*MyAccountApi* | [**get_my_account**](docs/MyAccountApi.md#get_my_account) | **GET** /my-account | Get My Account Info
*OperationsApi* | [**action_approve_operation**](docs/OperationsApi.md#action_approve_operation) | **POST** /operations/actions/approve | Approve operation
*OperationsApi* | [**action_cancel_operation**](docs/OperationsApi.md#action_cancel_operation) | **POST** /operations/actions/cancel | Cancel operation
*OperationsApi* | [**action_pause_operation**](docs/OperationsApi.md#action_pause_operation) | **POST** /operations/actions/pause | Pause operation
*OperationsApi* | [**action_resume_operation**](docs/OperationsApi.md#action_resume_operation) | **POST** /operations/actions/resume | Resume operation
*OperationsApi* | [**get_all_operations**](docs/OperationsApi.md#get_all_operations) | **GET** /operations | Get all queued operations
*PingApi* | [**ping**](docs/PingApi.md#ping) | **POST** /ping | Pings the API
*PushApi* | [**action_send_push**](docs/PushApi.md#action_send_push) | **POST** /campaigns/push/{campaign_hash}/actions/send | Send push message
*PushApi* | [**create_push_campaign**](docs/PushApi.md#create_push_campaign) | **POST** /campaigns/push | Create new push campaign
*PushApi* | [**patch_push_campaign**](docs/PushApi.md#patch_push_campaign) | **PATCH** /campaigns/push/{campaign_hash} | Update a specific push campaign
*ReportsApi* | [**get_sms_report**](docs/ReportsApi.md#get_sms_report) | **GET** /reports/sms/{campaign_hash} | Get sms report
*ReportsApi* | [**get_voice_report**](docs/ReportsApi.md#get_voice_report) | **GET** /reports/voice/{campaign_hash} | Get voice report
*ReportsApi* | [**get_web_push_report**](docs/ReportsApi.md#get_web_push_report) | **GET** /reports/web-push/{campaign_hash} | Get webpush report
*SegmentsApi* | [**delete_segment**](docs/SegmentsApi.md#delete_segment) | **DELETE** /lists/{list_id}/segments/{segment_id} | Remove segment
*SegmentsApi* | [**get_all_segments**](docs/SegmentsApi.md#get_all_segments) | **GET** /lists/{list_id}/segments | Get all segments
*SendersApi* | [**create_cellphone_sender**](docs/SendersApi.md#create_cellphone_sender) | **POST** /senders/cellphone | Create cellphone sender
*SendersApi* | [**create_email_sender**](docs/SendersApi.md#create_email_sender) | **POST** /senders/email | Create email sender
*SendersApi* | [**create_phone_sender**](docs/SendersApi.md#create_phone_sender) | **POST** /senders/phone | Create phone sender
*SendersApi* | [**delete_cellphone_sender**](docs/SendersApi.md#delete_cellphone_sender) | **DELETE** /senders/cellphone/{sender_id} | Remove cellphone sender
*SendersApi* | [**delete_email_sender**](docs/SendersApi.md#delete_email_sender) | **DELETE** /senders/email/{sender_id} | Remove email sender
*SendersApi* | [**delete_phone_sender**](docs/SendersApi.md#delete_phone_sender) | **DELETE** /senders/phone/{sender_id} | Remove phone sender
*SendersApi* | [**get_all_cellphone_senders**](docs/SendersApi.md#get_all_cellphone_senders) | **GET** /senders/cellphone | Get all cellphone senders
*SendersApi* | [**get_all_email_senders**](docs/SendersApi.md#get_all_email_senders) | **GET** /senders/email | Get all email senders
*SendersApi* | [**get_all_phone_senders**](docs/SendersApi.md#get_all_phone_senders) | **GET** /senders/phone | Get all phone senders
*SendersApi* | [**put_email_sender**](docs/SendersApi.md#put_email_sender) | **PUT** /senders/email/{sender_id} | Update email sender
*SmartSmsApi* | [**action_send_smart_sms**](docs/SmartSmsApi.md#action_send_smart_sms) | **POST** /campaigns/smart-sms/{campaign_hash}/actions/send | Send smart sms message
*SmartSmsApi* | [**create_smart_sms_campaign**](docs/SmartSmsApi.md#create_smart_sms_campaign) | **POST** /campaigns/smart-sms | Create new smart sms campaign
*SmartSmsApi* | [**patch_smart_sms_campaign**](docs/SmartSmsApi.md#patch_smart_sms_campaign) | **PATCH** /campaigns/smart-sms/{campaign_hash} | Update a specific smart sms campaign
*SmsApi* | [**action_send_sms**](docs/SmsApi.md#action_send_sms) | **POST** /campaigns/sms/{campaign_hash}/actions/send | Send sms message
*SmsApi* | [**create_sms_campaign**](docs/SmsApi.md#create_sms_campaign) | **POST** /campaigns/sms | Create new sms campaign
*SmsApi* | [**patch_sms_campaign**](docs/SmsApi.md#patch_sms_campaign) | **PATCH** /campaigns/sms/{campaign_hash} | Update a specific sms campaign
*SuppressionListApi* | [**get_all_suppression_list**](docs/SuppressionListApi.md#get_all_suppression_list) | **GET** /suppression-list | Get the suppression list
*TagsApi* | [**create_tag**](docs/TagsApi.md#create_tag) | **POST** /tags | Create new tag
*TagsApi* | [**delete_tag**](docs/TagsApi.md#delete_tag) | **DELETE** /tags/{tag_id} | Remove tag
*TagsApi* | [**get_all_tags**](docs/TagsApi.md#get_all_tags) | **GET** /tags | Get all tags
*TagsApi* | [**update_tag**](docs/TagsApi.md#update_tag) | **PUT** /tags/{tag_id} | Update a specific tag
*UsersApi* | [**delete_user**](docs/UsersApi.md#delete_user) | **DELETE** /users/{user_id} | Remove user
*UsersApi* | [**get_all_users**](docs/UsersApi.md#get_all_users) | **GET** /users | Get all users
*UtilitiesApi* | [**get_all_countries**](docs/UtilitiesApi.md#get_all_countries) | **GET** /utilities/countries | Get all countries
*VoiceApi* | [**action_send_voice**](docs/VoiceApi.md#action_send_voice) | **POST** /campaigns/voice/{campaign_hash}/actions/send | Send voice message
*VoiceApi* | [**create_voice_campaign**](docs/VoiceApi.md#create_voice_campaign) | **POST** /campaigns/voice | Create new voice campaign
*VoiceApi* | [**patch_voice_campaign**](docs/VoiceApi.md#patch_voice_campaign) | **PATCH** /campaigns/voice/{campaign_hash} | Update a specific voice campaign
*WebHooksApi* | [**create_webhook**](docs/WebHooksApi.md#create_webhook) | **POST** /webhooks | Create new webhook
*WebHooksApi* | [**delete_webhook**](docs/WebHooksApi.md#delete_webhook) | **DELETE** /webhooks/{webhook_id} | Remove webhook
*WebHooksApi* | [**get_all_webhooks**](docs/WebHooksApi.md#get_all_webhooks) | **GET** /webhooks | Get all webhooks
*WebpushApi* | [**action_enable_web_push_rss**](docs/WebpushApi.md#action_enable_web_push_rss) | **POST** /campaigns/webpush/rss/{campaign_hash}/actions/enable | Enable a rss webpush campaign
*WebpushApi* | [**action_send_web_push**](docs/WebpushApi.md#action_send_web_push) | **POST** /campaigns/web-push/{campaign_hash}/actions/send | Send webpush message
*WebpushApi* | [**create_web_push_campaign**](docs/WebpushApi.md#create_web_push_campaign) | **POST** /campaigns/web-push | Create new webpush campaign
*WebpushApi* | [**create_web_push_rss_campaign**](docs/WebpushApi.md#create_web_push_rss_campaign) | **POST** /campaigns/webpush/rss | Create new webpush rss campaign
*WebpushApi* | [**create_webpush_site**](docs/WebpushApi.md#create_webpush_site) | **POST** /webpush/sites | Creates a webpush site
*WebpushApi* | [**get_all_web_push_sites**](docs/WebpushApi.md#get_all_web_push_sites) | **GET** /webpush/sites | Get all webpush sites
*WebpushApi* | [**patch_web_push_campaign**](docs/WebpushApi.md#patch_web_push_campaign) | **PATCH** /campaigns/web-push/{campaign_hash} | Update a specific webpush campaign


## Documentation For Models

 - [AbstractCampaignSendRequest](docs/AbstractCampaignSendRequest.md)
 - [AbstractCampaignSendRequestSegments](docs/AbstractCampaignSendRequestSegments.md)
 - [AbstractCampaignTemplate](docs/AbstractCampaignTemplate.md)
 - [AbstractCellphoneSender](docs/AbstractCellphoneSender.md)
 - [AbstractCellphoneSenderAllOf](docs/AbstractCellphoneSenderAllOf.md)
 - [AbstractSegment](docs/AbstractSegment.md)
 - [AbstractSendEmail](docs/AbstractSendEmail.md)
 - [AbstractSendVoice](docs/AbstractSendVoice.md)
 - [AbstractSendVoiceAllOf](docs/AbstractSendVoiceAllOf.md)
 - [AcceptedResponse](docs/AcceptedResponse.md)
 - [ActivateContactsAll](docs/ActivateContactsAll.md)
 - [ActivateContactsMany](docs/ActivateContactsMany.md)
 - [ActivateContactsRequest](docs/ActivateContactsRequest.md)
 - [ActivityCollection](docs/ActivityCollection.md)
 - [AdvancedReport](docs/AdvancedReport.md)
 - [AdvancedReportCampaignsObject](docs/AdvancedReportCampaignsObject.md)
 - [AdvancedReportEmailBouncesColumns](docs/AdvancedReportEmailBouncesColumns.md)
 - [AdvancedReportEmailBouncesOptions](docs/AdvancedReportEmailBouncesOptions.md)
 - [AdvancedReportEmailClicksByContactColumns](docs/AdvancedReportEmailClicksByContactColumns.md)
 - [AdvancedReportEmailClicksByContactOptions](docs/AdvancedReportEmailClicksByContactOptions.md)
 - [AdvancedReportEmailClicksByUrlColumns](docs/AdvancedReportEmailClicksByUrlColumns.md)
 - [AdvancedReportEmailClicksByUrlOptions](docs/AdvancedReportEmailClicksByUrlOptions.md)
 - [AdvancedReportEmailEventsColumns](docs/AdvancedReportEmailEventsColumns.md)
 - [AdvancedReportEmailEventsOptions](docs/AdvancedReportEmailEventsOptions.md)
 - [AdvancedReportEmailUnsubscriptionsColumns](docs/AdvancedReportEmailUnsubscriptionsColumns.md)
 - [AdvancedReportEmailUnsubscriptionsOptions](docs/AdvancedReportEmailUnsubscriptionsOptions.md)
 - [AdvancedReportRange](docs/AdvancedReportRange.md)
 - [AdvancedReportSendsColumns](docs/AdvancedReportSendsColumns.md)
 - [AdvancedReportSendsOptions](docs/AdvancedReportSendsOptions.md)
 - [AdvancedReportSmsBouncesColumns](docs/AdvancedReportSmsBouncesColumns.md)
 - [AdvancedReportSmsBouncesOptions](docs/AdvancedReportSmsBouncesOptions.md)
 - [AdvancedReportSmsEventsColumns](docs/AdvancedReportSmsEventsColumns.md)
 - [AdvancedReportSmsEventsOptions](docs/AdvancedReportSmsEventsOptions.md)
 - [AdvancedReportSubscriptionsColumns](docs/AdvancedReportSubscriptionsColumns.md)
 - [AdvancedReportSubscriptionsOptions](docs/AdvancedReportSubscriptionsOptions.md)
 - [AdvancedReportUnsubscriptionsColumns](docs/AdvancedReportUnsubscriptionsColumns.md)
 - [AdvancedReportUnsubscriptionsOptions](docs/AdvancedReportUnsubscriptionsOptions.md)
 - [AdvancedReportsCollection](docs/AdvancedReportsCollection.md)
 - [AlphanumericCellphoneSender](docs/AlphanumericCellphoneSender.md)
 - [AlphanumericCellphoneSenderAllOf](docs/AlphanumericCellphoneSenderAllOf.md)
 - [AttachTagRequest](docs/AttachTagRequest.md)
 - [AttachTagResponse](docs/AttachTagResponse.md)
 - [AutomaticSegment](docs/AutomaticSegment.md)
 - [AutomaticSegmentAllOf](docs/AutomaticSegmentAllOf.md)
 - [Automation](docs/Automation.md)
 - [AutomationAllOf](docs/AutomationAllOf.md)
 - [AutomationCollection](docs/AutomationCollection.md)
 - [BadRequest](docs/BadRequest.md)
 - [BalanceInfo](docs/BalanceInfo.md)
 - [BalanceInfoBalanceInfo](docs/BalanceInfoBalanceInfo.md)
 - [BaseConflict](docs/BaseConflict.md)
 - [BasicProduct](docs/BasicProduct.md)
 - [BasicSender](docs/BasicSender.md)
 - [BillingInfo](docs/BillingInfo.md)
 - [BillingInfoAllOf](docs/BillingInfoAllOf.md)
 - [BillingInfoAllOfBillingInfo](docs/BillingInfoAllOfBillingInfo.md)
 - [BillingInfoAllOfBillingInfoCountry](docs/BillingInfoAllOfBillingInfoCountry.md)
 - [BulkActionResponse](docs/BulkActionResponse.md)
 - [CName](docs/CName.md)
 - [CNamesCollection](docs/CNamesCollection.md)
 - [Campaign](docs/Campaign.md)
 - [CampaignEmailBaseContent](docs/CampaignEmailBaseContent.md)
 - [CampaignEmailContent](docs/CampaignEmailContent.md)
 - [CampaignEmailContentFile](docs/CampaignEmailContentFile.md)
 - [CampaignEmailContentFileAllOf](docs/CampaignEmailContentFileAllOf.md)
 - [CampaignEmailContentHtml](docs/CampaignEmailContentHtml.md)
 - [CampaignEmailContentHtmlAllOf](docs/CampaignEmailContentHtmlAllOf.md)
 - [CampaignEmailContentHtmlPatch](docs/CampaignEmailContentHtmlPatch.md)
 - [CampaignEmailContentHtmlPatchAllOf](docs/CampaignEmailContentHtmlPatchAllOf.md)
 - [CampaignEmailContentTemplate](docs/CampaignEmailContentTemplate.md)
 - [CampaignEmailContentTemplateAllOf](docs/CampaignEmailContentTemplateAllOf.md)
 - [CampaignEmailContentWebPage](docs/CampaignEmailContentWebPage.md)
 - [CampaignEmailContentWebPageAllOf](docs/CampaignEmailContentWebPageAllOf.md)
 - [CampaignEmailRssContent](docs/CampaignEmailRssContent.md)
 - [CampaignEmailRssContentHtml](docs/CampaignEmailRssContentHtml.md)
 - [CampaignEmailRssContentHtmlAllOf](docs/CampaignEmailRssContentHtmlAllOf.md)
 - [CampaignEmailScheduleRequest](docs/CampaignEmailScheduleRequest.md)
 - [CampaignEmailScheduleRequestAllOf](docs/CampaignEmailScheduleRequestAllOf.md)
 - [CampaignEmailSendNowRequest](docs/CampaignEmailSendNowRequest.md)
 - [CampaignEmailSendRequest](docs/CampaignEmailSendRequest.md)
 - [CampaignGroup](docs/CampaignGroup.md)
 - [CampaignGroupAllOf](docs/CampaignGroupAllOf.md)
 - [CampaignGroupCollection](docs/CampaignGroupCollection.md)
 - [CampaignHash](docs/CampaignHash.md)
 - [CampaignPushContent](docs/CampaignPushContent.md)
 - [CampaignPushContentTemplate](docs/CampaignPushContentTemplate.md)
 - [CampaignPushContentText](docs/CampaignPushContentText.md)
 - [CampaignPushScheduleRequest](docs/CampaignPushScheduleRequest.md)
 - [CampaignPushSendRequest](docs/CampaignPushSendRequest.md)
 - [CampaignScheduleDate](docs/CampaignScheduleDate.md)
 - [CampaignSentLast30Days](docs/CampaignSentLast30Days.md)
 - [CampaignSentLast30DaysErrors](docs/CampaignSentLast30DaysErrors.md)
 - [CampaignSmartSmsHtml](docs/CampaignSmartSmsHtml.md)
 - [CampaignSmartSmsImport](docs/CampaignSmartSmsImport.md)
 - [CampaignSmartSmsOptions](docs/CampaignSmartSmsOptions.md)
 - [CampaignSmartSmsPageContent](docs/CampaignSmartSmsPageContent.md)
 - [CampaignSmartSmsRedirect](docs/CampaignSmartSmsRedirect.md)
 - [CampaignSmartSmsScheduleRequest](docs/CampaignSmartSmsScheduleRequest.md)
 - [CampaignSmartSmsSendRequest](docs/CampaignSmartSmsSendRequest.md)
 - [CampaignSmsContent](docs/CampaignSmsContent.md)
 - [CampaignSmsContentTemplate](docs/CampaignSmsContentTemplate.md)
 - [CampaignSmsContentText](docs/CampaignSmsContentText.md)
 - [CampaignSmsOptions](docs/CampaignSmsOptions.md)
 - [CampaignSmsScheduleRequest](docs/CampaignSmsScheduleRequest.md)
 - [CampaignSmsSendRequest](docs/CampaignSmsSendRequest.md)
 - [CampaignVoiceScheduleRequest](docs/CampaignVoiceScheduleRequest.md)
 - [CampaignVoiceSendRequest](docs/CampaignVoiceSendRequest.md)
 - [CampaignWebPushScheduleRequest](docs/CampaignWebPushScheduleRequest.md)
 - [CampaignWebPushSendRequest](docs/CampaignWebPushSendRequest.md)
 - [CampaignsCollection](docs/CampaignsCollection.md)
 - [Catalog](docs/Catalog.md)
 - [CatalogCollection](docs/CatalogCollection.md)
 - [CatalogPostRequest](docs/CatalogPostRequest.md)
 - [CellphoneSender](docs/CellphoneSender.md)
 - [CellphoneSenderCollection](docs/CellphoneSenderCollection.md)
 - [CnameExists](docs/CnameExists.md)
 - [CnameExistsErrors](docs/CnameExistsErrors.md)
 - [ComplexContact](docs/ComplexContact.md)
 - [ComplexContactAllOf](docs/ComplexContactAllOf.md)
 - [ComplexContactAllOfEmailStats](docs/ComplexContactAllOfEmailStats.md)
 - [ComplexContactAllOfPushStats](docs/ComplexContactAllOfPushStats.md)
 - [ComplexContactAllOfSmsStats](docs/ComplexContactAllOfSmsStats.md)
 - [ComplexContactAllOfVoiceStats](docs/ComplexContactAllOfVoiceStats.md)
 - [ComplexContactAllOfWebpushStats](docs/ComplexContactAllOfWebpushStats.md)
 - [ComplexField](docs/ComplexField.md)
 - [ComplexFieldAllOf](docs/ComplexFieldAllOf.md)
 - [ComplexList](docs/ComplexList.md)
 - [ComplexListAllOf](docs/ComplexListAllOf.md)
 - [ComplexListAllOfStats](docs/ComplexListAllOfStats.md)
 - [ComplexUser](docs/ComplexUser.md)
 - [ComplexUserAllOf](docs/ComplexUserAllOf.md)
 - [Conflict](docs/Conflict.md)
 - [ConflictAllOf](docs/ConflictAllOf.md)
 - [Contact](docs/Contact.md)
 - [ContactActivity](docs/ContactActivity.md)
 - [ContactActivityAbstractActionsWithData](docs/ContactActivityAbstractActionsWithData.md)
 - [ContactActivityClick](docs/ContactActivityClick.md)
 - [ContactActivityClickAllOf](docs/ContactActivityClickAllOf.md)
 - [ContactActivityClickAllOfActionData](docs/ContactActivityClickAllOfActionData.md)
 - [ContactBaseExtra](docs/ContactBaseExtra.md)
 - [ContactBaseExtraBulk](docs/ContactBaseExtraBulk.md)
 - [ContactBaseFieldsBulkSchema](docs/ContactBaseFieldsBulkSchema.md)
 - [ContactBaseFieldsSchema](docs/ContactBaseFieldsSchema.md)
 - [ContactBaseStatusExtra](docs/ContactBaseStatusExtra.md)
 - [ContactBaseStatusExtraBulk](docs/ContactBaseStatusExtraBulk.md)
 - [ContactBaseWithStatusFieldsBulkSchema](docs/ContactBaseWithStatusFieldsBulkSchema.md)
 - [ContactBaseWithStatusFieldsSchema](docs/ContactBaseWithStatusFieldsSchema.md)
 - [ContactBaseWithStatusFieldsSchemaBase](docs/ContactBaseWithStatusFieldsSchemaBase.md)
 - [ContactBaseWithStatusFieldsSchemaBasePushTokenAndroid](docs/ContactBaseWithStatusFieldsSchemaBasePushTokenAndroid.md)
 - [ContactBaseWithStatusFieldsSchemaBasePushTokenIos](docs/ContactBaseWithStatusFieldsSchemaBasePushTokenIos.md)
 - [ContactBulk](docs/ContactBulk.md)
 - [ContactCollection](docs/ContactCollection.md)
 - [ContactExportRequest](docs/ContactExportRequest.md)
 - [ContactExtraFieldCellphone](docs/ContactExtraFieldCellphone.md)
 - [ContactExtraFieldCellphoneBulk](docs/ContactExtraFieldCellphoneBulk.md)
 - [ContactExtraFieldDate](docs/ContactExtraFieldDate.md)
 - [ContactExtraFieldEmail](docs/ContactExtraFieldEmail.md)
 - [ContactExtraFieldEmailBulk](docs/ContactExtraFieldEmailBulk.md)
 - [ContactExtraFieldNumber](docs/ContactExtraFieldNumber.md)
 - [ContactExtraFieldOptions](docs/ContactExtraFieldOptions.md)
 - [ContactExtraFieldPhone](docs/ContactExtraFieldPhone.md)
 - [ContactExtraFieldPhoneBulk](docs/ContactExtraFieldPhoneBulk.md)
 - [ContactExtraFieldText](docs/ContactExtraFieldText.md)
 - [ContactExtraFields](docs/ContactExtraFields.md)
 - [ContactExtraFieldsBulk](docs/ContactExtraFieldsBulk.md)
 - [ContactExtraFieldsBulkSchema](docs/ContactExtraFieldsBulkSchema.md)
 - [ContactExtraFieldsSchema](docs/ContactExtraFieldsSchema.md)
 - [ContactForgetRequest](docs/ContactForgetRequest.md)
 - [ContactInsideBase](docs/ContactInsideBase.md)
 - [ContactInsideBaseBulk](docs/ContactInsideBaseBulk.md)
 - [ContactOtherActivity](docs/ContactOtherActivity.md)
 - [ContactSearchResponse](docs/ContactSearchResponse.md)
 - [ContactStatusFieldsBulkSchema](docs/ContactStatusFieldsBulkSchema.md)
 - [ContactStatusFieldsSchema](docs/ContactStatusFieldsSchema.md)
 - [ContactTags](docs/ContactTags.md)
 - [ContactTagsBulk](docs/ContactTagsBulk.md)
 - [ContentVoice](docs/ContentVoice.md)
 - [ContentVoiceAudio](docs/ContentVoiceAudio.md)
 - [ContentVoicePatch](docs/ContentVoicePatch.md)
 - [ContentVoiceTemplate](docs/ContentVoiceTemplate.md)
 - [Country](docs/Country.md)
 - [CountryCollection](docs/CountryCollection.md)
 - [CreateContactResponse](docs/CreateContactResponse.md)
 - [DeactivateContactsAll](docs/DeactivateContactsAll.md)
 - [DeactivateContactsMany](docs/DeactivateContactsMany.md)
 - [DeactivateContactsRequest](docs/DeactivateContactsRequest.md)
 - [DeleteCampaignsConflict](docs/DeleteCampaignsConflict.md)
 - [DeleteFieldsConflict](docs/DeleteFieldsConflict.md)
 - [DeleteListsConflict](docs/DeleteListsConflict.md)
 - [DeleteListsConflictsErrors](docs/DeleteListsConflictsErrors.md)
 - [DeleteSegmentsConflict](docs/DeleteSegmentsConflict.md)
 - [DeleteSegmentsConflictsErrors](docs/DeleteSegmentsConflictsErrors.md)
 - [DomainAlreadyDefined](docs/DomainAlreadyDefined.md)
 - [DomainAlreadyDefinedErrors](docs/DomainAlreadyDefinedErrors.md)
 - [EmailBouncesCampaignFields](docs/EmailBouncesCampaignFields.md)
 - [EmailBouncesListStatsFields](docs/EmailBouncesListStatsFields.md)
 - [EmailCampaignCreate](docs/EmailCampaignCreate.md)
 - [EmailCampaignPatch](docs/EmailCampaignPatch.md)
 - [EmailCampaignTemplate](docs/EmailCampaignTemplate.md)
 - [EmailCampaignTemplateAllOf](docs/EmailCampaignTemplateAllOf.md)
 - [EmailCampaignTemplateAllOfReplyToData](docs/EmailCampaignTemplateAllOfReplyToData.md)
 - [EmailCampaignTemplateAllOfSenderData](docs/EmailCampaignTemplateAllOfSenderData.md)
 - [EmailClicksByContactCampaignFields](docs/EmailClicksByContactCampaignFields.md)
 - [EmailClicksByContactListStatsFields](docs/EmailClicksByContactListStatsFields.md)
 - [EmailClicksByUrlCampaignFields](docs/EmailClicksByUrlCampaignFields.md)
 - [EmailClicksByUrlListStatsFields](docs/EmailClicksByUrlListStatsFields.md)
 - [EmailEventsCampaignFields](docs/EmailEventsCampaignFields.md)
 - [EmailEventsListStatsFields](docs/EmailEventsListStatsFields.md)
 - [EmailRssCampaignCreate](docs/EmailRssCampaignCreate.md)
 - [EmailSendSegment](docs/EmailSendSegment.md)
 - [EmailSender](docs/EmailSender.md)
 - [EmailSenderAllOf](docs/EmailSenderAllOf.md)
 - [EmailSenderCollection](docs/EmailSenderCollection.md)
 - [EmailSenderPutRequest](docs/EmailSenderPutRequest.md)
 - [EmailUnsubscriptionsCampaignFields](docs/EmailUnsubscriptionsCampaignFields.md)
 - [EmailUnsubscriptionsListStatsFields](docs/EmailUnsubscriptionsListStatsFields.md)
 - [EnableTeConflict](docs/EnableTeConflict.md)
 - [EnableTeConflictsErrors](docs/EnableTeConflictsErrors.md)
 - [ExportContactsWebhookData](docs/ExportContactsWebhookData.md)
 - [Field](docs/Field.md)
 - [FieldCollection](docs/FieldCollection.md)
 - [FieldInUse](docs/FieldInUse.md)
 - [FieldInUseErrors](docs/FieldInUseErrors.md)
 - [FieldInUseErrorsFieldInUseData](docs/FieldInUseErrorsFieldInUseData.md)
 - [FieldOption](docs/FieldOption.md)
 - [FieldOptionsCollection](docs/FieldOptionsCollection.md)
 - [Forbidden](docs/Forbidden.md)
 - [Form](docs/Form.md)
 - [GeneralInfo](docs/GeneralInfo.md)
 - [GeneralInfoAllOf](docs/GeneralInfoAllOf.md)
 - [GeneralInfoAllOfGeneralInfo](docs/GeneralInfoAllOfGeneralInfo.md)
 - [GenerateEmailBouncesReport](docs/GenerateEmailBouncesReport.md)
 - [GenerateEmailClicksByContactReport](docs/GenerateEmailClicksByContactReport.md)
 - [GenerateEmailClicksByUrlReport](docs/GenerateEmailClicksByUrlReport.md)
 - [GenerateEmailEventsReport](docs/GenerateEmailEventsReport.md)
 - [GenerateEmailUnsubscriptionsReport](docs/GenerateEmailUnsubscriptionsReport.md)
 - [GenerateFormAnswersReport](docs/GenerateFormAnswersReport.md)
 - [GenerateSendsReport](docs/GenerateSendsReport.md)
 - [GenerateSmsBouncesReport](docs/GenerateSmsBouncesReport.md)
 - [GenerateSmsEventsReport](docs/GenerateSmsEventsReport.md)
 - [GenerateSubscriptionsReport](docs/GenerateSubscriptionsReport.md)
 - [GenerateUnsubscriptionsReport](docs/GenerateUnsubscriptionsReport.md)
 - [HasAutomations](docs/HasAutomations.md)
 - [HasAutomationsErrors](docs/HasAutomationsErrors.md)
 - [HasCampaignsLastThirtyDays](docs/HasCampaignsLastThirtyDays.md)
 - [HasCampaignsLastThirtyDaysErrors](docs/HasCampaignsLastThirtyDaysErrors.md)
 - [HasPushApp](docs/HasPushApp.md)
 - [HasPushAppErrors](docs/HasPushAppErrors.md)
 - [HasQueuedCampaigns](docs/HasQueuedCampaigns.md)
 - [HasQueuedCampaignsErrors](docs/HasQueuedCampaignsErrors.md)
 - [HasQueuedOperations](docs/HasQueuedOperations.md)
 - [HasQueuedOperationsErrors](docs/HasQueuedOperationsErrors.md)
 - [HasWebPushSite](docs/HasWebPushSite.md)
 - [HasWebPushSiteErrors](docs/HasWebPushSiteErrors.md)
 - [HashcodeCampaign](docs/HashcodeCampaign.md)
 - [HeaderFooter](docs/HeaderFooter.md)
 - [HeaderFooterFooterLinks](docs/HeaderFooterFooterLinks.md)
 - [HeaderFooterHeaderLinks](docs/HeaderFooterHeaderLinks.md)
 - [HeaderFooterTemplate](docs/HeaderFooterTemplate.md)
 - [ImportBulkRequest](docs/ImportBulkRequest.md)
 - [ImportOrdersBulkBulkRequest](docs/ImportOrdersBulkBulkRequest.md)
 - [ImportOrdersBulkBulkRequestItems](docs/ImportOrdersBulkBulkRequestItems.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InternalServerError](docs/InternalServerError.md)
 - [InvalidSegmentType](docs/InvalidSegmentType.md)
 - [InvalidSegmentTypeErrors](docs/InvalidSegmentTypeErrors.md)
 - [Language](docs/Language.md)
 - [LimitContactsActionSend](docs/LimitContactsActionSend.md)
 - [LimitContactsPercentActionSend](docs/LimitContactsPercentActionSend.md)
 - [LimitContactsValueActionSend](docs/LimitContactsValueActionSend.md)
 - [LimitHourActionSend](docs/LimitHourActionSend.md)
 - [LimitHourActionSendLimitHour](docs/LimitHourActionSendLimitHour.md)
 - [LimitSpeedActionSend](docs/LimitSpeedActionSend.md)
 - [List](docs/List.md)
 - [ListCollection](docs/ListCollection.md)
 - [ListCollection1](docs/ListCollection1.md)
 - [ListLimitReached](docs/ListLimitReached.md)
 - [ListLimitReachedErrors](docs/ListLimitReachedErrors.md)
 - [MessageWebPush](docs/MessageWebPush.md)
 - [MessageWebPushPost](docs/MessageWebPushPost.md)
 - [MessageWebPushRss](docs/MessageWebPushRss.md)
 - [ModuleInfo](docs/ModuleInfo.md)
 - [ModuleInfoModuleInfo](docs/ModuleInfoModuleInfo.md)
 - [ModuleInfoModuleInfoTe](docs/ModuleInfoModuleInfoTe.md)
 - [MyAccount](docs/MyAccount.md)
 - [NameAlreadyExists](docs/NameAlreadyExists.md)
 - [NameAlreadyExistsErrors](docs/NameAlreadyExistsErrors.md)
 - [NotFound](docs/NotFound.md)
 - [NotifyUserIdArrayActionSend](docs/NotifyUserIdArrayActionSend.md)
 - [Now](docs/Now.md)
 - [NumericCellphoneSender](docs/NumericCellphoneSender.md)
 - [NumericCellphoneSenderAllOf](docs/NumericCellphoneSenderAllOf.md)
 - [OLimitContactsActionSend](docs/OLimitContactsActionSend.md)
 - [OSegmentsActionSend](docs/OSegmentsActionSend.md)
 - [OSegmentsWithoutContactActionSend](docs/OSegmentsWithoutContactActionSend.md)
 - [Operation](docs/Operation.md)
 - [OperationActionRequest](docs/OperationActionRequest.md)
 - [OperationActionResponse](docs/OperationActionResponse.md)
 - [OperationActionResponseError](docs/OperationActionResponseError.md)
 - [OperationOperationData](docs/OperationOperationData.md)
 - [OperationsCollection](docs/OperationsCollection.md)
 - [Overall](docs/Overall.md)
 - [OverallOverall](docs/OverallOverall.md)
 - [PatchRequestBaseField](docs/PatchRequestBaseField.md)
 - [PatchRequestField](docs/PatchRequestField.md)
 - [PatchRequestList](docs/PatchRequestList.md)
 - [PhoneCampaignTemplate](docs/PhoneCampaignTemplate.md)
 - [PhoneCampaignTemplateAllOf](docs/PhoneCampaignTemplateAllOf.md)
 - [PhoneReport](docs/PhoneReport.md)
 - [PhoneReportAllOf](docs/PhoneReportAllOf.md)
 - [PhoneReportAllOfNetworks](docs/PhoneReportAllOfNetworks.md)
 - [PhoneSender](docs/PhoneSender.md)
 - [PhoneSenderAllOf](docs/PhoneSenderAllOf.md)
 - [PhoneSenderCollection](docs/PhoneSenderCollection.md)
 - [Ping](docs/Ping.md)
 - [PlanInfo](docs/PlanInfo.md)
 - [PlanInfoPlanInfo](docs/PlanInfoPlanInfo.md)
 - [PostCNameConflict](docs/PostCNameConflict.md)
 - [PostContactsConflict](docs/PostContactsConflict.md)
 - [PostListsConflict](docs/PostListsConflict.md)
 - [PostProductsConflict](docs/PostProductsConflict.md)
 - [PostRequestList](docs/PostRequestList.md)
 - [PostWebpushSiteConflict](docs/PostWebpushSiteConflict.md)
 - [Product](docs/Product.md)
 - [ProductAllOf](docs/ProductAllOf.md)
 - [ProductAlreadyExists](docs/ProductAlreadyExists.md)
 - [ProductAlreadyExistsErrors](docs/ProductAlreadyExistsErrors.md)
 - [ProductBulkRequest](docs/ProductBulkRequest.md)
 - [ProductCollection](docs/ProductCollection.md)
 - [ProductPatchRequest](docs/ProductPatchRequest.md)
 - [ProductPatchRequestRelatedProducts](docs/ProductPatchRequestRelatedProducts.md)
 - [ProductPostRequest](docs/ProductPostRequest.md)
 - [PushCampaignPatchRequest](docs/PushCampaignPatchRequest.md)
 - [PushCampaignPatchRequestContent](docs/PushCampaignPatchRequestContent.md)
 - [PushCampaignPostRequest](docs/PushCampaignPostRequest.md)
 - [PushCampaignPostRequestActions](docs/PushCampaignPostRequestActions.md)
 - [PushCampaignPostRequestGeoOptions](docs/PushCampaignPostRequestGeoOptions.md)
 - [PushCampaignPostRequestNotificationOptions](docs/PushCampaignPostRequestNotificationOptions.md)
 - [PushNotificationSoundSchema](docs/PushNotificationSoundSchema.md)
 - [PushNotificationSoundSchemaDefault](docs/PushNotificationSoundSchemaDefault.md)
 - [PushNotificationSoundSchemaNone](docs/PushNotificationSoundSchemaNone.md)
 - [PushNotificationSoundSchemaUrl](docs/PushNotificationSoundSchemaUrl.md)
 - [PushReport](docs/PushReport.md)
 - [PushReportAllOf](docs/PushReportAllOf.md)
 - [PushVersions](docs/PushVersions.md)
 - [PushVersionsVersions](docs/PushVersionsVersions.md)
 - [RemoveRequest](docs/RemoveRequest.md)
 - [RemoveResponse](docs/RemoveResponse.md)
 - [RemoveResponseErrors](docs/RemoveResponseErrors.md)
 - [ReportCampaignsAll](docs/ReportCampaignsAll.md)
 - [ReportCampaignsGroup](docs/ReportCampaignsGroup.md)
 - [ReportCampaignsLast](docs/ReportCampaignsLast.md)
 - [ReportCampaignsSpecific](docs/ReportCampaignsSpecific.md)
 - [RequestItemsUnsubscribe](docs/RequestItemsUnsubscribe.md)
 - [RequestItemsUnsubscribeAllOf](docs/RequestItemsUnsubscribeAllOf.md)
 - [SavedSegment](docs/SavedSegment.md)
 - [SavedSegmentAllOf](docs/SavedSegmentAllOf.md)
 - [SavedSegmentAllOf1](docs/SavedSegmentAllOf1.md)
 - [SavedSegmentAllOfSegmentFilter](docs/SavedSegmentAllOfSegmentFilter.md)
 - [SavedSegmentAllOfSegmentFilterSegmentFilterArray](docs/SavedSegmentAllOfSegmentFilterSegmentFilterArray.md)
 - [Segment](docs/Segment.md)
 - [SegmentCollection](docs/SegmentCollection.md)
 - [SegmentsActionSend](docs/SegmentsActionSend.md)
 - [SegmentsWithoutContactActionSend](docs/SegmentsWithoutContactActionSend.md)
 - [SendContact](docs/SendContact.md)
 - [SendContactCellphone](docs/SendContactCellphone.md)
 - [SendEmailContact](docs/SendEmailContact.md)
 - [SendEmailContactAllOf](docs/SendEmailContactAllOf.md)
 - [SendNone](docs/SendNone.md)
 - [SendPush](docs/SendPush.md)
 - [SendPushAllOf](docs/SendPushAllOf.md)
 - [SendSegment](docs/SendSegment.md)
 - [SendSmartSms](docs/SendSmartSms.md)
 - [SendSmartSmsAllOf](docs/SendSmartSmsAllOf.md)
 - [SendSmartSmsAllOf1](docs/SendSmartSmsAllOf1.md)
 - [SendSmartSmsAllOf2](docs/SendSmartSmsAllOf2.md)
 - [SendSms](docs/SendSms.md)
 - [SendSmsAllOf](docs/SendSmsAllOf.md)
 - [SendSmsAllOf1](docs/SendSmsAllOf1.md)
 - [SendWebPush](docs/SendWebPush.md)
 - [SendWebPushAllOf](docs/SendWebPushAllOf.md)
 - [SendsCampaignFields](docs/SendsCampaignFields.md)
 - [SmartSmsCampaign](docs/SmartSmsCampaign.md)
 - [SmartSmsCampaignCampaignContent](docs/SmartSmsCampaignCampaignContent.md)
 - [SmartSmsCampaignPatchRequest](docs/SmartSmsCampaignPatchRequest.md)
 - [SmartSmsCampaignPatchRequestCampaignContent](docs/SmartSmsCampaignPatchRequestCampaignContent.md)
 - [SmartSmsCampaignPatchRequestPageContent](docs/SmartSmsCampaignPatchRequestPageContent.md)
 - [SmartSmsSegmentsActionSend](docs/SmartSmsSegmentsActionSend.md)
 - [SmsBouncesCampaignFields](docs/SmsBouncesCampaignFields.md)
 - [SmsBouncesListStatsFields](docs/SmsBouncesListStatsFields.md)
 - [SmsCampaign](docs/SmsCampaign.md)
 - [SmsCampaignPatchRequest](docs/SmsCampaignPatchRequest.md)
 - [SmsCampaignPatchRequestContent](docs/SmsCampaignPatchRequestContent.md)
 - [SmsCampaignTemplate](docs/SmsCampaignTemplate.md)
 - [SmsCampaignTemplateAllOf](docs/SmsCampaignTemplateAllOf.md)
 - [SmsEventsCampaignFields](docs/SmsEventsCampaignFields.md)
 - [SmsEventsListStatsFields](docs/SmsEventsListStatsFields.md)
 - [SmsSegmentsActionSend](docs/SmsSegmentsActionSend.md)
 - [StartAutomationRequest](docs/StartAutomationRequest.md)
 - [StartAutomationResponse](docs/StartAutomationResponse.md)
 - [SubscriptionsListStatsFields](docs/SubscriptionsListStatsFields.md)
 - [SuppressionList](docs/SuppressionList.md)
 - [SuppressionListItems](docs/SuppressionListItems.md)
 - [Tag](docs/Tag.md)
 - [TagCollection](docs/TagCollection.md)
 - [TagCollection1](docs/TagCollection1.md)
 - [TagRequest](docs/TagRequest.md)
 - [TagSegment](docs/TagSegment.md)
 - [TagSegmentAllOf](docs/TagSegmentAllOf.md)
 - [TeResponse](docs/TeResponse.md)
 - [TeResponseAllOf](docs/TeResponseAllOf.md)
 - [Unauthorized](docs/Unauthorized.md)
 - [UniqueFieldInUse](docs/UniqueFieldInUse.md)
 - [UniqueFieldInUseErrors](docs/UniqueFieldInUseErrors.md)
 - [UnprocessableEntity](docs/UnprocessableEntity.md)
 - [UnsubscriptionObject](docs/UnsubscriptionObject.md)
 - [UnsubscriptionsListStatsFields](docs/UnsubscriptionsListStatsFields.md)
 - [UsedInAutomations](docs/UsedInAutomations.md)
 - [UsedInAutomationsErrors](docs/UsedInAutomationsErrors.md)
 - [UsedInRecurringMessages](docs/UsedInRecurringMessages.md)
 - [UsedInRecurringMessagesErrors](docs/UsedInRecurringMessagesErrors.md)
 - [User](docs/User.md)
 - [UserAllOf](docs/UserAllOf.md)
 - [UserCollection](docs/UserCollection.md)
 - [UserPostRequest](docs/UserPostRequest.md)
 - [UserPostRequestAllOf](docs/UserPostRequestAllOf.md)
 - [VoiceCampaign](docs/VoiceCampaign.md)
 - [VoiceCampaignAllOf](docs/VoiceCampaignAllOf.md)
 - [VoiceCampaignTemplate](docs/VoiceCampaignTemplate.md)
 - [VoiceCampaignTemplateAllOf](docs/VoiceCampaignTemplateAllOf.md)
 - [VoicePatchCampaign](docs/VoicePatchCampaign.md)
 - [VoicePatchCampaignAllOf](docs/VoicePatchCampaignAllOf.md)
 - [WebPushCampaign](docs/WebPushCampaign.md)
 - [WebPushPatchCampaign](docs/WebPushPatchCampaign.md)
 - [WebPushReport](docs/WebPushReport.md)
 - [WebPushReportBrowsers](docs/WebPushReportBrowsers.md)
 - [WebPushReportOperatingSystems](docs/WebPushReportOperatingSystems.md)
 - [WebPushRssCampaign](docs/WebPushRssCampaign.md)
 - [WebPushSite](docs/WebPushSite.md)
 - [WebPushStats](docs/WebPushStats.md)
 - [Webhook](docs/Webhook.md)
 - [WebhookActionSchema](docs/WebhookActionSchema.md)


## Documentation For Authorization


## Apikey

- **Type**: API key
- **API key parameter name**: Apikey
- **Location**: HTTP header


## Author




