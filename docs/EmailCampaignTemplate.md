# EmailCampaignTemplate

Email campaign template schema
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **int** |  | [optional] [readonly] 
**template_hash** | **str** |  | [optional] [readonly] 
**internal_name** | **str** | Campaign internal name | [optional] 
**created** | **datetime** |  | [optional] [readonly] 
**updated** | **datetime** |  | [optional] [readonly] 
**sender_data** | [**EmailCampaignTemplateAllOfSenderData**](EmailCampaignTemplateAllOfSenderData.md) |  | [optional] 
**image** | **str** | Template image | [optional] 
**message_html_version** | **str** | Html message | [optional] 
**message_text_version** | **str** | Text message | [optional] 
**reply_to_data** | [**EmailCampaignTemplateAllOfReplyToData**](EmailCampaignTemplateAllOfReplyToData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


