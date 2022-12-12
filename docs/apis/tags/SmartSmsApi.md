<a name="__pageTop"></a>
# egoi_api.apis.tags.smart_sms_api.SmartSmsApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action_send_smart_sms**](#action_send_smart_sms) | **post** /campaigns/smart-sms/{campaign_hash}/actions/send | Send smart sms message
[**create_smart_sms_campaign**](#create_smart_sms_campaign) | **post** /campaigns/smart-sms | Create new smart sms campaign
[**patch_smart_sms_campaign**](#patch_smart_sms_campaign) | **patch** /campaigns/smart-sms/{campaign_hash} | Update a specific smart sms campaign

# **action_send_smart_sms**
<a name="action_send_smart_sms"></a>
> AcceptedResponse action_send_smart_sms(campaign_hashcampaign_sms_send_request)

Send smart sms message

Deploys and sends a smart sms message

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import smart_sms_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.campaign_sms_send_request import CampaignSmsSendRequest
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
    api_instance = smart_sms_api.SmartSmsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'campaign_hash': Hash("zBAMDTMv2D2ylmgd10Z3UB"),
    }
    body = CampaignSmsSendRequest()
    try:
        # Send smart sms message
        api_response = api_instance.action_send_smart_sms(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling SmartSmsApi->action_send_smart_sms: %s\n" % e)
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
[**CampaignSmsSendRequest**](../../models/CampaignSmsSendRequest.md) |  | 


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
202 | [ApiResponseFor202](#action_send_smart_sms.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#action_send_smart_sms.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#action_send_smart_sms.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#action_send_smart_sms.ApiResponseFor403) | Forbidden
408 | [ApiResponseFor408](#action_send_smart_sms.ApiResponseFor408) | Request Timeout
422 | [ApiResponseFor422](#action_send_smart_sms.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#action_send_smart_sms.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#action_send_smart_sms.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#action_send_smart_sms.ApiResponseFor503) | Service Unavailable

#### action_send_smart_sms.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AcceptedResponse**](../../models/AcceptedResponse.md) |  | 


#### action_send_smart_sms.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### action_send_smart_sms.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### action_send_smart_sms.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### action_send_smart_sms.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### action_send_smart_sms.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### action_send_smart_sms.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### action_send_smart_sms.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### action_send_smart_sms.ApiResponseFor503
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

# **create_smart_sms_campaign**
<a name="create_smart_sms_campaign"></a>
> HashcodeCampaign create_smart_sms_campaign(smart_sms_campaign)

Create new smart sms campaign

Creates a new smart sms campaign.                         **DISCLAIMER:** A URL will be added at the end of your SMS

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import smart_sms_api
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.smart_sms_campaign import SmartSmsCampaign
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.hashcode_campaign import HashcodeCampaign
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
    api_instance = smart_sms_api.SmartSmsApi(api_client)

    # example passing only required values which don't have defaults set
    body = SmartSmsCampaign(
        list_id=QueryId(1),
        internal_name="Internal Name",
        campaign_content=dict(
            message="message_example",
        ),
        page_content=CampaignSmartSmsPageContent(
            type="CampaignSmartSmsHtml",
            page_html="page_html_example",
            page_internal_name="page_internal_name_example",
        ),
        sender_id=QueryId(1),
        cname_id=QueryId(1),
        options=CampaignSmartSmsOptions(
            encoding="gsm",
            max_messages=5,
        ),
    )
    try:
        # Create new smart sms campaign
        api_response = api_instance.create_smart_sms_campaign(
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling SmartSmsApi->create_smart_sms_campaign: %s\n" % e)
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
[**SmartSmsCampaign**](../../models/SmartSmsCampaign.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_smart_sms_campaign.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_smart_sms_campaign.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#create_smart_sms_campaign.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#create_smart_sms_campaign.ApiResponseFor403) | Forbidden
422 | [ApiResponseFor422](#create_smart_sms_campaign.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#create_smart_sms_campaign.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#create_smart_sms_campaign.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#create_smart_sms_campaign.ApiResponseFor503) | Service Unavailable

#### create_smart_sms_campaign.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HashcodeCampaign**](../../models/HashcodeCampaign.md) |  | 


#### create_smart_sms_campaign.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### create_smart_sms_campaign.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### create_smart_sms_campaign.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### create_smart_sms_campaign.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### create_smart_sms_campaign.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### create_smart_sms_campaign.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### create_smart_sms_campaign.ApiResponseFor503
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

# **patch_smart_sms_campaign**
<a name="patch_smart_sms_campaign"></a>
> HashcodeCampaign patch_smart_sms_campaign(campaign_hashsmart_sms_campaign_patch_request)

Update a specific smart sms campaign

Update smart sms campaign

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import smart_sms_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.hash import Hash
from egoi_api.model.hashcode_campaign import HashcodeCampaign
from egoi_api.model.bad_request import BadRequest
from egoi_api.model.smart_sms_campaign_patch_request import SmartSmsCampaignPatchRequest
from egoi_api.model.unprocessable_entity import UnprocessableEntity
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
    api_instance = smart_sms_api.SmartSmsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'campaign_hash': Hash("zBAMDTMv2D2ylmgd10Z3UB"),
    }
    body = SmartSmsCampaignPatchRequest(
        internal_name="Internal Title",
        campaign_content=dict(
            message="message_example",
        ),
        page_content=dict(
            page_url="page_url_example",
            page_html="page_html_example",
            page_internal_name="page_internal_name_example",
        ),
        sender_id=QueryId(1),
        cname_id=QueryId(1),
        options=CampaignSmsOptions(
            encoding="gsm",
            max_messages=5,
        ),
    )
    try:
        # Update a specific smart sms campaign
        api_response = api_instance.patch_smart_sms_campaign(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling SmartSmsApi->patch_smart_sms_campaign: %s\n" % e)
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
[**SmartSmsCampaignPatchRequest**](../../models/SmartSmsCampaignPatchRequest.md) |  | 


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
200 | [ApiResponseFor200](#patch_smart_sms_campaign.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#patch_smart_sms_campaign.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#patch_smart_sms_campaign.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#patch_smart_sms_campaign.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#patch_smart_sms_campaign.ApiResponseFor404) | Not Found
408 | [ApiResponseFor408](#patch_smart_sms_campaign.ApiResponseFor408) | Request Timeout
422 | [ApiResponseFor422](#patch_smart_sms_campaign.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#patch_smart_sms_campaign.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#patch_smart_sms_campaign.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#patch_smart_sms_campaign.ApiResponseFor503) | Service Unavailable

#### patch_smart_sms_campaign.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HashcodeCampaign**](../../models/HashcodeCampaign.md) |  | 


#### patch_smart_sms_campaign.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### patch_smart_sms_campaign.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### patch_smart_sms_campaign.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### patch_smart_sms_campaign.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFound**](../../models/NotFound.md) |  | 


#### patch_smart_sms_campaign.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### patch_smart_sms_campaign.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### patch_smart_sms_campaign.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### patch_smart_sms_campaign.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### patch_smart_sms_campaign.ApiResponseFor503
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

