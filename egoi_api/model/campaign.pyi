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


class Campaign(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Campaign schema
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def campaign_hash() -> typing.Type['Hash']:
                return Hash
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def DRAFT(cls):
                    return cls("draft")
                
                @schemas.classproperty
                def CANCELED(cls):
                    return cls("canceled")
                
                @schemas.classproperty
                def QUEUED(cls):
                    return cls("queued")
                
                @schemas.classproperty
                def PAUSED(cls):
                    return cls("paused")
                
                @schemas.classproperty
                def SENDING(cls):
                    return cls("sending")
                
                @schemas.classproperty
                def SENT(cls):
                    return cls("sent")
            thumbnail = schemas.StrSchema
            
            
            class channel(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EMAIL(cls):
                    return cls("email")
                
                @schemas.classproperty
                def PUSH(cls):
                    return cls("push")
                
                @schemas.classproperty
                def SMS(cls):
                    return cls("sms")
                
                @schemas.classproperty
                def SMART_SMS(cls):
                    return cls("smart_sms")
                
                @schemas.classproperty
                def VOICE(cls):
                    return cls("voice")
                
                @schemas.classproperty
                def WEB_PUSH(cls):
                    return cls("web_push")
            internal_name = schemas.StrSchema
        
            @staticmethod
            def list_id() -> typing.Type['Id']:
                return Id
            title = schemas.StrSchema
        
            @staticmethod
            def created_by() -> typing.Type['Id']:
                return Id
        
            @staticmethod
            def group_id() -> typing.Type['Id']:
                return Id
            
            
            class created(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    all_of_0 = schemas.DateTimeSchema
                    
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
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'created':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class updated(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    all_of_0 = schemas.DateTimeSchema
                    
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
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'updated':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class start_date(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    all_of_0 = schemas.DateTimeSchema
                    
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
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'start_date':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class end_date(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    all_of_0 = schemas.DateTimeSchema
                    
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
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'end_date':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class schedule_date(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        enabled = schemas.BoolSchema
                        
                        
                        class date(
                            schemas.ComposedSchema,
                        ):
                        
                        
                            class MetaOapg:
                                all_of_0 = schemas.DateTimeSchema
                                
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
                                    ]
                        
                        
                            def __new__(
                                cls,
                                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'date':
                                return super().__new__(
                                    cls,
                                    *args,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "enabled": enabled,
                            "date": date,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["enabled", "date", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> typing.Union[MetaOapg.properties.enabled, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["enabled", "date", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    enabled: typing.Union[MetaOapg.properties.enabled, bool, schemas.Unset] = schemas.unset,
                    date: typing.Union[MetaOapg.properties.date, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'schedule_date':
                    return super().__new__(
                        cls,
                        *args,
                        enabled=enabled,
                        date=date,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "campaign_hash": campaign_hash,
                "status": status,
                "thumbnail": thumbnail,
                "channel": channel,
                "internal_name": internal_name,
                "list_id": list_id,
                "title": title,
                "created_by": created_by,
                "group_id": group_id,
                "created": created,
                "updated": updated,
                "start_date": start_date,
                "end_date": end_date,
                "schedule_date": schedule_date,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["campaign_hash"]) -> 'Hash': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thumbnail"]) -> MetaOapg.properties.thumbnail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channel"]) -> MetaOapg.properties.channel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["internal_name"]) -> MetaOapg.properties.internal_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["list_id"]) -> 'Id': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_by"]) -> 'Id': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["group_id"]) -> 'Id': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated"]) -> MetaOapg.properties.updated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schedule_date"]) -> MetaOapg.properties.schedule_date: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["campaign_hash", "status", "thumbnail", "channel", "internal_name", "list_id", "title", "created_by", "group_id", "created", "updated", "start_date", "end_date", "schedule_date", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["campaign_hash"]) -> typing.Union['Hash', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thumbnail"]) -> typing.Union[MetaOapg.properties.thumbnail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channel"]) -> typing.Union[MetaOapg.properties.channel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["internal_name"]) -> typing.Union[MetaOapg.properties.internal_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["list_id"]) -> typing.Union['Id', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_by"]) -> typing.Union['Id', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["group_id"]) -> typing.Union['Id', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> typing.Union[MetaOapg.properties.created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated"]) -> typing.Union[MetaOapg.properties.updated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union[MetaOapg.properties.start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> typing.Union[MetaOapg.properties.end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schedule_date"]) -> typing.Union[MetaOapg.properties.schedule_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["campaign_hash", "status", "thumbnail", "channel", "internal_name", "list_id", "title", "created_by", "group_id", "created", "updated", "start_date", "end_date", "schedule_date", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        campaign_hash: typing.Union['Hash', schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        thumbnail: typing.Union[MetaOapg.properties.thumbnail, str, schemas.Unset] = schemas.unset,
        channel: typing.Union[MetaOapg.properties.channel, str, schemas.Unset] = schemas.unset,
        internal_name: typing.Union[MetaOapg.properties.internal_name, str, schemas.Unset] = schemas.unset,
        list_id: typing.Union['Id', schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        created_by: typing.Union['Id', schemas.Unset] = schemas.unset,
        group_id: typing.Union['Id', schemas.Unset] = schemas.unset,
        created: typing.Union[MetaOapg.properties.created, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        updated: typing.Union[MetaOapg.properties.updated, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        start_date: typing.Union[MetaOapg.properties.start_date, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        end_date: typing.Union[MetaOapg.properties.end_date, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        schedule_date: typing.Union[MetaOapg.properties.schedule_date, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Campaign':
        return super().__new__(
            cls,
            *args,
            campaign_hash=campaign_hash,
            status=status,
            thumbnail=thumbnail,
            channel=channel,
            internal_name=internal_name,
            list_id=list_id,
            title=title,
            created_by=created_by,
            group_id=group_id,
            created=created,
            updated=updated,
            start_date=start_date,
            end_date=end_date,
            schedule_date=schedule_date,
            _configuration=_configuration,
            **kwargs,
        )

from egoi_api.model.hash import Hash
from egoi_api.model.id import Id
