# egoi_api.model.import_orders_bulk_bulk_request.ImportOrdersBulkBulkRequest

Order data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Order data | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[date](#date)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Ecommerce order date (For technical reasons, all orders synchronized will have the date of synchronization.) | 
**revenue** | decimal.Decimal, int, float,  | decimal.Decimal,  | Ecommerce order revenue | 
**[items](#items)** | list, tuple,  | tuple,  | Array of ordered products | 
**order_id** | str,  | str,  | Ecommerce order id | 
**store_url** | str,  | str,  | Ecommerce store url | 
**contact_id** | str,  | str,  | Contact ID is any non-empty unique string identifying the user (such as an email address or e-goi uid) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# date

Ecommerce order date (For technical reasons, all orders synchronized will have the date of synchronization.)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Ecommerce order date (For technical reasons, all orders synchronized will have the date of synchronization.) | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | str, datetime,  | str,  | The date and time | value must conform to RFC-3339 date-time

# all_of_0

The date and time

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  | The date and time | value must conform to RFC-3339 date-time

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

