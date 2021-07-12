# egoi_api.CampaignsApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_campaigns**](CampaignsApi.md#delete_campaigns) | **DELETE** /campaigns/{campaign_hash} | Remove Campaign
[**get_all_campaigns**](CampaignsApi.md#get_all_campaigns) | **GET** /campaigns | Get all Campaigns


# **delete_campaigns**
> delete_campaigns(campaign_hash)

Remove Campaign

Remove campaign information given its ID

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
api_instance = egoi_api.CampaignsApi(egoi_api.ApiClient(configuration))
campaign_hash = 'campaign_hash_example' # str | ID of the Campaign

try:
    # Remove Campaign
    api_instance.delete_campaigns(campaign_hash)
except ApiException as e:
    print("Exception when calling CampaignsApi->delete_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_hash** | **str**| ID of the Campaign | 

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
**408** | Request Timeout |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_campaigns**
> CampaignsCollection get_all_campaigns(channel=channel, campaign_hash=campaign_hash, list_id=list_id, status=status, internal_name=internal_name, created_by=created_by, group_id=group_id, created_min=created_min, created_max=created_max, updated_min=updated_min, updated_max=updated_max, start_date_min=start_date_min, start_date_max=start_date_max, end_date_min=end_date_min, end_date_max=end_date_max, schedule_date_min=schedule_date_min, schedule_date_max=schedule_date_max, offset=offset, limit=limit, order=order, order_by=order_by)

Get all Campaigns

Returns all campaigns

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
api_instance = egoi_api.CampaignsApi(egoi_api.ApiClient(configuration))
channel = 'channel_example' # str | Channel of the campaign (optional)
campaign_hash = 'campaign_hash_example' # str | Hash of the campaign (optional)
list_id = 56 # int | ID of the list where the campaign belongs (optional)
status = 'status_example' # str | Status of the campaign (optional)
internal_name = 'internal_name_example' # str | Internal name of the campaign (optional)
created_by = 56 # int | ID of the user who created the campaign (optional)
group_id = 56 # int | ID of the group where the campaign belongs (optional)
created_min = '2013-10-20T19:20:30+01:00' # datetime | Created initial date (optional)
created_max = '2013-10-20T19:20:30+01:00' # datetime | Created finish (optional)
updated_min = '2013-10-20T19:20:30+01:00' # datetime | Updated initial (optional)
updated_max = '2013-10-20T19:20:30+01:00' # datetime | Updated finish (optional)
start_date_min = '2013-10-20' # date | Start date initial (optional)
start_date_max = '2013-10-20' # date | Start date finish (optional)
end_date_min = '2013-10-20' # date | End Date initial (optional)
end_date_max = '2013-10-20' # date | End Date finish (optional)
schedule_date_min = '2013-10-20' # date | Schedule Date initial (optional)
schedule_date_max = '2013-10-20' # date | Schedule Date finish (optional)
offset = 56 # int | Element offset (starting at zero for the first element) (optional)
limit = 10 # int | Number of items to return (optional) (default to 10)
order = 'desc' # str | Type of order (optional) (default to 'desc')
order_by = 'created' # str | Reference attribute to order campaigns (optional) (default to 'created')

try:
    # Get all Campaigns
    api_response = api_instance.get_all_campaigns(channel=channel, campaign_hash=campaign_hash, list_id=list_id, status=status, internal_name=internal_name, created_by=created_by, group_id=group_id, created_min=created_min, created_max=created_max, updated_min=updated_min, updated_max=updated_max, start_date_min=start_date_min, start_date_max=start_date_max, end_date_min=end_date_min, end_date_max=end_date_max, schedule_date_min=schedule_date_min, schedule_date_max=schedule_date_max, offset=offset, limit=limit, order=order, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->get_all_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel** | **str**| Channel of the campaign | [optional] 
 **campaign_hash** | **str**| Hash of the campaign | [optional] 
 **list_id** | **int**| ID of the list where the campaign belongs | [optional] 
 **status** | **str**| Status of the campaign | [optional] 
 **internal_name** | **str**| Internal name of the campaign | [optional] 
 **created_by** | **int**| ID of the user who created the campaign | [optional] 
 **group_id** | **int**| ID of the group where the campaign belongs | [optional] 
 **created_min** | **datetime**| Created initial date | [optional] 
 **created_max** | **datetime**| Created finish | [optional] 
 **updated_min** | **datetime**| Updated initial | [optional] 
 **updated_max** | **datetime**| Updated finish | [optional] 
 **start_date_min** | **date**| Start date initial | [optional] 
 **start_date_max** | **date**| Start date finish | [optional] 
 **end_date_min** | **date**| End Date initial | [optional] 
 **end_date_max** | **date**| End Date finish | [optional] 
 **schedule_date_min** | **date**| Schedule Date initial | [optional] 
 **schedule_date_max** | **date**| Schedule Date finish | [optional] 
 **offset** | **int**| Element offset (starting at zero for the first element) | [optional] 
 **limit** | **int**| Number of items to return | [optional] [default to 10]
 **order** | **str**| Type of order | [optional] [default to &#39;desc&#39;]
 **order_by** | **str**| Reference attribute to order campaigns | [optional] [default to &#39;created&#39;]

### Return type

[**CampaignsCollection**](CampaignsCollection.md)

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

