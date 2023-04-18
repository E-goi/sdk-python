# coding: utf-8

"""
    APIv3 (New)

     # Introduction This is our new version of API. We invite you to start using it and give us your feedback # Getting Started  E-goi can be integrated with many environments and programming languages via our REST API. We've created a developer focused portal to give your organization a clear and quick overview of how to integrate with E-goi. The developer portal focuses on scenarios for integration and flow of events. We recommend familiarizing yourself with all of the content in the developer portal, before start using our rest API.  The E-goi  APIv3 is served over HTTPS. To ensure data privacy, unencrypted HTTP is not supported.  Request data is passed to the API by POSTing JSON objects to the API endpoints with the appropriate parameters.      BaseURL = api.egoiapp.com  # RESTful Services This API supports 5 HTTP methods:  * <b>GET</b>: The HTTP GET method is used to **read** (or retrieve) a representation of a resource. * <b>POST</b>: The POST verb is most-often utilized to **create** new resources. * <b>PATCH</b>: PATCH is used for **modify** capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource * <b>PUT</b>: PUT is most-often utilized for **update** capabilities, PUT-ing to a known resource URI with the request body containing the newly-updated representation of the original resource. * <b>DELETE</b>: DELETE is pretty easy to understand. It is used to **delete** a resource identified by a URI.  # Authentication  We use a custom authentication method, you will need a apikey that you can find in your account settings. Below you will see a curl example to get your account information:     #!/bin/bash     curl -X GET 'https://api.egoiapp.com/my-account' \\     -H 'accept: application/json' \\     -H 'Apikey: <YOUR_APY_KEY>'  Here you can see a curl Post example with authentication:     #!/bin/bash     curl -X POST 'http://api.egoiapp.com/tags' \\     -H 'accept: application/json' \\     -H 'Apikey: <YOUR_APY_KEY>' \\     -H 'Content-Type: application/json' \\     -d '{`name`:`Your custom tag`,`color`:`#FFFFFF`}'  # SDK Get started quickly with E-goi with our integration tools. Our SDK is a modern open source library that makes it easy to integrate your application with E-goi services.  * <a href='https://github.com/E-goi/sdk-java'>Java</a>  * <a href='https://github.com/E-goi/sdk-php'>PHP</a>  * <a href='https://github.com/E-goi/sdk-python'>Python</a>  * <a href='https://github.com/E-goi/sdk-ruby'>Ruby</a>  * <a href='https://github.com/E-goi/sdk-javascript'>Javascript</a>  * <a href='https://github.com/E-goi/sdk-csharp'>C#</a>  # Stream Limits Stream limits are security mesures we have to make sure our API have a fair use policy, for this reason, any request that creates or modifies data (**POST**, **PATCH** and **PUT**) is limited to a maximum of **20MB** of content length. If you arrive to this limit in one of your request, you'll receive a HTTP code **413 (Request Entity Too Large)** and the request will be ignored. To avoid this error in importation's requests, it's advised the request's division in batches that have each one less than 20MB.  # Timeouts Timeouts set a maximum waiting time on a request's response. Our API, sets a default timeout for each request and when breached, you'll receive an HTTP **408 (Request Timeout)** error code. You should take into consideration that response times can vary widely based on the complexity of the request, amount of data being analyzed, and the load on the system and workspace at the time of the query. When dealing with such errors, you should first attempt to reduce the complexity and amount of data under analysis, and only then, if problems are still occurring ask for support.  For all these reasons, the default timeout for each request is **10 Seconds** and any request that creates or modifies data (**POST**, **PATCH** and **PUT**) will have a timeout of **60 Seconds**. Specific timeouts may exist for specific requests, these can be found in the request's documentation.  # Callbacks A callback is an asynchronous API request that originates from the API server and is sent to the client in response to a previous request sent by that client.  The API will make a **POST** request to the address defined in the URL with the information regarding the event of interest and share data related to that event.  <a href='/usecases/callbacks/' target='_blank'>[Go to callbacks documentation]</a>  ***Note:*** Only http or https protocols are supported in the Url parameter.  <security-definitions/>  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from egoi_api import schemas  # noqa: F401


class AdvancedReportEmailEventsColumns(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Columns of the report
    """


    class MetaOapg:
        required = {
            "campaign_fields",
            "list_stats_fields",
            "list_extra_fields",
            "list_base_fields",
        }
        
        class properties:
            
            
            class list_base_fields(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'list_base_fields':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
        
            @staticmethod
            def list_extra_fields() -> typing.Type['AdvancedReportListExtraFields']:
                return AdvancedReportListExtraFields
        
            @staticmethod
            def list_stats_fields() -> typing.Type['EmailEventsListStatsFields']:
                return EmailEventsListStatsFields
        
            @staticmethod
            def campaign_fields() -> typing.Type['EmailEventsCampaignFields']:
                return EmailEventsCampaignFields
            __annotations__ = {
                "list_base_fields": list_base_fields,
                "list_extra_fields": list_extra_fields,
                "list_stats_fields": list_stats_fields,
                "campaign_fields": campaign_fields,
            }
    
    campaign_fields: 'EmailEventsCampaignFields'
    list_stats_fields: 'EmailEventsListStatsFields'
    list_extra_fields: 'AdvancedReportListExtraFields'
    list_base_fields: MetaOapg.properties.list_base_fields
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["list_base_fields"]) -> MetaOapg.properties.list_base_fields: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["list_extra_fields"]) -> 'AdvancedReportListExtraFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["list_stats_fields"]) -> 'EmailEventsListStatsFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["campaign_fields"]) -> 'EmailEventsCampaignFields': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["list_base_fields", "list_extra_fields", "list_stats_fields", "campaign_fields", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["list_base_fields"]) -> MetaOapg.properties.list_base_fields: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["list_extra_fields"]) -> 'AdvancedReportListExtraFields': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["list_stats_fields"]) -> 'EmailEventsListStatsFields': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["campaign_fields"]) -> 'EmailEventsCampaignFields': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["list_base_fields", "list_extra_fields", "list_stats_fields", "campaign_fields", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        campaign_fields: 'EmailEventsCampaignFields',
        list_stats_fields: 'EmailEventsListStatsFields',
        list_extra_fields: 'AdvancedReportListExtraFields',
        list_base_fields: typing.Union[MetaOapg.properties.list_base_fields, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AdvancedReportEmailEventsColumns':
        return super().__new__(
            cls,
            *args,
            campaign_fields=campaign_fields,
            list_stats_fields=list_stats_fields,
            list_extra_fields=list_extra_fields,
            list_base_fields=list_base_fields,
            _configuration=_configuration,
            **kwargs,
        )

from egoi_api.model.advanced_report_list_extra_fields import AdvancedReportListExtraFields
from egoi_api.model.email_events_campaign_fields import EmailEventsCampaignFields
from egoi_api.model.email_events_list_stats_fields import EmailEventsListStatsFields
