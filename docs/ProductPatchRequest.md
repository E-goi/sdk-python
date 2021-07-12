# ProductPatchRequest

Product patch request schema
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the product | [optional] 
**description** | **str** | Description of the product | [optional] 
**sku** | **str** | Stock Keeping Unit | [optional] 
**upc** | **str** | Universal Product Code | [optional] 
**ean** | **str** | European Article Numbering | [optional] 
**gtin** | **str** | Global Trade Item Number | [optional] 
**mpn** | **str** | Manufacturer Part Number | [optional] 
**link** | **str** | Link for the product | [optional] 
**image_link** | **str** | Link for the product image | [optional] 
**price** | **float** | Price of the product | [optional] [default to 0]
**sale_price** | **float** | Sale price of the product | [optional] [default to 0]
**brand** | **str** | Brand of the product | [optional] 
**categories** | **list[str]** | Array of product categories, using the character &#39;&gt;&#39; as delimiter for the breadcrumb                         syntax | [optional] 
**related_products** | [**ProductPatchRequestRelatedProducts**](ProductPatchRequestRelatedProducts.md) |  | [optional] 
**custom_attributes** | [**list[ProductCustomAttributes]**](ProductCustomAttributes.md) | Custom attributes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


