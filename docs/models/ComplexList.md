# egoi_api.model.complex_list.ComplexList

Complex list schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Complex list schema | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[ModelList](ModelList.md) | [**ModelList**](ModelList.md) | [**ModelList**](ModelList.md) |  | 

# all_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**language** | [**Language**](Language.md) | [**Language**](Language.md) |  | [optional] 
**[stats](#stats)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Contact stats of the list | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# stats

Contact stats of the list

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Contact stats of the list | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total_contacts** | decimal.Decimal, int,  | decimal.Decimal,  | Number of total contacts in the list | [optional] 
**total_active** | decimal.Decimal, int,  | decimal.Decimal,  | Number of total active contacts in the list | [optional] 
**total_inactive** | decimal.Decimal, int,  | decimal.Decimal,  | Number of total inactive contacts in the list | [optional] 
**total_removed** | decimal.Decimal, int,  | decimal.Decimal,  | Number of total removed contacts in the list | [optional] 
**total_unconfirmed** | decimal.Decimal, int,  | decimal.Decimal,  | Number of total unconfirmed contacts in the list | [optional] 
**total_waiting_new_confirmation** | decimal.Decimal, int,  | decimal.Decimal,  | Number of total contacts waiting for new confirmation in the list | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

