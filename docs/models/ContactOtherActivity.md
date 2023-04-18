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
**action_name** | str,  | str,  | Action name | [optional] must be one of ["subscription", "unsubscribe", "unsubscribe_api", "unsubscribe_manual", "unsubscribe_reason", "edit_subscription", "resubscription", "conversion", "facebook_like", "social_share", "cellphone_field_disable", "email_field_disable", "phone_field_disable", "email_field_enable", "cellphone_field_enable", "phone_field_enable", "web_push_subscription", "web_push_unsubscription", "add_push_contact", "remove_push_contact", "forget_subscription", "change_consent", "push_unsubscription", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

