# egoi_api.model.email_report.EmailReport

Email report schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Email report schema | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[EmailReportOverall](EmailReportOverall.md) | [**EmailReportOverall**](EmailReportOverall.md) | [**EmailReportOverall**](EmailReportOverall.md) |  | 
[EmailReportByDate](EmailReportByDate.md) | [**EmailReportByDate**](EmailReportByDate.md) | [**EmailReportByDate**](EmailReportByDate.md) |  | 
[EmailReportByWeekday](EmailReportByWeekday.md) | [**EmailReportByWeekday**](EmailReportByWeekday.md) | [**EmailReportByWeekday**](EmailReportByWeekday.md) |  | 
[EmailReportByHour](EmailReportByHour.md) | [**EmailReportByHour**](EmailReportByHour.md) | [**EmailReportByHour**](EmailReportByHour.md) |  | 
[EmailReportByLocation](EmailReportByLocation.md) | [**EmailReportByLocation**](EmailReportByLocation.md) | [**EmailReportByLocation**](EmailReportByLocation.md) |  | 
[EmailReportByDomain](EmailReportByDomain.md) | [**EmailReportByDomain**](EmailReportByDomain.md) | [**EmailReportByDomain**](EmailReportByDomain.md) |  | 
[EmailReportByUrl](EmailReportByUrl.md) | [**EmailReportByUrl**](EmailReportByUrl.md) | [**EmailReportByUrl**](EmailReportByUrl.md) |  | 
[EmailReportByReader](EmailReportByReader.md) | [**EmailReportByReader**](EmailReportByReader.md) | [**EmailReportByReader**](EmailReportByReader.md) |  | 

# all_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**campaign_hash** | [**Hash**](Hash.md) | [**Hash**](Hash.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

