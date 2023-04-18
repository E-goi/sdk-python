# egoi_api.model.webhook.Webhook

Webhook schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Webhook schema | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**list_id** | [**QueryId**](QueryId.md) | [**QueryId**](QueryId.md) |  | 
**[actions](#actions)** | list, tuple,  | tuple,  | Action that will trigger the webhook | 
**url** | str,  | str,  | Url to send the webhook &lt;a href&#x3D;&#x27;/usecases/webhooks/&#x27; target&#x3D;&#x27;_blank&#x27;&gt;[Go to webhooks documentation]&lt;/a&gt;:  *       Note: Only &#x27;http&#x27; or &#x27;https&#x27; protocols are supported. | 
**webhook_id** | [**Id**](Id.md) | [**Id**](Id.md) |  | [optional] 
**[fields](#fields)** | list, tuple,  | tuple,  | Array of contact field IDs to be displayed in the webhook | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# actions

Action that will trigger the webhook

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Action that will trigger the webhook | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WebhookActionSchema**](WebhookActionSchema.md) | [**WebhookActionSchema**](WebhookActionSchema.md) | [**WebhookActionSchema**](WebhookActionSchema.md) |  | 

# fields

Array of contact field IDs to be displayed in the webhook

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of contact field IDs to be displayed in the webhook | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

