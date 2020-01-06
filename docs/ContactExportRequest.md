# ContactExportRequest

Contact export request schema
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | File extension to export contacts | 
**callback_url** | **str** | Url to receive the webhook | [optional] 
**segments** | **list[str]** | Array of segment IDs to filter contacts to export. ***Note:*** segments of type ***auto*** and                         ***tag*** are not yet supported but they are expected to be supported soon! | [optional] 
**fields** | **list[str]** | Array of field IDs to be displayed in the exported file | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


