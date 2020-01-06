# EmailCampaignCreate

Email campaign schema
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | **int** |  | 
**internal_name** | **str** | Campaign internal name | 
**subject** | **str** | Campaign subject. If no value is sent, defaults to &#39;internal_name&#39; property value | [optional] 
**content** | [**CampaignEmailContent**](CampaignEmailContent.md) |  | 
**sender_id** | **int** |  | 
**reply_to** | **int** |  | [optional] 
**header_footer** | [**HeaderFooter**](HeaderFooter.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


