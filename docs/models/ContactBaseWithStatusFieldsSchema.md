# egoi_api.model.contact_base_with_status_fields_schema.ContactBaseWithStatusFieldsSchema

Contact base

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Contact base | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[base](#base)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Contact base fields | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# base

Contact base fields

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Contact base fields | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**contact_id** | [**ContactId**](ContactId.md) | [**ContactId**](ContactId.md) |  | [optional] 
**status** | str,  | str,  | Status of the contact | [optional] must be one of ["active", "inactive", "removed", "unconfirmed", ] if omitted the server will use the default value of "active"
**consent** | str,  | str,  | Contact consent | [optional] must be one of ["any", "consent", "contract", "legitimate_interest", "none", "protect_vital_interests", "public_interests", "required_by_law", "withdrawn", ] 
**first_name** | str,  | str,  | First name of the contact | [optional] 
**last_name** | str,  | str,  | Last name of the contact | [optional] 
**birth_date** | str, date,  | str,  | Birth date of the contact | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**language** | [**Language**](Language.md) | [**Language**](Language.md) |  | [optional] 
**email** | str,  | str,  | Email of the contact | [optional] 
**email_status** | str,  | str,  | Email channel status | [optional] must be one of ["active", "inactive", ] 
**cellphone** | str,  | str,  | Cellphone of the contact | [optional] 
**cellphone_status** | str,  | str,  | Cellphone channel status | [optional] must be one of ["active", "inactive", ] 
**phone** | str,  | str,  | Phone of the contact | [optional] 
**phone_status** | str,  | str,  | Phone channel status | [optional] must be one of ["active", "inactive", ] 
**[push_token_android](#push_token_android)** | list, tuple,  | tuple,  | Android push token of the contact | [optional] 
**[push_token_ios](#push_token_ios)** | list, tuple,  | tuple,  | IOS push token of the contact | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# push_token_android

Android push token of the contact

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Android push token of the contact | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**app_id** | [**PushAppId**](PushAppId.md) | [**PushAppId**](PushAppId.md) |  | [optional] 
**token** | str,  | str,  | Android push app ID | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# push_token_ios

IOS push token of the contact

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | IOS push token of the contact | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**app_id** | [**PushAppId**](PushAppId.md) | [**PushAppId**](PushAppId.md) |  | [optional] 
**token** | str,  | str,  | Ios push app ID | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

