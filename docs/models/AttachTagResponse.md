# egoi_api.model.attach_tag_response.AttachTagResponse

Attach tag to contact response schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Attach tag to contact response schema | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**tag_id** | [**Id**](Id.md) | [**Id**](Id.md) |  | [optional] 
**[success](#success)** | list, tuple,  | tuple,  | Array of contacts where the tag was successfully attached | [optional] 
**[error](#error)** | list, tuple,  | tuple,  | Array of contacts where the tag was not successfully attached | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# success

Array of contacts where the tag was successfully attached

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of contacts where the tag was successfully attached | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ContactId**](ContactId.md) | [**ContactId**](ContactId.md) | [**ContactId**](ContactId.md) |  | 

# error

Array of contacts where the tag was not successfully attached

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of contacts where the tag was not successfully attached | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ContactId**](ContactId.md) | [**ContactId**](ContactId.md) | [**ContactId**](ContactId.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

