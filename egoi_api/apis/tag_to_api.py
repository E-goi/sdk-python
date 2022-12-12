import typing_extensions

from egoi_api.apis.tags import TagValues
from egoi_api.apis.tags.push_api import PushApi
from egoi_api.apis.tags.advanced_reports_api import AdvancedReportsApi
from egoi_api.apis.tags.automations_api import AutomationsApi
from egoi_api.apis.tags.c_names_api import CNamesApi
from egoi_api.apis.tags.campaign_groups_api import CampaignGroupsApi
from egoi_api.apis.tags.campaigns_api import CampaignsApi
from egoi_api.apis.tags.connected_sites_api import ConnectedSitesApi
from egoi_api.apis.tags.contacts_api import ContactsApi
from egoi_api.apis.tags.ecommerce_api import EcommerceApi
from egoi_api.apis.tags.ecommerce_activity_api import EcommerceActivityApi
from egoi_api.apis.tags.email_api import EmailApi
from egoi_api.apis.tags.fields_api import FieldsApi
from egoi_api.apis.tags.lists_api import ListsApi
from egoi_api.apis.tags.my_account_api import MyAccountApi
from egoi_api.apis.tags.operations_api import OperationsApi
from egoi_api.apis.tags.ping_api import PingApi
from egoi_api.apis.tags.reports_api import ReportsApi
from egoi_api.apis.tags.segments_api import SegmentsApi
from egoi_api.apis.tags.senders_api import SendersApi
from egoi_api.apis.tags.smart_sms_api import SmartSmsApi
from egoi_api.apis.tags.sms_api import SmsApi
from egoi_api.apis.tags.suppression_list_api import SuppressionListApi
from egoi_api.apis.tags.tags_api import TagsApi
from egoi_api.apis.tags.track_engage_api import TrackEngageApi
from egoi_api.apis.tags.users_api import UsersApi
from egoi_api.apis.tags.utilities_api import UtilitiesApi
from egoi_api.apis.tags.voice_api import VoiceApi
from egoi_api.apis.tags.web_hooks_api import WebHooksApi
from egoi_api.apis.tags.webpush_api import WebpushApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PUSH: PushApi,
        TagValues.ADVANCED_REPORTS: AdvancedReportsApi,
        TagValues.AUTOMATIONS: AutomationsApi,
        TagValues.CNAMES: CNamesApi,
        TagValues.CAMPAIGN_GROUPS: CampaignGroupsApi,
        TagValues.CAMPAIGNS: CampaignsApi,
        TagValues.CONNECTED_SITES: ConnectedSitesApi,
        TagValues.CONTACTS: ContactsApi,
        TagValues.ECOMMERCE: EcommerceApi,
        TagValues.ECOMMERCE_ACTIVITY: EcommerceActivityApi,
        TagValues.EMAIL: EmailApi,
        TagValues.FIELDS: FieldsApi,
        TagValues.LISTS: ListsApi,
        TagValues.MY_ACCOUNT: MyAccountApi,
        TagValues.OPERATIONS: OperationsApi,
        TagValues.PING: PingApi,
        TagValues.REPORTS: ReportsApi,
        TagValues.SEGMENTS: SegmentsApi,
        TagValues.SENDERS: SendersApi,
        TagValues.SMART_SMS: SmartSmsApi,
        TagValues.SMS: SmsApi,
        TagValues.SUPPRESSION_LIST: SuppressionListApi,
        TagValues.TAGS: TagsApi,
        TagValues.TRACK_ENGAGE: TrackEngageApi,
        TagValues.USERS: UsersApi,
        TagValues.UTILITIES: UtilitiesApi,
        TagValues.VOICE: VoiceApi,
        TagValues.WEB_HOOKS: WebHooksApi,
        TagValues.WEBPUSH: WebpushApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PUSH: PushApi,
        TagValues.ADVANCED_REPORTS: AdvancedReportsApi,
        TagValues.AUTOMATIONS: AutomationsApi,
        TagValues.CNAMES: CNamesApi,
        TagValues.CAMPAIGN_GROUPS: CampaignGroupsApi,
        TagValues.CAMPAIGNS: CampaignsApi,
        TagValues.CONNECTED_SITES: ConnectedSitesApi,
        TagValues.CONTACTS: ContactsApi,
        TagValues.ECOMMERCE: EcommerceApi,
        TagValues.ECOMMERCE_ACTIVITY: EcommerceActivityApi,
        TagValues.EMAIL: EmailApi,
        TagValues.FIELDS: FieldsApi,
        TagValues.LISTS: ListsApi,
        TagValues.MY_ACCOUNT: MyAccountApi,
        TagValues.OPERATIONS: OperationsApi,
        TagValues.PING: PingApi,
        TagValues.REPORTS: ReportsApi,
        TagValues.SEGMENTS: SegmentsApi,
        TagValues.SENDERS: SendersApi,
        TagValues.SMART_SMS: SmartSmsApi,
        TagValues.SMS: SmsApi,
        TagValues.SUPPRESSION_LIST: SuppressionListApi,
        TagValues.TAGS: TagsApi,
        TagValues.TRACK_ENGAGE: TrackEngageApi,
        TagValues.USERS: UsersApi,
        TagValues.UTILITIES: UtilitiesApi,
        TagValues.VOICE: VoiceApi,
        TagValues.WEB_HOOKS: WebHooksApi,
        TagValues.WEBPUSH: WebpushApi,
    }
)
