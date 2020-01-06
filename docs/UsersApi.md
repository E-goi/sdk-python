# egoi-api.UsersApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{user_id} | Remove user
[**get_all_users**](UsersApi.md#get_all_users) | **GET** /users | Get all users


# **delete_user**
> delete_user(user_id)

Remove user

Remove user information given its ID

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
api_instance = egoi-api.UsersApi(egoi-api.ApiClient(configuration))
user_id = 56 # int | ID of the User

try:
    # Remove user
    api_instance.delete_user(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the User | 

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

# **get_all_users**
> UserCollection get_all_users(username=username, status=status, created_min=created_min, created_max=created_max, updated_min=updated_min, updated_max=updated_max, offset=offset, limit=limit, order=order, order_by=order_by)

Get all users

Returns all users

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
api_instance = egoi-api.UsersApi(egoi-api.ApiClient(configuration))
username = 'username_example' # str | Reference attribute to username user (optional)
status = 'status_example' # str | Status filter (optional)
created_min = '2013-10-20T19:20:30+01:00' # datetime | Created initial date (optional)
created_max = '2013-10-20T19:20:30+01:00' # datetime | Created finish (optional)
updated_min = '2013-10-20T19:20:30+01:00' # datetime | Updated initial (optional)
updated_max = '2013-10-20T19:20:30+01:00' # datetime | Updated finish (optional)
offset = 56 # int | Element offset (starting at zero for the first element) (optional)
limit = 10 # int | Number of items to return (optional) (default to 10)
order = 'desc' # str | Type of order (optional) (default to 'desc')
order_by = 'user_id' # str | Reference attribute to order users (optional) (default to 'user_id')

try:
    # Get all users
    api_response = api_instance.get_all_users(username=username, status=status, created_min=created_min, created_max=created_max, updated_min=updated_min, updated_max=updated_max, offset=offset, limit=limit, order=order, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_all_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Reference attribute to username user | [optional] 
 **status** | **str**| Status filter | [optional] 
 **created_min** | **datetime**| Created initial date | [optional] 
 **created_max** | **datetime**| Created finish | [optional] 
 **updated_min** | **datetime**| Updated initial | [optional] 
 **updated_max** | **datetime**| Updated finish | [optional] 
 **offset** | **int**| Element offset (starting at zero for the first element) | [optional] 
 **limit** | **int**| Number of items to return | [optional] [default to 10]
 **order** | **str**| Type of order | [optional] [default to &#39;desc&#39;]
 **order_by** | **str**| Reference attribute to order users | [optional] [default to &#39;user_id&#39;]

### Return type

[**UserCollection**](UserCollection.md)

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

