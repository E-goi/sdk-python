# egoi-api.SuppressionListApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_suppression_list**](SuppressionListApi.md#get_all_suppression_list) | **GET** /suppression-list | Get the suppression list


# **get_all_suppression_list**
> SuppressionListItems get_all_suppression_list(type=type, method=method, value=value, campaign_hash=campaign_hash, created_min=created_min, created_max=created_max, offset=offset, limit=limit, order=order, order_by=order_by)

Get the suppression list

Returns the suppression list

### Example

* Api Key Authentication (Apikey):
```python
from __future__ import print_function
import time
import egoi-api
from egoi-api.rest import ApiException
from pprint import pprint
configuration = egoi-api.Configuration()
# Configure API key authorization: Apikey
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# Defining host is optional and default to https://api.egoiapp.com
configuration.host = "https://api.egoiapp.com"
# Create an instance of the API class
api_instance = egoi-api.SuppressionListApi(egoi-api.ApiClient(configuration))
type = 'type_example' # str | Suppression type (optional)
method = 'method_example' # str | Suppression method (optional)
value = 'value_example' # str | Reference attribute to value suppression list (optional)
campaign_hash = 'campaign_hash_example' # str | Reference attribute to campaign id (optional)
created_min = '2013-10-20T19:20:30+01:00' # datetime | Created initial date (optional)
created_max = '2013-10-20T19:20:30+01:00' # datetime | Created finish (optional)
offset = 56 # int | Element offset (starting at zero for the first element) (optional)
limit = 10 # int | Number of items to return (optional) (default to 10)
order = 'desc' # str | Type of order (optional) (default to 'desc')
order_by = 'id' # str | Reference attribute to order the suppression list (optional) (default to 'id')

try:
    # Get the suppression list
    api_response = api_instance.get_all_suppression_list(type=type, method=method, value=value, campaign_hash=campaign_hash, created_min=created_min, created_max=created_max, offset=offset, limit=limit, order=order, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppressionListApi->get_all_suppression_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Suppression type | [optional] 
 **method** | **str**| Suppression method | [optional] 
 **value** | **str**| Reference attribute to value suppression list | [optional] 
 **campaign_hash** | **str**| Reference attribute to campaign id | [optional] 
 **created_min** | **datetime**| Created initial date | [optional] 
 **created_max** | **datetime**| Created finish | [optional] 
 **offset** | **int**| Element offset (starting at zero for the first element) | [optional] 
 **limit** | **int**| Number of items to return | [optional] [default to 10]
 **order** | **str**| Type of order | [optional] [default to &#39;desc&#39;]
 **order_by** | **str**| Reference attribute to order the suppression list | [optional] [default to &#39;id&#39;]

### Return type

[**SuppressionListItems**](SuppressionListItems.md)

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
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

