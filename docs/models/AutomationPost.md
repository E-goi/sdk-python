# egoi_api.model.automation_post.AutomationPost

Automation schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Automation schema | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**title** | str,  | str,  | Automation title | [optional] 
**list_id** | [**QueryId**](QueryId.md) | [**QueryId**](QueryId.md) |  | [optional] 
**status** | str,  | str,  | Automation status | [optional] must be one of ["active", "inactive", ] 
**allow_multiple_contacts** | bool,  | BoolClass,  | True if the automation allows multiple contacts, false otherwise | [optional] if omitted the server will use the default value of True
**contact_limit** | decimal.Decimal, int,  | decimal.Decimal,  | Contact limit for the automation. Contact limit value (value &#x27;0&#x27; is returned if contact limit is not enabled) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

