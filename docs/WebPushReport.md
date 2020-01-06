# WebPushReport

Webpush report schema
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_hash** | **str** |  | [optional] [readonly] 
**overall** | [**WebPushStats**](WebPushStats.md) |  | [optional] 
**devices** | **list[object]** | Stats of the campaign for each device | [optional] 
**operating_systems** | [**list[WebPushReportOperatingSystems]**](WebPushReportOperatingSystems.md) | Stats of the campaign for each operating system | [optional] 
**browsers** | [**list[WebPushReportBrowsers]**](WebPushReportBrowsers.md) | Stats of the campaign for each browser | [optional] 
**url** | **list[object]** | Stats of the campaign for each url | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


