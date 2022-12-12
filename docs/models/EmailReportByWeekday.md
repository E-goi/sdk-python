# egoi_api.model.email_report_by_weekday.EmailReportByWeekday

Email stats grouped by Weekday

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Email stats grouped by Weekday | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[weekday](#weekday)** | list, tuple,  | tuple,  | Email stats grouped by date | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# weekday

Email stats grouped by date

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Email stats grouped by date | 

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
**weekday** | str,  | str,  | Numeric representation of the day of the week (0 for sunday) | [optional] 
**sends** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of sent messages | [optional] 
**opens** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of open messages | [optional] 
**clicks** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of clicks in message | [optional] 
**hard_bounces** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of hard bounces | [optional] 
**soft_bounces** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of soft bounces | [optional] 
**complaints** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of complaints | [optional] 
**unsubscriptions** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of unsubscriptions | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

