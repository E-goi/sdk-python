# egoi_api.model.generate_sends_report.GenerateSendsReport

Generate sends report schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Generate sends report schema | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**columns** | [**AdvancedReportSendsColumns**](AdvancedReportSendsColumns.md) | [**AdvancedReportSendsColumns**](AdvancedReportSendsColumns.md) |  | 
**[lists](#lists)** | list, tuple,  | tuple,  | Array of List Id&#x27;s | 
**options** | [**AdvancedReportSendsOptions**](AdvancedReportSendsOptions.md) | [**AdvancedReportSendsOptions**](AdvancedReportSendsOptions.md) |  | 
**range** | [**AdvancedReportRange**](AdvancedReportRange.md) | [**AdvancedReportRange**](AdvancedReportRange.md) |  | 
**title** | str,  | str,  | Advanced report title | 
**callback_url** | str,  | str,  | URL which will receive the information of the report | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# lists

Array of List Id's

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of List Id&#x27;s | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Id**](Id.md) | [**Id**](Id.md) | [**Id**](Id.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

