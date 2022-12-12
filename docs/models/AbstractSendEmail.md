# egoi_api.model.abstract_send_email.AbstractSendEmail

Campaign email abstract schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Campaign email abstract schema | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**list_id** | [**QueryId**](QueryId.md) | [**QueryId**](QueryId.md) |  | 
**segments** | [**EmailSendSegment**](EmailSendSegment.md) | [**EmailSendSegment**](EmailSendSegment.md) |  | 
**[notify](#notify)** | list, tuple,  | tuple,  | Array of IDs of the users to notify | [optional] 
**destination_field** | str,  | str,  | Destination field of this campaign, which must be an email field (email or extra field id).                         If not sent, defaults to the general email field | [optional] 
**unique_contacts_only** | bool,  | BoolClass,  | True to send the campaign only to unique contacts | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# notify

Array of IDs of the users to notify

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of IDs of the users to notify | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

