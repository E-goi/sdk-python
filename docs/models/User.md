# egoi_api.model.user.User

User schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | User schema | 

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
**user_id** | [**Id**](Id.md) | [**Id**](Id.md) |  | [optional] 
**username** | str,  | str,  | User login | [optional] 
**is_admin** | bool,  | BoolClass,  | True if user is admin, false otherwise | [optional] if omitted the server will use the default value of False
**first_name** | str,  | str,  | First name of the user | [optional] 
**last_name** | str,  | str,  | Last name of the user | [optional] 
**email** | str,  | str,  | Email of the user | [optional] 
**phone** | str,  | str,  | User&#x27;s phone (may be cellphone or phone) | [optional] 
**profile_image** | str,  | str,  | User&#x27;s profile image | [optional] 
**status** | str,  | str,  | User status | [optional] must be one of ["active", "inactive", ] 
**created** | str, datetime,  | str,  | The date and time | [optional] value must conform to RFC-3339 date-time
**updated** | str, datetime,  | str,  | The date and time | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

