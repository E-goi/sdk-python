# egoi_api.model.email_campaign_create.EmailCampaignCreate

Email campaign schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Email campaign schema | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**internal_name** | str,  | str,  | Campaign internal name | 
**list_id** | [**QueryId**](QueryId.md) | [**QueryId**](QueryId.md) |  | 
**content** | [**CampaignEmailContent**](CampaignEmailContent.md) | [**CampaignEmailContent**](CampaignEmailContent.md) |  | 
**sender_id** | [**QueryId**](QueryId.md) | [**QueryId**](QueryId.md) |  | 
**subject** | str,  | str,  | Campaign subject. If no value is sent, defaults to &#x27;internal_name&#x27; property value | [optional] 
**reply_to** | [**QueryId**](QueryId.md) | [**QueryId**](QueryId.md) |  | [optional] 
**header_footer** | [**HeaderFooter**](HeaderFooter.md) | [**HeaderFooter**](HeaderFooter.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

