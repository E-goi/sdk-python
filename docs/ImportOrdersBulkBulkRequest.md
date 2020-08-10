# ImportOrdersBulkBulkRequest

Order data
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Ecommerce order id | 
**contact_id** | **str** | Contact ID is any non-empty unique string identifying the user (such as an email address or e-goi uid) | [optional] 
**revenue** | **float** | Ecommerce order revenue | 
**store_url** | **str** | Ecommerce store url | 
**date** | **datetime** | Ecommerce order date (For technical reasons, all orders synchronized will have the date of synchronization.) | 
**items** | [**list[ImportOrdersBulkBulkRequestItems]**](ImportOrdersBulkBulkRequestItems.md) | Array of ordered products | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


