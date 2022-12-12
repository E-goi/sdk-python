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


class PushCampaignPatchRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Push campaign patch request schema
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def campaign_hash() -> typing.Type['Hash']:
                return Hash
            title = schemas.StrSchema
            
            
            class content(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        message = schemas.StrSchema
                        __annotations__ = {
                            "message": message,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["message", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'content':
                    return super().__new__(
                        cls,
                        *args,
                        message=message,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class actions(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class type(
                            schemas.EnumBase,
                            schemas.StrSchema
                        ):
                            
                            @schemas.classproperty
                            def URL(cls):
                                return cls("url")
                            
                            @schemas.classproperty
                            def DEEPLINK(cls):
                                return cls("deeplink")
                        title = schemas.StrSchema
                        link = schemas.StrSchema
                        cancel_label = schemas.StrSchema
                        __annotations__ = {
                            "type": type,
                            "title": title,
                            "link": link,
                            "cancel_label": cancel_label,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["link"]) -> MetaOapg.properties.link: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["cancel_label"]) -> MetaOapg.properties.cancel_label: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "title", "link", "cancel_label", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["link"]) -> typing.Union[MetaOapg.properties.link, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["cancel_label"]) -> typing.Union[MetaOapg.properties.cancel_label, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "title", "link", "cancel_label", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
                    title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
                    link: typing.Union[MetaOapg.properties.link, str, schemas.Unset] = schemas.unset,
                    cancel_label: typing.Union[MetaOapg.properties.cancel_label, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'actions':
                    return super().__new__(
                        cls,
                        *args,
                        type=type,
                        title=title,
                        link=link,
                        cancel_label=cancel_label,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class geo_options(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class latitude(
                            schemas.IntSchema
                        ):
                            pass
                        
                        
                        class longitude(
                            schemas.IntSchema
                        ):
                            pass
                        
                        
                        class range(
                            schemas.IntSchema
                        ):
                            pass
                        __annotations__ = {
                            "latitude": latitude,
                            "longitude": longitude,
                            "range": range,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["latitude"]) -> MetaOapg.properties.latitude: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["longitude"]) -> MetaOapg.properties.longitude: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["range"]) -> MetaOapg.properties.range: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["latitude", "longitude", "range", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["latitude"]) -> typing.Union[MetaOapg.properties.latitude, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["longitude"]) -> typing.Union[MetaOapg.properties.longitude, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["range"]) -> typing.Union[MetaOapg.properties.range, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["latitude", "longitude", "range", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    latitude: typing.Union[MetaOapg.properties.latitude, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    longitude: typing.Union[MetaOapg.properties.longitude, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    range: typing.Union[MetaOapg.properties.range, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'geo_options':
                    return super().__new__(
                        cls,
                        *args,
                        latitude=latitude,
                        longitude=longitude,
                        range=range,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class notification_options(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        icon = schemas.StrSchema
                        __annotations__ = {
                            "icon": icon,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["icon"]) -> MetaOapg.properties.icon: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["icon", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["icon"]) -> typing.Union[MetaOapg.properties.icon, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["icon", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    icon: typing.Union[MetaOapg.properties.icon, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'notification_options':
                    return super().__new__(
                        cls,
                        *args,
                        icon=icon,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "campaign_hash": campaign_hash,
                "title": title,
                "content": content,
                "actions": actions,
                "geo_options": geo_options,
                "notification_options": notification_options,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["campaign_hash"]) -> 'Hash': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["content"]) -> MetaOapg.properties.content: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actions"]) -> MetaOapg.properties.actions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["geo_options"]) -> MetaOapg.properties.geo_options: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notification_options"]) -> MetaOapg.properties.notification_options: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["campaign_hash", "title", "content", "actions", "geo_options", "notification_options", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["campaign_hash"]) -> typing.Union['Hash', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["content"]) -> typing.Union[MetaOapg.properties.content, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actions"]) -> typing.Union[MetaOapg.properties.actions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["geo_options"]) -> typing.Union[MetaOapg.properties.geo_options, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notification_options"]) -> typing.Union[MetaOapg.properties.notification_options, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["campaign_hash", "title", "content", "actions", "geo_options", "notification_options", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        campaign_hash: typing.Union['Hash', schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        content: typing.Union[MetaOapg.properties.content, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        actions: typing.Union[MetaOapg.properties.actions, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        geo_options: typing.Union[MetaOapg.properties.geo_options, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        notification_options: typing.Union[MetaOapg.properties.notification_options, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PushCampaignPatchRequest':
        return super().__new__(
            cls,
            *args,
            campaign_hash=campaign_hash,
            title=title,
            content=content,
            actions=actions,
            geo_options=geo_options,
            notification_options=notification_options,
            _configuration=_configuration,
            **kwargs,
        )

from egoi_api.model.hash import Hash
