# egoi_api.model.abstract_send_voice.AbstractSendVoice

Campaign voice abstract schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Campaign voice abstract schema | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[all_of_2](#all_of_2) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[SegmentsActionSend](SegmentsActionSend.md) | [**SegmentsActionSend**](SegmentsActionSend.md) | [**SegmentsActionSend**](SegmentsActionSend.md) |  | 
[NotifyUserIdArrayActionSend](NotifyUserIdArrayActionSend.md) | [**NotifyUserIdArrayActionSend**](NotifyUserIdArrayActionSend.md) | [**NotifyUserIdArrayActionSend**](NotifyUserIdArrayActionSend.md) |  | 
[LimitContactsActionSend](LimitContactsActionSend.md) | [**LimitContactsActionSend**](LimitContactsActionSend.md) | [**LimitContactsActionSend**](LimitContactsActionSend.md) |  | 
[LimitHourActionSend](LimitHourActionSend.md) | [**LimitHourActionSend**](LimitHourActionSend.md) | [**LimitHourActionSend**](LimitHourActionSend.md) |  | 
[LimitSpeedActionSend](LimitSpeedActionSend.md) | [**LimitSpeedActionSend**](LimitSpeedActionSend.md) | [**LimitSpeedActionSend**](LimitSpeedActionSend.md) |  | 

# all_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**list_id** | [**QueryId**](QueryId.md) | [**QueryId**](QueryId.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**destination_field** | str,  | str,  | Destination field of this campaign | [optional] must be one of ["phone", "cellphone", "phone_failsafe_cellphone", "cellphone_failsafe_phone", "cellphone_phone", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# all_of_2

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**unique_contacts_only** | bool,  | BoolClass,  | True to send the campaign only to unique contacts | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

