<a name="__pageTop"></a>
# egoi_api.apis.tags.advanced_reports_api.AdvancedReportsApi

All URIs are relative to *https://api.egoiapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_email_bounces_report**](#generate_email_bounces_report) | **post** /reports/advanced/email-bounces | Generate email bounces report
[**generate_email_clicks_by_contact_report**](#generate_email_clicks_by_contact_report) | **post** /reports/advanced/email-clicks-by-contact | Generate email clicks by contact report
[**generate_email_clicks_by_url_report**](#generate_email_clicks_by_url_report) | **post** /reports/advanced/email-clicks-by-url | Generate email clicks by URL report
[**generate_email_events_report**](#generate_email_events_report) | **post** /reports/advanced/email-events | Generate email events report
[**generate_email_sms_report**](#generate_email_sms_report) | **post** /reports/advanced/sms-bounces | Generate SMS bounces report
[**generate_email_unsubscriptions_report**](#generate_email_unsubscriptions_report) | **post** /reports/advanced/email-unsubscriptions | Generate email unsubscriptions report
[**generate_form_answers_report**](#generate_form_answers_report) | **post** /reports/advanced/form-answers | Generate form answers report
[**generate_sends_report**](#generate_sends_report) | **post** /reports/advanced/sends | Generate sends report
[**generate_sms_events_report**](#generate_sms_events_report) | **post** /reports/advanced/sms-events | Generate SMS events report
[**generate_subscriptions_report**](#generate_subscriptions_report) | **post** /reports/advanced/subscriptions | Generate subscriptions report
[**generate_unsubscriptions_report**](#generate_unsubscriptions_report) | **post** /reports/advanced/unsubscriptions | Generate unsubscriptions report
[**get_all_advanced_reports**](#get_all_advanced_reports) | **get** /reports/advanced | Get all advanced reports

# **generate_email_bounces_report**
<a name="generate_email_bounces_report"></a>
> AcceptedResponse generate_email_bounces_report(generate_email_bounces_report)

Generate email bounces report

Generates a new email bounces report

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import advanced_reports_api
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.bad_request import BadRequest
from egoi_api.model.unprocessable_entity import UnprocessableEntity
from egoi_api.model.generate_email_bounces_report import GenerateEmailBouncesReport
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
    api_instance = advanced_reports_api.AdvancedReportsApi(api_client)

    # example passing only required values which don't have defaults set
    body = GenerateEmailBouncesReport(
        title="Report title",
        range=AdvancedReportRange(
            start=None,
,
        ),
        campaigns=AdvancedReportCampaigns([
            AdvancedReportCampaignsObject(
                list_id=QueryId(1),
                type="ReportCampaignsAll",
            )
        ]),
        columns=AdvancedReportEmailBouncesColumns(
            list_base_fields=[
                "list_base_fields_example"
            ],
            list_extra_fields=AdvancedReportListExtraFields([
                dict(
                    list_id=QueryId(1),
                    fields=[
                        "fields_example"
                    ],
                )
            ]),
            list_stats_fields=EmailBouncesListStatsFields(
                bounce_date=True,
                bounce_type=True,
                bounce_detail=True,
            ),
            campaign_fields=EmailBouncesCampaignFields(
                internal_name=True,
                campaign_hash=True,
            ),
        ),
        options=AdvancedReportEmailBouncesOptions(
            include_unopens=True,
            notify=[
                QueryId(1)
            ],
            grouping="by_campaign",
        ),
        callback_url="callback_url_example",
    )
    try:
        # Generate email bounces report
        api_response = api_instance.generate_email_bounces_report(
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling AdvancedReportsApi->generate_email_bounces_report: %s\n" % e)
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
[**GenerateEmailBouncesReport**](../../models/GenerateEmailBouncesReport.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#generate_email_bounces_report.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#generate_email_bounces_report.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#generate_email_bounces_report.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#generate_email_bounces_report.ApiResponseFor403) | Forbidden
422 | [ApiResponseFor422](#generate_email_bounces_report.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#generate_email_bounces_report.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#generate_email_bounces_report.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#generate_email_bounces_report.ApiResponseFor503) | Service Unavailable

#### generate_email_bounces_report.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AcceptedResponse**](../../models/AcceptedResponse.md) |  | 


#### generate_email_bounces_report.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### generate_email_bounces_report.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### generate_email_bounces_report.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### generate_email_bounces_report.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### generate_email_bounces_report.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### generate_email_bounces_report.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### generate_email_bounces_report.ApiResponseFor503
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

# **generate_email_clicks_by_contact_report**
<a name="generate_email_clicks_by_contact_report"></a>
> AcceptedResponse generate_email_clicks_by_contact_report(generate_email_clicks_by_contact_report)

Generate email clicks by contact report

Generates a new email clicks by contact report

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import advanced_reports_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.generate_email_clicks_by_contact_report import GenerateEmailClicksByContactReport
from egoi_api.model.service_unavailable import ServiceUnavailable
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
    api_instance = advanced_reports_api.AdvancedReportsApi(api_client)

    # example passing only required values which don't have defaults set
    body = GenerateEmailClicksByContactReport(
        title="Report title",
        range=AdvancedReportRange(
            start=None,
,
        ),
        campaigns=AdvancedReportCampaigns([
            AdvancedReportCampaignsObject(
                list_id=QueryId(1),
                type="ReportCampaignsAll",
            )
        ]),
        columns=AdvancedReportEmailClicksByContactColumns(
            list_base_fields=[
                "list_base_fields_example"
            ],
            list_extra_fields=AdvancedReportListExtraFields([
                dict(
                    list_id=QueryId(1),
                    fields=[
                        "fields_example"
                    ],
                )
            ]),
            list_stats_fields=EmailClicksByContactListStatsFields(
                clicks=True,
            ),
            campaign_fields=EmailClicksByContactCampaignFields(
                internal_name=True,
                campaign_hash=True,
                url=True,
                city=True,
                country=True,
                region=True,
                program=True,
                os=True,
            ),
        ),
        options=AdvancedReportEmailClicksByContactOptions(
            notify=[
                QueryId(1)
            ],
        ),
        callback_url="callback_url_example",
    )
    try:
        # Generate email clicks by contact report
        api_response = api_instance.generate_email_clicks_by_contact_report(
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling AdvancedReportsApi->generate_email_clicks_by_contact_report: %s\n" % e)
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
[**GenerateEmailClicksByContactReport**](../../models/GenerateEmailClicksByContactReport.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#generate_email_clicks_by_contact_report.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#generate_email_clicks_by_contact_report.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#generate_email_clicks_by_contact_report.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#generate_email_clicks_by_contact_report.ApiResponseFor403) | Forbidden
408 | [ApiResponseFor408](#generate_email_clicks_by_contact_report.ApiResponseFor408) | Request Timeout
422 | [ApiResponseFor422](#generate_email_clicks_by_contact_report.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#generate_email_clicks_by_contact_report.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#generate_email_clicks_by_contact_report.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#generate_email_clicks_by_contact_report.ApiResponseFor503) | Service Unavailable

#### generate_email_clicks_by_contact_report.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AcceptedResponse**](../../models/AcceptedResponse.md) |  | 


#### generate_email_clicks_by_contact_report.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### generate_email_clicks_by_contact_report.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### generate_email_clicks_by_contact_report.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### generate_email_clicks_by_contact_report.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### generate_email_clicks_by_contact_report.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### generate_email_clicks_by_contact_report.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### generate_email_clicks_by_contact_report.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### generate_email_clicks_by_contact_report.ApiResponseFor503
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

# **generate_email_clicks_by_url_report**
<a name="generate_email_clicks_by_url_report"></a>
> AcceptedResponse generate_email_clicks_by_url_report(generate_email_clicks_by_url_report)

Generate email clicks by URL report

Generates a new email clicks by URL report

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import advanced_reports_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.generate_email_clicks_by_url_report import GenerateEmailClicksByUrlReport
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
    api_instance = advanced_reports_api.AdvancedReportsApi(api_client)

    # example passing only required values which don't have defaults set
    body = GenerateEmailClicksByUrlReport(
        title="Report title",
        range=AdvancedReportRange(
            start=None,
,
        ),
        campaigns=AdvancedReportCampaigns([
            AdvancedReportCampaignsObject(
                list_id=QueryId(1),
                type="ReportCampaignsAll",
            )
        ]),
        columns=AdvancedReportEmailClicksByUrlColumns(
            list_base_fields=[
                "list_base_fields_example"
            ],
            list_extra_fields=AdvancedReportListExtraFields([
                dict(
                    list_id=QueryId(1),
                    fields=[
                        "fields_example"
                    ],
                )
            ]),
            list_stats_fields=EmailClicksByUrlListStatsFields(
                clicks=True,
                unique_clicks=True,
                click_rate_per_url=True,
            ),
            campaign_fields=EmailClicksByUrlCampaignFields(
                internal_name=True,
                campaign_hash=True,
                url=True,
                city=True,
                country=True,
                region=True,
                program=True,
                os=True,
            ),
        ),
        options=AdvancedReportEmailClicksByUrlOptions(
            notify=[
                QueryId(1)
            ],
        ),
        callback_url="callback_url_example",
    )
    try:
        # Generate email clicks by URL report
        api_response = api_instance.generate_email_clicks_by_url_report(
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling AdvancedReportsApi->generate_email_clicks_by_url_report: %s\n" % e)
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
[**GenerateEmailClicksByUrlReport**](../../models/GenerateEmailClicksByUrlReport.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#generate_email_clicks_by_url_report.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#generate_email_clicks_by_url_report.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#generate_email_clicks_by_url_report.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#generate_email_clicks_by_url_report.ApiResponseFor403) | Forbidden
408 | [ApiResponseFor408](#generate_email_clicks_by_url_report.ApiResponseFor408) | Request Timeout
422 | [ApiResponseFor422](#generate_email_clicks_by_url_report.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#generate_email_clicks_by_url_report.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#generate_email_clicks_by_url_report.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#generate_email_clicks_by_url_report.ApiResponseFor503) | Service Unavailable

#### generate_email_clicks_by_url_report.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AcceptedResponse**](../../models/AcceptedResponse.md) |  | 


#### generate_email_clicks_by_url_report.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### generate_email_clicks_by_url_report.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### generate_email_clicks_by_url_report.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### generate_email_clicks_by_url_report.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### generate_email_clicks_by_url_report.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### generate_email_clicks_by_url_report.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### generate_email_clicks_by_url_report.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### generate_email_clicks_by_url_report.ApiResponseFor503
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

# **generate_email_events_report**
<a name="generate_email_events_report"></a>
> AcceptedResponse generate_email_events_report(generate_email_events_report)

Generate email events report

Generates a new email events report

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import advanced_reports_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.bad_request import BadRequest
from egoi_api.model.unprocessable_entity import UnprocessableEntity
from egoi_api.model.internal_server_error import InternalServerError
from egoi_api.model.accepted_response import AcceptedResponse
from egoi_api.model.generate_email_events_report import GenerateEmailEventsReport
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
    api_instance = advanced_reports_api.AdvancedReportsApi(api_client)

    # example passing only required values which don't have defaults set
    body = GenerateEmailEventsReport(
        title="Report title",
        range=AdvancedReportRange(
            start=None,
,
        ),
        campaigns=AdvancedReportCampaigns([
            AdvancedReportCampaignsObject(
                list_id=QueryId(1),
                type="ReportCampaignsAll",
            )
        ]),
        columns=AdvancedReportEmailEventsColumns(
            list_base_fields=[
                "list_base_fields_example"
            ],
            list_extra_fields=AdvancedReportListExtraFields([
                dict(
                    list_id=QueryId(1),
                    fields=[
                        "fields_example"
                    ],
                )
            ]),
            list_stats_fields=EmailEventsListStatsFields(
                opens=True,
                clicks=True,
                complaints=True,
                unsubscribes=True,
                bounces=True,
                forwards=True,
                forwards_conversion=True,
                fb_likes=True,
                fb_shares=True,
                tw_shares=True,
                social_shares=True,
            ),
            campaign_fields=EmailEventsCampaignFields(
                internal_name=True,
                campaign_hash=True,
                send_date=True,
                group=True,
                city=True,
                country=True,
                region=True,
                program=True,
                os=True,
            ),
        ),
        options=AdvancedReportEmailEventsOptions(
            include_unopens=True,
            notify=[
                QueryId(1)
            ],
        ),
        callback_url="callback_url_example",
    )
    try:
        # Generate email events report
        api_response = api_instance.generate_email_events_report(
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling AdvancedReportsApi->generate_email_events_report: %s\n" % e)
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
[**GenerateEmailEventsReport**](../../models/GenerateEmailEventsReport.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#generate_email_events_report.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#generate_email_events_report.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#generate_email_events_report.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#generate_email_events_report.ApiResponseFor403) | Forbidden
408 | [ApiResponseFor408](#generate_email_events_report.ApiResponseFor408) | Request Timeout
422 | [ApiResponseFor422](#generate_email_events_report.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#generate_email_events_report.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#generate_email_events_report.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#generate_email_events_report.ApiResponseFor503) | Service Unavailable

#### generate_email_events_report.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AcceptedResponse**](../../models/AcceptedResponse.md) |  | 


#### generate_email_events_report.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### generate_email_events_report.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### generate_email_events_report.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### generate_email_events_report.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### generate_email_events_report.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### generate_email_events_report.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### generate_email_events_report.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### generate_email_events_report.ApiResponseFor503
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

# **generate_email_sms_report**
<a name="generate_email_sms_report"></a>
> AcceptedResponse generate_email_sms_report(generate_sms_bounces_report)

Generate SMS bounces report

Generates a new SMS bounces report

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import advanced_reports_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.generate_sms_bounces_report import GenerateSmsBouncesReport
from egoi_api.model.service_unavailable import ServiceUnavailable
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
    api_instance = advanced_reports_api.AdvancedReportsApi(api_client)

    # example passing only required values which don't have defaults set
    body = GenerateSmsBouncesReport(
        title="Report title",
        range=AdvancedReportRange(
            start=None,
,
        ),
        campaigns=AdvancedReportCampaigns([
            AdvancedReportCampaignsObject(
                list_id=QueryId(1),
                type="ReportCampaignsAll",
            )
        ]),
        columns=AdvancedReportSmsBouncesColumns(
            list_base_fields=[
                "list_base_fields_example"
            ],
            list_extra_fields=AdvancedReportListExtraFields([
                dict(
                    list_id=QueryId(1),
                    fields=[
                        "fields_example"
                    ],
                )
            ]),
            list_stats_fields=SmsBouncesListStatsFields(
                delivery_answer=True,
                delivery_date=True,
            ),
            campaign_fields=SmsBouncesCampaignFields(
                internal_name=True,
                campaign_hash=True,
                send_date=True,
                sender=True,
            ),
        ),
        options=AdvancedReportSmsBouncesOptions(
            notify=[
                QueryId(1)
            ],
            grouping="by_campaign",
        ),
        callback_url="callback_url_example",
    )
    try:
        # Generate SMS bounces report
        api_response = api_instance.generate_email_sms_report(
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling AdvancedReportsApi->generate_email_sms_report: %s\n" % e)
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
[**GenerateSmsBouncesReport**](../../models/GenerateSmsBouncesReport.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#generate_email_sms_report.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#generate_email_sms_report.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#generate_email_sms_report.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#generate_email_sms_report.ApiResponseFor403) | Forbidden
408 | [ApiResponseFor408](#generate_email_sms_report.ApiResponseFor408) | Request Timeout
422 | [ApiResponseFor422](#generate_email_sms_report.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#generate_email_sms_report.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#generate_email_sms_report.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#generate_email_sms_report.ApiResponseFor503) | Service Unavailable

#### generate_email_sms_report.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AcceptedResponse**](../../models/AcceptedResponse.md) |  | 


#### generate_email_sms_report.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### generate_email_sms_report.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### generate_email_sms_report.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### generate_email_sms_report.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### generate_email_sms_report.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### generate_email_sms_report.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### generate_email_sms_report.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### generate_email_sms_report.ApiResponseFor503
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

# **generate_email_unsubscriptions_report**
<a name="generate_email_unsubscriptions_report"></a>
> AcceptedResponse generate_email_unsubscriptions_report(generate_email_unsubscriptions_report)

Generate email unsubscriptions report

Generates a new email unsubscriptions report

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import advanced_reports_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.bad_request import BadRequest
from egoi_api.model.unprocessable_entity import UnprocessableEntity
from egoi_api.model.internal_server_error import InternalServerError
from egoi_api.model.accepted_response import AcceptedResponse
from egoi_api.model.too_many_requests import TooManyRequests
from egoi_api.model.forbidden import Forbidden
from egoi_api.model.generate_email_unsubscriptions_report import GenerateEmailUnsubscriptionsReport
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
    api_instance = advanced_reports_api.AdvancedReportsApi(api_client)

    # example passing only required values which don't have defaults set
    body = GenerateEmailUnsubscriptionsReport(
        title="Report title",
        range=AdvancedReportRange(
            start=None,
,
        ),
        campaigns=AdvancedReportCampaigns([
            AdvancedReportCampaignsObject(
                list_id=QueryId(1),
                type="ReportCampaignsAll",
            )
        ]),
        columns=AdvancedReportEmailUnsubscriptionsColumns(
            list_base_fields=[
                "list_base_fields_example"
            ],
            list_extra_fields=AdvancedReportListExtraFields([
                dict(
                    list_id=QueryId(1),
                    fields=[
                        "fields_example"
                    ],
                )
            ]),
            list_stats_fields=EmailUnsubscriptionsListStatsFields(
                unsubscription_method=True,
                unsubscription_motive=True,
                unsubscription_date=True,
            ),
            campaign_fields=EmailUnsubscriptionsCampaignFields(
                internal_name=True,
                campaign_hash=True,
                sender=True,
            ),
        ),
        options=AdvancedReportEmailUnsubscriptionsOptions(
            notify=[
                QueryId(1)
            ],
        ),
        callback_url="callback_url_example",
    )
    try:
        # Generate email unsubscriptions report
        api_response = api_instance.generate_email_unsubscriptions_report(
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling AdvancedReportsApi->generate_email_unsubscriptions_report: %s\n" % e)
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
[**GenerateEmailUnsubscriptionsReport**](../../models/GenerateEmailUnsubscriptionsReport.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#generate_email_unsubscriptions_report.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#generate_email_unsubscriptions_report.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#generate_email_unsubscriptions_report.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#generate_email_unsubscriptions_report.ApiResponseFor403) | Forbidden
408 | [ApiResponseFor408](#generate_email_unsubscriptions_report.ApiResponseFor408) | Request Timeout
422 | [ApiResponseFor422](#generate_email_unsubscriptions_report.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#generate_email_unsubscriptions_report.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#generate_email_unsubscriptions_report.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#generate_email_unsubscriptions_report.ApiResponseFor503) | Service Unavailable

#### generate_email_unsubscriptions_report.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AcceptedResponse**](../../models/AcceptedResponse.md) |  | 


#### generate_email_unsubscriptions_report.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### generate_email_unsubscriptions_report.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### generate_email_unsubscriptions_report.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### generate_email_unsubscriptions_report.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### generate_email_unsubscriptions_report.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### generate_email_unsubscriptions_report.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### generate_email_unsubscriptions_report.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### generate_email_unsubscriptions_report.ApiResponseFor503
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

# **generate_form_answers_report**
<a name="generate_form_answers_report"></a>
> AcceptedResponse generate_form_answers_report(generate_form_answers_report)

Generate form answers report

Generates a new form answers report

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import advanced_reports_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.bad_request import BadRequest
from egoi_api.model.unprocessable_entity import UnprocessableEntity
from egoi_api.model.internal_server_error import InternalServerError
from egoi_api.model.accepted_response import AcceptedResponse
from egoi_api.model.too_many_requests import TooManyRequests
from egoi_api.model.forbidden import Forbidden
from egoi_api.model.generate_form_answers_report import GenerateFormAnswersReport
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
    api_instance = advanced_reports_api.AdvancedReportsApi(api_client)

    # example passing only required values which don't have defaults set
    body = GenerateFormAnswersReport(
        title="Report title",
        range=AdvancedReportRange(
            start=None,
,
        ),
        forms=AdvancedReportForms([
            dict(
                list_id=QueryId(1),
                forms=[
                    QueryId(1)
                ],
            )
        ]),
        callback_url="callback_url_example",
    )
    try:
        # Generate form answers report
        api_response = api_instance.generate_form_answers_report(
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling AdvancedReportsApi->generate_form_answers_report: %s\n" % e)
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
[**GenerateFormAnswersReport**](../../models/GenerateFormAnswersReport.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#generate_form_answers_report.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#generate_form_answers_report.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#generate_form_answers_report.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#generate_form_answers_report.ApiResponseFor403) | Forbidden
408 | [ApiResponseFor408](#generate_form_answers_report.ApiResponseFor408) | Request Timeout
422 | [ApiResponseFor422](#generate_form_answers_report.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#generate_form_answers_report.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#generate_form_answers_report.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#generate_form_answers_report.ApiResponseFor503) | Service Unavailable

#### generate_form_answers_report.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AcceptedResponse**](../../models/AcceptedResponse.md) |  | 


#### generate_form_answers_report.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### generate_form_answers_report.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### generate_form_answers_report.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### generate_form_answers_report.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### generate_form_answers_report.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### generate_form_answers_report.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### generate_form_answers_report.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### generate_form_answers_report.ApiResponseFor503
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

# **generate_sends_report**
<a name="generate_sends_report"></a>
> AcceptedResponse generate_sends_report(generate_sends_report)

Generate sends report

Generates a new sends report

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import advanced_reports_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.generate_sends_report import GenerateSendsReport
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
    api_instance = advanced_reports_api.AdvancedReportsApi(api_client)

    # example passing only required values which don't have defaults set
    body = GenerateSendsReport(
        title="Report title",
        range=AdvancedReportRange(
            start=None,
,
        ),
        lists=[
            Id(1)
        ],
        columns=AdvancedReportSendsColumns(
            list_base_fields=[
                "list_base_fields_example"
            ],
            list_extra_fields=AdvancedReportListExtraFields([
                dict(
                    list_id=QueryId(1),
                    fields=[
                        "fields_example"
                    ],
                )
            ]),
            campaign_fields=SendsCampaignFields(
                internal_name=True,
                campaign_hash=True,
                group=True,
                channel=True,
                type=True,
                sender=True,
            ),
        ),
        options=AdvancedReportSendsOptions(
            notify=[
                QueryId(1)
            ],
        ),
        callback_url="callback_url_example",
    )
    try:
        # Generate sends report
        api_response = api_instance.generate_sends_report(
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling AdvancedReportsApi->generate_sends_report: %s\n" % e)
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
[**GenerateSendsReport**](../../models/GenerateSendsReport.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#generate_sends_report.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#generate_sends_report.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#generate_sends_report.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#generate_sends_report.ApiResponseFor403) | Forbidden
408 | [ApiResponseFor408](#generate_sends_report.ApiResponseFor408) | Request Timeout
422 | [ApiResponseFor422](#generate_sends_report.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#generate_sends_report.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#generate_sends_report.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#generate_sends_report.ApiResponseFor503) | Service Unavailable

#### generate_sends_report.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AcceptedResponse**](../../models/AcceptedResponse.md) |  | 


#### generate_sends_report.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### generate_sends_report.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### generate_sends_report.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### generate_sends_report.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### generate_sends_report.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### generate_sends_report.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### generate_sends_report.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### generate_sends_report.ApiResponseFor503
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

# **generate_sms_events_report**
<a name="generate_sms_events_report"></a>
> AcceptedResponse generate_sms_events_report(generate_sms_events_report)

Generate SMS events report

Generates a new SMS events report

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import advanced_reports_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.bad_request import BadRequest
from egoi_api.model.unprocessable_entity import UnprocessableEntity
from egoi_api.model.generate_sms_events_report import GenerateSmsEventsReport
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
    api_instance = advanced_reports_api.AdvancedReportsApi(api_client)

    # example passing only required values which don't have defaults set
    body = GenerateSmsEventsReport(
        title="Report title",
        range=AdvancedReportRange(
            start=None,
,
        ),
        campaigns=AdvancedReportCampaigns([
            AdvancedReportCampaignsObject(
                list_id=QueryId(1),
                type="ReportCampaignsAll",
            )
        ]),
        columns=AdvancedReportSmsEventsColumns(
            list_base_fields=[
                "list_base_fields_example"
            ],
            list_extra_fields=AdvancedReportListExtraFields([
                dict(
                    list_id=QueryId(1),
                    fields=[
                        "fields_example"
                    ],
                )
            ]),
            list_stats_fields=SmsEventsListStatsFields(
                delivery_answer=True,
                delivery_date=True,
            ),
            campaign_fields=SmsEventsCampaignFields(
                internal_name=True,
                campaign_hash=True,
                send_date=True,
                group=True,
                sender=True,
            ),
        ),
        options=AdvancedReportSmsEventsOptions(
            notify=[
                QueryId(1)
            ],
        ),
        callback_url="callback_url_example",
    )
    try:
        # Generate SMS events report
        api_response = api_instance.generate_sms_events_report(
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling AdvancedReportsApi->generate_sms_events_report: %s\n" % e)
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
[**GenerateSmsEventsReport**](../../models/GenerateSmsEventsReport.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#generate_sms_events_report.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#generate_sms_events_report.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#generate_sms_events_report.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#generate_sms_events_report.ApiResponseFor403) | Forbidden
408 | [ApiResponseFor408](#generate_sms_events_report.ApiResponseFor408) | Request Timeout
422 | [ApiResponseFor422](#generate_sms_events_report.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#generate_sms_events_report.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#generate_sms_events_report.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#generate_sms_events_report.ApiResponseFor503) | Service Unavailable

#### generate_sms_events_report.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AcceptedResponse**](../../models/AcceptedResponse.md) |  | 


#### generate_sms_events_report.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### generate_sms_events_report.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### generate_sms_events_report.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### generate_sms_events_report.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### generate_sms_events_report.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### generate_sms_events_report.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### generate_sms_events_report.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### generate_sms_events_report.ApiResponseFor503
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

# **generate_subscriptions_report**
<a name="generate_subscriptions_report"></a>
> AcceptedResponse generate_subscriptions_report(generate_subscriptions_report)

Generate subscriptions report

Generates a new subscriptions report

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import advanced_reports_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.generate_subscriptions_report import GenerateSubscriptionsReport
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
    api_instance = advanced_reports_api.AdvancedReportsApi(api_client)

    # example passing only required values which don't have defaults set
    body = GenerateSubscriptionsReport(
        title="Report title",
        range=AdvancedReportRange(
            start=None,
,
        ),
        lists=[
            Id(1)
        ],
        columns=AdvancedReportSubscriptionsColumns(
            list_base_fields=[
                "list_base_fields_example"
            ],
            list_extra_fields=AdvancedReportListExtraFields([
                dict(
                    list_id=QueryId(1),
                    fields=[
                        "fields_example"
                    ],
                )
            ]),
            list_stats_fields=SubscriptionsListStatsFields(
                subscription_method=True,
                subscription_src=True,
            ),
        ),
        options=AdvancedReportSubscriptionsOptions(
            notify=[
                QueryId(1)
            ],
        ),
        callback_url="callback_url_example",
    )
    try:
        # Generate subscriptions report
        api_response = api_instance.generate_subscriptions_report(
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling AdvancedReportsApi->generate_subscriptions_report: %s\n" % e)
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
[**GenerateSubscriptionsReport**](../../models/GenerateSubscriptionsReport.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#generate_subscriptions_report.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#generate_subscriptions_report.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#generate_subscriptions_report.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#generate_subscriptions_report.ApiResponseFor403) | Forbidden
408 | [ApiResponseFor408](#generate_subscriptions_report.ApiResponseFor408) | Request Timeout
422 | [ApiResponseFor422](#generate_subscriptions_report.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#generate_subscriptions_report.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#generate_subscriptions_report.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#generate_subscriptions_report.ApiResponseFor503) | Service Unavailable

#### generate_subscriptions_report.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AcceptedResponse**](../../models/AcceptedResponse.md) |  | 


#### generate_subscriptions_report.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### generate_subscriptions_report.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### generate_subscriptions_report.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### generate_subscriptions_report.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### generate_subscriptions_report.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### generate_subscriptions_report.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### generate_subscriptions_report.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### generate_subscriptions_report.ApiResponseFor503
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

# **generate_unsubscriptions_report**
<a name="generate_unsubscriptions_report"></a>
> AcceptedResponse generate_unsubscriptions_report(generate_unsubscriptions_report)

Generate unsubscriptions report

Generates a new unsubscriptions report

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import advanced_reports_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.generate_unsubscriptions_report import GenerateUnsubscriptionsReport
from egoi_api.model.service_unavailable import ServiceUnavailable
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
    api_instance = advanced_reports_api.AdvancedReportsApi(api_client)

    # example passing only required values which don't have defaults set
    body = GenerateUnsubscriptionsReport(
        title="Report title",
        range=AdvancedReportRange(
            start=None,
,
        ),
        lists=[
            Id(1)
        ],
        columns=AdvancedReportUnsubscriptionsColumns(
            list_base_fields=[
                "list_base_fields_example"
            ],
            list_extra_fields=AdvancedReportListExtraFields([
                dict(
                    list_id=QueryId(1),
                    fields=[
                        "fields_example"
                    ],
                )
            ]),
            list_stats_fields=UnsubscriptionsListStatsFields(
                unsubscription_method=True,
                unsubscription_src=True,
                unsubscription_date=True,
            ),
        ),
        options=AdvancedReportUnsubscriptionsOptions(
            notify=[
                QueryId(1)
            ],
        ),
        callback_url="callback_url_example",
    )
    try:
        # Generate unsubscriptions report
        api_response = api_instance.generate_unsubscriptions_report(
            body=body,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling AdvancedReportsApi->generate_unsubscriptions_report: %s\n" % e)
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
[**GenerateUnsubscriptionsReport**](../../models/GenerateUnsubscriptionsReport.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#generate_unsubscriptions_report.ApiResponseFor202) | Accepted
400 | [ApiResponseFor400](#generate_unsubscriptions_report.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#generate_unsubscriptions_report.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#generate_unsubscriptions_report.ApiResponseFor403) | Forbidden
408 | [ApiResponseFor408](#generate_unsubscriptions_report.ApiResponseFor408) | Request Timeout
422 | [ApiResponseFor422](#generate_unsubscriptions_report.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#generate_unsubscriptions_report.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#generate_unsubscriptions_report.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#generate_unsubscriptions_report.ApiResponseFor503) | Service Unavailable

#### generate_unsubscriptions_report.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AcceptedResponse**](../../models/AcceptedResponse.md) |  | 


#### generate_unsubscriptions_report.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequest**](../../models/BadRequest.md) |  | 


#### generate_unsubscriptions_report.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### generate_unsubscriptions_report.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### generate_unsubscriptions_report.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### generate_unsubscriptions_report.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### generate_unsubscriptions_report.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### generate_unsubscriptions_report.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### generate_unsubscriptions_report.ApiResponseFor503
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

# **get_all_advanced_reports**
<a name="get_all_advanced_reports"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_all_advanced_reports()

Get all advanced reports

Returns all advanced reports

### Example

* Api Key Authentication (Apikey):
```python
import egoi_api
from egoi_api.apis.tags import advanced_reports_api
from egoi_api.model.request_timeout import RequestTimeout
from egoi_api.model.unauthorized import Unauthorized
from egoi_api.model.service_unavailable import ServiceUnavailable
from egoi_api.model.advanced_report import AdvancedReport
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
    api_instance = advanced_reports_api.AdvancedReportsApi(api_client)

    # example passing only optional values
    query_params = {
        'status': "queued",
        'title': "title_example",
        'created_min': "1970-01-01T00:00:00.00Z",
        'created_max': "1970-01-01T00:00:00.00Z",
        'offset': 0,
        'limit': 10,
        'order': "desc",
        'order_by': "advanced_report_id",
    }
    try:
        # Get all advanced reports
        api_response = api_instance.get_all_advanced_reports(
            query_params=query_params,
        )
        pprint(api_response)
    except egoi_api.ApiException as e:
        print("Exception when calling AdvancedReportsApi->get_all_advanced_reports: %s\n" % e)
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
status | StatusSchema | | optional
title | TitleSchema | | optional
created_min | CreatedMinSchema | | optional
created_max | CreatedMaxSchema | | optional
offset | OffsetSchema | | optional
limit | LimitSchema | | optional
order | OrderSchema | | optional
order_by | OrderBySchema | | optional


# StatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["queued", "running", "finished", "stopped", "canceled", "paused", "error", ] 

# TitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CreatedMinSchema

The date and time

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  | The date and time | value must conform to RFC-3339 date-time

# CreatedMaxSchema

The date and time

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  | The date and time | value must conform to RFC-3339 date-time

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
str,  | str,  |  | must be one of ["advanced_report_id", "title", "created", ] if omitted the server will use the default value of "advanced_report_id"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_all_advanced_reports.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#get_all_advanced_reports.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_all_advanced_reports.ApiResponseFor403) | Forbidden
408 | [ApiResponseFor408](#get_all_advanced_reports.ApiResponseFor408) | Request Timeout
422 | [ApiResponseFor422](#get_all_advanced_reports.ApiResponseFor422) | Unprocessable Entity
429 | [ApiResponseFor429](#get_all_advanced_reports.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#get_all_advanced_reports.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#get_all_advanced_reports.ApiResponseFor503) | Service Unavailable

#### get_all_advanced_reports.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

Collection of advanced reports

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Collection of advanced reports | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total_items** | decimal.Decimal, int,  | decimal.Decimal,  | Total advanced reports | [optional] 
**[items](#items)** | list, tuple,  | tuple,  | Returned advanced reports | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# items

Returned advanced reports

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Returned advanced reports | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AdvancedReport**]({{complexTypePrefix}}AdvancedReport.md) | [**AdvancedReport**]({{complexTypePrefix}}AdvancedReport.md) | [**AdvancedReport**]({{complexTypePrefix}}AdvancedReport.md) |  | 

#### get_all_advanced_reports.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Unauthorized**](../../models/Unauthorized.md) |  | 


#### get_all_advanced_reports.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Forbidden**](../../models/Forbidden.md) |  | 


#### get_all_advanced_reports.ApiResponseFor408
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor408ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor408ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RequestTimeout**](../../models/RequestTimeout.md) |  | 


#### get_all_advanced_reports.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnprocessableEntity**](../../models/UnprocessableEntity.md) |  | 


#### get_all_advanced_reports.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TooManyRequests**](../../models/TooManyRequests.md) |  | 


#### get_all_advanced_reports.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServerError**](../../models/InternalServerError.md) |  | 


#### get_all_advanced_reports.ApiResponseFor503
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

