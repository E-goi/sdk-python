# egoi-api.FieldsApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_extra_field**](FieldsApi.md#create_extra_field) | **POST** /lists/{list_id}/fields/extra | Create extra field
[**create_field_option**](FieldsApi.md#create_field_option) | **POST** /lists/{list_id}/fields/extra/{field_id}/options | Create new field option
[**delete_extra_field**](FieldsApi.md#delete_extra_field) | **DELETE** /lists/{list_id}/fields/extra/{field_id} | Remove extra field
[**delete_field_option**](FieldsApi.md#delete_field_option) | **DELETE** /lists/{list_id}/fields/extra/{field_id}/options/{option_id} | Deletes an option
[**get_all_field_options**](FieldsApi.md#get_all_field_options) | **GET** /lists/{list_id}/fields/extra/{field_id}/options | Get all field options
[**get_all_fields**](FieldsApi.md#get_all_fields) | **GET** /lists/{list_id}/fields | Get all fields
[**patch_base_field**](FieldsApi.md#patch_base_field) | **PATCH** /lists/{list_id}/fields/base/{field_id} | Update base field
[**patch_extra_field**](FieldsApi.md#patch_extra_field) | **PATCH** /lists/{list_id}/fields/extra/{field_id} | Update extra field
[**update_field_option**](FieldsApi.md#update_field_option) | **PATCH** /lists/{list_id}/fields/extra/{field_id}/options/{option_id} | Update field option


# **create_extra_field**
> Field create_extra_field(list_id, field)

Create extra field

Creates an extra field

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
api_instance = egoi-api.FieldsApi(egoi-api.ApiClient(configuration))
list_id = 56 # int | ID of the List
field = egoi-api.Field() # Field | Parameters for the extra field

try:
    # Create extra field
    api_response = api_instance.create_extra_field(list_id, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->create_extra_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the List | 
 **field** | [**Field**](Field.md)| Parameters for the extra field | 

### Return type

[**Field**](Field.md)

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
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_field_option**
> FieldOption create_field_option(list_id, field_id, field_option)

Create new field option

Creates a field option

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
api_instance = egoi-api.FieldsApi(egoi-api.ApiClient(configuration))
list_id = 56 # int | ID of the List
field_id = 56 # int | ID of the Field
field_option = egoi-api.FieldOption() # FieldOption | Parameters for the field option

try:
    # Create new field option
    api_response = api_instance.create_field_option(list_id, field_id, field_option)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->create_field_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the List | 
 **field_id** | **int**| ID of the Field | 
 **field_option** | [**FieldOption**](FieldOption.md)| Parameters for the field option | 

### Return type

[**FieldOption**](FieldOption.md)

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
**404** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_extra_field**
> delete_extra_field(list_id, field_id)

Remove extra field

Removes an extra field given its ID

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
api_instance = egoi-api.FieldsApi(egoi-api.ApiClient(configuration))
list_id = 56 # int | ID of the List
field_id = 56 # int | ID of the Field

try:
    # Remove extra field
    api_instance.delete_extra_field(list_id, field_id)
except ApiException as e:
    print("Exception when calling FieldsApi->delete_extra_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the List | 
 **field_id** | **int**| ID of the Field | 

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

# **delete_field_option**
> delete_field_option(list_id, field_id, option_id)

Deletes an option

Deletes an option of a list of values field

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
api_instance = egoi-api.FieldsApi(egoi-api.ApiClient(configuration))
list_id = 56 # int | ID of the List
field_id = 56 # int | ID of the Field
option_id = 56 # int | ID of the field option

try:
    # Deletes an option
    api_instance.delete_field_option(list_id, field_id, option_id)
except ApiException as e:
    print("Exception when calling FieldsApi->delete_field_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the List | 
 **field_id** | **int**| ID of the Field | 
 **option_id** | **int**| ID of the field option | 

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_field_options**
> FieldOptionsCollection get_all_field_options(list_id, field_id)

Get all field options

Returns all options of a given field

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
api_instance = egoi-api.FieldsApi(egoi-api.ApiClient(configuration))
list_id = 56 # int | ID of the List
field_id = 56 # int | ID of the Field

try:
    # Get all field options
    api_response = api_instance.get_all_field_options(list_id, field_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->get_all_field_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the List | 
 **field_id** | **int**| ID of the Field | 

### Return type

[**FieldOptionsCollection**](FieldOptionsCollection.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_fields**
> FieldCollection get_all_fields(list_id, offset=offset, limit=limit)

Get all fields

Returns all fields

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
api_instance = egoi-api.FieldsApi(egoi-api.ApiClient(configuration))
list_id = 56 # int | ID of the List
offset = 56 # int | Element offset (starting at zero for the first element) (optional)
limit = 10 # int | Number of items to return (optional) (default to 10)

try:
    # Get all fields
    api_response = api_instance.get_all_fields(list_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->get_all_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the List | 
 **offset** | **int**| Element offset (starting at zero for the first element) | [optional] 
 **limit** | **int**| Number of items to return | [optional] [default to 10]

### Return type

[**FieldCollection**](FieldCollection.md)

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

# **patch_base_field**
> Field patch_base_field(list_id, field_id, patch_request_base_field)

Update base field

Updates a base field

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
api_instance = egoi-api.FieldsApi(egoi-api.ApiClient(configuration))
list_id = 56 # int | ID of the List
field_id = 'field_id_example' # str | ID of the base field
patch_request_base_field = egoi-api.PatchRequestBaseField() # PatchRequestBaseField | Parameters for the extra field

try:
    # Update base field
    api_response = api_instance.patch_base_field(list_id, field_id, patch_request_base_field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->patch_base_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the List | 
 **field_id** | **str**| ID of the base field | 
 **patch_request_base_field** | [**PatchRequestBaseField**](PatchRequestBaseField.md)| Parameters for the extra field | 

### Return type

[**Field**](Field.md)

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

# **patch_extra_field**
> Field patch_extra_field(list_id, field_id, patch_request_field)

Update extra field

Updates an extra field

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
api_instance = egoi-api.FieldsApi(egoi-api.ApiClient(configuration))
list_id = 56 # int | ID of the List
field_id = 56 # int | ID of the Field
patch_request_field = egoi-api.PatchRequestField() # PatchRequestField | Parameters for the extra field

try:
    # Update extra field
    api_response = api_instance.patch_extra_field(list_id, field_id, patch_request_field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->patch_extra_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the List | 
 **field_id** | **int**| ID of the Field | 
 **patch_request_field** | [**PatchRequestField**](PatchRequestField.md)| Parameters for the extra field | 

### Return type

[**Field**](Field.md)

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

# **update_field_option**
> FieldOption update_field_option(list_id, field_id, option_id, field_option)

Update field option

Updates a field option

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
api_instance = egoi-api.FieldsApi(egoi-api.ApiClient(configuration))
list_id = 56 # int | ID of the List
field_id = 56 # int | ID of the Field
option_id = 56 # int | ID of the field option
field_option = egoi-api.FieldOption() # FieldOption | Parameters for the field option

try:
    # Update field option
    api_response = api_instance.update_field_option(list_id, field_id, option_id, field_option)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->update_field_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the List | 
 **field_id** | **int**| ID of the Field | 
 **option_id** | **int**| ID of the field option | 
 **field_option** | [**FieldOption**](FieldOption.md)| Parameters for the field option | 

### Return type

[**FieldOption**](FieldOption.md)

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

