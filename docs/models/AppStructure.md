# egoi_api.model.app_structure.AppStructure

Structure of an E-goi app.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Structure of an E-goi app. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**app_id** | str,  | str,  | The ID of the app. | [optional] 
**[list](#list)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The list of the app. | [optional] 
**name** | str,  | str,  | The name of the app. | [optional] 
**description** | str,  | str,  | The description of the app. | [optional] 
**two_steps_config** | str,  | str,  | The column of the list used to map the token. | [optional] 
**development** | bool,  | BoolClass,  | Is app a development app. | [optional] 
**created** | str,  | str,  | When the app was created. | [optional] 
**updated** | str,  | str,  | The last time the app was updated. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# list

The list of the app.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The list of the app. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The ID of the list. | [optional] 
**internal_name** | str,  | str,  | The internal name of the list. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

