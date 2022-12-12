# egoi_api.model.push_campaign_post_request.PushCampaignPostRequest

Push campaign post request schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Push campaign post request schema | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**title** | str,  | str,  | Push campaign subject | 
**app_id** | [**PushAppId**](PushAppId.md) | [**PushAppId**](PushAppId.md) |  | 
**content** | [**CampaignPushContent**](CampaignPushContent.md) | [**CampaignPushContent**](CampaignPushContent.md) |  | 
**[actions](#actions)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Actions for push campaign | [optional] 
**[geo_options](#geo_options)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Push geolocation options | [optional] 
**[notification_options](#notification_options)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Push notification options | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# actions

Actions for push campaign

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Actions for push campaign | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Type of action | [optional] must be one of ["url", "deeplink", ] 
**title** | str,  | str,  | Action title | [optional] 
**link** | str,  | str,  | Action link (may be either URL or deeplink) | [optional] 
**cancel_label** | str,  | str,  | Action cancel label text | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# geo_options

Push geolocation options

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Push geolocation options | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**latitude** | decimal.Decimal, int,  | decimal.Decimal,  | Geolocation latitude | [optional] 
**longitude** | decimal.Decimal, int,  | decimal.Decimal,  | Geolocation longitude | [optional] 
**range** | decimal.Decimal, int,  | decimal.Decimal,  | Geolocation range | [optional] 
**duration** | decimal.Decimal, int,  | decimal.Decimal,  | Geolocation duration | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# notification_options

Push notification options

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Push notification options | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**icon** | str,  | str,  | Url for the icon of the notification | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

