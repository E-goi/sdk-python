# egoi_api.model.product_bulk_request.ProductBulkRequest

Product bulk request schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Product bulk request schema | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[products](#products)** | list, tuple,  | tuple,  | Collection of products to import. Products having an incorrect format will be ignored | 
**mode** | str,  | str,  | How the import will be processed:  *                      &#x27;rewrite&#x27; - catalog content will be erased and then the imported products will be added  *                      &#x27;add&#x27; - adds imported products to the catalog without replacing any content. Duplicates will                         not be added  *                      &#x27;update&#x27; - adds imported products to the catalog and updates any duplicates found | [optional] must be one of ["rewrite", "add", "update", ] if omitted the server will use the default value of "update"
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# products

Collection of products to import. Products having an incorrect format will be ignored

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Collection of products to import. Products having an incorrect format will be ignored | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Product**](Product.md) | [**Product**](Product.md) | [**Product**](Product.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

