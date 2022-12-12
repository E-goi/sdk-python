# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from egoi_api.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    PUSH = "Push"
    ADVANCED_REPORTS = "Advanced Reports"
    AUTOMATIONS = "Automations"
    CNAMES = "CNames"
    CAMPAIGN_GROUPS = "Campaign Groups"
    CAMPAIGNS = "Campaigns"
    CONNECTED_SITES = "Connected Sites"
    CONTACTS = "Contacts"
    ECOMMERCE = "Ecommerce"
    ECOMMERCE_ACTIVITY = "Ecommerce Activity"
    EMAIL = "Email"
    FIELDS = "Fields"
    LISTS = "Lists"
    MY_ACCOUNT = "My Account"
    OPERATIONS = "Operations"
    PING = "Ping"
    REPORTS = "Reports"
    SEGMENTS = "Segments"
    SENDERS = "Senders"
    SMART_SMS = "Smart Sms"
    SMS = "Sms"
    SUPPRESSION_LIST = "Suppression List"
    TAGS = "Tags"
    TRACK_ENGAGE = "TrackEngage"
    USERS = "Users"
    UTILITIES = "Utilities"
    VOICE = "Voice"
    WEB_HOOKS = "Web Hooks"
    WEBPUSH = "Webpush"
