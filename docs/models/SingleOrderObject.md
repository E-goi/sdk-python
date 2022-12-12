# egoi_api.model.single_order_object.SingleOrderObject

Single Order data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Single Order data | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**date** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**revenue** | decimal.Decimal, int, float,  | decimal.Decimal,  | Ecommerce order revenue | 
**[items](#items)** | list, tuple,  | tuple,  | Array of ordered products | 
**order_id** | str,  | str,  | Ecommerce order id | 
**store_url** | str,  | str,  | Ecommerce store url | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# items

Array of ordered products

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of ordered products | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ImportOrdersBulkBulkRequestItems**](ImportOrdersBulkBulkRequestItems.md) | [**ImportOrdersBulkBulkRequestItems**](ImportOrdersBulkBulkRequestItems.md) | [**ImportOrdersBulkBulkRequestItems**](ImportOrdersBulkBulkRequestItems.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

