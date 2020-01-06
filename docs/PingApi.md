# egoi-api.PingApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping**](PingApi.md#ping) | **POST** /ping | Pings the API


# **ping**
> Ping ping()

Pings the API

Checks if API is up and running

### Example

```python
from __future__ import print_function
import time
import egoi-api
from egoi-api.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = egoi-api.PingApi()

try:
    # Pings the API
    api_response = api_instance.ping()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingApi->ping: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Ping**](Ping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

