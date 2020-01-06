# egoi-api.CampaignGroupsApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_campaign_group**](CampaignGroupsApi.md#create_campaign_group) | **POST** /campaign-groups | Create new campaign group
[**delete_campaign_group**](CampaignGroupsApi.md#delete_campaign_group) | **DELETE** /campaign-groups/{group_id} | Remove Campaign Group
[**get_all_campaign_groups**](CampaignGroupsApi.md#get_all_campaign_groups) | **GET** /campaign-groups | Get all campaign groups
[**update_campaign_group**](CampaignGroupsApi.md#update_campaign_group) | **PUT** /campaign-groups/{group_id} | Update a specific campaign group


# **create_campaign_group**
> CampaignGroup create_campaign_group(campaign_group)

Create new campaign group

Create a new campaign group

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
api_instance = egoi-api.CampaignGroupsApi(egoi-api.ApiClient(configuration))
campaign_group = egoi-api.CampaignGroup() # CampaignGroup | Parameters for the Campaign Group

try:
    # Create new campaign group
    api_response = api_instance.create_campaign_group(campaign_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignGroupsApi->create_campaign_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_group** | [**CampaignGroup**](CampaignGroup.md)| Parameters for the Campaign Group | 

### Return type

[**CampaignGroup**](CampaignGroup.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_campaign_group**
> delete_campaign_group(group_id)

Remove Campaign Group

Remove campaign group information given its ID

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
api_instance = egoi-api.CampaignGroupsApi(egoi-api.ApiClient(configuration))
group_id = 56 # int | ID of the Campaign Group

try:
    # Remove Campaign Group
    api_instance.delete_campaign_group(group_id)
except ApiException as e:
    print("Exception when calling CampaignGroupsApi->delete_campaign_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| ID of the Campaign Group | 

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
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_campaign_groups**
> CampaignGroupCollection get_all_campaign_groups(group_id=group_id, name=name, limit=limit, offset=offset)

Get all campaign groups

Returns all campaign groups

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
api_instance = egoi-api.CampaignGroupsApi(egoi-api.ApiClient(configuration))
group_id = 56 # int | Reference attribute to campaign group id (optional)
name = 'name_example' # str | Reference attribute to campaign group id (optional)
limit = 10 # int | Number of items to return (optional) (default to 10)
offset = 56 # int | Element offset (starting at zero for the first element) (optional)

try:
    # Get all campaign groups
    api_response = api_instance.get_all_campaign_groups(group_id=group_id, name=name, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignGroupsApi->get_all_campaign_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Reference attribute to campaign group id | [optional] 
 **name** | **str**| Reference attribute to campaign group id | [optional] 
 **limit** | **int**| Number of items to return | [optional] [default to 10]
 **offset** | **int**| Element offset (starting at zero for the first element) | [optional] 

### Return type

[**CampaignGroupCollection**](CampaignGroupCollection.md)

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

# **update_campaign_group**
> CampaignGroup update_campaign_group(group_id, campaign_group)

Update a specific campaign group

Update a campaign group

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
api_instance = egoi-api.CampaignGroupsApi(egoi-api.ApiClient(configuration))
group_id = 56 # int | ID of the Campaign Group
campaign_group = egoi-api.CampaignGroup() # CampaignGroup | Parameters for the Campaign Group

try:
    # Update a specific campaign group
    api_response = api_instance.update_campaign_group(group_id, campaign_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignGroupsApi->update_campaign_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| ID of the Campaign Group | 
 **campaign_group** | [**CampaignGroup**](CampaignGroup.md)| Parameters for the Campaign Group | 

### Return type

[**CampaignGroup**](CampaignGroup.md)

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

