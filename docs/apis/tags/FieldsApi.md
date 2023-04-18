<a name="__pageTop"></a>
# egoi_api.apis.tags.fields_api.FieldsApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_extra_field**](#create_extra_field) | **post** /lists/{list_id}/fields/extra | Create extra field
[**create_field_option**](#create_field_option) | **post** /lists/{list_id}/fields/extra/{field_id}/options | Create new field option
[**delete_extra_field**](#delete_extra_field) | **delete** /lists/{list_id}/fields/extra/{field_id} | Remove extra field
[**delete_field_option**](#delete_field_option) | **delete** /lists/{list_id}/fields/extra/{field_id}/options/{option_id} | Deletes an option
[**get_all_field_options**](#get_all_field_options) | **get** /lists/{list_id}/fields/extra/{field_id}/options | Get all field options
[**get_all_fields**](#get_all_fields) | **get** /lists/{list_id}/fields | Get all fields
[**patch_base_field**](#patch_base_field) | **patch** /lists/{list_id}/fields/base/{field_id} | Update base field
[**patch_extra_field**](#patch_extra_field) | **patch** /lists/{list_id}/fields/extra/{field_id} | Update extra field
[**update_field_option**](#update_field_option) | **patch** /lists/{list_id}/fields/extra/{field_id}/options/{option_id} | Update field option

# **create_extra_field**
<a name="create_extra_field"></a>
> Field create_extra_field(list_idfield)

Create extra field

Creates an extra field

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import fields_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.field import Field
from egoi_api.model.bad_request import BadRequest
from egoi_api.model.unprocessable_entity import UnprocessableEntity
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
    api_instance = fields_api.FieldsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'list_id': QueryId(1),
    }
    body = Field(
        field_id="field_id_example",
        name="name_example",
        format="date",
        unique=True,
    )
    try:
        # Create extra field
        api_response = api_instance.create_extra_field(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling FieldsApi->create_extra_field: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Field**](../../models/Field.md) |  | 


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
201 | [ApiResponseFor201](#create_extra_field.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_extra_field.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#create_extra_field.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#create_extra_field.ApiResponseFor403) | Forbidden
408 | [ApiResponseFor408](#create_extra_field.ApiResponseFor408) | Request Timeout
422 | [ApiResponseFor422](#create_extra_field.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#create_extra_field.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#create_extra_field.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#create_extra_field.ApiResponseFor503) | Service Unavailable

#### create_extra_field.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Field**](../../models/Field.md) |  | 


#### create_extra_field.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### create_extra_field.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### create_extra_field.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### create_extra_field.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### create_extra_field.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### create_extra_field.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### create_extra_field.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### create_extra_field.ApiResponseFor503
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

# **create_field_option**
<a name="create_field_option"></a>
> FieldOption create_field_option(list_idfield_idfield_option_post)

Create new field option

Creates a field option

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import fields_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.field_option import FieldOption
from egoi_api.model.bad_request import BadRequest
from egoi_api.model.unprocessable_entity import UnprocessableEntity
from egoi_api.model.field_option_post import FieldOptionPost
from egoi_api.model.internal_server_error import InternalServerError
from egoi_api.model.not_found import NotFound
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
    api_instance = fields_api.FieldsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'list_id': QueryId(1),
        'field_id': QueryId(1),
    }
    body = FieldOptionPost(
        en="English example",
        pt="Portuguese example",
        br="Brazilian portuguese example",
        es="Spanish example",
        de="German example",
        hu="Hungarian example",
        fr="French example",
    )
    try:
        # Create new field option
        api_response = api_instance.create_field_option(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling FieldsApi->create_field_option: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FieldOptionPost**](../../models/FieldOptionPost.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
list_id | ListIdSchema | | 
field_id | FieldIdSchema | | 

# ListIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**QueryId**](../../models/QueryId.md) |  | 


# FieldIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**QueryId**](../../models/QueryId.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_field_option.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_field_option.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#create_field_option.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#create_field_option.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_field_option.ApiResponseFor404) | Forbidden
408 | [ApiResponseFor408](#create_field_option.ApiResponseFor408) | Request Timeout
422 | [ApiResponseFor422](#create_field_option.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#create_field_option.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#create_field_option.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#create_field_option.ApiResponseFor503) | Service Unavailable

#### create_field_option.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FieldOption**](../../models/FieldOption.md) |  | 


#### create_field_option.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### create_field_option.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### create_field_option.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### create_field_option.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### create_field_option.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### create_field_option.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### create_field_option.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### create_field_option.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### create_field_option.ApiResponseFor503
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

# **delete_extra_field**
<a name="delete_extra_field"></a>
> delete_extra_field(list_idfield_id)

Remove extra field

Removes an extra field given its ID

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import fields_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.internal_server_error import InternalServerError
from egoi_api.model.not_found import NotFound
from egoi_api.model.delete_fields_conflict import DeleteFieldsConflict
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
    api_instance = fields_api.FieldsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'list_id': QueryId(1),
        'field_id': QueryId(1),
    }
    try:
        # Remove extra field
        api_response = api_instance.delete_extra_field(
            path_params=path_params,
        )
    except egoi_api.ApiException as e:
        print("Exception when calling FieldsApi->delete_extra_field: %s\n" % e)
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
list_id | ListIdSchema | | 
field_id | FieldIdSchema | | 

# ListIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**QueryId**](../../models/QueryId.md) |  | 


# FieldIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**QueryId**](../../models/QueryId.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_extra_field.ApiResponseFor204) | No Content
401 | [ApiResponseFor401](#delete_extra_field.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#delete_extra_field.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_extra_field.ApiResponseFor404) | Not Found
408 | [ApiResponseFor408](#delete_extra_field.ApiResponseFor408) | Request Timeout
409 | [ApiResponseFor409](#delete_extra_field.ApiResponseFor409) | Conflict
429 | [ApiResponseFor429](#delete_extra_field.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#delete_extra_field.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#delete_extra_field.ApiResponseFor503) | Service Unavailable

#### delete_extra_field.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_extra_field.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### delete_extra_field.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### delete_extra_field.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### delete_extra_field.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### delete_extra_field.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeleteFieldsConflict**](../../models/DeleteFieldsConflict.md) |  | 


#### delete_extra_field.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### delete_extra_field.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### delete_extra_field.ApiResponseFor503
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

# **delete_field_option**
<a name="delete_field_option"></a>
> delete_field_option(list_idfield_idoption_id)

Deletes an option

Deletes an option of a list of values field

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import fields_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.internal_server_error import InternalServerError
from egoi_api.model.not_found import NotFound
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
    api_instance = fields_api.FieldsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'list_id': QueryId(1),
        'field_id': QueryId(1),
        'option_id': QueryId(1),
    }
    try:
        # Deletes an option
        api_response = api_instance.delete_field_option(
            path_params=path_params,
        )
    except egoi_api.ApiException as e:
        print("Exception when calling FieldsApi->delete_field_option: %s\n" % e)
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
list_id | ListIdSchema | | 
field_id | FieldIdSchema | | 
option_id | OptionIdSchema | | 

# ListIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**QueryId**](../../models/QueryId.md) |  | 


# FieldIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**QueryId**](../../models/QueryId.md) |  | 


# OptionIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**QueryId**](../../models/QueryId.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_field_option.ApiResponseFor204) | No Content
401 | [ApiResponseFor401](#delete_field_option.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#delete_field_option.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_field_option.ApiResponseFor404) | Not Found
408 | [ApiResponseFor408](#delete_field_option.ApiResponseFor408) | Request Timeout
429 | [ApiResponseFor429](#delete_field_option.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#delete_field_option.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#delete_field_option.ApiResponseFor503) | Service Unavailable

#### delete_field_option.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_field_option.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### delete_field_option.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### delete_field_option.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### delete_field_option.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### delete_field_option.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### delete_field_option.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### delete_field_option.ApiResponseFor503
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

# **get_all_field_options**
<a name="get_all_field_options"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_all_field_options(list_idfield_id)

Get all field options

Returns all options of a given field

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import fields_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.field_option import FieldOption
from egoi_api.model.internal_server_error import InternalServerError
from egoi_api.model.not_found import NotFound
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
    api_instance = fields_api.FieldsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'list_id': QueryId(1),
        'field_id': QueryId(1),
    }
    try:
        # Get all field options
        api_response = api_instance.get_all_field_options(
            path_params=path_params,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling FieldsApi->get_all_field_options: %s\n" % e)
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
list_id | ListIdSchema | | 
field_id | FieldIdSchema | | 

# ListIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**QueryId**](../../models/QueryId.md) |  | 


# FieldIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**QueryId**](../../models/QueryId.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_all_field_options.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#get_all_field_options.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_all_field_options.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_all_field_options.ApiResponseFor404) | Not Found
408 | [ApiResponseFor408](#get_all_field_options.ApiResponseFor408) | Request Timeout
429 | [ApiResponseFor429](#get_all_field_options.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#get_all_field_options.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#get_all_field_options.ApiResponseFor503) | Service Unavailable

#### get_all_field_options.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

Collection of field options

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Collection of field options | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[items](#items)** | list, tuple,  | tuple,  | Returned field options | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# items

Returned field options

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Returned field options | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FieldOption**]({{complexTypePrefix}}FieldOption.md) | [**FieldOption**]({{complexTypePrefix}}FieldOption.md) | [**FieldOption**]({{complexTypePrefix}}FieldOption.md) |  | 

#### get_all_field_options.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### get_all_field_options.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### get_all_field_options.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### get_all_field_options.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### get_all_field_options.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### get_all_field_options.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### get_all_field_options.ApiResponseFor503
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

# **get_all_fields**
<a name="get_all_fields"></a>
> [ComplexField] get_all_fields(list_id)

Get all fields

Returns all fields

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import fields_api
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.complex_field import ComplexField
from egoi_api.model.unprocessable_entity import UnprocessableEntity
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
    api_instance = fields_api.FieldsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'list_id': QueryId(1),
    }
    query_params = {
    }
    try:
        # Get all fields
        api_response = api_instance.get_all_fields(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling FieldsApi->get_all_fields: %s\n" % e)

    # example passing only optional values
    path_params = {
        'list_id': QueryId(1),
    }
    query_params = {
        'offset': 0,
        'limit': 10,
    }
    try:
        # Get all fields
        api_response = api_instance.get_all_fields(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling FieldsApi->get_all_fields: %s\n" % e)
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
offset | OffsetSchema | | optional
limit | LimitSchema | | optional


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
200 | [ApiResponseFor200](#get_all_fields.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#get_all_fields.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_all_fields.ApiResponseFor403) | Forbidden
422 | [ApiResponseFor422](#get_all_fields.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#get_all_fields.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#get_all_fields.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#get_all_fields.ApiResponseFor503) | Service Unavailable

#### get_all_fields.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ComplexField**]({{complexTypePrefix}}ComplexField.md) | [**ComplexField**]({{complexTypePrefix}}ComplexField.md) | [**ComplexField**]({{complexTypePrefix}}ComplexField.md) |  | 

#### get_all_fields.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### get_all_fields.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### get_all_fields.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### get_all_fields.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### get_all_fields.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### get_all_fields.ApiResponseFor503
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

# **patch_base_field**
<a name="patch_base_field"></a>
> Field patch_base_field(list_idfield_idpatch_request_base_field)

Update base field

Updates a base field

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import fields_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.field import Field
from egoi_api.model.bad_request import BadRequest
from egoi_api.model.unprocessable_entity import UnprocessableEntity
from egoi_api.model.internal_server_error import InternalServerError
from egoi_api.model.not_found import NotFound
from egoi_api.model.patch_request_base_field import PatchRequestBaseField
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
    api_instance = fields_api.FieldsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'list_id': QueryId(1),
        'field_id': "field_id_example",
    }
    body = PatchRequestBaseField(
        unique=True,
    )
    try:
        # Update base field
        api_response = api_instance.patch_base_field(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling FieldsApi->patch_base_field: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PatchRequestBaseField**](../../models/PatchRequestBaseField.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
list_id | ListIdSchema | | 
field_id | FieldIdSchema | | 

# ListIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**QueryId**](../../models/QueryId.md) |  | 


# FieldIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#patch_base_field.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#patch_base_field.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#patch_base_field.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#patch_base_field.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#patch_base_field.ApiResponseFor404) | Not Found
408 | [ApiResponseFor408](#patch_base_field.ApiResponseFor408) | Request Timeout
422 | [ApiResponseFor422](#patch_base_field.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#patch_base_field.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#patch_base_field.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#patch_base_field.ApiResponseFor503) | Service Unavailable

#### patch_base_field.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Field**](../../models/Field.md) |  | 


#### patch_base_field.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### patch_base_field.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### patch_base_field.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### patch_base_field.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### patch_base_field.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### patch_base_field.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### patch_base_field.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### patch_base_field.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### patch_base_field.ApiResponseFor503
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

# **patch_extra_field**
<a name="patch_extra_field"></a>
> Field patch_extra_field(list_idfield_idpatch_request_field)

Update extra field

Updates an extra field

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import fields_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.field import Field
from egoi_api.model.patch_request_field import PatchRequestField
from egoi_api.model.bad_request import BadRequest
from egoi_api.model.unprocessable_entity import UnprocessableEntity
from egoi_api.model.internal_server_error import InternalServerError
from egoi_api.model.not_found import NotFound
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
    api_instance = fields_api.FieldsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'list_id': QueryId(1),
        'field_id': QueryId(1),
    }
    body = PatchRequestField(
        name="Field name",
        unique=True,
    )
    try:
        # Update extra field
        api_response = api_instance.patch_extra_field(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling FieldsApi->patch_extra_field: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PatchRequestField**](../../models/PatchRequestField.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
list_id | ListIdSchema | | 
field_id | FieldIdSchema | | 

# ListIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**QueryId**](../../models/QueryId.md) |  | 


# FieldIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**QueryId**](../../models/QueryId.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#patch_extra_field.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#patch_extra_field.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#patch_extra_field.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#patch_extra_field.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#patch_extra_field.ApiResponseFor404) | Not Found
408 | [ApiResponseFor408](#patch_extra_field.ApiResponseFor408) | Request Timeout
422 | [ApiResponseFor422](#patch_extra_field.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#patch_extra_field.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#patch_extra_field.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#patch_extra_field.ApiResponseFor503) | Service Unavailable

#### patch_extra_field.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Field**](../../models/Field.md) |  | 


#### patch_extra_field.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### patch_extra_field.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### patch_extra_field.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### patch_extra_field.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### patch_extra_field.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### patch_extra_field.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### patch_extra_field.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### patch_extra_field.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### patch_extra_field.ApiResponseFor503
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

# **update_field_option**
<a name="update_field_option"></a>
> FieldOption update_field_option(list_idfield_idoption_idfield_option_post)

Update field option

Updates a field option

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import fields_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.field_option import FieldOption
from egoi_api.model.bad_request import BadRequest
from egoi_api.model.unprocessable_entity import UnprocessableEntity
from egoi_api.model.field_option_post import FieldOptionPost
from egoi_api.model.internal_server_error import InternalServerError
from egoi_api.model.not_found import NotFound
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
    api_instance = fields_api.FieldsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'list_id': QueryId(1),
        'field_id': QueryId(1),
        'option_id': QueryId(1),
    }
    body = FieldOptionPost(
        en="English example",
        pt="Portuguese example",
        br="Brazilian portuguese example",
        es="Spanish example",
        de="German example",
        hu="Hungarian example",
        fr="French example",
    )
    try:
        # Update field option
        api_response = api_instance.update_field_option(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling FieldsApi->update_field_option: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FieldOptionPost**](../../models/FieldOptionPost.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
list_id | ListIdSchema | | 
field_id | FieldIdSchema | | 
option_id | OptionIdSchema | | 

# ListIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**QueryId**](../../models/QueryId.md) |  | 


# FieldIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**QueryId**](../../models/QueryId.md) |  | 


# OptionIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**QueryId**](../../models/QueryId.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_field_option.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#update_field_option.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#update_field_option.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#update_field_option.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_field_option.ApiResponseFor404) | Not Found
408 | [ApiResponseFor408](#update_field_option.ApiResponseFor408) | Request Timeout
422 | [ApiResponseFor422](#update_field_option.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#update_field_option.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#update_field_option.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#update_field_option.ApiResponseFor503) | Service Unavailable

#### update_field_option.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FieldOption**](../../models/FieldOption.md) |  | 


#### update_field_option.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### update_field_option.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### update_field_option.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### update_field_option.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### update_field_option.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### update_field_option.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### update_field_option.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### update_field_option.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### update_field_option.ApiResponseFor503
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

