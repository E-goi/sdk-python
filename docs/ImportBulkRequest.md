# ImportBulkRequest

Contact import bulk request schema
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Add new contacts only (&#39;add&#39;) or add and replace existing ones (&#39;update&#39;) | 
**compare_field** | **str** | Field ID which will be mapped for comparison to prevent duplicates) | 
**contacts** | [**list[ContactBulk]**](ContactBulk.md) | Array of contacts to import | 
**force_empty** | **bool** | If &#39;true&#39; accepts empty values and erases those fields | [optional] [default to False]
**notify** | **list[int]** | Array of IDs of the users to notify | [optional] 
**callback_url** | **str** | Url to receive the report | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


