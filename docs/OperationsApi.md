# egoi_api.OperationsApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action_approve_operation**](OperationsApi.md#action_approve_operation) | **POST** /operations/actions/approve | Approve operation
[**action_cancel_operation**](OperationsApi.md#action_cancel_operation) | **POST** /operations/actions/cancel | Cancel operation
[**action_pause_operation**](OperationsApi.md#action_pause_operation) | **POST** /operations/actions/pause | Pause operation
[**action_resume_operation**](OperationsApi.md#action_resume_operation) | **POST** /operations/actions/resume | Resume operation
[**get_all_operations**](OperationsApi.md#get_all_operations) | **GET** /operations | Get all queued operations


# **action_approve_operation**
> OperationActionResponse action_approve_operation(operation_action_request)

Approve operation

Approves an operation

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
api_instance = egoi_api.OperationsApi(egoi_api.ApiClient(configuration))
operation_action_request = egoi_api.OperationActionRequest() # OperationActionRequest | Parameters for the request

try:
    # Approve operation
    api_response = api_instance.action_approve_operation(operation_action_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->action_approve_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_action_request** | [**OperationActionRequest**](OperationActionRequest.md)| Parameters for the request | 

### Return type

[**OperationActionResponse**](OperationActionResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json
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

# **action_cancel_operation**
> OperationActionResponse action_cancel_operation(operation_action_request)

Cancel operation

Cancels an operation

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
api_instance = egoi_api.OperationsApi(egoi_api.ApiClient(configuration))
operation_action_request = egoi_api.OperationActionRequest() # OperationActionRequest | Parameters for the request

try:
    # Cancel operation
    api_response = api_instance.action_cancel_operation(operation_action_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->action_cancel_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_action_request** | [**OperationActionRequest**](OperationActionRequest.md)| Parameters for the request | 

### Return type

[**OperationActionResponse**](OperationActionResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json
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

# **action_pause_operation**
> OperationActionResponse action_pause_operation(operation_action_request)

Pause operation

Pauses an operation

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
api_instance = egoi_api.OperationsApi(egoi_api.ApiClient(configuration))
operation_action_request = egoi_api.OperationActionRequest() # OperationActionRequest | Parameters for the request

try:
    # Pause operation
    api_response = api_instance.action_pause_operation(operation_action_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->action_pause_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_action_request** | [**OperationActionRequest**](OperationActionRequest.md)| Parameters for the request | 

### Return type

[**OperationActionResponse**](OperationActionResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json
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

# **action_resume_operation**
> OperationActionResponse action_resume_operation(operation_action_request)

Resume operation

Resumes an operation

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
api_instance = egoi_api.OperationsApi(egoi_api.ApiClient(configuration))
operation_action_request = egoi_api.OperationActionRequest() # OperationActionRequest | Parameters for the request

try:
    # Resume operation
    api_response = api_instance.action_resume_operation(operation_action_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->action_resume_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_action_request** | [**OperationActionRequest**](OperationActionRequest.md)| Parameters for the request | 

### Return type

[**OperationActionResponse**](OperationActionResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_operations**
> OperationsCollection get_all_operations(type=type, status=status, offset=offset, limit=limit, order=order, order_by=order_by)

Get all queued operations

Returns all operations in queue

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
api_instance = egoi_api.OperationsApi(egoi_api.ApiClient(configuration))
type = 'type_example' # str | Operation type (optional)
status = 'status_example' # str | Operation state (optional)
offset = 56 # int | Element offset (starting at zero for the first element) (optional)
limit = 10 # int | Number of items to return (optional) (default to 10)
order = 'desc' # str | Type of order (optional) (default to 'desc')
order_by = 'order_by_example' # str | Reference attribute to order operations (optional)

try:
    # Get all queued operations
    api_response = api_instance.get_all_operations(type=type, status=status, offset=offset, limit=limit, order=order, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->get_all_operations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Operation type | [optional] 
 **status** | **str**| Operation state | [optional] 
 **offset** | **int**| Element offset (starting at zero for the first element) | [optional] 
 **limit** | **int**| Number of items to return | [optional] [default to 10]
 **order** | **str**| Type of order | [optional] [default to &#39;desc&#39;]
 **order_by** | **str**| Reference attribute to order operations | [optional] 

### Return type

[**OperationsCollection**](OperationsCollection.md)

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

