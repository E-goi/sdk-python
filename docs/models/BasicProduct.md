# egoi_api.model.basic_product.BasicProduct

Basic Product schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Basic Product schema | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**product_identifier** | str,  | str,  | The ID of the product in your store | [optional] 
**catalog_id** | [**Id**](Id.md) | [**Id**](Id.md) |  | [optional] 
**name** | str,  | str,  | Name of the product | [optional] 
**description** | str,  | str,  | Description of the product | [optional] 
**sku** | str,  | str,  | Stock Keeping Unit | [optional] 
**upc** | str,  | str,  | Universal Product Code | [optional] 
**ean** | str,  | str,  | European Article Numbering | [optional] 
**gtin** | str,  | str,  | Global Trade Item Number | [optional] 
**mpn** | str,  | str,  | Manufacturer Part Number | [optional] 
**link** | str,  | str,  | Link for the product | [optional] 
**image_link** | str,  | str,  | Link for the product image | [optional] 
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  | Price of the product | [optional] if omitted the server will use the default value of 0value must be a 64 bit float
**sale_price** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sale price of the product | [optional] if omitted the server will use the default value of 0value must be a 64 bit float
**brand** | str,  | str,  | Brand of the product | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

