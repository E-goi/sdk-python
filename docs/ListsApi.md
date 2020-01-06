# egoi-api.ListsApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_list**](ListsApi.md#create_list) | **POST** /lists | Create new list
[**delete_list**](ListsApi.md#delete_list) | **DELETE** /lists/{list_id} | Remove list
[**get_all_lists**](ListsApi.md#get_all_lists) | **GET** /lists | Get all lists
[**update_list**](ListsApi.md#update_list) | **PATCH** /lists/{list_id} | Update a specific list


# **create_list**
> List create_list(post_request_list)

Create new list

Create a new list

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
api_instance = egoi-api.ListsApi(egoi-api.ApiClient(configuration))
post_request_list = egoi-api.PostRequestList() # PostRequestList | Parameters for the List

try:
    # Create new list
    api_response = api_instance.create_list(post_request_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListsApi->create_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_request_list** | [**PostRequestList**](PostRequestList.md)| Parameters for the List | 

### Return type

[**List**](List.md)

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
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_list**
> delete_list(list_id)

Remove list

Remove list information given its ID

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
api_instance = egoi-api.ListsApi(egoi-api.ApiClient(configuration))
list_id = 56 # int | ID of the List

try:
    # Remove list
    api_instance.delete_list(list_id)
except ApiException as e:
    print("Exception when calling ListsApi->delete_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the List | 

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
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_lists**
> ListCollection get_all_lists(offset=offset, limit=limit, order=order, order_by=order_by, internal_name=internal_name, public_name=public_name, created_min=created_min, created_max=created_max, updated_min=updated_min, updated_max=updated_max)

Get all lists

Returns all lists

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
api_instance = egoi-api.ListsApi(egoi-api.ApiClient(configuration))
offset = 56 # int | Element offset (starting at zero for the first element) (optional)
limit = 10 # int | Number of items to return (optional) (default to 10)
order = 'desc' # str | Type of order (optional) (default to 'desc')
order_by = 'list_id' # str | Reference attribute to order lists (optional) (default to 'list_id')
internal_name = 'internal_name_example' # str | Internal name of the list (optional)
public_name = 'public_name_example' # str | Public name of the list (optional)
created_min = '2013-10-20T19:20:30+01:00' # datetime | Created initial date (optional)
created_max = '2013-10-20T19:20:30+01:00' # datetime | Created finish (optional)
updated_min = '2013-10-20T19:20:30+01:00' # datetime | Updated initial (optional)
updated_max = '2013-10-20T19:20:30+01:00' # datetime | Updated finish (optional)

try:
    # Get all lists
    api_response = api_instance.get_all_lists(offset=offset, limit=limit, order=order, order_by=order_by, internal_name=internal_name, public_name=public_name, created_min=created_min, created_max=created_max, updated_min=updated_min, updated_max=updated_max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListsApi->get_all_lists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Element offset (starting at zero for the first element) | [optional] 
 **limit** | **int**| Number of items to return | [optional] [default to 10]
 **order** | **str**| Type of order | [optional] [default to &#39;desc&#39;]
 **order_by** | **str**| Reference attribute to order lists | [optional] [default to &#39;list_id&#39;]
 **internal_name** | **str**| Internal name of the list | [optional] 
 **public_name** | **str**| Public name of the list | [optional] 
 **created_min** | **datetime**| Created initial date | [optional] 
 **created_max** | **datetime**| Created finish | [optional] 
 **updated_min** | **datetime**| Updated initial | [optional] 
 **updated_max** | **datetime**| Updated finish | [optional] 

### Return type

[**ListCollection**](ListCollection.md)

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

# **update_list**
> List update_list(list_id, patch_request_list)

Update a specific list

Update a list

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
api_instance = egoi-api.ListsApi(egoi-api.ApiClient(configuration))
list_id = 56 # int | ID of the List
patch_request_list = egoi-api.PatchRequestList() # PatchRequestList | Parameters for the List

try:
    # Update a specific list
    api_response = api_instance.update_list(list_id, patch_request_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListsApi->update_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the List | 
 **patch_request_list** | [**PatchRequestList**](PatchRequestList.md)| Parameters for the List | 

### Return type

[**List**](List.md)

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
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

