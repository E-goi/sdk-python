# coding: utf-8

"""
    APIv3 (New)

     # Introduction This is our new version of API. We invite you to start using it and give us your feedback # Getting Started  E-goi can be integrated with many environments and programming languages via our REST API. We've created a developer focused portal to give your organization a clear and quick overview of how to integrate with E-goi. The developer portal focuses on scenarios for integration and flow of events. We recommend familiarizing yourself with all of the content in the developer portal, before start using our rest API.  The E-goi  APIv3 is served over HTTPS. To ensure data privacy, unencrypted HTTP is not supported.  Request data is passed to the API by POSTing JSON objects to the API endpoints with the appropriate parameters.      BaseURL = api.egoiapp.com  # RESTful Services This API supports 5 HTTP methods:  * <b>GET</b>: The HTTP GET method is used to **read** (or retrieve) a representation of a resource. * <b>POST</b>: The POST verb is most-often utilized to **create** new resources. * <b>PATCH</b>: PATCH is used for **modify** capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource * <b>PUT</b>: PUT is most-often utilized for **update** capabilities, PUT-ing to a known resource URI with the request body containing the newly-updated representation of the original resource. * <b>DELETE</b>: DELETE is pretty easy to understand. It is used to **delete** a resource identified by a URI.  # Authentication  We use a custom authentication method, you will need a apikey that you can find in your account settings. Below you will see a curl example to get your account information:     #!/bin/bash     curl -X GET 'https://api.egoiapp.com/my-account' \\     -H 'accept: application/json' \\     -H 'Apikey: <YOUR_APY_KEY>'  Here you can see a curl Post example with authentication:     #!/bin/bash     curl -X POST 'http://api.egoiapp.com/tags' \\     -H 'accept: application/json' \\     -H 'Apikey: <YOUR_APY_KEY>' \\     -H 'Content-Type: application/json' \\     -d '{`name`:`Your custom tag`,`color`:`#FFFFFF`}'  # SDK Get started quickly with E-goi with our integration tools. Our SDK is a modern open source library that makes it easy to integrate your application with E-goi services.  * <a href='https://github.com/E-goi/sdk-java'>Java</a>  * <a href='https://github.com/E-goi/sdk-php'>PHP</a>  * <a href='https://github.com/E-goi/sdk-python'>Python</a>  * <a href='https://github.com/E-goi/sdk-ruby'>Ruby</a>  * <a href='https://github.com/E-goi/sdk-javascript'>Javascript</a>  * <a href='https://github.com/E-goi/sdk-csharp'>C#</a>  # Stream Limits Stream limits are security mesures we have to make sure our API have a fair use policy, for this reason, any request that creates or modifies data (**POST**, **PATCH** and **PUT**) is limited to a maximum of **20MB** of content length. If you arrive to this limit in one of your request, you'll receive a HTTP code **413 (Request Entity Too Large)** and the request will be ignored. To avoid this error in importation's requests, it's advised the request's division in batches that have each one less than 20MB.  # Timeouts Timeouts set a maximum waiting time on a request's response. Our API, sets a default timeout for each request and when breached, you'll receive an HTTP **408 (Request Timeout)** error code. You should take into consideration that response times can vary widely based on the complexity of the request, amount of data being analyzed, and the load on the system and workspace at the time of the query. When dealing with such errors, you should first attempt to reduce the complexity and amount of data under analysis, and only then, if problems are still occurring ask for support.  For all these reasons, the default timeout for each request is **10 Seconds** and any request that creates or modifies data (**POST**, **PATCH** and **PUT**) will have a timeout of **60 Seconds**. Specific timeouts may exist for specific requests, these can be found in the request's documentation.  # Callbacks A callback is an asynchronous API request that originates from the API server and is sent to the client in response to a previous request sent by that client.  The API will make a **POST** request to the address defined in the URL with the information regarding the event of interest and share data related to that event.  ***Note:*** Only http or https protocols are supported in the Url parameter.  <security-definitions/>  # noqa: E501

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


class EmailEventsListStatsFields(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    List stats fields to include in the report
    """


    class MetaOapg:
        required = {
            "forwards",
            "social_shares",
            "tw_shares",
            "fb_likes",
            "unsubscribes",
            "forwards_conversion",
            "complaints",
            "clicks",
            "opens",
            "bounces",
            "fb_shares",
        }
        
        class properties:
            opens = schemas.BoolSchema
            clicks = schemas.BoolSchema
            complaints = schemas.BoolSchema
            unsubscribes = schemas.BoolSchema
            bounces = schemas.BoolSchema
            forwards = schemas.BoolSchema
            forwards_conversion = schemas.BoolSchema
            fb_likes = schemas.BoolSchema
            fb_shares = schemas.BoolSchema
            tw_shares = schemas.BoolSchema
            social_shares = schemas.BoolSchema
            __annotations__ = {
                "opens": opens,
                "clicks": clicks,
                "complaints": complaints,
                "unsubscribes": unsubscribes,
                "bounces": bounces,
                "forwards": forwards,
                "forwards_conversion": forwards_conversion,
                "fb_likes": fb_likes,
                "fb_shares": fb_shares,
                "tw_shares": tw_shares,
                "social_shares": social_shares,
            }
    
    forwards: MetaOapg.properties.forwards
    social_shares: MetaOapg.properties.social_shares
    tw_shares: MetaOapg.properties.tw_shares
    fb_likes: MetaOapg.properties.fb_likes
    unsubscribes: MetaOapg.properties.unsubscribes
    forwards_conversion: MetaOapg.properties.forwards_conversion
    complaints: MetaOapg.properties.complaints
    clicks: MetaOapg.properties.clicks
    opens: MetaOapg.properties.opens
    bounces: MetaOapg.properties.bounces
    fb_shares: MetaOapg.properties.fb_shares
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["opens"]) -> MetaOapg.properties.opens: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clicks"]) -> MetaOapg.properties.clicks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["complaints"]) -> MetaOapg.properties.complaints: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unsubscribes"]) -> MetaOapg.properties.unsubscribes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bounces"]) -> MetaOapg.properties.bounces: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["forwards"]) -> MetaOapg.properties.forwards: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["forwards_conversion"]) -> MetaOapg.properties.forwards_conversion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fb_likes"]) -> MetaOapg.properties.fb_likes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fb_shares"]) -> MetaOapg.properties.fb_shares: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tw_shares"]) -> MetaOapg.properties.tw_shares: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["social_shares"]) -> MetaOapg.properties.social_shares: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["opens", "clicks", "complaints", "unsubscribes", "bounces", "forwards", "forwards_conversion", "fb_likes", "fb_shares", "tw_shares", "social_shares", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["opens"]) -> MetaOapg.properties.opens: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clicks"]) -> MetaOapg.properties.clicks: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["complaints"]) -> MetaOapg.properties.complaints: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unsubscribes"]) -> MetaOapg.properties.unsubscribes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bounces"]) -> MetaOapg.properties.bounces: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["forwards"]) -> MetaOapg.properties.forwards: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["forwards_conversion"]) -> MetaOapg.properties.forwards_conversion: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fb_likes"]) -> MetaOapg.properties.fb_likes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fb_shares"]) -> MetaOapg.properties.fb_shares: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tw_shares"]) -> MetaOapg.properties.tw_shares: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["social_shares"]) -> MetaOapg.properties.social_shares: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["opens", "clicks", "complaints", "unsubscribes", "bounces", "forwards", "forwards_conversion", "fb_likes", "fb_shares", "tw_shares", "social_shares", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        forwards: typing.Union[MetaOapg.properties.forwards, bool, ],
        social_shares: typing.Union[MetaOapg.properties.social_shares, bool, ],
        tw_shares: typing.Union[MetaOapg.properties.tw_shares, bool, ],
        fb_likes: typing.Union[MetaOapg.properties.fb_likes, bool, ],
        unsubscribes: typing.Union[MetaOapg.properties.unsubscribes, bool, ],
        forwards_conversion: typing.Union[MetaOapg.properties.forwards_conversion, bool, ],
        complaints: typing.Union[MetaOapg.properties.complaints, bool, ],
        clicks: typing.Union[MetaOapg.properties.clicks, bool, ],
        opens: typing.Union[MetaOapg.properties.opens, bool, ],
        bounces: typing.Union[MetaOapg.properties.bounces, bool, ],
        fb_shares: typing.Union[MetaOapg.properties.fb_shares, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmailEventsListStatsFields':
        return super().__new__(
            cls,
            *args,
            forwards=forwards,
            social_shares=social_shares,
            tw_shares=tw_shares,
            fb_likes=fb_likes,
            unsubscribes=unsubscribes,
            forwards_conversion=forwards_conversion,
            complaints=complaints,
            clicks=clicks,
            opens=opens,
            bounces=bounces,
            fb_shares=fb_shares,
            _configuration=_configuration,
            **kwargs,
        )
