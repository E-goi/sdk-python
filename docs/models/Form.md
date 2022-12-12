# egoi_api.model.form.Form

Form schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Form schema | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**title** | str,  | str,  | Title of the form | 
**form_id** | [**Id**](Id.md) | [**Id**](Id.md) |  | [optional] 
**internal_title** | str,  | str,  | Internal title of the form | [optional] if omitted the server will use the default value of "$request.body#/title"
**language** | [**Language**](Language.md) | [**Language**](Language.md) |  | [optional] 
**list_id** | [**QueryId**](QueryId.md) | [**QueryId**](QueryId.md) |  | [optional] 
**default** | bool,  | BoolClass,  | True if this is the default form in the list, false otherwise | [optional] 
**owner** | [**QueryId**](QueryId.md) | [**QueryId**](QueryId.md) |  | [optional] 
**status** | str,  | str,  | Status of the form | [optional] must be one of ["active", "unpublished", "cloned", "deleted", ] 
**created** | str, datetime,  | str,  | The date and time | [optional] value must conform to RFC-3339 date-time
**updated** | str, datetime,  | str,  | The date and time | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

