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


class EmailReportByHour(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Email stats grouped by Hour
    """


    class MetaOapg:
        
        class properties:
            
            
            class hour(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                hour = schemas.StrSchema
                                
                                
                                class sends(
                                    schemas.IntSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        inclusive_minimum = 0
                                
                                
                                class opens(
                                    schemas.IntSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        inclusive_minimum = 0
                                
                                
                                class clicks(
                                    schemas.IntSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        inclusive_minimum = 0
                                
                                
                                class hard_bounces(
                                    schemas.IntSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        inclusive_minimum = 0
                                
                                
                                class soft_bounces(
                                    schemas.IntSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        inclusive_minimum = 0
                                
                                
                                class complaints(
                                    schemas.IntSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        inclusive_minimum = 0
                                
                                
                                class unsubscriptions(
                                    schemas.IntSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        inclusive_minimum = 0
                                __annotations__ = {
                                    "hour": hour,
                                    "sends": sends,
                                    "opens": opens,
                                    "clicks": clicks,
                                    "hard_bounces": hard_bounces,
                                    "soft_bounces": soft_bounces,
                                    "complaints": complaints,
                                    "unsubscriptions": unsubscriptions,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["hour"]) -> MetaOapg.properties.hour: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["sends"]) -> MetaOapg.properties.sends: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["opens"]) -> MetaOapg.properties.opens: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["clicks"]) -> MetaOapg.properties.clicks: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["hard_bounces"]) -> MetaOapg.properties.hard_bounces: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["soft_bounces"]) -> MetaOapg.properties.soft_bounces: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["complaints"]) -> MetaOapg.properties.complaints: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["unsubscriptions"]) -> MetaOapg.properties.unsubscriptions: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["hour", "sends", "opens", "clicks", "hard_bounces", "soft_bounces", "complaints", "unsubscriptions", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["hour"]) -> typing.Union[MetaOapg.properties.hour, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["sends"]) -> typing.Union[MetaOapg.properties.sends, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["opens"]) -> typing.Union[MetaOapg.properties.opens, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["clicks"]) -> typing.Union[MetaOapg.properties.clicks, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["hard_bounces"]) -> typing.Union[MetaOapg.properties.hard_bounces, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["soft_bounces"]) -> typing.Union[MetaOapg.properties.soft_bounces, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["complaints"]) -> typing.Union[MetaOapg.properties.complaints, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["unsubscriptions"]) -> typing.Union[MetaOapg.properties.unsubscriptions, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["hour", "sends", "opens", "clicks", "hard_bounces", "soft_bounces", "complaints", "unsubscriptions", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            hour: typing.Union[MetaOapg.properties.hour, str, schemas.Unset] = schemas.unset,
                            sends: typing.Union[MetaOapg.properties.sends, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            opens: typing.Union[MetaOapg.properties.opens, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            clicks: typing.Union[MetaOapg.properties.clicks, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            hard_bounces: typing.Union[MetaOapg.properties.hard_bounces, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            soft_bounces: typing.Union[MetaOapg.properties.soft_bounces, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            complaints: typing.Union[MetaOapg.properties.complaints, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            unsubscriptions: typing.Union[MetaOapg.properties.unsubscriptions, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *args,
                                hour=hour,
                                sends=sends,
                                opens=opens,
                                clicks=clicks,
                                hard_bounces=hard_bounces,
                                soft_bounces=soft_bounces,
                                complaints=complaints,
                                unsubscriptions=unsubscriptions,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'hour':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "hour": hour,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hour"]) -> MetaOapg.properties.hour: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["hour", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hour"]) -> typing.Union[MetaOapg.properties.hour, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["hour", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        hour: typing.Union[MetaOapg.properties.hour, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmailReportByHour':
        return super().__new__(
            cls,
            *args,
            hour=hour,
            _configuration=_configuration,
            **kwargs,
        )
