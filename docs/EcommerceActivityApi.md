# egoi_api.EcommerceActivityApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_orders_bulk**](EcommerceActivityApi.md#import_orders_bulk) | **POST** /lists/{list_id}/orders | Orders import bulk request


# **import_orders_bulk**
> AcceptedResponse import_orders_bulk(list_id, import_orders_bulk_bulk_request)

Orders import bulk request

Creates new bulk orders syncronization

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
api_instance = egoi_api.EcommerceActivityApi(egoi_api.ApiClient(configuration))
list_id = 56 # int | ID of the List
import_orders_bulk_bulk_request = [egoi_api.ImportOrdersBulkBulkRequest()] # list[ImportOrdersBulkBulkRequest] | Parameters for the Orders

try:
    # Orders import bulk request
    api_response = api_instance.import_orders_bulk(list_id, import_orders_bulk_bulk_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EcommerceActivityApi->import_orders_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the List | 
 **import_orders_bulk_bulk_request** | [**list[ImportOrdersBulkBulkRequest]**](ImportOrdersBulkBulkRequest.md)| Parameters for the Orders | 

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

