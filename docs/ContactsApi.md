# egoi-api.ContactsApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action_attach_tag**](ContactsApi.md#action_attach_tag) | **POST** /lists/{list_id}/contacts/actions/attach-tag | Attach tag to contact
[**action_detach_tag**](ContactsApi.md#action_detach_tag) | **POST** /lists/{list_id}/contacts/actions/detach-tag | Detach tag to contact
[**action_export_contacts**](ContactsApi.md#action_export_contacts) | **POST** /lists/{list_id}/contacts/actions/export | Exports a list of contacts
[**action_start_automation**](ContactsApi.md#action_start_automation) | **POST** /lists/{list_id}/contacts/actions/start-automation | Start automation
[**action_unsubscribe_contact**](ContactsApi.md#action_unsubscribe_contact) | **POST** /lists/{list_id}/contacts/actions/unsubscribe | Unsubscribes contacts
[**create_contact**](ContactsApi.md#create_contact) | **POST** /lists/{list_id}/contacts | Create new contact
[**get_all_contact_activities**](ContactsApi.md#get_all_contact_activities) | **GET** /lists/{list_id}/contacts/{contact_id}/activities | Get all contact activities
[**get_all_contacts**](ContactsApi.md#get_all_contacts) | **GET** /lists/{list_id}/contacts | Get all contacts
[**get_contact**](ContactsApi.md#get_contact) | **GET** /lists/{list_id}/contacts/{contact_id} | Get contact
[**patch_contact**](ContactsApi.md#patch_contact) | **PATCH** /lists/{list_id}/contacts/{contact_id} | Update a specific contact


# **action_attach_tag**
> AttachTagResponse action_attach_tag(list_id, attach_tag_request)

Attach tag to contact

Attaches a tag to the provided contacts

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
api_instance = egoi-api.ContactsApi(egoi-api.ApiClient(configuration))
list_id = 56 # int | ID of the List
attach_tag_request = egoi-api.AttachTagRequest() # AttachTagRequest | Parameters for the Tag

try:
    # Attach tag to contact
    api_response = api_instance.action_attach_tag(list_id, attach_tag_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->action_attach_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the List | 
 **attach_tag_request** | [**AttachTagRequest**](AttachTagRequest.md)| Parameters for the Tag | 

### Return type

[**AttachTagResponse**](AttachTagResponse.md)

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

# **action_detach_tag**
> AttachTagResponse action_detach_tag(list_id, attach_tag_request)

Detach tag to contact

Detach a tag to the provided contacts

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
api_instance = egoi-api.ContactsApi(egoi-api.ApiClient(configuration))
list_id = 56 # int | ID of the List
attach_tag_request = egoi-api.AttachTagRequest() # AttachTagRequest | Parameters for the Tag

try:
    # Detach tag to contact
    api_response = api_instance.action_detach_tag(list_id, attach_tag_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->action_detach_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the List | 
 **attach_tag_request** | [**AttachTagRequest**](AttachTagRequest.md)| Parameters for the Tag | 

### Return type

[**AttachTagResponse**](AttachTagResponse.md)

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

# **action_export_contacts**
> AcceptedResponse action_export_contacts(list_id, contact_export_request)

Exports a list of contacts

Exports a list of contacts to the desired callback url

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
api_instance = egoi-api.ContactsApi(egoi-api.ApiClient(configuration))
list_id = 56 # int | ID of the List
contact_export_request = egoi-api.ContactExportRequest() # ContactExportRequest | Parameters for export

try:
    # Exports a list of contacts
    api_response = api_instance.action_export_contacts(list_id, contact_export_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->action_export_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the List | 
 **contact_export_request** | [**ContactExportRequest**](ContactExportRequest.md)| Parameters for export | 

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_start_automation**
> StartAutomationResponse action_start_automation(list_id, start_automation_request)

Start automation

Start automation to the provided contacts

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
api_instance = egoi-api.ContactsApi(egoi-api.ApiClient(configuration))
list_id = 56 # int | ID of the List
start_automation_request = egoi-api.StartAutomationRequest() # StartAutomationRequest | Parameters for the operation to start automation

try:
    # Start automation
    api_response = api_instance.action_start_automation(list_id, start_automation_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->action_start_automation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the List | 
 **start_automation_request** | [**StartAutomationRequest**](StartAutomationRequest.md)| Parameters for the operation to start automation | 

### Return type

[**StartAutomationResponse**](StartAutomationResponse.md)

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

# **action_unsubscribe_contact**
> RemoveResponse action_unsubscribe_contact(list_id, remove_request)

Unsubscribes contacts

Unsubscribes contacts

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
api_instance = egoi-api.ContactsApi(egoi-api.ApiClient(configuration))
list_id = 56 # int | ID of the List
remove_request = egoi-api.RemoveRequest() # RemoveRequest | Parameters for the contact to unsubscribe

try:
    # Unsubscribes contacts
    api_response = api_instance.action_unsubscribe_contact(list_id, remove_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->action_unsubscribe_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the List | 
 **remove_request** | [**RemoveRequest**](RemoveRequest.md)| Parameters for the contact to unsubscribe | 

### Return type

[**RemoveResponse**](RemoveResponse.md)

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
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact**
> CreateContactResponse create_contact(list_id, contact_base_extra)

Create new contact

Create a new contact

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
api_instance = egoi-api.ContactsApi(egoi-api.ApiClient(configuration))
list_id = 56 # int | ID of the list where the contact belongs
contact_base_extra = egoi-api.ContactBaseExtra() # ContactBaseExtra | Parameters for the Contact

try:
    # Create new contact
    api_response = api_instance.create_contact(list_id, contact_base_extra)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->create_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the list where the contact belongs | 
 **contact_base_extra** | [**ContactBaseExtra**](ContactBaseExtra.md)| Parameters for the Contact | 

### Return type

[**CreateContactResponse**](CreateContactResponse.md)

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_contact_activities**
> ActivityCollection get_all_contact_activities(contact_id, list_id, offset=offset, limit=limit, date_min=date_min, date_max=date_max)

Get all contact activities

Returns all contact activities

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
api_instance = egoi-api.ContactsApi(egoi-api.ApiClient(configuration))
contact_id = 'contact_id_example' # str | ID of the Contact
list_id = 56 # int | ID of the List
offset = 56 # int | Element offset (starting at zero for the first element) (optional)
limit = 10 # int | Number of items to return (optional) (default to 10)
date_min = '2013-10-20T19:20:30+01:00' # datetime | Start date (optional)
date_max = '2013-10-20T19:20:30+01:00' # datetime | End date (optional)

try:
    # Get all contact activities
    api_response = api_instance.get_all_contact_activities(contact_id, list_id, offset=offset, limit=limit, date_min=date_min, date_max=date_max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_all_contact_activities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**| ID of the Contact | 
 **list_id** | **int**| ID of the List | 
 **offset** | **int**| Element offset (starting at zero for the first element) | [optional] 
 **limit** | **int**| Number of items to return | [optional] [default to 10]
 **date_min** | **datetime**| Start date | [optional] 
 **date_max** | **datetime**| End date | [optional] 

### Return type

[**ActivityCollection**](ActivityCollection.md)

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

# **get_all_contacts**
> ContactCollection get_all_contacts(list_id, offset=offset, limit=limit)

Get all contacts

Returns all contacts

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
api_instance = egoi-api.ContactsApi(egoi-api.ApiClient(configuration))
list_id = 56 # int | ID of the List
offset = 56 # int | Element offset (starting at zero for the first element) (optional)
limit = 10 # int | Number of items to return (optional) (default to 10)

try:
    # Get all contacts
    api_response = api_instance.get_all_contacts(list_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_all_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the List | 
 **offset** | **int**| Element offset (starting at zero for the first element) | [optional] 
 **limit** | **int**| Number of items to return | [optional] [default to 10]

### Return type

[**ContactCollection**](ContactCollection.md)

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
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact**
> ComplexContact get_contact(contact_id, list_id)

Get contact

Returns contact information given its ID

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
api_instance = egoi-api.ContactsApi(egoi-api.ApiClient(configuration))
contact_id = 'contact_id_example' # str | ID of the Contact
list_id = 56 # int | ID of the List

try:
    # Get contact
    api_response = api_instance.get_contact(contact_id, list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->get_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**| ID of the Contact | 
 **list_id** | **int**| ID of the List | 

### Return type

[**ComplexContact**](ComplexContact.md)

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
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_contact**
> CreateContactResponse patch_contact(contact_id, list_id, contact_base_status_extra)

Update a specific contact

Update contact

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
api_instance = egoi-api.ContactsApi(egoi-api.ApiClient(configuration))
contact_id = 'contact_id_example' # str | ID of the Contact
list_id = 56 # int | ID of the List
contact_base_status_extra = egoi-api.ContactBaseStatusExtra() # ContactBaseStatusExtra | Parameters for the contact

try:
    # Update a specific contact
    api_response = api_instance.patch_contact(contact_id, list_id, contact_base_status_extra)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->patch_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**| ID of the Contact | 
 **list_id** | **int**| ID of the List | 
 **contact_base_status_extra** | [**ContactBaseStatusExtra**](ContactBaseStatusExtra.md)| Parameters for the contact | 

### Return type

[**CreateContactResponse**](CreateContactResponse.md)

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

