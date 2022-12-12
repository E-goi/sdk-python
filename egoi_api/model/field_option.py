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


class FieldOption(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Field option schema
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def option_id() -> typing.Type['Id']:
                return Id
            en = schemas.StrSchema
            pt = schemas.StrSchema
            br = schemas.StrSchema
            es = schemas.StrSchema
            de = schemas.StrSchema
            hu = schemas.StrSchema
            fr = schemas.StrSchema
            __annotations__ = {
                "option_id": option_id,
                "en": en,
                "pt": pt,
                "br": br,
                "es": es,
                "de": de,
                "hu": hu,
                "fr": fr,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["option_id"]) -> 'Id': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["en"]) -> MetaOapg.properties.en: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pt"]) -> MetaOapg.properties.pt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["br"]) -> MetaOapg.properties.br: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["es"]) -> MetaOapg.properties.es: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["de"]) -> MetaOapg.properties.de: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hu"]) -> MetaOapg.properties.hu: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fr"]) -> MetaOapg.properties.fr: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["option_id", "en", "pt", "br", "es", "de", "hu", "fr", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["option_id"]) -> typing.Union['Id', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["en"]) -> typing.Union[MetaOapg.properties.en, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pt"]) -> typing.Union[MetaOapg.properties.pt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["br"]) -> typing.Union[MetaOapg.properties.br, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["es"]) -> typing.Union[MetaOapg.properties.es, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["de"]) -> typing.Union[MetaOapg.properties.de, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hu"]) -> typing.Union[MetaOapg.properties.hu, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fr"]) -> typing.Union[MetaOapg.properties.fr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["option_id", "en", "pt", "br", "es", "de", "hu", "fr", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        option_id: typing.Union['Id', schemas.Unset] = schemas.unset,
        en: typing.Union[MetaOapg.properties.en, str, schemas.Unset] = schemas.unset,
        pt: typing.Union[MetaOapg.properties.pt, str, schemas.Unset] = schemas.unset,
        br: typing.Union[MetaOapg.properties.br, str, schemas.Unset] = schemas.unset,
        es: typing.Union[MetaOapg.properties.es, str, schemas.Unset] = schemas.unset,
        de: typing.Union[MetaOapg.properties.de, str, schemas.Unset] = schemas.unset,
        hu: typing.Union[MetaOapg.properties.hu, str, schemas.Unset] = schemas.unset,
        fr: typing.Union[MetaOapg.properties.fr, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FieldOption':
        return super().__new__(
            cls,
            *args,
            option_id=option_id,
            en=en,
            pt=pt,
            br=br,
            es=es,
            de=de,
            hu=hu,
            fr=fr,
            _configuration=_configuration,
            **kwargs,
        )

from egoi_api.model.id import Id
