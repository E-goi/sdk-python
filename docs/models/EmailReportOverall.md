# egoi_api.model.email_report_overall.EmailReportOverall

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
**sends** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of sent messages | [optional] 
**opens** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of open messages | [optional] 
**unique_opens** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of unique open messages | [optional] 
**clicks** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of clicks in message | [optional] 
**unique_clicks** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of unique clicks in message | [optional] 
**hard_bounces** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of hard bounces | [optional] 
**soft_bounces** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of soft bounces | [optional] 
**complaints** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of complaints | [optional] 
**unsubscriptions** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of unsubscriptions | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

