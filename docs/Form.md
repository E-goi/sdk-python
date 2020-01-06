# Form

Form schema
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form_id** | **int** |  | [optional] [readonly] 
**internal_title** | **str** | Internal title of the form | [optional] [default to '$request.body#/title']
**title** | **str** | Title of the form | 
**language** | [**Language**](Language.md) |  | [optional] 
**list_id** | **int** |  | [optional] 
**default** | **bool** | True if this is the default form in the list, false otherwise | [optional] 
**owner** | **int** |  | [optional] 
**status** | **str** | Status of the form | [optional] [readonly] 
**created** | **datetime** | The date and time | [optional] 
**updated** | **datetime** | The date and time | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


