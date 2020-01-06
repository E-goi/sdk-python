# egoi-api.PushApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action_send_push**](PushApi.md#action_send_push) | **POST** /campaigns/push/{campaign_hash}/actions/send | Send push message
[**create_push_campaign**](PushApi.md#create_push_campaign) | **POST** /campaigns/push | Create new push campaign
[**patch_push_campaign**](PushApi.md#patch_push_campaign) | **PATCH** /campaigns/push/{campaign_hash} | Update a specific push campaign


# **action_send_push**
> AcceptedResponse action_send_push(campaign_hash, campaign_push_send_request)

Send push message

Deploys and sends a push message

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
api_instance = egoi-api.PushApi(egoi-api.ApiClient(configuration))
campaign_hash = 'campaign_hash_example' # str | ID of the Campaign
campaign_push_send_request = egoi-api.CampaignPushSendRequest() # CampaignPushSendRequest | Parameters for the 'send push' action

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
**500** | Internal Server Error |  -  |

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
api_instance = egoi-api.PushApi(egoi-api.ApiClient(configuration))
push_campaign_post_request = egoi-api.PushCampaignPostRequest() # PushCampaignPostRequest | Parameters for the push campaign

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
**500** | Internal Server Error |  -  |

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
api_instance = egoi-api.PushApi(egoi-api.ApiClient(configuration))
campaign_hash = 'campaign_hash_example' # str | ID of the Campaign
push_campaign_patch_request = egoi-api.PushCampaignPatchRequest() # PushCampaignPatchRequest | Parameters for the push campaign

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
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

