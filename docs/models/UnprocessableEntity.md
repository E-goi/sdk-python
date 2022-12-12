# egoi_api.model.unprocessable_entity.UnprocessableEntity

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[errors](#errors)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Information about the input validation | [optional] 
**type** | str,  | str,  | RFC for status code definitions | [optional] 
**title** | str,  | str,  | Error title | [optional] must be one of ["Unprocessable Entity", ] 
**status** | decimal.Decimal, int,  | decimal.Decimal,  | Status code | [optional] 
**detail** | str,  | str,  | Error detail | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# errors

Information about the input validation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Information about the input validation | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

