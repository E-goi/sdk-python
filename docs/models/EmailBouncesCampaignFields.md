# egoi_api.model.email_bounces_campaign_fields.EmailBouncesCampaignFields

Campaign fields to include in the report

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Campaign fields to include in the report | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**internal_name** | bool,  | BoolClass,  | True to include the internal name of the campaign, false otherwise | 
**campaign_hash** | bool,  | BoolClass,  | True to include the hash of the campaign, false otherwise | 
**send_date** | bool,  | BoolClass,  | True to include the send date of the campaign, false otherwise | [optional] 
**group** | bool,  | BoolClass,  | True to include the group of the campaign, false otherwise | [optional] 
**channel** | bool,  | BoolClass,  | True to include the channel of the campaign, false otherwise | [optional] 
**sender** | bool,  | BoolClass,  | True to include the sender of the campaign, false otherwise | [optional] 
**type** | bool,  | BoolClass,  | True to include the type of the campaign, false otherwise | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

