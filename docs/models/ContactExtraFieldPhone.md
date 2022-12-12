# egoi_api.model.contact_extra_field_phone.ContactExtraFieldPhone

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**field_id** | [**QueryId**](QueryId.md) | [**QueryId**](QueryId.md) |  | [optional] 
**format** | str,  | str,  | Extra field format | [optional] must be one of ["phone", ] 
**value** | str,  | str,  | Extra field value | [optional] 
**status** | str,  | str,  | Extra field status | [optional] must be one of ["active", "inactive", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

