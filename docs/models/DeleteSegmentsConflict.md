# egoi_api.model.delete_segments_conflict.DeleteSegmentsConflict

Error schema for delete segments conflicts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Error schema for delete segments conflicts | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[BaseConflict](BaseConflict.md) | [**BaseConflict**](BaseConflict.md) | [**BaseConflict**](BaseConflict.md) |  | 
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[InvalidSegmentType](InvalidSegmentType.md) | [**InvalidSegmentType**](InvalidSegmentType.md) | [**InvalidSegmentType**](InvalidSegmentType.md) |  | 
[UsedInAutomations](UsedInAutomations.md) | [**UsedInAutomations**](UsedInAutomations.md) | [**UsedInAutomations**](UsedInAutomations.md) |  | 
[UsedInRecurringMessages](UsedInRecurringMessages.md) | [**UsedInRecurringMessages**](UsedInRecurringMessages.md) | [**UsedInRecurringMessages**](UsedInRecurringMessages.md) |  | 
[HasQueuedCampaigns](HasQueuedCampaigns.md) | [**HasQueuedCampaigns**](HasQueuedCampaigns.md) | [**HasQueuedCampaigns**](HasQueuedCampaigns.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

