# egoi_api.model.country.Country

Country schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Country schema | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**country** | [**Id**](Id.md) | [**Id**](Id.md) |  | [optional] 
**name** | str,  | str,  | Name of the country | [optional] 
**iso_code** | str,  | str,  | ISO code of the country | [optional] 
**currency** | str,  | str,  | Currency of the country | [optional] 
**country_code** | str,  | str,  | Country code to be used in phone numbers | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

