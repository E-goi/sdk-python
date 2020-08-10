# CampaignSmartSmsScheduleRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_date** | **datetime** | The date and time | [optional] 
**list_id** | **int** |  | 
**destination_field** | **str** | Smart SMS campaign destination field. Must be &#39;cellphone&#39; or the other field ID of type                                 cellphone | 
**segments** | [**SmartSmsSegmentsActionSend**](SmartSmsSegmentsActionSend.md) |  | 
**limit_hour** | [**LimitHourActionSendLimitHour**](LimitHourActionSendLimitHour.md) |  | [optional] 
**notify** | **list[int]** | Array of IDs of the users to notify | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


