# egoi_api.AdvancedReportsApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_email_bounces_report**](AdvancedReportsApi.md#generate_email_bounces_report) | **POST** /reports/advanced/email-bounces | Generate email bounces report
[**generate_email_clicks_by_contact_report**](AdvancedReportsApi.md#generate_email_clicks_by_contact_report) | **POST** /reports/advanced/email-clicks-by-contact | Generate email clicks by contact report
[**generate_email_clicks_by_url_report**](AdvancedReportsApi.md#generate_email_clicks_by_url_report) | **POST** /reports/advanced/email-clicks-by-url | Generate email clicks by URL report
[**generate_email_events_report**](AdvancedReportsApi.md#generate_email_events_report) | **POST** /reports/advanced/email-events | Generate email events report
[**generate_email_sms_report**](AdvancedReportsApi.md#generate_email_sms_report) | **POST** /reports/advanced/sms-bounces | Generate SMS bounces report
[**generate_email_unsubscriptions_report**](AdvancedReportsApi.md#generate_email_unsubscriptions_report) | **POST** /reports/advanced/email-unsubscriptions | Generate email unsubscriptions report
[**generate_form_answers_report**](AdvancedReportsApi.md#generate_form_answers_report) | **POST** /reports/advanced/form-answers | Generate form answers report
[**generate_sends_report**](AdvancedReportsApi.md#generate_sends_report) | **POST** /reports/advanced/sends | Generate sends report
[**generate_sms_events_report**](AdvancedReportsApi.md#generate_sms_events_report) | **POST** /reports/advanced/sms-events | Generate SMS events report
[**generate_subscriptions_report**](AdvancedReportsApi.md#generate_subscriptions_report) | **POST** /reports/advanced/subscriptions | Generate subscriptions report
[**generate_unsubscriptions_report**](AdvancedReportsApi.md#generate_unsubscriptions_report) | **POST** /reports/advanced/unsubscriptions | Generate unsubscriptions report
[**get_all_advanced_reports**](AdvancedReportsApi.md#get_all_advanced_reports) | **GET** /reports/advanced | Get all advanced reports


# **generate_email_bounces_report**
> AcceptedResponse generate_email_bounces_report(generate_email_bounces_report)

Generate email bounces report

Generates a new email bounces report

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
api_instance = egoi_api.AdvancedReportsApi(egoi_api.ApiClient(configuration))
generate_email_bounces_report = egoi_api.GenerateEmailBouncesReport() # GenerateEmailBouncesReport | Parameters for the email bounces report

try:
    # Generate email bounces report
    api_response = api_instance.generate_email_bounces_report(generate_email_bounces_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedReportsApi->generate_email_bounces_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_email_bounces_report** | [**GenerateEmailBouncesReport**](GenerateEmailBouncesReport.md)| Parameters for the email bounces report | 

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
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_email_clicks_by_contact_report**
> AcceptedResponse generate_email_clicks_by_contact_report(generate_email_clicks_by_contact_report)

Generate email clicks by contact report

Generates a new email clicks by contact report

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
api_instance = egoi_api.AdvancedReportsApi(egoi_api.ApiClient(configuration))
generate_email_clicks_by_contact_report = egoi_api.GenerateEmailClicksByContactReport() # GenerateEmailClicksByContactReport | Parameters for the email clicks by contact report

try:
    # Generate email clicks by contact report
    api_response = api_instance.generate_email_clicks_by_contact_report(generate_email_clicks_by_contact_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedReportsApi->generate_email_clicks_by_contact_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_email_clicks_by_contact_report** | [**GenerateEmailClicksByContactReport**](GenerateEmailClicksByContactReport.md)| Parameters for the email clicks by contact report | 

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
**408** | Request Timeout |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_email_clicks_by_url_report**
> AcceptedResponse generate_email_clicks_by_url_report(generate_email_clicks_by_url_report)

Generate email clicks by URL report

Generates a new email clicks by URL report

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
api_instance = egoi_api.AdvancedReportsApi(egoi_api.ApiClient(configuration))
generate_email_clicks_by_url_report = egoi_api.GenerateEmailClicksByUrlReport() # GenerateEmailClicksByUrlReport | Parameters for the email clicks by URL report

try:
    # Generate email clicks by URL report
    api_response = api_instance.generate_email_clicks_by_url_report(generate_email_clicks_by_url_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedReportsApi->generate_email_clicks_by_url_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_email_clicks_by_url_report** | [**GenerateEmailClicksByUrlReport**](GenerateEmailClicksByUrlReport.md)| Parameters for the email clicks by URL report | 

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
**408** | Request Timeout |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_email_events_report**
> AcceptedResponse generate_email_events_report(generate_email_events_report)

Generate email events report

Generates a new email events report

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
api_instance = egoi_api.AdvancedReportsApi(egoi_api.ApiClient(configuration))
generate_email_events_report = egoi_api.GenerateEmailEventsReport() # GenerateEmailEventsReport | Parameters for the email events report

try:
    # Generate email events report
    api_response = api_instance.generate_email_events_report(generate_email_events_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedReportsApi->generate_email_events_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_email_events_report** | [**GenerateEmailEventsReport**](GenerateEmailEventsReport.md)| Parameters for the email events report | 

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
**408** | Request Timeout |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_email_sms_report**
> AcceptedResponse generate_email_sms_report(generate_sms_bounces_report)

Generate SMS bounces report

Generates a new SMS bounces report

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
api_instance = egoi_api.AdvancedReportsApi(egoi_api.ApiClient(configuration))
generate_sms_bounces_report = egoi_api.GenerateSmsBouncesReport() # GenerateSmsBouncesReport | Parameters for the SMS bounces report

try:
    # Generate SMS bounces report
    api_response = api_instance.generate_email_sms_report(generate_sms_bounces_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedReportsApi->generate_email_sms_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_sms_bounces_report** | [**GenerateSmsBouncesReport**](GenerateSmsBouncesReport.md)| Parameters for the SMS bounces report | 

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
**408** | Request Timeout |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_email_unsubscriptions_report**
> AcceptedResponse generate_email_unsubscriptions_report(generate_email_unsubscriptions_report)

Generate email unsubscriptions report

Generates a new email unsubscriptions report

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
api_instance = egoi_api.AdvancedReportsApi(egoi_api.ApiClient(configuration))
generate_email_unsubscriptions_report = egoi_api.GenerateEmailUnsubscriptionsReport() # GenerateEmailUnsubscriptionsReport | Parameters for the email unsubscriptions report

try:
    # Generate email unsubscriptions report
    api_response = api_instance.generate_email_unsubscriptions_report(generate_email_unsubscriptions_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedReportsApi->generate_email_unsubscriptions_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_email_unsubscriptions_report** | [**GenerateEmailUnsubscriptionsReport**](GenerateEmailUnsubscriptionsReport.md)| Parameters for the email unsubscriptions report | 

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
**408** | Request Timeout |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_form_answers_report**
> AcceptedResponse generate_form_answers_report(generate_form_answers_report)

Generate form answers report

Generates a new form answers report

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
api_instance = egoi_api.AdvancedReportsApi(egoi_api.ApiClient(configuration))
generate_form_answers_report = egoi_api.GenerateFormAnswersReport() # GenerateFormAnswersReport | Parameters for the form answers report

try:
    # Generate form answers report
    api_response = api_instance.generate_form_answers_report(generate_form_answers_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedReportsApi->generate_form_answers_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_form_answers_report** | [**GenerateFormAnswersReport**](GenerateFormAnswersReport.md)| Parameters for the form answers report | 

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
**408** | Request Timeout |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_sends_report**
> AcceptedResponse generate_sends_report(generate_sends_report)

Generate sends report

Generates a new sends report

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
api_instance = egoi_api.AdvancedReportsApi(egoi_api.ApiClient(configuration))
generate_sends_report = egoi_api.GenerateSendsReport() # GenerateSendsReport | Parameters for the sends report

try:
    # Generate sends report
    api_response = api_instance.generate_sends_report(generate_sends_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedReportsApi->generate_sends_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_sends_report** | [**GenerateSendsReport**](GenerateSendsReport.md)| Parameters for the sends report | 

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
**408** | Request Timeout |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_sms_events_report**
> AcceptedResponse generate_sms_events_report(generate_sms_events_report)

Generate SMS events report

Generates a new SMS events report

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
api_instance = egoi_api.AdvancedReportsApi(egoi_api.ApiClient(configuration))
generate_sms_events_report = egoi_api.GenerateSmsEventsReport() # GenerateSmsEventsReport | Parameters for the SMS events report

try:
    # Generate SMS events report
    api_response = api_instance.generate_sms_events_report(generate_sms_events_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedReportsApi->generate_sms_events_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_sms_events_report** | [**GenerateSmsEventsReport**](GenerateSmsEventsReport.md)| Parameters for the SMS events report | 

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
**408** | Request Timeout |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_subscriptions_report**
> AcceptedResponse generate_subscriptions_report(generate_subscriptions_report)

Generate subscriptions report

Generates a new subscriptions report

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
api_instance = egoi_api.AdvancedReportsApi(egoi_api.ApiClient(configuration))
generate_subscriptions_report = egoi_api.GenerateSubscriptionsReport() # GenerateSubscriptionsReport | Parameters for the subscriptions report

try:
    # Generate subscriptions report
    api_response = api_instance.generate_subscriptions_report(generate_subscriptions_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedReportsApi->generate_subscriptions_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_subscriptions_report** | [**GenerateSubscriptionsReport**](GenerateSubscriptionsReport.md)| Parameters for the subscriptions report | 

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
**408** | Request Timeout |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_unsubscriptions_report**
> AcceptedResponse generate_unsubscriptions_report(generate_unsubscriptions_report)

Generate unsubscriptions report

Generates a new unsubscriptions report

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
api_instance = egoi_api.AdvancedReportsApi(egoi_api.ApiClient(configuration))
generate_unsubscriptions_report = egoi_api.GenerateUnsubscriptionsReport() # GenerateUnsubscriptionsReport | Parameters for the unsubscriptions report

try:
    # Generate unsubscriptions report
    api_response = api_instance.generate_unsubscriptions_report(generate_unsubscriptions_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedReportsApi->generate_unsubscriptions_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_unsubscriptions_report** | [**GenerateUnsubscriptionsReport**](GenerateUnsubscriptionsReport.md)| Parameters for the unsubscriptions report | 

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
**408** | Request Timeout |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_advanced_reports**
> AdvancedReportsCollection get_all_advanced_reports(status=status, title=title, created_min=created_min, created_max=created_max, offset=offset, limit=limit, order=order, order_by=order_by)

Get all advanced reports

Returns all advanced reports

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
api_instance = egoi_api.AdvancedReportsApi(egoi_api.ApiClient(configuration))
status = 'status_example' # str | Advanced report status (optional)
title = 'title_example' # str | Advanced report title (optional)
created_min = '2013-10-20T19:20:30+01:00' # datetime | Created initial date (optional)
created_max = '2013-10-20T19:20:30+01:00' # datetime | Created finish (optional)
offset = 56 # int | Element offset (starting at zero for the first element) (optional)
limit = 10 # int | Number of items to return (optional) (default to 10)
order = 'desc' # str | Type of order (optional) (default to 'desc')
order_by = 'advanced_report_id' # str | Reference attribute to order the advanced reports (optional) (default to 'advanced_report_id')

try:
    # Get all advanced reports
    api_response = api_instance.get_all_advanced_reports(status=status, title=title, created_min=created_min, created_max=created_max, offset=offset, limit=limit, order=order, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvancedReportsApi->get_all_advanced_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Advanced report status | [optional] 
 **title** | **str**| Advanced report title | [optional] 
 **created_min** | **datetime**| Created initial date | [optional] 
 **created_max** | **datetime**| Created finish | [optional] 
 **offset** | **int**| Element offset (starting at zero for the first element) | [optional] 
 **limit** | **int**| Number of items to return | [optional] [default to 10]
 **order** | **str**| Type of order | [optional] [default to &#39;desc&#39;]
 **order_by** | **str**| Reference attribute to order the advanced reports | [optional] [default to &#39;advanced_report_id&#39;]

### Return type

[**AdvancedReportsCollection**](AdvancedReportsCollection.md)

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
**408** | Request Timeout |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

