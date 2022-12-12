# egoi_api.model.web_push_campaign.WebPushCampaign

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**internal_name** | str,  | str,  | Webpush campaign internal title | 
**site_id** | [**QueryId**](QueryId.md) | [**QueryId**](QueryId.md) |  | 
**content** | [**MessageWebPushPost**](MessageWebPushPost.md) | [**MessageWebPushPost**](MessageWebPushPost.md) |  | 
**actions** | [**WebpushActions**](WebpushActions.md) | [**WebpushActions**](WebpushActions.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

