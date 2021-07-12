# egoi_api.PushApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action_send_push**](PushApi.md#action_send_push) | **POST** /campaigns/push/{campaign_hash}/actions/send | Send push message
[**create_push_campaign**](PushApi.md#create_push_campaign) | **POST** /campaigns/push | Create new push campaign
[**get_push_app**](PushApi.md#get_push_app) | **GET** /push/apps/{app_id} | Get a Push application from E-goi
[**get_push_apps**](PushApi.md#get_push_apps) | **GET** /push/apps | Get all Push applications from E-goi
[**patch_push_campaign**](PushApi.md#patch_push_campaign) | **PATCH** /campaigns/push/{campaign_hash} | Update a specific push campaign
[**register_push_event**](PushApi.md#register_push_event) | **POST** /push/apps/{app_id}/event | Registers an event from the push notification.
[**register_push_token**](PushApi.md#register_push_token) | **POST** /push/apps/{app_id}/token | Registers a Firebase token


# **action_send_push**
> AcceptedResponse action_send_push(campaign_hash, campaign_push_send_request)

Send push message

Deploys and sends a push message

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
api_instance = egoi_api.PushApi(egoi_api.ApiClient(configuration))
campaign_hash = 'campaign_hash_example' # str | ID of the Campaign
campaign_push_send_request = egoi_api.CampaignPushSendRequest() # CampaignPushSendRequest | Parameters for the 'send push' action

try:
    # Send push message
    api_response = api_instance.action_send_push(campaign_hash, campaign_push_send_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PushApi->action_send_push: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_hash** | **str**| ID of the Campaign | 
 **campaign_push_send_request** | [**CampaignPushSendRequest**](CampaignPushSendRequest.md)| Parameters for the &#39;send push&#39; action | 

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
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_push_campaign**
> HashcodeCampaign create_push_campaign(push_campaign_post_request)

Create new push campaign

Create a new push campaign

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
api_instance = egoi_api.PushApi(egoi_api.ApiClient(configuration))
push_campaign_post_request = egoi_api.PushCampaignPostRequest() # PushCampaignPostRequest | Parameters for the push campaign

try:
    # Create new push campaign
    api_response = api_instance.create_push_campaign(push_campaign_post_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PushApi->create_push_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **push_campaign_post_request** | [**PushCampaignPostRequest**](PushCampaignPostRequest.md)| Parameters for the push campaign | 

### Return type

[**HashcodeCampaign**](HashcodeCampaign.md)

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
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_push_app**
> AppStructure get_push_app(app_id)

Get a Push application from E-goi

Get a Push application from E-goi

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
api_instance = egoi_api.PushApi(egoi_api.ApiClient(configuration))
app_id = 'app_id_example' # str | ID of the E-goi push app.

try:
    # Get a Push application from E-goi
    api_response = api_instance.get_push_app(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PushApi->get_push_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the E-goi push app. | 

### Return type

[**AppStructure**](AppStructure.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_push_apps**
> list[AppStructure] get_push_apps(list_id=list_id)

Get all Push applications from E-goi

Get all Push applications from E-goi

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
api_instance = egoi_api.PushApi(egoi_api.ApiClient(configuration))
list_id = 56 # int | ID of the list to search for. (optional)

try:
    # Get all Push applications from E-goi
    api_response = api_instance.get_push_apps(list_id=list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PushApi->get_push_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **int**| ID of the list to search for. | [optional] 

### Return type

[**list[AppStructure]**](AppStructure.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_push_campaign**
> HashcodeCampaign patch_push_campaign(campaign_hash, push_campaign_patch_request)

Update a specific push campaign

Update push campaign

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
api_instance = egoi_api.PushApi(egoi_api.ApiClient(configuration))
campaign_hash = 'campaign_hash_example' # str | ID of the Campaign
push_campaign_patch_request = egoi_api.PushCampaignPatchRequest() # PushCampaignPatchRequest | Parameters for the push campaign

try:
    # Update a specific push campaign
    api_response = api_instance.patch_push_campaign(campaign_hash, push_campaign_patch_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PushApi->patch_push_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_hash** | **str**| ID of the Campaign | 
 **push_campaign_patch_request** | [**PushCampaignPatchRequest**](PushCampaignPatchRequest.md)| Parameters for the push campaign | 

### Return type

[**HashcodeCampaign**](HashcodeCampaign.md)

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

# **register_push_event**
> PushResponse register_push_event(app_id, push_event)

Registers an event from the push notification.

Registers an event from the push notification.

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
api_instance = egoi_api.PushApi(egoi_api.ApiClient(configuration))
app_id = 'app_id_example' # str | ID of the E-goi push app.
push_event = egoi_api.PushEvent() # PushEvent | Parameters for the event

try:
    # Registers an event from the push notification.
    api_response = api_instance.register_push_event(app_id, push_event)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PushApi->register_push_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the E-goi push app. | 
 **push_event** | [**PushEvent**](PushEvent.md)| Parameters for the event | 

### Return type

[**PushResponse**](PushResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_push_token**
> PushResponse register_push_token(app_id, push_token)

Registers a Firebase token

Registers a Firebase token

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
api_instance = egoi_api.PushApi(egoi_api.ApiClient(configuration))
app_id = 'app_id_example' # str | ID of the E-goi push app.
push_token = egoi_api.PushToken() # PushToken | Parameters for the token

try:
    # Registers a Firebase token
    api_response = api_instance.register_push_token(app_id, push_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PushApi->register_push_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| ID of the E-goi push app. | 
 **push_token** | [**PushToken**](PushToken.md)| Parameters for the token | 

### Return type

[**PushResponse**](PushResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

