# egoi_api.model.delete_lists_conflict.DeleteListsConflict

Error schema for delete lists conflicts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Error schema for delete lists conflicts | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[BaseConflict](BaseConflict.md) | [**BaseConflict**](BaseConflict.md) | [**BaseConflict**](BaseConflict.md) |  | 
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[HasQueuedOperations](HasQueuedOperations.md) | [**HasQueuedOperations**](HasQueuedOperations.md) | [**HasQueuedOperations**](HasQueuedOperations.md) |  | 
[HasAutomations](HasAutomations.md) | [**HasAutomations**](HasAutomations.md) | [**HasAutomations**](HasAutomations.md) |  | 
[HasPushApp](HasPushApp.md) | [**HasPushApp**](HasPushApp.md) | [**HasPushApp**](HasPushApp.md) |  | 
[HasWebPushSite](HasWebPushSite.md) | [**HasWebPushSite**](HasWebPushSite.md) | [**HasWebPushSite**](HasWebPushSite.md) |  | 
[HasCampaignsLastThirtyDays](HasCampaignsLastThirtyDays.md) | [**HasCampaignsLastThirtyDays**](HasCampaignsLastThirtyDays.md) | [**HasCampaignsLastThirtyDays**](HasCampaignsLastThirtyDays.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

