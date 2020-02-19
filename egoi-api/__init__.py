# coding: utf-8

# flake8: noqa

"""
    APIv3 (Beta)

     # Introduction Just a quick peek!!! This is our new version of API. Remember, it is not stable yet!!! But we invite you play with it and give us your feedback ;) # Getting Started  E-goi can be integrated with many environments and programming languages via our REST API. We've created a developer focused portal to give your organization a clear and quick overview of how to integrate with E-goi. The developer portal focuses on scenarios for integration and flow of events. We recommend familiarizing yourself with all of the content in the developer portal, before start using our rest API.   The E-goi  APIv3 is served over HTTPS. To ensure data privacy, unencrypted HTTP is not supported.  Request data is passed to the API by POSTing JSON objects to the API endpoints with the appropriate parameters.   BaseURL = api.egoiapp.com  # RESTful Services This API supports 5 HTTP methods:  * <b>GET</b>: The HTTP GET method is used to **read** (or retrieve) a representation of a resource. * <b>POST</b>: The POST verb is most-often utilized to **create** new resources. * <b>PATCH</b>: PATCH is used for **modify** capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource * <b>PUT</b>: PUT is most-often utilized for **update** capabilities, PUT-ing to a known resource URI with the request body containing the newly-updated representation of the original resource. * <b>DELETE</b>: DELETE is pretty easy to understand. It is used to **delete** a resource identified by a URI.  # Authentication   We use a custom authentication method, you will need a apikey that you can find in your account settings. Below you will see a curl example to get your account information:  #!/bin/bash  curl -X GET 'https://api.egoiapp.com/my-account' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>'  Here you can see a curl Post example with authentication:  #!/bin/bash  curl -X POST 'http://api.egoiapp.com/tags' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>' \\  -H 'Content-Type: application/json' \\  -d '{`name`:`Your custom tag`,`color`:`#FFFFFF`}'  # SDK Get started quickly with E-goi with our integration tools. Our SDK is a modern open source library that makes it easy to integrate your application with E-goi services. * <b><a href='https://github.com/E-goi/sdk-java'>Java</a></b> * <b><a href='https://github.com/E-goi/sdk-php'>PHP</a></b> * <b><a href='https://github.com/E-goi/sdk-python'>Python</a></b>  <security-definitions/>  # noqa: E501

    The version of the OpenAPI document: 3.0.0-beta
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0RC1"

# import apis into sdk package
from egoi-api.api.advanced_reports_api import AdvancedReportsApi
from egoi-api.api.automations_api import AutomationsApi
from egoi-api.api.c_names_api import CNamesApi
from egoi-api.api.campaign_groups_api import CampaignGroupsApi
from egoi-api.api.campaigns_api import CampaignsApi
from egoi-api.api.contacts_api import ContactsApi
from egoi-api.api.ecommerce_api import EcommerceApi
from egoi-api.api.email_api import EmailApi
from egoi-api.api.fields_api import FieldsApi
from egoi-api.api.lists_api import ListsApi
from egoi-api.api.my_account_api import MyAccountApi
from egoi-api.api.operations_api import OperationsApi
from egoi-api.api.ping_api import PingApi
from egoi-api.api.push_api import PushApi
from egoi-api.api.reports_api import ReportsApi
from egoi-api.api.segments_api import SegmentsApi
from egoi-api.api.senders_api import SendersApi
from egoi-api.api.smart_sms_api import SmartSmsApi
from egoi-api.api.sms_api import SmsApi
from egoi-api.api.suppression_list_api import SuppressionListApi
from egoi-api.api.tags_api import TagsApi
from egoi-api.api.users_api import UsersApi
from egoi-api.api.utilities_api import UtilitiesApi
from egoi-api.api.voice_api import VoiceApi
from egoi-api.api.webpush_api import WebpushApi

# import ApiClient
from egoi-api.api_client import ApiClient
from egoi-api.configuration import Configuration
from egoi-api.exceptions import OpenApiException
from egoi-api.exceptions import ApiTypeError
from egoi-api.exceptions import ApiValueError
from egoi-api.exceptions import ApiKeyError
from egoi-api.exceptions import ApiException
# import models into sdk package
from egoi-api.models.abstract_campaign_send_request import AbstractCampaignSendRequest
from egoi-api.models.abstract_campaign_send_request_segments import AbstractCampaignSendRequestSegments
from egoi-api.models.abstract_campaign_template import AbstractCampaignTemplate
from egoi-api.models.abstract_cellphone_sender import AbstractCellphoneSender
from egoi-api.models.abstract_cellphone_sender_all_of import AbstractCellphoneSenderAllOf
from egoi-api.models.abstract_segment import AbstractSegment
from egoi-api.models.abstract_send_email import AbstractSendEmail
from egoi-api.models.abstract_send_voice import AbstractSendVoice
from egoi-api.models.abstract_send_voice_all_of import AbstractSendVoiceAllOf
from egoi-api.models.accepted_response import AcceptedResponse
from egoi-api.models.activity_collection import ActivityCollection
from egoi-api.models.advanced_report import AdvancedReport
from egoi-api.models.advanced_report_campaigns_object import AdvancedReportCampaignsObject
from egoi-api.models.advanced_report_email_bounces_columns import AdvancedReportEmailBouncesColumns
from egoi-api.models.advanced_report_email_bounces_options import AdvancedReportEmailBouncesOptions
from egoi-api.models.advanced_report_email_clicks_by_contact_columns import AdvancedReportEmailClicksByContactColumns
from egoi-api.models.advanced_report_email_clicks_by_contact_options import AdvancedReportEmailClicksByContactOptions
from egoi-api.models.advanced_report_email_clicks_by_url_columns import AdvancedReportEmailClicksByUrlColumns
from egoi-api.models.advanced_report_email_clicks_by_url_options import AdvancedReportEmailClicksByUrlOptions
from egoi-api.models.advanced_report_email_events_columns import AdvancedReportEmailEventsColumns
from egoi-api.models.advanced_report_email_events_options import AdvancedReportEmailEventsOptions
from egoi-api.models.advanced_report_email_unsubscriptions_columns import AdvancedReportEmailUnsubscriptionsColumns
from egoi-api.models.advanced_report_email_unsubscriptions_options import AdvancedReportEmailUnsubscriptionsOptions
from egoi-api.models.advanced_report_range import AdvancedReportRange
from egoi-api.models.advanced_report_sends_columns import AdvancedReportSendsColumns
from egoi-api.models.advanced_report_sends_options import AdvancedReportSendsOptions
from egoi-api.models.advanced_report_sms_bounces_columns import AdvancedReportSmsBouncesColumns
from egoi-api.models.advanced_report_sms_bounces_options import AdvancedReportSmsBouncesOptions
from egoi-api.models.advanced_report_sms_events_columns import AdvancedReportSmsEventsColumns
from egoi-api.models.advanced_report_sms_events_options import AdvancedReportSmsEventsOptions
from egoi-api.models.advanced_report_subscriptions_columns import AdvancedReportSubscriptionsColumns
from egoi-api.models.advanced_report_subscriptions_options import AdvancedReportSubscriptionsOptions
from egoi-api.models.advanced_report_unsubscriptions_columns import AdvancedReportUnsubscriptionsColumns
from egoi-api.models.advanced_report_unsubscriptions_options import AdvancedReportUnsubscriptionsOptions
from egoi-api.models.advanced_reports_collection import AdvancedReportsCollection
from egoi-api.models.alphanumeric_cellphone_sender import AlphanumericCellphoneSender
from egoi-api.models.alphanumeric_cellphone_sender_all_of import AlphanumericCellphoneSenderAllOf
from egoi-api.models.attach_tag_request import AttachTagRequest
from egoi-api.models.attach_tag_response import AttachTagResponse
from egoi-api.models.automatic_segment import AutomaticSegment
from egoi-api.models.automatic_segment_all_of import AutomaticSegmentAllOf
from egoi-api.models.automation import Automation
from egoi-api.models.automation_all_of import AutomationAllOf
from egoi-api.models.automation_collection import AutomationCollection
from egoi-api.models.bad_request import BadRequest
from egoi-api.models.balance_info import BalanceInfo
from egoi-api.models.balance_info_balance_info import BalanceInfoBalanceInfo
from egoi-api.models.base_conflict import BaseConflict
from egoi-api.models.basic_product import BasicProduct
from egoi-api.models.basic_sender import BasicSender
from egoi-api.models.billing_info import BillingInfo
from egoi-api.models.billing_info_all_of import BillingInfoAllOf
from egoi-api.models.billing_info_all_of_billing_info import BillingInfoAllOfBillingInfo
from egoi-api.models.billing_info_all_of_billing_info_country import BillingInfoAllOfBillingInfoCountry
from egoi-api.models.bulk_action_response import BulkActionResponse
from egoi-api.models.c_name import CName
from egoi-api.models.c_names_collection import CNamesCollection
from egoi-api.models.campaign import Campaign
from egoi-api.models.campaign_email_base_content import CampaignEmailBaseContent
from egoi-api.models.campaign_email_content import CampaignEmailContent
from egoi-api.models.campaign_email_content_file import CampaignEmailContentFile
from egoi-api.models.campaign_email_content_file_all_of import CampaignEmailContentFileAllOf
from egoi-api.models.campaign_email_content_html import CampaignEmailContentHtml
from egoi-api.models.campaign_email_content_html_all_of import CampaignEmailContentHtmlAllOf
from egoi-api.models.campaign_email_content_html_patch import CampaignEmailContentHtmlPatch
from egoi-api.models.campaign_email_content_html_patch_all_of import CampaignEmailContentHtmlPatchAllOf
from egoi-api.models.campaign_email_content_template import CampaignEmailContentTemplate
from egoi-api.models.campaign_email_content_template_all_of import CampaignEmailContentTemplateAllOf
from egoi-api.models.campaign_email_content_web_page import CampaignEmailContentWebPage
from egoi-api.models.campaign_email_content_web_page_all_of import CampaignEmailContentWebPageAllOf
from egoi-api.models.campaign_email_rss_content import CampaignEmailRssContent
from egoi-api.models.campaign_email_rss_content_html import CampaignEmailRssContentHtml
from egoi-api.models.campaign_email_rss_content_html_all_of import CampaignEmailRssContentHtmlAllOf
from egoi-api.models.campaign_email_schedule_request import CampaignEmailScheduleRequest
from egoi-api.models.campaign_email_schedule_request_all_of import CampaignEmailScheduleRequestAllOf
from egoi-api.models.campaign_email_send_now_request import CampaignEmailSendNowRequest
from egoi-api.models.campaign_email_send_request import CampaignEmailSendRequest
from egoi-api.models.campaign_group import CampaignGroup
from egoi-api.models.campaign_group_all_of import CampaignGroupAllOf
from egoi-api.models.campaign_group_collection import CampaignGroupCollection
from egoi-api.models.campaign_hash import CampaignHash
from egoi-api.models.campaign_push_content import CampaignPushContent
from egoi-api.models.campaign_push_content_template import CampaignPushContentTemplate
from egoi-api.models.campaign_push_content_text import CampaignPushContentText
from egoi-api.models.campaign_push_schedule_request import CampaignPushScheduleRequest
from egoi-api.models.campaign_push_send_request import CampaignPushSendRequest
from egoi-api.models.campaign_schedule_date import CampaignScheduleDate
from egoi-api.models.campaign_sent_last30_days import CampaignSentLast30Days
from egoi-api.models.campaign_sent_last30_days_errors import CampaignSentLast30DaysErrors
from egoi-api.models.campaign_smart_sms_html import CampaignSmartSmsHtml
from egoi-api.models.campaign_smart_sms_import import CampaignSmartSmsImport
from egoi-api.models.campaign_smart_sms_options import CampaignSmartSmsOptions
from egoi-api.models.campaign_smart_sms_page_content import CampaignSmartSmsPageContent
from egoi-api.models.campaign_smart_sms_redirect import CampaignSmartSmsRedirect
from egoi-api.models.campaign_smart_sms_schedule_request import CampaignSmartSmsScheduleRequest
from egoi-api.models.campaign_smart_sms_send_request import CampaignSmartSmsSendRequest
from egoi-api.models.campaign_sms_content import CampaignSmsContent
from egoi-api.models.campaign_sms_content_template import CampaignSmsContentTemplate
from egoi-api.models.campaign_sms_content_text import CampaignSmsContentText
from egoi-api.models.campaign_sms_options import CampaignSmsOptions
from egoi-api.models.campaign_sms_schedule_request import CampaignSmsScheduleRequest
from egoi-api.models.campaign_sms_send_request import CampaignSmsSendRequest
from egoi-api.models.campaign_voice_schedule_request import CampaignVoiceScheduleRequest
from egoi-api.models.campaign_voice_send_request import CampaignVoiceSendRequest
from egoi-api.models.campaign_web_push_schedule_request import CampaignWebPushScheduleRequest
from egoi-api.models.campaign_web_push_send_request import CampaignWebPushSendRequest
from egoi-api.models.campaigns_collection import CampaignsCollection
from egoi-api.models.catalog import Catalog
from egoi-api.models.catalog_collection import CatalogCollection
from egoi-api.models.catalog_post_request import CatalogPostRequest
from egoi-api.models.cellphone_sender import CellphoneSender
from egoi-api.models.cellphone_sender_collection import CellphoneSenderCollection
from egoi-api.models.complex_contact import ComplexContact
from egoi-api.models.complex_contact_all_of import ComplexContactAllOf
from egoi-api.models.complex_contact_all_of_email_stats import ComplexContactAllOfEmailStats
from egoi-api.models.complex_contact_all_of_push_stats import ComplexContactAllOfPushStats
from egoi-api.models.complex_contact_all_of_sms_stats import ComplexContactAllOfSmsStats
from egoi-api.models.complex_contact_all_of_voice_stats import ComplexContactAllOfVoiceStats
from egoi-api.models.complex_contact_all_of_webpush_stats import ComplexContactAllOfWebpushStats
from egoi-api.models.complex_field import ComplexField
from egoi-api.models.complex_field_all_of import ComplexFieldAllOf
from egoi-api.models.complex_list import ComplexList
from egoi-api.models.complex_list_all_of import ComplexListAllOf
from egoi-api.models.complex_list_all_of_stats import ComplexListAllOfStats
from egoi-api.models.complex_user import ComplexUser
from egoi-api.models.complex_user_all_of import ComplexUserAllOf
from egoi-api.models.conflict import Conflict
from egoi-api.models.conflict_all_of import ConflictAllOf
from egoi-api.models.contact import Contact
from egoi-api.models.contact_activity import ContactActivity
from egoi-api.models.contact_activity_abstract_actions_with_data import ContactActivityAbstractActionsWithData
from egoi-api.models.contact_activity_click import ContactActivityClick
from egoi-api.models.contact_activity_click_all_of import ContactActivityClickAllOf
from egoi-api.models.contact_activity_click_all_of_action_data import ContactActivityClickAllOfActionData
from egoi-api.models.contact_base_extra import ContactBaseExtra
from egoi-api.models.contact_base_extra_bulk import ContactBaseExtraBulk
from egoi-api.models.contact_base_fields_bulk_schema import ContactBaseFieldsBulkSchema
from egoi-api.models.contact_base_fields_schema import ContactBaseFieldsSchema
from egoi-api.models.contact_base_status_extra import ContactBaseStatusExtra
from egoi-api.models.contact_base_status_extra_bulk import ContactBaseStatusExtraBulk
from egoi-api.models.contact_base_with_status_fields_bulk_schema import ContactBaseWithStatusFieldsBulkSchema
from egoi-api.models.contact_base_with_status_fields_schema import ContactBaseWithStatusFieldsSchema
from egoi-api.models.contact_base_with_status_fields_schema_base import ContactBaseWithStatusFieldsSchemaBase
from egoi-api.models.contact_base_with_status_fields_schema_base_push_token_android import ContactBaseWithStatusFieldsSchemaBasePushTokenAndroid
from egoi-api.models.contact_base_with_status_fields_schema_base_push_token_ios import ContactBaseWithStatusFieldsSchemaBasePushTokenIos
from egoi-api.models.contact_bulk import ContactBulk
from egoi-api.models.contact_collection import ContactCollection
from egoi-api.models.contact_export_request import ContactExportRequest
from egoi-api.models.contact_extra_field_cellphone import ContactExtraFieldCellphone
from egoi-api.models.contact_extra_field_cellphone_bulk import ContactExtraFieldCellphoneBulk
from egoi-api.models.contact_extra_field_date import ContactExtraFieldDate
from egoi-api.models.contact_extra_field_email import ContactExtraFieldEmail
from egoi-api.models.contact_extra_field_email_bulk import ContactExtraFieldEmailBulk
from egoi-api.models.contact_extra_field_number import ContactExtraFieldNumber
from egoi-api.models.contact_extra_field_options import ContactExtraFieldOptions
from egoi-api.models.contact_extra_field_phone import ContactExtraFieldPhone
from egoi-api.models.contact_extra_field_phone_bulk import ContactExtraFieldPhoneBulk
from egoi-api.models.contact_extra_field_text import ContactExtraFieldText
from egoi-api.models.contact_extra_fields import ContactExtraFields
from egoi-api.models.contact_extra_fields_bulk import ContactExtraFieldsBulk
from egoi-api.models.contact_extra_fields_bulk_schema import ContactExtraFieldsBulkSchema
from egoi-api.models.contact_extra_fields_schema import ContactExtraFieldsSchema
from egoi-api.models.contact_inside_base import ContactInsideBase
from egoi-api.models.contact_inside_base_bulk import ContactInsideBaseBulk
from egoi-api.models.contact_other_activity import ContactOtherActivity
from egoi-api.models.contact_status_fields_bulk_schema import ContactStatusFieldsBulkSchema
from egoi-api.models.contact_status_fields_schema import ContactStatusFieldsSchema
from egoi-api.models.contact_tags import ContactTags
from egoi-api.models.contact_tags_bulk import ContactTagsBulk
from egoi-api.models.content_voice import ContentVoice
from egoi-api.models.content_voice_audio import ContentVoiceAudio
from egoi-api.models.content_voice_patch import ContentVoicePatch
from egoi-api.models.content_voice_template import ContentVoiceTemplate
from egoi-api.models.country import Country
from egoi-api.models.country_collection import CountryCollection
from egoi-api.models.create_contact_response import CreateContactResponse
from egoi-api.models.delete_campaigns_conflict import DeleteCampaignsConflict
from egoi-api.models.delete_fields_conflict import DeleteFieldsConflict
from egoi-api.models.delete_lists_conflict import DeleteListsConflict
from egoi-api.models.delete_lists_conflicts_errors import DeleteListsConflictsErrors
from egoi-api.models.delete_segments_conflict import DeleteSegmentsConflict
from egoi-api.models.delete_segments_conflicts_errors import DeleteSegmentsConflictsErrors
from egoi-api.models.domain_already_defined import DomainAlreadyDefined
from egoi-api.models.domain_already_defined_errors import DomainAlreadyDefinedErrors
from egoi-api.models.email_bounces_campaign_fields import EmailBouncesCampaignFields
from egoi-api.models.email_bounces_list_stats_fields import EmailBouncesListStatsFields
from egoi-api.models.email_campaign_create import EmailCampaignCreate
from egoi-api.models.email_campaign_patch import EmailCampaignPatch
from egoi-api.models.email_campaign_template import EmailCampaignTemplate
from egoi-api.models.email_campaign_template_all_of import EmailCampaignTemplateAllOf
from egoi-api.models.email_campaign_template_all_of_reply_to_data import EmailCampaignTemplateAllOfReplyToData
from egoi-api.models.email_campaign_template_all_of_sender_data import EmailCampaignTemplateAllOfSenderData
from egoi-api.models.email_clicks_by_contact_campaign_fields import EmailClicksByContactCampaignFields
from egoi-api.models.email_clicks_by_contact_list_stats_fields import EmailClicksByContactListStatsFields
from egoi-api.models.email_clicks_by_url_campaign_fields import EmailClicksByUrlCampaignFields
from egoi-api.models.email_clicks_by_url_list_stats_fields import EmailClicksByUrlListStatsFields
from egoi-api.models.email_events_campaign_fields import EmailEventsCampaignFields
from egoi-api.models.email_events_list_stats_fields import EmailEventsListStatsFields
from egoi-api.models.email_rss_campaign_create import EmailRssCampaignCreate
from egoi-api.models.email_send_segment import EmailSendSegment
from egoi-api.models.email_sender import EmailSender
from egoi-api.models.email_sender_all_of import EmailSenderAllOf
from egoi-api.models.email_sender_collection import EmailSenderCollection
from egoi-api.models.email_sender_put_request import EmailSenderPutRequest
from egoi-api.models.email_unsubscriptions_campaign_fields import EmailUnsubscriptionsCampaignFields
from egoi-api.models.email_unsubscriptions_list_stats_fields import EmailUnsubscriptionsListStatsFields
from egoi-api.models.enable_te_conflict import EnableTeConflict
from egoi-api.models.enable_te_conflicts_errors import EnableTeConflictsErrors
from egoi-api.models.export_contacts_webhook_data import ExportContactsWebhookData
from egoi-api.models.field import Field
from egoi-api.models.field_collection import FieldCollection
from egoi-api.models.field_in_use import FieldInUse
from egoi-api.models.field_in_use_errors import FieldInUseErrors
from egoi-api.models.field_in_use_errors_field_in_use_data import FieldInUseErrorsFieldInUseData
from egoi-api.models.field_option import FieldOption
from egoi-api.models.field_options_collection import FieldOptionsCollection
from egoi-api.models.forbidden import Forbidden
from egoi-api.models.form import Form
from egoi-api.models.general_info import GeneralInfo
from egoi-api.models.general_info_all_of import GeneralInfoAllOf
from egoi-api.models.general_info_all_of_general_info import GeneralInfoAllOfGeneralInfo
from egoi-api.models.generate_email_bounces_report import GenerateEmailBouncesReport
from egoi-api.models.generate_email_clicks_by_contact_report import GenerateEmailClicksByContactReport
from egoi-api.models.generate_email_clicks_by_url_report import GenerateEmailClicksByUrlReport
from egoi-api.models.generate_email_events_report import GenerateEmailEventsReport
from egoi-api.models.generate_email_unsubscriptions_report import GenerateEmailUnsubscriptionsReport
from egoi-api.models.generate_form_answers_report import GenerateFormAnswersReport
from egoi-api.models.generate_sends_report import GenerateSendsReport
from egoi-api.models.generate_sms_bounces_report import GenerateSmsBouncesReport
from egoi-api.models.generate_sms_events_report import GenerateSmsEventsReport
from egoi-api.models.generate_subscriptions_report import GenerateSubscriptionsReport
from egoi-api.models.generate_unsubscriptions_report import GenerateUnsubscriptionsReport
from egoi-api.models.has_automations import HasAutomations
from egoi-api.models.has_automations_errors import HasAutomationsErrors
from egoi-api.models.has_campaigns_last_thirty_days import HasCampaignsLastThirtyDays
from egoi-api.models.has_campaigns_last_thirty_days_errors import HasCampaignsLastThirtyDaysErrors
from egoi-api.models.has_push_app import HasPushApp
from egoi-api.models.has_push_app_errors import HasPushAppErrors
from egoi-api.models.has_queued_campaigns import HasQueuedCampaigns
from egoi-api.models.has_queued_campaigns_errors import HasQueuedCampaignsErrors
from egoi-api.models.has_queued_operations import HasQueuedOperations
from egoi-api.models.has_queued_operations_errors import HasQueuedOperationsErrors
from egoi-api.models.has_web_push_site import HasWebPushSite
from egoi-api.models.has_web_push_site_errors import HasWebPushSiteErrors
from egoi-api.models.hashcode_campaign import HashcodeCampaign
from egoi-api.models.header_footer import HeaderFooter
from egoi-api.models.header_footer_footer_links import HeaderFooterFooterLinks
from egoi-api.models.header_footer_header_links import HeaderFooterHeaderLinks
from egoi-api.models.header_footer_template import HeaderFooterTemplate
from egoi-api.models.import_bulk_request import ImportBulkRequest
from egoi-api.models.inline_object import InlineObject
from egoi-api.models.internal_server_error import InternalServerError
from egoi-api.models.invalid_segment_type import InvalidSegmentType
from egoi-api.models.invalid_segment_type_errors import InvalidSegmentTypeErrors
from egoi-api.models.language import Language
from egoi-api.models.limit_contacts_action_send import LimitContactsActionSend
from egoi-api.models.limit_contacts_percent_action_send import LimitContactsPercentActionSend
from egoi-api.models.limit_contacts_value_action_send import LimitContactsValueActionSend
from egoi-api.models.limit_hour_action_send import LimitHourActionSend
from egoi-api.models.limit_hour_action_send_limit_hour import LimitHourActionSendLimitHour
from egoi-api.models.limit_speed_action_send import LimitSpeedActionSend
from egoi-api.models.list import List
from egoi-api.models.list_collection import ListCollection
from egoi-api.models.list_limit_reached import ListLimitReached
from egoi-api.models.list_limit_reached_errors import ListLimitReachedErrors
from egoi-api.models.message_web_push import MessageWebPush
from egoi-api.models.message_web_push_post import MessageWebPushPost
from egoi-api.models.message_web_push_rss import MessageWebPushRss
from egoi-api.models.module_info import ModuleInfo
from egoi-api.models.module_info_module_info import ModuleInfoModuleInfo
from egoi-api.models.module_info_module_info_te import ModuleInfoModuleInfoTe
from egoi-api.models.my_account import MyAccount
from egoi-api.models.not_found import NotFound
from egoi-api.models.notify_user_id_array_action_send import NotifyUserIdArrayActionSend
from egoi-api.models.now import Now
from egoi-api.models.numeric_cellphone_sender import NumericCellphoneSender
from egoi-api.models.numeric_cellphone_sender_all_of import NumericCellphoneSenderAllOf
from egoi-api.models.o_limit_contacts_action_send import OLimitContactsActionSend
from egoi-api.models.o_segments_action_send import OSegmentsActionSend
from egoi-api.models.o_segments_without_contact_action_send import OSegmentsWithoutContactActionSend
from egoi-api.models.operation import Operation
from egoi-api.models.operation_action_request import OperationActionRequest
from egoi-api.models.operation_action_response import OperationActionResponse
from egoi-api.models.operation_action_response_error import OperationActionResponseError
from egoi-api.models.operation_operation_data import OperationOperationData
from egoi-api.models.operations_collection import OperationsCollection
from egoi-api.models.overall import Overall
from egoi-api.models.overall_overall import OverallOverall
from egoi-api.models.patch_request_base_field import PatchRequestBaseField
from egoi-api.models.patch_request_field import PatchRequestField
from egoi-api.models.patch_request_list import PatchRequestList
from egoi-api.models.phone_campaign_template import PhoneCampaignTemplate
from egoi-api.models.phone_campaign_template_all_of import PhoneCampaignTemplateAllOf
from egoi-api.models.phone_report import PhoneReport
from egoi-api.models.phone_report_all_of import PhoneReportAllOf
from egoi-api.models.phone_report_all_of_networks import PhoneReportAllOfNetworks
from egoi-api.models.phone_sender import PhoneSender
from egoi-api.models.phone_sender_all_of import PhoneSenderAllOf
from egoi-api.models.phone_sender_collection import PhoneSenderCollection
from egoi-api.models.ping import Ping
from egoi-api.models.plan_info import PlanInfo
from egoi-api.models.plan_info_plan_info import PlanInfoPlanInfo
from egoi-api.models.post_contacts_conflict import PostContactsConflict
from egoi-api.models.post_lists_conflict import PostListsConflict
from egoi-api.models.post_products_conflict import PostProductsConflict
from egoi-api.models.post_request_list import PostRequestList
from egoi-api.models.product import Product
from egoi-api.models.product_all_of import ProductAllOf
from egoi-api.models.product_already_exists import ProductAlreadyExists
from egoi-api.models.product_already_exists_errors import ProductAlreadyExistsErrors
from egoi-api.models.product_bulk_request import ProductBulkRequest
from egoi-api.models.product_collection import ProductCollection
from egoi-api.models.product_patch_request import ProductPatchRequest
from egoi-api.models.product_patch_request_related_products import ProductPatchRequestRelatedProducts
from egoi-api.models.product_post_request import ProductPostRequest
from egoi-api.models.push_campaign_patch_request import PushCampaignPatchRequest
from egoi-api.models.push_campaign_patch_request_content import PushCampaignPatchRequestContent
from egoi-api.models.push_campaign_post_request import PushCampaignPostRequest
from egoi-api.models.push_campaign_post_request_actions import PushCampaignPostRequestActions
from egoi-api.models.push_campaign_post_request_geo_options import PushCampaignPostRequestGeoOptions
from egoi-api.models.push_campaign_post_request_notification_options import PushCampaignPostRequestNotificationOptions
from egoi-api.models.push_notification_sound_schema import PushNotificationSoundSchema
from egoi-api.models.push_notification_sound_schema_default import PushNotificationSoundSchemaDefault
from egoi-api.models.push_notification_sound_schema_none import PushNotificationSoundSchemaNone
from egoi-api.models.push_notification_sound_schema_url import PushNotificationSoundSchemaUrl
from egoi-api.models.push_report import PushReport
from egoi-api.models.push_report_all_of import PushReportAllOf
from egoi-api.models.push_versions import PushVersions
from egoi-api.models.push_versions_versions import PushVersionsVersions
from egoi-api.models.remove_request import RemoveRequest
from egoi-api.models.remove_response import RemoveResponse
from egoi-api.models.remove_response_errors import RemoveResponseErrors
from egoi-api.models.report_campaigns_all import ReportCampaignsAll
from egoi-api.models.report_campaigns_group import ReportCampaignsGroup
from egoi-api.models.report_campaigns_last import ReportCampaignsLast
from egoi-api.models.report_campaigns_specific import ReportCampaignsSpecific
from egoi-api.models.request_items_unsubscribe import RequestItemsUnsubscribe
from egoi-api.models.request_items_unsubscribe_all_of import RequestItemsUnsubscribeAllOf
from egoi-api.models.saved_segment import SavedSegment
from egoi-api.models.saved_segment_all_of import SavedSegmentAllOf
from egoi-api.models.saved_segment_all_of1 import SavedSegmentAllOf1
from egoi-api.models.saved_segment_all_of_segment_filter import SavedSegmentAllOfSegmentFilter
from egoi-api.models.saved_segment_all_of_segment_filter_segment_filter_array import SavedSegmentAllOfSegmentFilterSegmentFilterArray
from egoi-api.models.segment import Segment
from egoi-api.models.segment_collection import SegmentCollection
from egoi-api.models.segments_action_send import SegmentsActionSend
from egoi-api.models.segments_without_contact_action_send import SegmentsWithoutContactActionSend
from egoi-api.models.send_contact import SendContact
from egoi-api.models.send_contact_cellphone import SendContactCellphone
from egoi-api.models.send_email_contact import SendEmailContact
from egoi-api.models.send_email_contact_all_of import SendEmailContactAllOf
from egoi-api.models.send_none import SendNone
from egoi-api.models.send_push import SendPush
from egoi-api.models.send_push_all_of import SendPushAllOf
from egoi-api.models.send_segment import SendSegment
from egoi-api.models.send_smart_sms import SendSmartSms
from egoi-api.models.send_smart_sms_all_of import SendSmartSmsAllOf
from egoi-api.models.send_smart_sms_all_of1 import SendSmartSmsAllOf1
from egoi-api.models.send_smart_sms_all_of2 import SendSmartSmsAllOf2
from egoi-api.models.send_sms import SendSms
from egoi-api.models.send_sms_all_of import SendSmsAllOf
from egoi-api.models.send_sms_all_of1 import SendSmsAllOf1
from egoi-api.models.send_web_push import SendWebPush
from egoi-api.models.send_web_push_all_of import SendWebPushAllOf
from egoi-api.models.sends_campaign_fields import SendsCampaignFields
from egoi-api.models.smart_sms_campaign import SmartSmsCampaign
from egoi-api.models.smart_sms_campaign_campaign_content import SmartSmsCampaignCampaignContent
from egoi-api.models.smart_sms_campaign_patch_request import SmartSmsCampaignPatchRequest
from egoi-api.models.smart_sms_campaign_patch_request_campaign_content import SmartSmsCampaignPatchRequestCampaignContent
from egoi-api.models.smart_sms_campaign_patch_request_page_content import SmartSmsCampaignPatchRequestPageContent
from egoi-api.models.smart_sms_segments_action_send import SmartSmsSegmentsActionSend
from egoi-api.models.sms_bounces_campaign_fields import SmsBouncesCampaignFields
from egoi-api.models.sms_bounces_list_stats_fields import SmsBouncesListStatsFields
from egoi-api.models.sms_campaign import SmsCampaign
from egoi-api.models.sms_campaign_patch_request import SmsCampaignPatchRequest
from egoi-api.models.sms_campaign_patch_request_content import SmsCampaignPatchRequestContent
from egoi-api.models.sms_campaign_template import SmsCampaignTemplate
from egoi-api.models.sms_campaign_template_all_of import SmsCampaignTemplateAllOf
from egoi-api.models.sms_events_campaign_fields import SmsEventsCampaignFields
from egoi-api.models.sms_events_list_stats_fields import SmsEventsListStatsFields
from egoi-api.models.sms_segments_action_send import SmsSegmentsActionSend
from egoi-api.models.start_automation_request import StartAutomationRequest
from egoi-api.models.start_automation_response import StartAutomationResponse
from egoi-api.models.subscriptions_list_stats_fields import SubscriptionsListStatsFields
from egoi-api.models.suppression_list import SuppressionList
from egoi-api.models.suppression_list_items import SuppressionListItems
from egoi-api.models.tag import Tag
from egoi-api.models.tag_collection import TagCollection
from egoi-api.models.tag_collection1 import TagCollection1
from egoi-api.models.tag_request import TagRequest
from egoi-api.models.tag_segment import TagSegment
from egoi-api.models.tag_segment_all_of import TagSegmentAllOf
from egoi-api.models.te_response import TeResponse
from egoi-api.models.te_response_all_of import TeResponseAllOf
from egoi-api.models.unauthorized import Unauthorized
from egoi-api.models.unique_field_in_use import UniqueFieldInUse
from egoi-api.models.unique_field_in_use_errors import UniqueFieldInUseErrors
from egoi-api.models.unprocessable_entity import UnprocessableEntity
from egoi-api.models.unsubscription_object import UnsubscriptionObject
from egoi-api.models.unsubscriptions_list_stats_fields import UnsubscriptionsListStatsFields
from egoi-api.models.used_in_automations import UsedInAutomations
from egoi-api.models.used_in_automations_errors import UsedInAutomationsErrors
from egoi-api.models.used_in_recurring_messages import UsedInRecurringMessages
from egoi-api.models.used_in_recurring_messages_errors import UsedInRecurringMessagesErrors
from egoi-api.models.user import User
from egoi-api.models.user_all_of import UserAllOf
from egoi-api.models.user_collection import UserCollection
from egoi-api.models.user_post_request import UserPostRequest
from egoi-api.models.user_post_request_all_of import UserPostRequestAllOf
from egoi-api.models.voice_campaign import VoiceCampaign
from egoi-api.models.voice_campaign_all_of import VoiceCampaignAllOf
from egoi-api.models.voice_campaign_template import VoiceCampaignTemplate
from egoi-api.models.voice_campaign_template_all_of import VoiceCampaignTemplateAllOf
from egoi-api.models.voice_patch_campaign import VoicePatchCampaign
from egoi-api.models.voice_patch_campaign_all_of import VoicePatchCampaignAllOf
from egoi-api.models.web_push_campaign import WebPushCampaign
from egoi-api.models.web_push_patch_campaign import WebPushPatchCampaign
from egoi-api.models.web_push_report import WebPushReport
from egoi-api.models.web_push_report_browsers import WebPushReportBrowsers
from egoi-api.models.web_push_report_operating_systems import WebPushReportOperatingSystems
from egoi-api.models.web_push_rss_campaign import WebPushRssCampaign
from egoi-api.models.web_push_site import WebPushSite
from egoi-api.models.web_push_stats import WebPushStats

