# CampaignVoiceScheduleRequest

Campaign voice schedule request schema
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_date** | **datetime** | The date and time | [optional] 
**list_id** | **int** |  | 
**segments** | [**OSegmentsActionSend**](OSegmentsActionSend.md) |  | 
**notify** | **list[int]** | Array of IDs of the users to notify | [optional] 
**destination_field** | **str** | Destination field of this campaign | 
**limit_contacts** | [**OLimitContactsActionSend**](OLimitContactsActionSend.md) |  | [optional] 
**limit_hour** | [**LimitHourActionSendLimitHour**](LimitHourActionSendLimitHour.md) |  | [optional] 
**limit_speed** | **int** | Speed limit to send the campaign | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


