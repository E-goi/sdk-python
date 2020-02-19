# egoi-api.SmartSmsApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action_send_smart_sms**](SmartSmsApi.md#action_send_smart_sms) | **POST** /campaigns/smart-sms/{campaign_hash}/actions/send | Send smart sms message
[**create_smart_sms_campaign**](SmartSmsApi.md#create_smart_sms_campaign) | **POST** /campaigns/smart-sms | Create new smart sms campaign
[**patch_smart_sms_campaign**](SmartSmsApi.md#patch_smart_sms_campaign) | **PATCH** /campaigns/smart-sms/{campaign_hash} | Update a specific smart sms campaign


# **action_send_smart_sms**
> AcceptedResponse action_send_smart_sms(campaign_hash, campaign_sms_send_request)

Send smart sms message

Deploys and sends a smart sms message

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
api_instance = egoi-api.SmartSmsApi(egoi-api.ApiClient(configuration))
campaign_hash = 'campaign_hash_example' # str | ID of the Campaign
campaign_sms_send_request = egoi-api.CampaignSmsSendRequest() # CampaignSmsSendRequest | Parameters for the 'send sms' action

try:
    # Send smart sms message
    api_response = api_instance.action_send_smart_sms(campaign_hash, campaign_sms_send_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmartSmsApi->action_send_smart_sms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_hash** | **str**| ID of the Campaign | 
 **campaign_sms_send_request** | [**CampaignSmsSendRequest**](CampaignSmsSendRequest.md)| Parameters for the &#39;send sms&#39; action | 

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
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_smart_sms_campaign**
> HashcodeCampaign create_smart_sms_campaign(smart_sms_campaign)

Create new smart sms campaign

Creates a new smart sms campaign.                         **DISCLAIMER:** A URL will be added at the end of your SMS

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
api_instance = egoi-api.SmartSmsApi(egoi-api.ApiClient(configuration))
smart_sms_campaign = egoi-api.SmartSmsCampaign() # SmartSmsCampaign | Parameters for the Smart Sms Campaign

try:
    # Create new smart sms campaign
    api_response = api_instance.create_smart_sms_campaign(smart_sms_campaign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmartSmsApi->create_smart_sms_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_sms_campaign** | [**SmartSmsCampaign**](SmartSmsCampaign.md)| Parameters for the Smart Sms Campaign | 

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
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_smart_sms_campaign**
> HashcodeCampaign patch_smart_sms_campaign(campaign_hash, smart_sms_campaign_patch_request)

Update a specific smart sms campaign

Update smart sms campaign

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
api_instance = egoi-api.SmartSmsApi(egoi-api.ApiClient(configuration))
campaign_hash = 'campaign_hash_example' # str | ID of the Campaign
smart_sms_campaign_patch_request = egoi-api.SmartSmsCampaignPatchRequest() # SmartSmsCampaignPatchRequest | Parameters for the Smart Sms Campaign

try:
    # Update a specific smart sms campaign
    api_response = api_instance.patch_smart_sms_campaign(campaign_hash, smart_sms_campaign_patch_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmartSmsApi->patch_smart_sms_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_hash** | **str**| ID of the Campaign | 
 **smart_sms_campaign_patch_request** | [**SmartSmsCampaignPatchRequest**](SmartSmsCampaignPatchRequest.md)| Parameters for the Smart Sms Campaign | 

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

