# egoi-api.VoiceApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action_send_voice**](VoiceApi.md#action_send_voice) | **POST** /campaigns/voice/{campaign_hash}/actions/send | Send voice message
[**create_voice_campaign**](VoiceApi.md#create_voice_campaign) | **POST** /campaigns/voice | Create new voice campaign
[**patch_voice_campaign**](VoiceApi.md#patch_voice_campaign) | **PATCH** /campaigns/voice/{campaign_hash} | Update a specific voice campaign


# **action_send_voice**
> AcceptedResponse action_send_voice(campaign_hash, campaign_voice_send_request)

Send voice message

Deploys and sends an voice message

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
api_instance = egoi-api.VoiceApi(egoi-api.ApiClient(configuration))
campaign_hash = 'campaign_hash_example' # str | ID of the Campaign
campaign_voice_send_request = {"schedule_date":"2019-04-01 12:30:23","list_id":1,"segments":{"type":"none"},"notify":[0],"destination_field":"cellphone","limit_contacts":{"type":"percent","value":10},"limit_hour":{"hour_start":"01:00","hour_end":"04:00"},"limit_speed":1} # CampaignVoiceSendRequest | Parameters for the 'send voice' action

try:
    # Send voice message
    api_response = api_instance.action_send_voice(campaign_hash, campaign_voice_send_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->action_send_voice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_hash** | **str**| ID of the Campaign | 
 **campaign_voice_send_request** | [**CampaignVoiceSendRequest**](CampaignVoiceSendRequest.md)| Parameters for the &#39;send voice&#39; action | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_voice_campaign**
> CampaignHash create_voice_campaign(voice_campaign)

Create new voice campaign

Create a new voice campaign

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
api_instance = egoi-api.VoiceApi(egoi-api.ApiClient(configuration))
voice_campaign = egoi-api.VoiceCampaign() # VoiceCampaign | Parameters for the Voice Campaign

try:
    # Create new voice campaign
    api_response = api_instance.create_voice_campaign(voice_campaign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->create_voice_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voice_campaign** | [**VoiceCampaign**](VoiceCampaign.md)| Parameters for the Voice Campaign | 

### Return type

[**CampaignHash**](CampaignHash.md)

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

# **patch_voice_campaign**
> CampaignHash patch_voice_campaign(campaign_hash, voice_patch_campaign)

Update a specific voice campaign

Update a voice campaign

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
api_instance = egoi-api.VoiceApi(egoi-api.ApiClient(configuration))
campaign_hash = 'campaign_hash_example' # str | ID of the Campaign
voice_patch_campaign = egoi-api.VoicePatchCampaign() # VoicePatchCampaign | Parameters for the Voice Campaign

try:
    # Update a specific voice campaign
    api_response = api_instance.patch_voice_campaign(campaign_hash, voice_patch_campaign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->patch_voice_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_hash** | **str**| ID of the Campaign | 
 **voice_patch_campaign** | [**VoicePatchCampaign**](VoicePatchCampaign.md)| Parameters for the Voice Campaign | 

### Return type

[**CampaignHash**](CampaignHash.md)

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

