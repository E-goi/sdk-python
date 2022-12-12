# egoi_api.model.import_orders_bulk_bulk_request_items.ImportOrdersBulkBulkRequestItems

Ecommerce Order Items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Ecommerce Order Items | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Ecommerce order item name | 
**id** | str,  | str,  | Ecommerce order item id | 
**category** | str,  | str,  | Ecommerce order item category id (comma separated if more than one) | [optional] 
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  | Ecommerce order item price | [optional] 
**quantity** | decimal.Decimal, int,  | decimal.Decimal,  | Ecommerce order item quantity | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

