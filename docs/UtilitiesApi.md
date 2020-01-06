# egoi-api.UtilitiesApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_countries**](UtilitiesApi.md#get_all_countries) | **GET** /utilities/countries | Get all countries


# **get_all_countries**
> CountryCollection get_all_countries(phone=phone)

Get all countries

Returns all countries

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
api_instance = egoi-api.UtilitiesApi(egoi-api.ApiClient(configuration))
phone = 'phone_example' # str | Phone number without country code to get all countries which can use that phone number (optional)

try:
    # Get all countries
    api_response = api_instance.get_all_countries(phone=phone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilitiesApi->get_all_countries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**| Phone number without country code to get all countries which can use that phone number | [optional] 

### Return type

[**CountryCollection**](CountryCollection.md)

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

