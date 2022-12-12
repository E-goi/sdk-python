<a name="__pageTop"></a>
# egoi_api.apis.tags.segments_api.SegmentsApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_segment**](#delete_segment) | **delete** /lists/{list_id}/segments/{segment_id} | Remove segment
[**get_all_segments**](#get_all_segments) | **get** /lists/{list_id}/segments | Get all segments

# **delete_segment**
<a name="delete_segment"></a>
> delete_segment(segment_idlist_id)

Remove segment

Remove segment information given its ID

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import segments_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.internal_server_error import InternalServerError
from egoi_api.model.not_found import NotFound
from egoi_api.model.too_many_requests import TooManyRequests
from egoi_api.model.query_id import QueryId
from egoi_api.model.delete_segments_conflict import DeleteSegmentsConflict
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
    api_instance = segments_api.SegmentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'segment_id': "segment_id_example",
        'list_id': QueryId(1),
    }
    try:
        # Remove segment
        api_response = api_instance.delete_segment(
            path_params=path_params,
        )
    except egoi_api.ApiException as e:
        print("Exception when calling SegmentsApi->delete_segment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
segment_id | SegmentIdSchema | | 
list_id | ListIdSchema | | 

# SegmentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ListIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**QueryId**](../../models/QueryId.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_segment.ApiResponseFor204) | No Content
401 | [ApiResponseFor401](#delete_segment.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#delete_segment.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_segment.ApiResponseFor404) | Not Found
408 | [ApiResponseFor408](#delete_segment.ApiResponseFor408) | Request Timeout
409 | [ApiResponseFor409](#delete_segment.ApiResponseFor409) | Conflict
429 | [ApiResponseFor429](#delete_segment.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#delete_segment.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#delete_segment.ApiResponseFor503) | Service Unavailable

#### delete_segment.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_segment.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### delete_segment.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### delete_segment.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### delete_segment.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### delete_segment.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeleteSegmentsConflict**](../../models/DeleteSegmentsConflict.md) |  | 


#### delete_segment.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### delete_segment.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### delete_segment.ApiResponseFor503
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

# **get_all_segments**
<a name="get_all_segments"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_all_segments(list_id)

Get all segments

Returns all segments

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import segments_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.unprocessable_entity import UnprocessableEntity
from egoi_api.model.segment import Segment
from egoi_api.model.internal_server_error import InternalServerError
from egoi_api.model.too_many_requests import TooManyRequests
from egoi_api.model.query_id import QueryId
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
    api_instance = segments_api.SegmentsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'list_id': QueryId(1),
    }
    query_params = {
    }
    try:
        # Get all segments
        api_response = api_instance.get_all_segments(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling SegmentsApi->get_all_segments: %s\n" % e)

    # example passing only optional values
    path_params = {
        'list_id': QueryId(1),
    }
    query_params = {
        'type': "auto",
        'name': "name_example",
        'offset': 0,
        'limit': 10,
    }
    try:
        # Get all segments
        api_response = api_instance.get_all_segments(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling SegmentsApi->get_all_segments: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
type | TypeSchema | | optional
name | NameSchema | | optional
offset | OffsetSchema | | optional
limit | LimitSchema | | optional


# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["auto", "saved", "tag", ] 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
list_id | ListIdSchema | | 

# ListIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**QueryId**](../../models/QueryId.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_all_segments.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#get_all_segments.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_all_segments.ApiResponseFor403) | Forbidden
408 | [ApiResponseFor408](#get_all_segments.ApiResponseFor408) | Request Timeout
422 | [ApiResponseFor422](#get_all_segments.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#get_all_segments.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#get_all_segments.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#get_all_segments.ApiResponseFor503) | Service Unavailable

#### get_all_segments.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

Collection of segments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Collection of segments | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total_items** | decimal.Decimal, int,  | decimal.Decimal,  | Total returned segments | [optional] 
**[items](#items)** | list, tuple,  | tuple,  | Returned segments | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# items

Returned segments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Returned segments | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Segment**]({{complexTypePrefix}}Segment.md) | [**Segment**]({{complexTypePrefix}}Segment.md) | [**Segment**]({{complexTypePrefix}}Segment.md) |  | 

#### get_all_segments.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### get_all_segments.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### get_all_segments.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### get_all_segments.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### get_all_segments.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### get_all_segments.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### get_all_segments.ApiResponseFor503
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

