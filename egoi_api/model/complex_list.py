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


class ComplexList(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Complex list schema
    """


    class MetaOapg:
        
        
        class all_of_0(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                
                    @staticmethod
                    def language() -> typing.Type['Language']:
                        return Language
                    
                    
                    class stats(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                total_contacts = schemas.IntSchema
                                total_active = schemas.IntSchema
                                total_inactive = schemas.IntSchema
                                total_removed = schemas.IntSchema
                                total_unconfirmed = schemas.IntSchema
                                total_waiting_new_confirmation = schemas.IntSchema
                                __annotations__ = {
                                    "total_contacts": total_contacts,
                                    "total_active": total_active,
                                    "total_inactive": total_inactive,
                                    "total_removed": total_removed,
                                    "total_unconfirmed": total_unconfirmed,
                                    "total_waiting_new_confirmation": total_waiting_new_confirmation,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["total_contacts"]) -> MetaOapg.properties.total_contacts: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["total_active"]) -> MetaOapg.properties.total_active: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["total_inactive"]) -> MetaOapg.properties.total_inactive: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["total_removed"]) -> MetaOapg.properties.total_removed: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["total_unconfirmed"]) -> MetaOapg.properties.total_unconfirmed: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["total_waiting_new_confirmation"]) -> MetaOapg.properties.total_waiting_new_confirmation: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["total_contacts", "total_active", "total_inactive", "total_removed", "total_unconfirmed", "total_waiting_new_confirmation", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["total_contacts"]) -> typing.Union[MetaOapg.properties.total_contacts, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["total_active"]) -> typing.Union[MetaOapg.properties.total_active, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["total_inactive"]) -> typing.Union[MetaOapg.properties.total_inactive, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["total_removed"]) -> typing.Union[MetaOapg.properties.total_removed, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["total_unconfirmed"]) -> typing.Union[MetaOapg.properties.total_unconfirmed, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["total_waiting_new_confirmation"]) -> typing.Union[MetaOapg.properties.total_waiting_new_confirmation, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total_contacts", "total_active", "total_inactive", "total_removed", "total_unconfirmed", "total_waiting_new_confirmation", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            total_contacts: typing.Union[MetaOapg.properties.total_contacts, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            total_active: typing.Union[MetaOapg.properties.total_active, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            total_inactive: typing.Union[MetaOapg.properties.total_inactive, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            total_removed: typing.Union[MetaOapg.properties.total_removed, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            total_unconfirmed: typing.Union[MetaOapg.properties.total_unconfirmed, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            total_waiting_new_confirmation: typing.Union[MetaOapg.properties.total_waiting_new_confirmation, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'stats':
                            return super().__new__(
                                cls,
                                *args,
                                total_contacts=total_contacts,
                                total_active=total_active,
                                total_inactive=total_inactive,
                                total_removed=total_removed,
                                total_unconfirmed=total_unconfirmed,
                                total_waiting_new_confirmation=total_waiting_new_confirmation,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    __annotations__ = {
                        "language": language,
                        "stats": stats,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["language"]) -> 'Language': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["stats"]) -> MetaOapg.properties.stats: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["language", "stats", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["language"]) -> typing.Union['Language', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["stats"]) -> typing.Union[MetaOapg.properties.stats, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["language", "stats", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                language: typing.Union['Language', schemas.Unset] = schemas.unset,
                stats: typing.Union[MetaOapg.properties.stats, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    language=language,
                    stats=stats,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.all_of_0,
                ModelList,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ComplexList':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from egoi_api.model.language import Language
from egoi_api.model.model_list import ModelList
