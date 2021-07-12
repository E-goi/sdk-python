# egoi_api.ReportsApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sms_report**](ReportsApi.md#get_sms_report) | **GET** /reports/sms/{campaign_hash} | Get sms report
[**get_voice_report**](ReportsApi.md#get_voice_report) | **GET** /reports/voice/{campaign_hash} | Get voice report
[**get_web_push_report**](ReportsApi.md#get_web_push_report) | **GET** /reports/web-push/{campaign_hash} | Get webpush report


# **get_sms_report**
> PhoneReport get_sms_report(campaign_hash, networks=networks)

Get sms report

Returns sms report given the campaign hash

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
api_instance = egoi_api.ReportsApi(egoi_api.ApiClient(configuration))
campaign_hash = 'campaign_hash_example' # str | ID of the Campaign
networks = True # bool | True to show network stats (optional) (default to True)

try:
    # Get sms report
    api_response = api_instance.get_sms_report(campaign_hash, networks=networks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_sms_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_hash** | **str**| ID of the Campaign | 
 **networks** | **bool**| True to show network stats | [optional] [default to True]

### Return type

[**PhoneReport**](PhoneReport.md)

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
**404** | NotFound |  -  |
**408** | Request Timeout |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voice_report**
> PhoneReport get_voice_report(campaign_hash, networks=networks)

Get voice report

Returns voice report given the campaign hash

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
api_instance = egoi_api.ReportsApi(egoi_api.ApiClient(configuration))
campaign_hash = 'campaign_hash_example' # str | ID of the Campaign
networks = True # bool | True to show network stats (optional) (default to True)

try:
    # Get voice report
    api_response = api_instance.get_voice_report(campaign_hash, networks=networks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_voice_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_hash** | **str**| ID of the Campaign | 
 **networks** | **bool**| True to show network stats | [optional] [default to True]

### Return type

[**PhoneReport**](PhoneReport.md)

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
**404** | NotFound |  -  |
**408** | Request Timeout |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_push_report**
> WebPushReport get_web_push_report(campaign_hash, devices=devices, operating_systems=operating_systems, browsers=browsers, url=url)

Get webpush report

Returns webpush report given the campaign hash

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
api_instance = egoi_api.ReportsApi(egoi_api.ApiClient(configuration))
campaign_hash = 'campaign_hash_example' # str | ID of the Campaign
devices = True # bool | True to show device stats (optional) (default to True)
operating_systems = True # bool | True to show operating systems stats (optional) (default to True)
browsers = True # bool | True to show browser stats (optional) (default to True)
url = True # bool | True to show url stats (optional) (default to True)

try:
    # Get webpush report
    api_response = api_instance.get_web_push_report(campaign_hash, devices=devices, operating_systems=operating_systems, browsers=browsers, url=url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_web_push_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_hash** | **str**| ID of the Campaign | 
 **devices** | **bool**| True to show device stats | [optional] [default to True]
 **operating_systems** | **bool**| True to show operating systems stats | [optional] [default to True]
 **browsers** | **bool**| True to show browser stats | [optional] [default to True]
 **url** | **bool**| True to show url stats | [optional] [default to True]

### Return type

[**WebPushReport**](WebPushReport.md)

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
**404** | NotFound |  -  |
**408** | Request Timeout |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

