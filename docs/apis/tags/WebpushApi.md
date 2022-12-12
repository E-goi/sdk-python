<a name="__pageTop"></a>
# egoi_api.apis.tags.webpush_api.WebpushApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action_enable_web_push_rss**](#action_enable_web_push_rss) | **post** /campaigns/webpush/rss/{campaign_hash}/actions/enable | Enable a rss webpush campaign
[**action_send_web_push**](#action_send_web_push) | **post** /campaigns/web-push/{campaign_hash}/actions/send | Send webpush message
[**create_web_push_campaign**](#create_web_push_campaign) | **post** /campaigns/web-push | Create new webpush campaign
[**create_web_push_rss_campaign**](#create_web_push_rss_campaign) | **post** /campaigns/webpush/rss | Create new webpush rss campaign
[**create_webpush_site**](#create_webpush_site) | **post** /webpush/sites | Creates a webpush site
[**get_all_web_push_sites**](#get_all_web_push_sites) | **get** /webpush/sites | Get all webpush sites
[**patch_web_push_campaign**](#patch_web_push_campaign) | **patch** /campaigns/web-push/{campaign_hash} | Update a specific webpush campaign

# **action_enable_web_push_rss**
<a name="action_enable_web_push_rss"></a>
> AcceptedResponse action_enable_web_push_rss(campaign_hash)

Enable a rss webpush campaign

Enable rss webpush message

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import webpush_api
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.hash import Hash
from egoi_api.model.bad_request import BadRequest
from egoi_api.model.unprocessable_entity import UnprocessableEntity
from egoi_api.model.internal_server_error import InternalServerError
from egoi_api.model.accepted_response import AcceptedResponse
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
    api_instance = webpush_api.WebpushApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'campaign_hash': Hash("zBAMDTMv2D2ylmgd10Z3UB"),
    }
    try:
        # Enable a rss webpush campaign
        api_response = api_instance.action_enable_web_push_rss(
            path_params=path_params,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling WebpushApi->action_enable_web_push_rss: %s\n" % e)
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
campaign_hash | CampaignHashSchema | | 

# CampaignHashSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Hash**](../../models/Hash.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#action_enable_web_push_rss.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#action_enable_web_push_rss.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#action_enable_web_push_rss.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#action_enable_web_push_rss.ApiResponseFor403) | Forbidden
422 | [ApiResponseFor422](#action_enable_web_push_rss.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#action_enable_web_push_rss.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#action_enable_web_push_rss.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#action_enable_web_push_rss.ApiResponseFor503) | Service Unavailable

#### action_enable_web_push_rss.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AcceptedResponse**](../../models/AcceptedResponse.md) |  | 


#### action_enable_web_push_rss.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### action_enable_web_push_rss.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### action_enable_web_push_rss.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### action_enable_web_push_rss.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### action_enable_web_push_rss.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### action_enable_web_push_rss.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### action_enable_web_push_rss.ApiResponseFor503
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

# **action_send_web_push**
<a name="action_send_web_push"></a>
> AcceptedResponse action_send_web_push(campaign_hashcampaign_web_push_send_request)

Send webpush message

Deploys and sends a webpush message

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import webpush_api
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.hash import Hash
from egoi_api.model.bad_request import BadRequest
from egoi_api.model.unprocessable_entity import UnprocessableEntity
from egoi_api.model.internal_server_error import InternalServerError
from egoi_api.model.accepted_response import AcceptedResponse
from egoi_api.model.campaign_web_push_send_request import CampaignWebPushSendRequest
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
    api_instance = webpush_api.WebpushApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'campaign_hash': Hash("zBAMDTMv2D2ylmgd10Z3UB"),
    }
    body = CampaignWebPushSendRequest()
    try:
        # Send webpush message
        api_response = api_instance.action_send_web_push(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling WebpushApi->action_send_web_push: %s\n" % e)
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
[**CampaignWebPushSendRequest**](../../models/CampaignWebPushSendRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
campaign_hash | CampaignHashSchema | | 

# CampaignHashSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Hash**](../../models/Hash.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#action_send_web_push.ApiResponseFor202) | OK
400 | [ApiResponseFor400](#action_send_web_push.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#action_send_web_push.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#action_send_web_push.ApiResponseFor403) | Forbidden
422 | [ApiResponseFor422](#action_send_web_push.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#action_send_web_push.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#action_send_web_push.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#action_send_web_push.ApiResponseFor503) | Service Unavailable

#### action_send_web_push.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AcceptedResponse**](../../models/AcceptedResponse.md) |  | 


#### action_send_web_push.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### action_send_web_push.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### action_send_web_push.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### action_send_web_push.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### action_send_web_push.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### action_send_web_push.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### action_send_web_push.ApiResponseFor503
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

# **create_web_push_campaign**
<a name="create_web_push_campaign"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_web_push_campaign(web_push_campaign)

Create new webpush campaign

Create a new webpush campaign

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import webpush_api
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.hash import Hash
from egoi_api.model.conflict import Conflict
from egoi_api.model.web_push_campaign import WebPushCampaign
from egoi_api.model.bad_request import BadRequest
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
    api_instance = webpush_api.WebpushApi(api_client)

    # example passing only required values which don't have defaults set
    body = WebPushCampaign(
        site_id=QueryId(1),
        internal_name="internal_name_example",
        content=MessageWebPushPost(),
        actions=WebpushActions([
            dict(
                title="title_example",
                link="link_example",
            )
        ]),
    )
    try:
        # Create new webpush campaign
        api_response = api_instance.create_web_push_campaign(
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling WebpushApi->create_web_push_campaign: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WebPushCampaign**](../../models/WebPushCampaign.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_web_push_campaign.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_web_push_campaign.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#create_web_push_campaign.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#create_web_push_campaign.ApiResponseFor403) | Forbidden
409 | [ApiResponseFor409](#create_web_push_campaign.ApiResponseFor409) | Conflict
422 | [ApiResponseFor422](#create_web_push_campaign.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#create_web_push_campaign.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#create_web_push_campaign.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#create_web_push_campaign.ApiResponseFor503) | Service Unavailable

#### create_web_push_campaign.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**campaign_hash** | [**Hash**]({{complexTypePrefix}}Hash.md) | [**Hash**]({{complexTypePrefix}}Hash.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### create_web_push_campaign.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### create_web_push_campaign.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### create_web_push_campaign.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### create_web_push_campaign.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Conflict**](../../models/Conflict.md) |  | 


#### create_web_push_campaign.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### create_web_push_campaign.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### create_web_push_campaign.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### create_web_push_campaign.ApiResponseFor503
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

# **create_web_push_rss_campaign**
<a name="create_web_push_rss_campaign"></a>
> HashcodeCampaign create_web_push_rss_campaign(web_push_rss_campaign)

Create new webpush rss campaign

Create a new webpush rss campaign

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import webpush_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.conflict import Conflict
from egoi_api.model.hashcode_campaign import HashcodeCampaign
from egoi_api.model.bad_request import BadRequest
from egoi_api.model.unprocessable_entity import UnprocessableEntity
from egoi_api.model.internal_server_error import InternalServerError
from egoi_api.model.not_found import NotFound
from egoi_api.model.web_push_rss_campaign import WebPushRssCampaign
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
    api_instance = webpush_api.WebpushApi(api_client)

    # example passing only required values which don't have defaults set
    body = WebPushRssCampaign(
        site_id=QueryId(1),
        internal_name="internal_name_example",
        content=MessageWebPushRss(
            feed="https://localhost/feed",
        ),
    )
    try:
        # Create new webpush rss campaign
        api_response = api_instance.create_web_push_rss_campaign(
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling WebpushApi->create_web_push_rss_campaign: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WebPushRssCampaign**](../../models/WebPushRssCampaign.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_web_push_rss_campaign.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_web_push_rss_campaign.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#create_web_push_rss_campaign.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#create_web_push_rss_campaign.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_web_push_rss_campaign.ApiResponseFor404) | Not Found
408 | [ApiResponseFor408](#create_web_push_rss_campaign.ApiResponseFor408) | Request Timeout
409 | [ApiResponseFor409](#create_web_push_rss_campaign.ApiResponseFor409) | Conflict
422 | [ApiResponseFor422](#create_web_push_rss_campaign.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#create_web_push_rss_campaign.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#create_web_push_rss_campaign.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#create_web_push_rss_campaign.ApiResponseFor503) | Service Unavailable

#### create_web_push_rss_campaign.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HashcodeCampaign**](../../models/HashcodeCampaign.md) |  | 


#### create_web_push_rss_campaign.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### create_web_push_rss_campaign.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### create_web_push_rss_campaign.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### create_web_push_rss_campaign.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### create_web_push_rss_campaign.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### create_web_push_rss_campaign.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Conflict**](../../models/Conflict.md) |  | 


#### create_web_push_rss_campaign.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### create_web_push_rss_campaign.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### create_web_push_rss_campaign.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### create_web_push_rss_campaign.ApiResponseFor503
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

# **create_webpush_site**
<a name="create_webpush_site"></a>
> WebPushSite create_webpush_site(web_push_site)

Creates a webpush site

Create a new webpush site

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import webpush_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.web_push_site import WebPushSite
from egoi_api.model.post_webpush_site_conflict import PostWebpushSiteConflict
from egoi_api.model.bad_request import BadRequest
from egoi_api.model.unprocessable_entity import UnprocessableEntity
from egoi_api.model.internal_server_error import InternalServerError
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
    api_instance = webpush_api.WebpushApi(api_client)

    # example passing only required values which don't have defaults set
    body = WebPushSite(
        site_id=Id(1),
        site="site_example",
        list_id=QueryId(1),
        app_code="7b89dfsb9a6ab6fbsfbasbd6f6",
        name="name_example",
    )
    try:
        # Creates a webpush site
        api_response = api_instance.create_webpush_site(
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling WebpushApi->create_webpush_site: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WebPushSite**](../../models/WebPushSite.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_webpush_site.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_webpush_site.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#create_webpush_site.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#create_webpush_site.ApiResponseFor403) | Forbidden
408 | [ApiResponseFor408](#create_webpush_site.ApiResponseFor408) | Request Timeout
409 | [ApiResponseFor409](#create_webpush_site.ApiResponseFor409) | Conflict
422 | [ApiResponseFor422](#create_webpush_site.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#create_webpush_site.ApiResponseFor500) | Internal Server Error

#### create_webpush_site.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WebPushSite**](../../models/WebPushSite.md) |  | 


#### create_webpush_site.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### create_webpush_site.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### create_webpush_site.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### create_webpush_site.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### create_webpush_site.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PostWebpushSiteConflict**](../../models/PostWebpushSiteConflict.md) |  | 


#### create_webpush_site.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### create_webpush_site.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


### Authorization

[Apikey](../../../README.md#Apikey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_all_web_push_sites**
<a name="get_all_web_push_sites"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_all_web_push_sites()

Get all webpush sites

Returns all wepush's sites

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import webpush_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.id import Id
from egoi_api.model.web_push_site import WebPushSite
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
    api_instance = webpush_api.WebpushApi(api_client)

    # example passing only optional values
    query_params = {
        'offset': 0,
        'limit': 10,
        'order': "desc",
        'order_by': "list_id",
        'list_id': Id(1),
    }
    try:
        # Get all webpush sites
        api_response = api_instance.get_all_web_push_sites(
            query_params=query_params,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling WebpushApi->get_all_web_push_sites: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
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
order | OrderSchema | | optional
order_by | OrderBySchema | | optional
list_id | ListIdSchema | | optional


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

# OrderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["asc", "desc", ] if omitted the server will use the default value of "desc"

# OrderBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["list_id", "created", "updated", ] if omitted the server will use the default value of "list_id"

# ListIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Id**](../../models/Id.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_all_web_push_sites.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#get_all_web_push_sites.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_all_web_push_sites.ApiResponseFor403) | Forbidden
408 | [ApiResponseFor408](#get_all_web_push_sites.ApiResponseFor408) | Request Timeout
422 | [ApiResponseFor422](#get_all_web_push_sites.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#get_all_web_push_sites.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#get_all_web_push_sites.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#get_all_web_push_sites.ApiResponseFor503) | Service Unavailable

#### get_all_web_push_sites.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

Collection of sites

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Collection of sites | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total_items** | decimal.Decimal, int,  | decimal.Decimal,  | Returned sites | [optional] 
**[items](#items)** | list, tuple,  | tuple,  | Returned sites | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# items

Returned sites

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Returned sites | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WebPushSite**]({{complexTypePrefix}}WebPushSite.md) | [**WebPushSite**]({{complexTypePrefix}}WebPushSite.md) | [**WebPushSite**]({{complexTypePrefix}}WebPushSite.md) |  | 

#### get_all_web_push_sites.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### get_all_web_push_sites.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### get_all_web_push_sites.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### get_all_web_push_sites.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### get_all_web_push_sites.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### get_all_web_push_sites.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### get_all_web_push_sites.ApiResponseFor503
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

# **patch_web_push_campaign**
<a name="patch_web_push_campaign"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} patch_web_push_campaign(campaign_hashweb_push_patch_campaign)

Update a specific webpush campaign

Update a webpush campaign

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import webpush_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.hash import Hash
from egoi_api.model.bad_request import BadRequest
from egoi_api.model.unprocessable_entity import UnprocessableEntity
from egoi_api.model.web_push_patch_campaign import WebPushPatchCampaign
from egoi_api.model.internal_server_error import InternalServerError
from egoi_api.model.not_found import NotFound
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
    api_instance = webpush_api.WebpushApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'campaign_hash': Hash("zBAMDTMv2D2ylmgd10Z3UB"),
    }
    body = WebPushPatchCampaign(
        internal_name="internal_name_example",
        content=MessageWebPush(
            title="title_example",
            message="Campaign message",
            link="link_example",
            icon="icon_example",
        ),
        actions=WebpushActions([
            dict(
                title="title_example",
                link="link_example",
            )
        ]),
    )
    try:
        # Update a specific webpush campaign
        api_response = api_instance.patch_web_push_campaign(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling WebpushApi->patch_web_push_campaign: %s\n" % e)
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
[**WebPushPatchCampaign**](../../models/WebPushPatchCampaign.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
campaign_hash | CampaignHashSchema | | 

# CampaignHashSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Hash**](../../models/Hash.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#patch_web_push_campaign.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#patch_web_push_campaign.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#patch_web_push_campaign.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#patch_web_push_campaign.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#patch_web_push_campaign.ApiResponseFor404) | Not Found
408 | [ApiResponseFor408](#patch_web_push_campaign.ApiResponseFor408) | Request Timeout
422 | [ApiResponseFor422](#patch_web_push_campaign.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#patch_web_push_campaign.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#patch_web_push_campaign.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#patch_web_push_campaign.ApiResponseFor503) | Service Unavailable

#### patch_web_push_campaign.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**campaign_hash** | [**Hash**]({{complexTypePrefix}}Hash.md) | [**Hash**]({{complexTypePrefix}}Hash.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### patch_web_push_campaign.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### patch_web_push_campaign.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### patch_web_push_campaign.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### patch_web_push_campaign.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### patch_web_push_campaign.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### patch_web_push_campaign.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### patch_web_push_campaign.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### patch_web_push_campaign.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### patch_web_push_campaign.ApiResponseFor503
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

