<a name="__pageTop"></a>
# egoi_api.apis.tags.track_engage_api.TrackEngageApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_domains**](#get_all_domains) | **get** /trackengage/domains | Get all domains
[**get_all_goals**](#get_all_goals) | **get** /trackengage/goals | Get all goals

# **get_all_domains**
<a name="get_all_domains"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_all_domains()

Get all domains

Returns all domains

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import track_engage_api
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.domain import Domain
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.unprocessable_entity import UnprocessableEntity
from egoi_api.model.internal_server_error import InternalServerError
from egoi_api.model.too_many_requests import TooManyRequests
from egoi_api.model.forbidden import Forbidden
from pprint import pprint
# Defining the host is optional and defaults to https://api.egoiapp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = egoi_api.Configuration(
    host = "https://api.egoiapp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Apikey
configuration.api_key['Apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'
# Enter a context with an instance of the API client
with egoi_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = track_engage_api.TrackEngageApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all domains
        api_response = api_instance.get_all_domains()
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling TrackEngageApi->get_all_domains: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_all_domains.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#get_all_domains.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_all_domains.ApiResponseFor403) | Forbidden
422 | [ApiResponseFor422](#get_all_domains.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#get_all_domains.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#get_all_domains.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#get_all_domains.ApiResponseFor503) | Service Unavailable

#### get_all_domains.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

Collection of Domains

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Collection of Domains | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total_items** | decimal.Decimal, int,  | decimal.Decimal,  | Returned domains | [optional] 
**[items](#items)** | list, tuple,  | tuple,  | Returned domains | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# items

Returned domains

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Returned domains | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Domain**]({{complexTypePrefix}}Domain.md) | [**Domain**]({{complexTypePrefix}}Domain.md) | [**Domain**]({{complexTypePrefix}}Domain.md) |  | 

#### get_all_domains.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### get_all_domains.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### get_all_domains.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### get_all_domains.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### get_all_domains.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### get_all_domains.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServiceUnavailable**](../../models/ServiceUnavailable.md) |  | 


### Authorization

[Apikey](../../../README.md#Apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_all_goals**
<a name="get_all_goals"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_all_goals()

Get all goals

Returns all goals

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import track_engage_api
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.unprocessable_entity import UnprocessableEntity
from egoi_api.model.internal_server_error import InternalServerError
from egoi_api.model.goal import Goal
from egoi_api.model.too_many_requests import TooManyRequests
from egoi_api.model.forbidden import Forbidden
from pprint import pprint
# Defining the host is optional and defaults to https://api.egoiapp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = egoi_api.Configuration(
    host = "https://api.egoiapp.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Apikey
configuration.api_key['Apikey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'
# Enter a context with an instance of the API client
with egoi_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = track_engage_api.TrackEngageApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all goals
        api_response = api_instance.get_all_goals()
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling TrackEngageApi->get_all_goals: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_all_goals.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#get_all_goals.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_all_goals.ApiResponseFor403) | Forbidden
422 | [ApiResponseFor422](#get_all_goals.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#get_all_goals.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#get_all_goals.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#get_all_goals.ApiResponseFor503) | Service Unavailable

#### get_all_goals.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

Collection of Goals

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Collection of Goals | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total_items** | decimal.Decimal, int,  | decimal.Decimal,  | Returned goals | [optional] 
**[items](#items)** | list, tuple,  | tuple,  | Returned goals | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# items

Returned goals

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Returned goals | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Goal**]({{complexTypePrefix}}Goal.md) | [**Goal**]({{complexTypePrefix}}Goal.md) | [**Goal**]({{complexTypePrefix}}Goal.md) |  | 

#### get_all_goals.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### get_all_goals.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### get_all_goals.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### get_all_goals.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### get_all_goals.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### get_all_goals.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ServiceUnavailable**](../../models/ServiceUnavailable.md) |  | 


### Authorization

[Apikey](../../../README.md#Apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

