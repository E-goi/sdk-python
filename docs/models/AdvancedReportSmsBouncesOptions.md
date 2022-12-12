# egoi_api.model.advanced_report_sms_bounces_options.AdvancedReportSmsBouncesOptions

Columns of the report

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Columns of the report | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[notify](#notify)** | list, tuple,  | tuple,  | Array of user IDs to notify | [optional] 
**grouping** | str,  | str,  | Field to group data | [optional] must be one of ["by_contact", "by_campaign", ] if omitted the server will use the default value of "by_campaign"
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# notify

Array of user IDs to notify

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of user IDs to notify | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**QueryId**](QueryId.md) | [**QueryId**](QueryId.md) | [**QueryId**](QueryId.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

