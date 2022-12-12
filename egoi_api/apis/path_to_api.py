import typing_extensions

from egoi_api.paths import PathValues
from egoi_api.apis.paths.automations import Automations
from egoi_api.apis.paths.automations_automation_id import AutomationsAutomationId
from egoi_api.apis.paths.campaigns import Campaigns
from egoi_api.apis.paths.campaigns_campaign_hash import CampaignsCampaignHash
from egoi_api.apis.paths.campaigns_email_campaign_hash_actions_send import CampaignsEmailCampaignHashActionsSend
from egoi_api.apis.paths.campaigns_email import CampaignsEmail
from egoi_api.apis.paths.campaigns_email_campaign_hash import CampaignsEmailCampaignHash
from egoi_api.apis.paths.campaigns_email_rss_campaign_hash_actions_enable import CampaignsEmailRssCampaignHashActionsEnable
from egoi_api.apis.paths.campaigns_email_rss import CampaignsEmailRss
from egoi_api.apis.paths.campaigns_push_campaign_hash_actions_send import CampaignsPushCampaignHashActionsSend
from egoi_api.apis.paths.campaigns_push import CampaignsPush
from egoi_api.apis.paths.campaigns_push_campaign_hash import CampaignsPushCampaignHash
from egoi_api.apis.paths.campaigns_smart_sms_campaign_hash_actions_send import CampaignsSmartSmsCampaignHashActionsSend
from egoi_api.apis.paths.campaigns_smart_sms import CampaignsSmartSms
from egoi_api.apis.paths.campaigns_smart_sms_campaign_hash import CampaignsSmartSmsCampaignHash
from egoi_api.apis.paths.campaigns_sms_campaign_hash_actions_send import CampaignsSmsCampaignHashActionsSend
from egoi_api.apis.paths.campaigns_sms import CampaignsSms
from egoi_api.apis.paths.campaigns_sms_campaign_hash import CampaignsSmsCampaignHash
from egoi_api.apis.paths.campaigns_voice_campaign_hash_actions_send import CampaignsVoiceCampaignHashActionsSend
from egoi_api.apis.paths.campaigns_voice import CampaignsVoice
from egoi_api.apis.paths.campaigns_voice_campaign_hash import CampaignsVoiceCampaignHash
from egoi_api.apis.paths.campaigns_web_push_campaign_hash_actions_send import CampaignsWebPushCampaignHashActionsSend
from egoi_api.apis.paths.campaigns_web_push import CampaignsWebPush
from egoi_api.apis.paths.campaigns_web_push_campaign_hash import CampaignsWebPushCampaignHash
from egoi_api.apis.paths.campaigns_webpush_rss_campaign_hash_actions_enable import CampaignsWebpushRssCampaignHashActionsEnable
from egoi_api.apis.paths.campaigns_webpush_rss import CampaignsWebpushRss
from egoi_api.apis.paths.campaign_groups import CampaignGroups
from egoi_api.apis.paths.campaign_groups_group_id import CampaignGroupsGroupId
from egoi_api.apis.paths.connectedsites import Connectedsites
from egoi_api.apis.paths.connectedsites_domain import ConnectedsitesDomain
from egoi_api.apis.paths.lists_list_id_contacts_actions_activate import ListsListIdContactsActionsActivate
from egoi_api.apis.paths.lists_list_id_contacts_actions_attach_tag import ListsListIdContactsActionsAttachTag
from egoi_api.apis.paths.lists_list_id_contacts_actions_deactivate import ListsListIdContactsActionsDeactivate
from egoi_api.apis.paths.lists_list_id_contacts_actions_detach_tag import ListsListIdContactsActionsDetachTag
from egoi_api.apis.paths.lists_list_id_contacts_actions_export import ListsListIdContactsActionsExport
from egoi_api.apis.paths.lists_list_id_contacts_actions_forget import ListsListIdContactsActionsForget
from egoi_api.apis.paths.lists_list_id_contacts_actions_import_bulk import ListsListIdContactsActionsImportBulk
from egoi_api.apis.paths.lists_list_id_contacts_actions_unsubscribe import ListsListIdContactsActionsUnsubscribe
from egoi_api.apis.paths.lists_list_id_contacts_actions_start_automation import ListsListIdContactsActionsStartAutomation
from egoi_api.apis.paths.lists_list_id_contacts_actions_update import ListsListIdContactsActionsUpdate
from egoi_api.apis.paths.lists_list_id_contacts_contact_id_activities import ListsListIdContactsContactIdActivities
from egoi_api.apis.paths.lists_list_id_contacts import ListsListIdContacts
from egoi_api.apis.paths.lists_list_id_contacts_contact_id import ListsListIdContactsContactId
from egoi_api.apis.paths.contacts_search import ContactsSearch
from egoi_api.apis.paths.lists_list_id_contacts_segment_segment_id import ListsListIdContactsSegmentSegmentId
from egoi_api.apis.paths.cnames import Cnames
from egoi_api.apis.paths.domain_carts import DomainCarts
from egoi_api.apis.paths.catalogs import Catalogs
from egoi_api.apis.paths.catalogs_catalog_id import CatalogsCatalogId
from egoi_api.apis.paths.domain_orders import DomainOrders
from egoi_api.apis.paths.lists_list_id_orders import ListsListIdOrders
from egoi_api.apis.paths.catalogs_catalog_id_products_actions_import import CatalogsCatalogIdProductsActionsImport
from egoi_api.apis.paths.catalogs_catalog_id_products import CatalogsCatalogIdProducts
from egoi_api.apis.paths.catalogs_catalog_id_products_product_identifier import CatalogsCatalogIdProductsProductIdentifier
from egoi_api.apis.paths.lists_list_id_fields_base_field_id import ListsListIdFieldsBaseFieldId
from egoi_api.apis.paths.lists_list_id_fields_extra_field_id import ListsListIdFieldsExtraFieldId
from egoi_api.apis.paths.lists_list_id_fields_extra import ListsListIdFieldsExtra
from egoi_api.apis.paths.lists_list_id_fields import ListsListIdFields
from egoi_api.apis.paths.lists_list_id_fields_extra_field_id_options import ListsListIdFieldsExtraFieldIdOptions
from egoi_api.apis.paths.lists_list_id_fields_extra_field_id_options_option_id import ListsListIdFieldsExtraFieldIdOptionsOptionId
from egoi_api.apis.paths.lists import Lists
from egoi_api.apis.paths.lists_list_id import ListsListId
from egoi_api.apis.paths.my_account_actions_enable_te import MyAccountActionsEnableTe
from egoi_api.apis.paths.my_account_actions_enable_transactional import MyAccountActionsEnableTransactional
from egoi_api.apis.paths.my_account import MyAccount
from egoi_api.apis.paths.operations_actions_approve import OperationsActionsApprove
from egoi_api.apis.paths.operations_actions_cancel import OperationsActionsCancel
from egoi_api.apis.paths.operations_actions_pause import OperationsActionsPause
from egoi_api.apis.paths.operations_actions_resume import OperationsActionsResume
from egoi_api.apis.paths.operations import Operations
from egoi_api.apis.paths.ping import Ping
from egoi_api.apis.paths.push_apps import PushApps
from egoi_api.apis.paths.push_apps_app_id import PushAppsAppId
from egoi_api.apis.paths.push_apps_app_id_event import PushAppsAppIdEvent
from egoi_api.apis.paths.push_apps_app_id_token import PushAppsAppIdToken
from egoi_api.apis.paths.reports_advanced import ReportsAdvanced
from egoi_api.apis.paths.reports_advanced_email_bounces import ReportsAdvancedEmailBounces
from egoi_api.apis.paths.reports_advanced_email_clicks_by_contact import ReportsAdvancedEmailClicksByContact
from egoi_api.apis.paths.reports_advanced_email_clicks_by_url import ReportsAdvancedEmailClicksByUrl
from egoi_api.apis.paths.reports_advanced_email_events import ReportsAdvancedEmailEvents
from egoi_api.apis.paths.reports_advanced_email_unsubscriptions import ReportsAdvancedEmailUnsubscriptions
from egoi_api.apis.paths.reports_advanced_form_answers import ReportsAdvancedFormAnswers
from egoi_api.apis.paths.reports_advanced_sends import ReportsAdvancedSends
from egoi_api.apis.paths.reports_advanced_sms_bounces import ReportsAdvancedSmsBounces
from egoi_api.apis.paths.reports_advanced_sms_events import ReportsAdvancedSmsEvents
from egoi_api.apis.paths.reports_advanced_subscriptions import ReportsAdvancedSubscriptions
from egoi_api.apis.paths.reports_advanced_unsubscriptions import ReportsAdvancedUnsubscriptions
from egoi_api.apis.paths.reports_email_campaign_hash import ReportsEmailCampaignHash
from egoi_api.apis.paths.reports_sms_campaign_hash import ReportsSmsCampaignHash
from egoi_api.apis.paths.reports_voice_campaign_hash import ReportsVoiceCampaignHash
from egoi_api.apis.paths.reports_web_push_campaign_hash import ReportsWebPushCampaignHash
from egoi_api.apis.paths.lists_list_id_segments import ListsListIdSegments
from egoi_api.apis.paths.lists_list_id_segments_segment_id import ListsListIdSegmentsSegmentId
from egoi_api.apis.paths.senders_cellphone import SendersCellphone
from egoi_api.apis.paths.senders_cellphone_sender_id import SendersCellphoneSenderId
from egoi_api.apis.paths.senders_email import SendersEmail
from egoi_api.apis.paths.senders_email_sender_id import SendersEmailSenderId
from egoi_api.apis.paths.senders_phone import SendersPhone
from egoi_api.apis.paths.senders_phone_sender_id import SendersPhoneSenderId
from egoi_api.apis.paths.suppression_list import SuppressionList
from egoi_api.apis.paths.suppression_list_suppression_id import SuppressionListSuppressionId
from egoi_api.apis.paths.tags import Tags
from egoi_api.apis.paths.tags_tag_id import TagsTagId
from egoi_api.apis.paths.trackengage_domains import TrackengageDomains
from egoi_api.apis.paths.trackengage_goals import TrackengageGoals
from egoi_api.apis.paths.users import Users
from egoi_api.apis.paths.users_user_id import UsersUserId
from egoi_api.apis.paths.utilities_countries import UtilitiesCountries
from egoi_api.apis.paths.webpush_sites import WebpushSites
from egoi_api.apis.paths.webhooks import Webhooks
from egoi_api.apis.paths.webhooks_webhook_id import WebhooksWebhookId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AUTOMATIONS: Automations,
        PathValues.AUTOMATIONS_AUTOMATION_ID: AutomationsAutomationId,
        PathValues.CAMPAIGNS: Campaigns,
        PathValues.CAMPAIGNS_CAMPAIGN_HASH: CampaignsCampaignHash,
        PathValues.CAMPAIGNS_EMAIL_CAMPAIGN_HASH_ACTIONS_SEND: CampaignsEmailCampaignHashActionsSend,
        PathValues.CAMPAIGNS_EMAIL: CampaignsEmail,
        PathValues.CAMPAIGNS_EMAIL_CAMPAIGN_HASH: CampaignsEmailCampaignHash,
        PathValues.CAMPAIGNS_EMAIL_RSS_CAMPAIGN_HASH_ACTIONS_ENABLE: CampaignsEmailRssCampaignHashActionsEnable,
        PathValues.CAMPAIGNS_EMAIL_RSS: CampaignsEmailRss,
        PathValues.CAMPAIGNS_PUSH_CAMPAIGN_HASH_ACTIONS_SEND: CampaignsPushCampaignHashActionsSend,
        PathValues.CAMPAIGNS_PUSH: CampaignsPush,
        PathValues.CAMPAIGNS_PUSH_CAMPAIGN_HASH: CampaignsPushCampaignHash,
        PathValues.CAMPAIGNS_SMARTSMS_CAMPAIGN_HASH_ACTIONS_SEND: CampaignsSmartSmsCampaignHashActionsSend,
        PathValues.CAMPAIGNS_SMARTSMS: CampaignsSmartSms,
        PathValues.CAMPAIGNS_SMARTSMS_CAMPAIGN_HASH: CampaignsSmartSmsCampaignHash,
        PathValues.CAMPAIGNS_SMS_CAMPAIGN_HASH_ACTIONS_SEND: CampaignsSmsCampaignHashActionsSend,
        PathValues.CAMPAIGNS_SMS: CampaignsSms,
        PathValues.CAMPAIGNS_SMS_CAMPAIGN_HASH: CampaignsSmsCampaignHash,
        PathValues.CAMPAIGNS_VOICE_CAMPAIGN_HASH_ACTIONS_SEND: CampaignsVoiceCampaignHashActionsSend,
        PathValues.CAMPAIGNS_VOICE: CampaignsVoice,
        PathValues.CAMPAIGNS_VOICE_CAMPAIGN_HASH: CampaignsVoiceCampaignHash,
        PathValues.CAMPAIGNS_WEBPUSH_CAMPAIGN_HASH_ACTIONS_SEND: CampaignsWebPushCampaignHashActionsSend,
        PathValues.CAMPAIGNS_WEBPUSH: CampaignsWebPush,
        PathValues.CAMPAIGNS_WEBPUSH_CAMPAIGN_HASH: CampaignsWebPushCampaignHash,
        PathValues.CAMPAIGNS_WEBPUSH_RSS_CAMPAIGN_HASH_ACTIONS_ENABLE: CampaignsWebpushRssCampaignHashActionsEnable,
        PathValues.CAMPAIGNS_WEBPUSH_RSS: CampaignsWebpushRss,
        PathValues.CAMPAIGNGROUPS: CampaignGroups,
        PathValues.CAMPAIGNGROUPS_GROUP_ID: CampaignGroupsGroupId,
        PathValues.CONNECTEDSITES: Connectedsites,
        PathValues.CONNECTEDSITES_DOMAIN: ConnectedsitesDomain,
        PathValues.LISTS_LIST_ID_CONTACTS_ACTIONS_ACTIVATE: ListsListIdContactsActionsActivate,
        PathValues.LISTS_LIST_ID_CONTACTS_ACTIONS_ATTACHTAG: ListsListIdContactsActionsAttachTag,
        PathValues.LISTS_LIST_ID_CONTACTS_ACTIONS_DEACTIVATE: ListsListIdContactsActionsDeactivate,
        PathValues.LISTS_LIST_ID_CONTACTS_ACTIONS_DETACHTAG: ListsListIdContactsActionsDetachTag,
        PathValues.LISTS_LIST_ID_CONTACTS_ACTIONS_EXPORT: ListsListIdContactsActionsExport,
        PathValues.LISTS_LIST_ID_CONTACTS_ACTIONS_FORGET: ListsListIdContactsActionsForget,
        PathValues.LISTS_LIST_ID_CONTACTS_ACTIONS_IMPORTBULK: ListsListIdContactsActionsImportBulk,
        PathValues.LISTS_LIST_ID_CONTACTS_ACTIONS_UNSUBSCRIBE: ListsListIdContactsActionsUnsubscribe,
        PathValues.LISTS_LIST_ID_CONTACTS_ACTIONS_STARTAUTOMATION: ListsListIdContactsActionsStartAutomation,
        PathValues.LISTS_LIST_ID_CONTACTS_ACTIONS_UPDATE: ListsListIdContactsActionsUpdate,
        PathValues.LISTS_LIST_ID_CONTACTS_CONTACT_ID_ACTIVITIES: ListsListIdContactsContactIdActivities,
        PathValues.LISTS_LIST_ID_CONTACTS: ListsListIdContacts,
        PathValues.LISTS_LIST_ID_CONTACTS_CONTACT_ID: ListsListIdContactsContactId,
        PathValues.CONTACTS_SEARCH: ContactsSearch,
        PathValues.LISTS_LIST_ID_CONTACTS_SEGMENT_SEGMENT_ID: ListsListIdContactsSegmentSegmentId,
        PathValues.CNAMES: Cnames,
        PathValues.DOMAIN_CARTS: DomainCarts,
        PathValues.CATALOGS: Catalogs,
        PathValues.CATALOGS_CATALOG_ID: CatalogsCatalogId,
        PathValues.DOMAIN_ORDERS: DomainOrders,
        PathValues.LISTS_LIST_ID_ORDERS: ListsListIdOrders,
        PathValues.CATALOGS_CATALOG_ID_PRODUCTS_ACTIONS_IMPORT: CatalogsCatalogIdProductsActionsImport,
        PathValues.CATALOGS_CATALOG_ID_PRODUCTS: CatalogsCatalogIdProducts,
        PathValues.CATALOGS_CATALOG_ID_PRODUCTS_PRODUCT_IDENTIFIER: CatalogsCatalogIdProductsProductIdentifier,
        PathValues.LISTS_LIST_ID_FIELDS_BASE_FIELD_ID: ListsListIdFieldsBaseFieldId,
        PathValues.LISTS_LIST_ID_FIELDS_EXTRA_FIELD_ID: ListsListIdFieldsExtraFieldId,
        PathValues.LISTS_LIST_ID_FIELDS_EXTRA: ListsListIdFieldsExtra,
        PathValues.LISTS_LIST_ID_FIELDS: ListsListIdFields,
        PathValues.LISTS_LIST_ID_FIELDS_EXTRA_FIELD_ID_OPTIONS: ListsListIdFieldsExtraFieldIdOptions,
        PathValues.LISTS_LIST_ID_FIELDS_EXTRA_FIELD_ID_OPTIONS_OPTION_ID: ListsListIdFieldsExtraFieldIdOptionsOptionId,
        PathValues.LISTS: Lists,
        PathValues.LISTS_LIST_ID: ListsListId,
        PathValues.MYACCOUNT_ACTIONS_ENABLETE: MyAccountActionsEnableTe,
        PathValues.MYACCOUNT_ACTIONS_ENABLETRANSACTIONAL: MyAccountActionsEnableTransactional,
        PathValues.MYACCOUNT: MyAccount,
        PathValues.OPERATIONS_ACTIONS_APPROVE: OperationsActionsApprove,
        PathValues.OPERATIONS_ACTIONS_CANCEL: OperationsActionsCancel,
        PathValues.OPERATIONS_ACTIONS_PAUSE: OperationsActionsPause,
        PathValues.OPERATIONS_ACTIONS_RESUME: OperationsActionsResume,
        PathValues.OPERATIONS: Operations,
        PathValues.PING: Ping,
        PathValues.PUSH_APPS: PushApps,
        PathValues.PUSH_APPS_APP_ID: PushAppsAppId,
        PathValues.PUSH_APPS_APP_ID_EVENT: PushAppsAppIdEvent,
        PathValues.PUSH_APPS_APP_ID_TOKEN: PushAppsAppIdToken,
        PathValues.REPORTS_ADVANCED: ReportsAdvanced,
        PathValues.REPORTS_ADVANCED_EMAILBOUNCES: ReportsAdvancedEmailBounces,
        PathValues.REPORTS_ADVANCED_EMAILCLICKSBYCONTACT: ReportsAdvancedEmailClicksByContact,
        PathValues.REPORTS_ADVANCED_EMAILCLICKSBYURL: ReportsAdvancedEmailClicksByUrl,
        PathValues.REPORTS_ADVANCED_EMAILEVENTS: ReportsAdvancedEmailEvents,
        PathValues.REPORTS_ADVANCED_EMAILUNSUBSCRIPTIONS: ReportsAdvancedEmailUnsubscriptions,
        PathValues.REPORTS_ADVANCED_FORMANSWERS: ReportsAdvancedFormAnswers,
        PathValues.REPORTS_ADVANCED_SENDS: ReportsAdvancedSends,
        PathValues.REPORTS_ADVANCED_SMSBOUNCES: ReportsAdvancedSmsBounces,
        PathValues.REPORTS_ADVANCED_SMSEVENTS: ReportsAdvancedSmsEvents,
        PathValues.REPORTS_ADVANCED_SUBSCRIPTIONS: ReportsAdvancedSubscriptions,
        PathValues.REPORTS_ADVANCED_UNSUBSCRIPTIONS: ReportsAdvancedUnsubscriptions,
        PathValues.REPORTS_EMAIL_CAMPAIGN_HASH: ReportsEmailCampaignHash,
        PathValues.REPORTS_SMS_CAMPAIGN_HASH: ReportsSmsCampaignHash,
        PathValues.REPORTS_VOICE_CAMPAIGN_HASH: ReportsVoiceCampaignHash,
        PathValues.REPORTS_WEBPUSH_CAMPAIGN_HASH: ReportsWebPushCampaignHash,
        PathValues.LISTS_LIST_ID_SEGMENTS: ListsListIdSegments,
        PathValues.LISTS_LIST_ID_SEGMENTS_SEGMENT_ID: ListsListIdSegmentsSegmentId,
        PathValues.SENDERS_CELLPHONE: SendersCellphone,
        PathValues.SENDERS_CELLPHONE_SENDER_ID: SendersCellphoneSenderId,
        PathValues.SENDERS_EMAIL: SendersEmail,
        PathValues.SENDERS_EMAIL_SENDER_ID: SendersEmailSenderId,
        PathValues.SENDERS_PHONE: SendersPhone,
        PathValues.SENDERS_PHONE_SENDER_ID: SendersPhoneSenderId,
        PathValues.SUPPRESSIONLIST: SuppressionList,
        PathValues.SUPPRESSIONLIST_SUPPRESSION_ID: SuppressionListSuppressionId,
        PathValues.TAGS: Tags,
        PathValues.TAGS_TAG_ID: TagsTagId,
        PathValues.TRACKENGAGE_DOMAINS: TrackengageDomains,
        PathValues.TRACKENGAGE_GOALS: TrackengageGoals,
        PathValues.USERS: Users,
        PathValues.USERS_USER_ID: UsersUserId,
        PathValues.UTILITIES_COUNTRIES: UtilitiesCountries,
        PathValues.WEBPUSH_SITES: WebpushSites,
        PathValues.WEBHOOKS: Webhooks,
        PathValues.WEBHOOKS_WEBHOOK_ID: WebhooksWebhookId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AUTOMATIONS: Automations,
        PathValues.AUTOMATIONS_AUTOMATION_ID: AutomationsAutomationId,
        PathValues.CAMPAIGNS: Campaigns,
        PathValues.CAMPAIGNS_CAMPAIGN_HASH: CampaignsCampaignHash,
        PathValues.CAMPAIGNS_EMAIL_CAMPAIGN_HASH_ACTIONS_SEND: CampaignsEmailCampaignHashActionsSend,
        PathValues.CAMPAIGNS_EMAIL: CampaignsEmail,
        PathValues.CAMPAIGNS_EMAIL_CAMPAIGN_HASH: CampaignsEmailCampaignHash,
        PathValues.CAMPAIGNS_EMAIL_RSS_CAMPAIGN_HASH_ACTIONS_ENABLE: CampaignsEmailRssCampaignHashActionsEnable,
        PathValues.CAMPAIGNS_EMAIL_RSS: CampaignsEmailRss,
        PathValues.CAMPAIGNS_PUSH_CAMPAIGN_HASH_ACTIONS_SEND: CampaignsPushCampaignHashActionsSend,
        PathValues.CAMPAIGNS_PUSH: CampaignsPush,
        PathValues.CAMPAIGNS_PUSH_CAMPAIGN_HASH: CampaignsPushCampaignHash,
        PathValues.CAMPAIGNS_SMARTSMS_CAMPAIGN_HASH_ACTIONS_SEND: CampaignsSmartSmsCampaignHashActionsSend,
        PathValues.CAMPAIGNS_SMARTSMS: CampaignsSmartSms,
        PathValues.CAMPAIGNS_SMARTSMS_CAMPAIGN_HASH: CampaignsSmartSmsCampaignHash,
        PathValues.CAMPAIGNS_SMS_CAMPAIGN_HASH_ACTIONS_SEND: CampaignsSmsCampaignHashActionsSend,
        PathValues.CAMPAIGNS_SMS: CampaignsSms,
        PathValues.CAMPAIGNS_SMS_CAMPAIGN_HASH: CampaignsSmsCampaignHash,
        PathValues.CAMPAIGNS_VOICE_CAMPAIGN_HASH_ACTIONS_SEND: CampaignsVoiceCampaignHashActionsSend,
        PathValues.CAMPAIGNS_VOICE: CampaignsVoice,
        PathValues.CAMPAIGNS_VOICE_CAMPAIGN_HASH: CampaignsVoiceCampaignHash,
        PathValues.CAMPAIGNS_WEBPUSH_CAMPAIGN_HASH_ACTIONS_SEND: CampaignsWebPushCampaignHashActionsSend,
        PathValues.CAMPAIGNS_WEBPUSH: CampaignsWebPush,
        PathValues.CAMPAIGNS_WEBPUSH_CAMPAIGN_HASH: CampaignsWebPushCampaignHash,
        PathValues.CAMPAIGNS_WEBPUSH_RSS_CAMPAIGN_HASH_ACTIONS_ENABLE: CampaignsWebpushRssCampaignHashActionsEnable,
        PathValues.CAMPAIGNS_WEBPUSH_RSS: CampaignsWebpushRss,
        PathValues.CAMPAIGNGROUPS: CampaignGroups,
        PathValues.CAMPAIGNGROUPS_GROUP_ID: CampaignGroupsGroupId,
        PathValues.CONNECTEDSITES: Connectedsites,
        PathValues.CONNECTEDSITES_DOMAIN: ConnectedsitesDomain,
        PathValues.LISTS_LIST_ID_CONTACTS_ACTIONS_ACTIVATE: ListsListIdContactsActionsActivate,
        PathValues.LISTS_LIST_ID_CONTACTS_ACTIONS_ATTACHTAG: ListsListIdContactsActionsAttachTag,
        PathValues.LISTS_LIST_ID_CONTACTS_ACTIONS_DEACTIVATE: ListsListIdContactsActionsDeactivate,
        PathValues.LISTS_LIST_ID_CONTACTS_ACTIONS_DETACHTAG: ListsListIdContactsActionsDetachTag,
        PathValues.LISTS_LIST_ID_CONTACTS_ACTIONS_EXPORT: ListsListIdContactsActionsExport,
        PathValues.LISTS_LIST_ID_CONTACTS_ACTIONS_FORGET: ListsListIdContactsActionsForget,
        PathValues.LISTS_LIST_ID_CONTACTS_ACTIONS_IMPORTBULK: ListsListIdContactsActionsImportBulk,
        PathValues.LISTS_LIST_ID_CONTACTS_ACTIONS_UNSUBSCRIBE: ListsListIdContactsActionsUnsubscribe,
        PathValues.LISTS_LIST_ID_CONTACTS_ACTIONS_STARTAUTOMATION: ListsListIdContactsActionsStartAutomation,
        PathValues.LISTS_LIST_ID_CONTACTS_ACTIONS_UPDATE: ListsListIdContactsActionsUpdate,
        PathValues.LISTS_LIST_ID_CONTACTS_CONTACT_ID_ACTIVITIES: ListsListIdContactsContactIdActivities,
        PathValues.LISTS_LIST_ID_CONTACTS: ListsListIdContacts,
        PathValues.LISTS_LIST_ID_CONTACTS_CONTACT_ID: ListsListIdContactsContactId,
        PathValues.CONTACTS_SEARCH: ContactsSearch,
        PathValues.LISTS_LIST_ID_CONTACTS_SEGMENT_SEGMENT_ID: ListsListIdContactsSegmentSegmentId,
        PathValues.CNAMES: Cnames,
        PathValues.DOMAIN_CARTS: DomainCarts,
        PathValues.CATALOGS: Catalogs,
        PathValues.CATALOGS_CATALOG_ID: CatalogsCatalogId,
        PathValues.DOMAIN_ORDERS: DomainOrders,
        PathValues.LISTS_LIST_ID_ORDERS: ListsListIdOrders,
        PathValues.CATALOGS_CATALOG_ID_PRODUCTS_ACTIONS_IMPORT: CatalogsCatalogIdProductsActionsImport,
        PathValues.CATALOGS_CATALOG_ID_PRODUCTS: CatalogsCatalogIdProducts,
        PathValues.CATALOGS_CATALOG_ID_PRODUCTS_PRODUCT_IDENTIFIER: CatalogsCatalogIdProductsProductIdentifier,
        PathValues.LISTS_LIST_ID_FIELDS_BASE_FIELD_ID: ListsListIdFieldsBaseFieldId,
        PathValues.LISTS_LIST_ID_FIELDS_EXTRA_FIELD_ID: ListsListIdFieldsExtraFieldId,
        PathValues.LISTS_LIST_ID_FIELDS_EXTRA: ListsListIdFieldsExtra,
        PathValues.LISTS_LIST_ID_FIELDS: ListsListIdFields,
        PathValues.LISTS_LIST_ID_FIELDS_EXTRA_FIELD_ID_OPTIONS: ListsListIdFieldsExtraFieldIdOptions,
        PathValues.LISTS_LIST_ID_FIELDS_EXTRA_FIELD_ID_OPTIONS_OPTION_ID: ListsListIdFieldsExtraFieldIdOptionsOptionId,
        PathValues.LISTS: Lists,
        PathValues.LISTS_LIST_ID: ListsListId,
        PathValues.MYACCOUNT_ACTIONS_ENABLETE: MyAccountActionsEnableTe,
        PathValues.MYACCOUNT_ACTIONS_ENABLETRANSACTIONAL: MyAccountActionsEnableTransactional,
        PathValues.MYACCOUNT: MyAccount,
        PathValues.OPERATIONS_ACTIONS_APPROVE: OperationsActionsApprove,
        PathValues.OPERATIONS_ACTIONS_CANCEL: OperationsActionsCancel,
        PathValues.OPERATIONS_ACTIONS_PAUSE: OperationsActionsPause,
        PathValues.OPERATIONS_ACTIONS_RESUME: OperationsActionsResume,
        PathValues.OPERATIONS: Operations,
        PathValues.PING: Ping,
        PathValues.PUSH_APPS: PushApps,
        PathValues.PUSH_APPS_APP_ID: PushAppsAppId,
        PathValues.PUSH_APPS_APP_ID_EVENT: PushAppsAppIdEvent,
        PathValues.PUSH_APPS_APP_ID_TOKEN: PushAppsAppIdToken,
        PathValues.REPORTS_ADVANCED: ReportsAdvanced,
        PathValues.REPORTS_ADVANCED_EMAILBOUNCES: ReportsAdvancedEmailBounces,
        PathValues.REPORTS_ADVANCED_EMAILCLICKSBYCONTACT: ReportsAdvancedEmailClicksByContact,
        PathValues.REPORTS_ADVANCED_EMAILCLICKSBYURL: ReportsAdvancedEmailClicksByUrl,
        PathValues.REPORTS_ADVANCED_EMAILEVENTS: ReportsAdvancedEmailEvents,
        PathValues.REPORTS_ADVANCED_EMAILUNSUBSCRIPTIONS: ReportsAdvancedEmailUnsubscriptions,
        PathValues.REPORTS_ADVANCED_FORMANSWERS: ReportsAdvancedFormAnswers,
        PathValues.REPORTS_ADVANCED_SENDS: ReportsAdvancedSends,
        PathValues.REPORTS_ADVANCED_SMSBOUNCES: ReportsAdvancedSmsBounces,
        PathValues.REPORTS_ADVANCED_SMSEVENTS: ReportsAdvancedSmsEvents,
        PathValues.REPORTS_ADVANCED_SUBSCRIPTIONS: ReportsAdvancedSubscriptions,
        PathValues.REPORTS_ADVANCED_UNSUBSCRIPTIONS: ReportsAdvancedUnsubscriptions,
        PathValues.REPORTS_EMAIL_CAMPAIGN_HASH: ReportsEmailCampaignHash,
        PathValues.REPORTS_SMS_CAMPAIGN_HASH: ReportsSmsCampaignHash,
        PathValues.REPORTS_VOICE_CAMPAIGN_HASH: ReportsVoiceCampaignHash,
        PathValues.REPORTS_WEBPUSH_CAMPAIGN_HASH: ReportsWebPushCampaignHash,
        PathValues.LISTS_LIST_ID_SEGMENTS: ListsListIdSegments,
        PathValues.LISTS_LIST_ID_SEGMENTS_SEGMENT_ID: ListsListIdSegmentsSegmentId,
        PathValues.SENDERS_CELLPHONE: SendersCellphone,
        PathValues.SENDERS_CELLPHONE_SENDER_ID: SendersCellphoneSenderId,
        PathValues.SENDERS_EMAIL: SendersEmail,
        PathValues.SENDERS_EMAIL_SENDER_ID: SendersEmailSenderId,
        PathValues.SENDERS_PHONE: SendersPhone,
        PathValues.SENDERS_PHONE_SENDER_ID: SendersPhoneSenderId,
        PathValues.SUPPRESSIONLIST: SuppressionList,
        PathValues.SUPPRESSIONLIST_SUPPRESSION_ID: SuppressionListSuppressionId,
        PathValues.TAGS: Tags,
        PathValues.TAGS_TAG_ID: TagsTagId,
        PathValues.TRACKENGAGE_DOMAINS: TrackengageDomains,
        PathValues.TRACKENGAGE_GOALS: TrackengageGoals,
        PathValues.USERS: Users,
        PathValues.USERS_USER_ID: UsersUserId,
        PathValues.UTILITIES_COUNTRIES: UtilitiesCountries,
        PathValues.WEBPUSH_SITES: WebpushSites,
        PathValues.WEBHOOKS: Webhooks,
        PathValues.WEBHOOKS_WEBHOOK_ID: WebhooksWebhookId,
    }
)
