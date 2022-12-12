# egoi_api.model.send_push.SendPush

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[SegmentsWithoutContactActionSend](SegmentsWithoutContactActionSend.md) | [**SegmentsWithoutContactActionSend**](SegmentsWithoutContactActionSend.md) | [**SegmentsWithoutContactActionSend**](SegmentsWithoutContactActionSend.md) |  | 
[NotifyUserIdArrayActionSend](NotifyUserIdArrayActionSend.md) | [**NotifyUserIdArrayActionSend**](NotifyUserIdArrayActionSend.md) | [**NotifyUserIdArrayActionSend**](NotifyUserIdArrayActionSend.md) |  | 

# all_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**app_id** | [**PushAppId**](PushAppId.md) | [**PushAppId**](PushAppId.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

