# egoi-api.EmailApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action_enable_email_rss**](EmailApi.md#action_enable_email_rss) | **POST** /campaigns/email/rss/{campaign_hash}/actions/enable | Enables a rss email campaign
[**action_send_email**](EmailApi.md#action_send_email) | **POST** /campaigns/email/{campaign_hash}/actions/send | Send email message
[**create_email_campaign**](EmailApi.md#create_email_campaign) | **POST** /campaigns/email | Create new email campaign
[**create_email_rss_campaign**](EmailApi.md#create_email_rss_campaign) | **POST** /campaigns/email/rss | Create new email rss campaign
[**patch_email_campaign**](EmailApi.md#patch_email_campaign) | **PATCH** /campaigns/email/{campaign_hash} | Update a specific email campaign


# **action_enable_email_rss**
> AcceptedResponse action_enable_email_rss(campaign_hash)

Enables a rss email campaign

Enables a rss email message

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
api_instance = egoi-api.EmailApi(egoi-api.ApiClient(configuration))
campaign_hash = 'campaign_hash_example' # str | ID of the Campaign

try:
    # Enables a rss email campaign
    api_response = api_instance.action_enable_email_rss(campaign_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailApi->action_enable_email_rss: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_hash** | **str**| ID of the Campaign | 

### Return type

[**AcceptedResponse**](AcceptedResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **action_send_email**
> AcceptedResponse action_send_email(campaign_hash, campaign_email_send_request)

Send email message

Deploys and sends an email message

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
api_instance = egoi-api.EmailApi(egoi-api.ApiClient(configuration))
campaign_hash = 'campaign_hash_example' # str | ID of the Campaign
campaign_email_send_request = egoi-api.CampaignEmailSendRequest() # CampaignEmailSendRequest | Parameters for the 'send email' action

try:
    # Send email message
    api_response = api_instance.action_send_email(campaign_hash, campaign_email_send_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailApi->action_send_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_hash** | **str**| ID of the Campaign | 
 **campaign_email_send_request** | [**CampaignEmailSendRequest**](CampaignEmailSendRequest.md)| Parameters for the &#39;send email&#39; action | 

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

# **create_email_campaign**
> HashcodeCampaign create_email_campaign(email_campaign_create)

Create new email campaign

Create a new email campaign

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
api_instance = egoi-api.EmailApi(egoi-api.ApiClient(configuration))
email_campaign_create = egoi-api.EmailCampaignCreate() # EmailCampaignCreate | Parameters for the Email Campaign

try:
    # Create new email campaign
    api_response = api_instance.create_email_campaign(email_campaign_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailApi->create_email_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_campaign_create** | [**EmailCampaignCreate**](EmailCampaignCreate.md)| Parameters for the Email Campaign | 

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_email_rss_campaign**
> HashcodeCampaign create_email_rss_campaign(email_rss_campaign_create)

Create new email rss campaign

Create a new email rss campaign

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
api_instance = egoi-api.EmailApi(egoi-api.ApiClient(configuration))
email_rss_campaign_create = egoi-api.EmailRssCampaignCreate() # EmailRssCampaignCreate | Parameters for the Email Campaign

try:
    # Create new email rss campaign
    api_response = api_instance.create_email_rss_campaign(email_rss_campaign_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailApi->create_email_rss_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_rss_campaign_create** | [**EmailRssCampaignCreate**](EmailRssCampaignCreate.md)| Parameters for the Email Campaign | 

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_email_campaign**
> HashcodeCampaign patch_email_campaign(campaign_hash, email_campaign_patch)

Update a specific email campaign

Update email campaign

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
api_instance = egoi-api.EmailApi(egoi-api.ApiClient(configuration))
campaign_hash = 'campaign_hash_example' # str | ID of the Campaign
email_campaign_patch = egoi-api.EmailCampaignPatch() # EmailCampaignPatch | Parameters for the Email Campaign

try:
    # Update a specific email campaign
    api_response = api_instance.patch_email_campaign(campaign_hash, email_campaign_patch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailApi->patch_email_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_hash** | **str**| ID of the Campaign | 
 **email_campaign_patch** | [**EmailCampaignPatch**](EmailCampaignPatch.md)| Parameters for the Email Campaign | 

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

