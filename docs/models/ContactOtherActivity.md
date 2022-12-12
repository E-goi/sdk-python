# egoi_api.model.contact_other_activity.ContactOtherActivity

Other contact activity schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Other contact activity schema | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date** | str, datetime,  | str,  | The date and time | [optional] value must conform to RFC-3339 date-time
**action_name** | str,  | str,  | Action name | [optional] must be one of ["email_open", "forward", "conversion", "email_send", "sms_send", "voice_send", "mms_send", "sms_report", "voice_report", "invitation_send", "invitation_open", "mms_open", "unsubscribe", "email_soft_bounce", "email_hard_bounce", "subscription", "resubscription", "unsubscribe_reason", "facebook_like", "social_share", "unsubscribe_manual", "double_optin", "double_optin_resend", "email_spam_complaint", "email_field_disable", "cellphone_field_disable", "phone_field_disable", "unsubscribe_api", "email_field_enable", "cellphone_field_enable", "phone_field_enable", "edit_subscription", "double_optedit", "automation_event", "push_send", "push_open", "push_received", "push_error", "push_canceled", "reply_to_email", "web_push_send", "web_push_delivered", "web_push_open", "web_push_bounce", "web_push_subscription", "web_push_unsubscription", "add_push_contact", "remove_push_contact", "forget_subscription", "change_consent", "push_unsubscription", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

