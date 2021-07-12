# egoi_api.CNamesApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_c_name**](CNamesApi.md#create_c_name) | **POST** /cnames | Create cname
[**get_all_c_names**](CNamesApi.md#get_all_c_names) | **GET** /cnames | Get All CNames


# **create_c_name**
> CName create_c_name(c_name)

Create cname

Creates a cnames

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
api_instance = egoi_api.CNamesApi(egoi_api.ApiClient(configuration))
c_name = egoi_api.CName() # CName | Parameters for the cname

try:
    # Create cname
    api_response = api_instance.create_c_name(c_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CNamesApi->create_c_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **c_name** | [**CName**](CName.md)| Parameters for the cname | 

### Return type

[**CName**](CName.md)

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
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_c_names**
> CNamesCollection get_all_c_names()

Get All CNames

Returns all cnames

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
api_instance = egoi_api.CNamesApi(egoi_api.ApiClient(configuration))

try:
    # Get All CNames
    api_response = api_instance.get_all_c_names()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CNamesApi->get_all_c_names: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CNamesCollection**](CNamesCollection.md)

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
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

