# egoi_api.model.generate_sms_bounces_report.GenerateSmsBouncesReport

Generate SMS bounces report schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Generate SMS bounces report schema | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**campaigns** | [**AdvancedReportCampaigns**](AdvancedReportCampaigns.md) | [**AdvancedReportCampaigns**](AdvancedReportCampaigns.md) |  | 
**columns** | [**AdvancedReportSmsBouncesColumns**](AdvancedReportSmsBouncesColumns.md) | [**AdvancedReportSmsBouncesColumns**](AdvancedReportSmsBouncesColumns.md) |  | 
**options** | [**AdvancedReportSmsBouncesOptions**](AdvancedReportSmsBouncesOptions.md) | [**AdvancedReportSmsBouncesOptions**](AdvancedReportSmsBouncesOptions.md) |  | 
**range** | [**AdvancedReportRange**](AdvancedReportRange.md) | [**AdvancedReportRange**](AdvancedReportRange.md) |  | 
**title** | str,  | str,  | Advanced report title | 
**callback_url** | str,  | str,  | URL which will receive the information of the report&lt;a href&#x3D;&#x27;/usecases/callbacks/&#x27; target&#x3D;&#x27;_blank&#x27;&gt;[Go to callback documentation]&lt;/a&gt; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

