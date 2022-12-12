# egoi_api.model.contact_status_fields_schema.ContactStatusFieldsSchema

Contact status schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Contact status schema | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**email_status** | str,  | str,  | Email channel status | [optional] must be one of ["active", "inactive", ] 
**cellphone_status** | str,  | str,  | Cellphone channel status | [optional] must be one of ["active", "inactive", ] 
**phone_status** | str,  | str,  | Phone channel status | [optional] must be one of ["active", "inactive", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

