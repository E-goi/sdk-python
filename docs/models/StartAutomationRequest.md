# egoi_api.model.start_automation_request.StartAutomationRequest

Start automation to the provided contacts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Start automation to the provided contacts | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**automation_id** | [**QueryId**](QueryId.md) | [**QueryId**](QueryId.md) |  | 
**action_id** | [**QueryId**](QueryId.md) | [**QueryId**](QueryId.md) |  | 
**[contacts](#contacts)** | list, tuple,  | tuple,  | Array of contact IDs to start automation | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# contacts

Array of contact IDs to start automation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of contact IDs to start automation | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ContactBodyId**](ContactBodyId.md) | [**ContactBodyId**](ContactBodyId.md) | [**ContactBodyId**](ContactBodyId.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

