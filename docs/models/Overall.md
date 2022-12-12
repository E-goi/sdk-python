# egoi_api.model.overall.Overall

Overall stats schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Overall stats schema | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[overall](#overall)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Overall message information | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# overall

Overall message information

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Overall message information | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**destinations** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of destinations | [optional] 
**sends** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of sent messages | [optional] 
**delivered** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of delivered messages | [optional] 
**error** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of failed messages | [optional] 
**invalid** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of invalid messages | [optional] 
**pending** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of pending messages | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

