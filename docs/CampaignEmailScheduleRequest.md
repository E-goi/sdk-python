# CampaignEmailScheduleRequest

Campaign email schedule request schema
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_date** | **datetime** | The date and time | [optional] 
**list_id** | **int** |  | 
**segments** | [**EmailSendSegment**](EmailSendSegment.md) |  | 
**notify** | **list[int]** | Array of IDs of the users to notify | [optional] 
**destination_field** | **str** | Destination field of this campaign, which must be an email field (email or extra field id).                         If not sent, defaults to the general email field | [optional] 
**unique_contacts_only** | **bool** | True to send the campaign only to unique contacts | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


