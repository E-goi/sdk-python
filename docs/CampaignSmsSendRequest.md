# CampaignSmsSendRequest

Campaign sms send request schema
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | **int** |  | 
**destination_field** | **str** | SMS campaign destination field. Must be &#39;cellphone&#39; or the other field ID of type                                 cellphone | 
**segments** | [**SmsSegmentsActionSend**](SmsSegmentsActionSend.md) |  | 
**notify** | **list[int]** | Array of IDs of the users to notify | [optional] 
**schedule_date** | **datetime** | The date and time | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


