# egoi_api.EcommerceApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cart**](EcommerceApi.md#create_cart) | **POST** /{domain}/carts | Create cart
[**create_catalog**](EcommerceApi.md#create_catalog) | **POST** /catalogs | Create new catalog
[**create_order**](EcommerceApi.md#create_order) | **POST** /{domain}/orders | Create order
[**create_product**](EcommerceApi.md#create_product) | **POST** /catalogs/{catalog_id}/products | Create new product
[**delete_catalog**](EcommerceApi.md#delete_catalog) | **DELETE** /catalogs/{catalog_id} | Remove catalog
[**delete_product**](EcommerceApi.md#delete_product) | **DELETE** /catalogs/{catalog_id}/products/{product_identifier} | Remove product
[**get_all_catalogs**](EcommerceApi.md#get_all_catalogs) | **GET** /catalogs | Get all catalogs
[**get_all_products**](EcommerceApi.md#get_all_products) | **GET** /catalogs/{catalog_id}/products | Get all products
[**get_product**](EcommerceApi.md#get_product) | **GET** /catalogs/{catalog_id}/products/{product_identifier} | Get product
[**import_products**](EcommerceApi.md#import_products) | **POST** /catalogs/{catalog_id}/products/actions/import | Import products
[**update_product**](EcommerceApi.md#update_product) | **PATCH** /catalogs/{catalog_id}/products/{product_identifier} | Update product


# **create_cart**
> AcceptedResponse create_cart(domain, cart)

Create cart

Creates a new cart. If ***contact_id*** is specified, order will be atached to the contact, if the contact propreties are specified, we'll create the user, if its already in your list it will get the correct contact (**make sure you are sending atleast all configured list's unique fields**). This same logic is also applied to the **product_identifier**.

### Example

* Api Key Authentication (Apikey):
```python
from __future__ import print_function
import time
import egoi_api
from egoi_api.rest import ApiException
from pprint import pprint
configuration = egoi_api.Configuration()
# Configure API key authorization: Apikey
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# Defining host is optional and default to https://api.egoiapp.com
configuration.host = "https://api.egoiapp.com"
# Create an instance of the API class
api_instance = egoi_api.EcommerceApi(egoi_api.ApiClient(configuration))
domain = 'domain_example' # str | Domain
cart = egoi_api.Cart() # Cart | Parameters for the Carts

try:
    # Create cart
    api_response = api_instance.create_cart(domain, cart)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->create_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 
 **cart** | [**Cart**](Cart.md)| Parameters for the Carts | 

### Return type

[**AcceptedResponse**](AcceptedResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | NotFound |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_catalog**
> Catalog create_catalog(catalog_post_request)

Create new catalog

Creates a new catalog

### Example

* Api Key Authentication (Apikey):
```python
from __future__ import print_function
import time
import egoi_api
from egoi_api.rest import ApiException
from pprint import pprint
configuration = egoi_api.Configuration()
# Configure API key authorization: Apikey
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# Defining host is optional and default to https://api.egoiapp.com
configuration.host = "https://api.egoiapp.com"
# Create an instance of the API class
api_instance = egoi_api.EcommerceApi(egoi_api.ApiClient(configuration))
catalog_post_request = egoi_api.CatalogPostRequest() # CatalogPostRequest | Parameters for the Catalog

try:
    # Create new catalog
    api_response = api_instance.create_catalog(catalog_post_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->create_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_post_request** | [**CatalogPostRequest**](CatalogPostRequest.md)| Parameters for the Catalog | 

### Return type

[**Catalog**](Catalog.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**408** | Request Timeout |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> AcceptedResponse create_order(domain, create_order)

Create order

Creates a new order. If **contact_id** is specified, order will be atached to the contact, if the contact propreties are specified, we'll create the user, if its already in your list it will get the correct contact (***make sure you are sending atleast all configured list's unique fields***). This same logic is also applied to the **product_identifier**.

### Example

* Api Key Authentication (Apikey):
```python
from __future__ import print_function
import time
import egoi_api
from egoi_api.rest import ApiException
from pprint import pprint
configuration = egoi_api.Configuration()
# Configure API key authorization: Apikey
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# Defining host is optional and default to https://api.egoiapp.com
configuration.host = "https://api.egoiapp.com"
# Create an instance of the API class
api_instance = egoi_api.EcommerceApi(egoi_api.ApiClient(configuration))
domain = 'domain_example' # str | Domain
create_order = egoi_api.CreateOrder() # CreateOrder | Parameters for the Orders

try:
    # Create order
    api_response = api_instance.create_order(domain, create_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->create_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain | 
 **create_order** | [**CreateOrder**](CreateOrder.md)| Parameters for the Orders | 

### Return type

[**AcceptedResponse**](AcceptedResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | NotFound |  -  |
**408** | Request Timeout |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_product**
> Product create_product(catalog_id, product_post_request)

Create new product

Creates a new product

### Example

* Api Key Authentication (Apikey):
```python
from __future__ import print_function
import time
import egoi_api
from egoi_api.rest import ApiException
from pprint import pprint
configuration = egoi_api.Configuration()
# Configure API key authorization: Apikey
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# Defining host is optional and default to https://api.egoiapp.com
configuration.host = "https://api.egoiapp.com"
# Create an instance of the API class
api_instance = egoi_api.EcommerceApi(egoi_api.ApiClient(configuration))
catalog_id = 56 # int | ID of the Catalog
product_post_request = egoi_api.ProductPostRequest() # ProductPostRequest | Parameters for the Product

try:
    # Create new product
    api_response = api_instance.create_product(catalog_id, product_post_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->create_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **int**| ID of the Catalog | 
 **product_post_request** | [**ProductPostRequest**](ProductPostRequest.md)| Parameters for the Product | 

### Return type

[**Product**](Product.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | NotFound |  -  |
**408** | Request Timeout |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_catalog**
> delete_catalog(catalog_id)

Remove catalog

Remove catalog information given its ID

### Example

* Api Key Authentication (Apikey):
```python
from __future__ import print_function
import time
import egoi_api
from egoi_api.rest import ApiException
from pprint import pprint
configuration = egoi_api.Configuration()
# Configure API key authorization: Apikey
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# Defining host is optional and default to https://api.egoiapp.com
configuration.host = "https://api.egoiapp.com"
# Create an instance of the API class
api_instance = egoi_api.EcommerceApi(egoi_api.ApiClient(configuration))
catalog_id = 56 # int | ID of the Catalog

try:
    # Remove catalog
    api_instance.delete_catalog(catalog_id)
except ApiException as e:
    print("Exception when calling EcommerceApi->delete_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **int**| ID of the Catalog | 

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**408** | Request Timeout |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_product**
> delete_product(catalog_id, product_identifier)

Remove product

Remove product information given its ID

### Example

* Api Key Authentication (Apikey):
```python
from __future__ import print_function
import time
import egoi_api
from egoi_api.rest import ApiException
from pprint import pprint
configuration = egoi_api.Configuration()
# Configure API key authorization: Apikey
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# Defining host is optional and default to https://api.egoiapp.com
configuration.host = "https://api.egoiapp.com"
# Create an instance of the API class
api_instance = egoi_api.EcommerceApi(egoi_api.ApiClient(configuration))
catalog_id = 56 # int | ID of the Catalog
product_identifier = 'product_identifier_example' # str | ID of the Product

try:
    # Remove product
    api_instance.delete_product(catalog_id, product_identifier)
except ApiException as e:
    print("Exception when calling EcommerceApi->delete_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **int**| ID of the Catalog | 
 **product_identifier** | **str**| ID of the Product | 

### Return type

void (empty response body)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**408** | Request Timeout |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_catalogs**
> CatalogCollection get_all_catalogs()

Get all catalogs

Returns all catalogs

### Example

* Api Key Authentication (Apikey):
```python
from __future__ import print_function
import time
import egoi_api
from egoi_api.rest import ApiException
from pprint import pprint
configuration = egoi_api.Configuration()
# Configure API key authorization: Apikey
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# Defining host is optional and default to https://api.egoiapp.com
configuration.host = "https://api.egoiapp.com"
# Create an instance of the API class
api_instance = egoi_api.EcommerceApi(egoi_api.ApiClient(configuration))

try:
    # Get all catalogs
    api_response = api_instance.get_all_catalogs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->get_all_catalogs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CatalogCollection**](CatalogCollection.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**408** | Request Timeout |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_products**
> ProductCollection get_all_products(catalog_id, product_identifier=product_identifier, offset=offset, limit=limit)

Get all products

Returns all products for the given catalog

### Example

* Api Key Authentication (Apikey):
```python
from __future__ import print_function
import time
import egoi_api
from egoi_api.rest import ApiException
from pprint import pprint
configuration = egoi_api.Configuration()
# Configure API key authorization: Apikey
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# Defining host is optional and default to https://api.egoiapp.com
configuration.host = "https://api.egoiapp.com"
# Create an instance of the API class
api_instance = egoi_api.EcommerceApi(egoi_api.ApiClient(configuration))
catalog_id = 56 # int | ID of the Catalog
product_identifier = 'product_identifier_example' # str | Product ID in your store (optional)
offset = 56 # int | Element offset (starting at zero for the first element) (optional)
limit = 10 # int | Number of items to return (optional) (default to 10)

try:
    # Get all products
    api_response = api_instance.get_all_products(catalog_id, product_identifier=product_identifier, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->get_all_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **int**| ID of the Catalog | 
 **product_identifier** | **str**| Product ID in your store | [optional] 
 **offset** | **int**| Element offset (starting at zero for the first element) | [optional] 
 **limit** | **int**| Number of items to return | [optional] [default to 10]

### Return type

[**ProductCollection**](ProductCollection.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | NotFound |  -  |
**408** | Request Timeout |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product**
> Product get_product(catalog_id, product_identifier)

Get product

Returns product information given its ID

### Example

* Api Key Authentication (Apikey):
```python
from __future__ import print_function
import time
import egoi_api
from egoi_api.rest import ApiException
from pprint import pprint
configuration = egoi_api.Configuration()
# Configure API key authorization: Apikey
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# Defining host is optional and default to https://api.egoiapp.com
configuration.host = "https://api.egoiapp.com"
# Create an instance of the API class
api_instance = egoi_api.EcommerceApi(egoi_api.ApiClient(configuration))
catalog_id = 56 # int | ID of the Catalog
product_identifier = 'product_identifier_example' # str | ID of the Product

try:
    # Get product
    api_response = api_instance.get_product(catalog_id, product_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->get_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **int**| ID of the Catalog | 
 **product_identifier** | **str**| ID of the Product | 

### Return type

[**Product**](Product.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**408** | Request Timeout |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_products**
> AcceptedResponse import_products(catalog_id, product_bulk_request)

Import products

Imports a collection of products</br>      **DISCLAIMER:** stream limits applied. [view here](#section/Stream-Limits 'Stream Limits')

### Example

* Api Key Authentication (Apikey):
```python
from __future__ import print_function
import time
import egoi_api
from egoi_api.rest import ApiException
from pprint import pprint
configuration = egoi_api.Configuration()
# Configure API key authorization: Apikey
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# Defining host is optional and default to https://api.egoiapp.com
configuration.host = "https://api.egoiapp.com"
# Create an instance of the API class
api_instance = egoi_api.EcommerceApi(egoi_api.ApiClient(configuration))
catalog_id = 56 # int | ID of the Catalog
product_bulk_request = egoi_api.ProductBulkRequest() # ProductBulkRequest | Parameters for the Product

try:
    # Import products
    api_response = api_instance.import_products(catalog_id, product_bulk_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->import_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **int**| ID of the Catalog | 
 **product_bulk_request** | [**ProductBulkRequest**](ProductBulkRequest.md)| Parameters for the Product | 

### Return type

[**AcceptedResponse**](AcceptedResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | NotFound |  -  |
**408** | Request Timeout |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product**
> Product update_product(catalog_id, product_identifier, product_patch_request)

Update product

Updates a product

### Example

* Api Key Authentication (Apikey):
```python
from __future__ import print_function
import time
import egoi_api
from egoi_api.rest import ApiException
from pprint import pprint
configuration = egoi_api.Configuration()
# Configure API key authorization: Apikey
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# Defining host is optional and default to https://api.egoiapp.com
configuration.host = "https://api.egoiapp.com"
# Create an instance of the API class
api_instance = egoi_api.EcommerceApi(egoi_api.ApiClient(configuration))
catalog_id = 56 # int | ID of the Catalog
product_identifier = 'product_identifier_example' # str | ID of the Product
product_patch_request = egoi_api.ProductPatchRequest() # ProductPatchRequest | Parameters for the product

try:
    # Update product
    api_response = api_instance.update_product(catalog_id, product_identifier, product_patch_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceApi->update_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_id** | **int**| ID of the Catalog | 
 **product_identifier** | **str**| ID of the Product | 
 **product_patch_request** | [**ProductPatchRequest**](ProductPatchRequest.md)| Parameters for the product | 

### Return type

[**Product**](Product.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**408** | Request Timeout |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

