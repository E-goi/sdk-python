# egoi_api.model.contact_activity_abstract_actions_with_campaign.ContactActivityAbstractActionsWithCampaign

Campaign contact activity schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Campaign contact activity schema | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date** | str, datetime,  | str,  | The date and time | [optional] value must conform to RFC-3339 date-time
**action_name** | str,  | str,  | Action name | [optional] must be one of ["email_open", "forward", "email_send", "sms_send", "voice_send", "sms_report", "voice_report", "invitation_send", "invitation_open", "email_soft_bounce", "email_hard_bounce", "double_optin", "double_optin_resend", "email_spam_complaint", "double_optedit", "push_send", "push_open", "push_received", "push_error", "push_canceled", "reply_to_email", "web_push_send", "web_push_delivered", "web_push_open", "web_push_bounce", "voice_menu_event", "voice_redirect", "push_delivered", "smart_sms_send", "smart_sms_open", "smart_sms_report", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

