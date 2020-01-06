# ComplexUser

Complex user schema
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] [readonly] 
**username** | **str** | User login | [optional] [readonly] 
**is_admin** | **bool** | True if user is admin, false otherwise | [optional] [readonly] [default to False]
**first_name** | **str** | First name of the user | [optional] 
**last_name** | **str** | Last name of the user | [optional] 
**email** | **str** | Email of the user | [optional] 
**phone** | **str** | User&#39;s phone (may be cellphone or phone) | [optional] 
**profile_image** | **str** | User&#39;s profile image | [optional] [readonly] 
**status** | **str** | User status | [optional] [readonly] 
**created** | **datetime** | The date and time | [optional] 
**updated** | **datetime** | The date and time | [optional] 
**language** | [**Language**](Language.md) |  | [optional] 
**timezone** | **str** | User timezone | [optional] [readonly] 
**show_removed_contacts** | **bool** | True if the user can see removed contacts, false otherwise | [optional] [readonly] [default to True]
**gender** | **str** | User gender | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


