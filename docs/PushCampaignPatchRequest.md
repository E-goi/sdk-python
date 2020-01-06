# PushCampaignPatchRequest

Push campaign patch request schema
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_hash** | **str** |  | [optional] [readonly] 
**title** | **str** | Push campaign subject | [optional] 
**content** | [**PushCampaignPatchRequestContent**](PushCampaignPatchRequestContent.md) |  | [optional] 
**actions** | [**list[PushCampaignPostRequestActions]**](PushCampaignPostRequestActions.md) | Actions for push campaign | [optional] 
**geo_options** | [**PushCampaignPostRequestGeoOptions**](PushCampaignPostRequestGeoOptions.md) |  | [optional] 
**notification_options** | [**PushCampaignPostRequestNotificationOptions**](PushCampaignPostRequestNotificationOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


