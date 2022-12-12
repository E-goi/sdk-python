# egoi_api.model.start_automation_response.StartAutomationResponse

Start automation to the provided contacts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Start automation to the provided contacts | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**automation_id** | [**Id**](Id.md) | [**Id**](Id.md) |  | [optional] 
**action_id** | [**Id**](Id.md) | [**Id**](Id.md) |  | [optional] 
**[success](#success)** | list, tuple,  | tuple,  | Array of contacts where the automation was successfully started | [optional] 
**[error](#error)** | list, tuple,  | tuple,  | Array of contacts where the automation was not successfully started | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# success

Array of contacts where the automation was successfully started

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of contacts where the automation was successfully started | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ContactId**](ContactId.md) | [**ContactId**](ContactId.md) | [**ContactId**](ContactId.md) |  | 

# error

Array of contacts where the automation was not successfully started

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of contacts where the automation was not successfully started | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ContactId**](ContactId.md) | [**ContactId**](ContactId.md) | [**ContactId**](ContactId.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

