# egoi_api.model.product_patch_request.ProductPatchRequest

Product patch request schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Product patch request schema | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
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
**[categories](#categories)** | list, tuple,  | tuple,  | Array of product categories, using the character &#x27;&gt;&#x27; as delimiter for the breadcrumb                         syntax | [optional] 
**[related_products](#related_products)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Related products | [optional] 
**[custom_attributes](#custom_attributes)** | list, tuple,  | tuple,  | Custom attributes | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# categories

Array of product categories, using the character '>' as delimiter for the breadcrumb                         syntax

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of product categories, using the character &#x27;&gt;&#x27; as delimiter for the breadcrumb                         syntax | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# related_products

Related products

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Related products | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[external_product_id](#external_product_id)** | list, tuple,  | tuple,  | Array of &#x27;product_identifier&#x27; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# external_product_id

Array of 'product_identifier'

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of &#x27;product_identifier&#x27; | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# custom_attributes

Custom attributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Custom attributes | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductCustomAttributes**](ProductCustomAttributes.md) | [**ProductCustomAttributes**](ProductCustomAttributes.md) | [**ProductCustomAttributes**](ProductCustomAttributes.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

