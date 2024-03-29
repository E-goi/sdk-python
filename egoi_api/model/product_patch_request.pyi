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


class ProductPatchRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Product patch request schema
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            description = schemas.StrSchema
            sku = schemas.StrSchema
            upc = schemas.StrSchema
            ean = schemas.StrSchema
            gtin = schemas.StrSchema
            mpn = schemas.StrSchema
            link = schemas.StrSchema
            image_link = schemas.StrSchema
            price = schemas.Float64Schema
            sale_price = schemas.Float64Schema
            brand = schemas.StrSchema
            
            
            class categories(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'categories':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class related_products(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class external_product_id(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                items = schemas.StrSchema
                        
                            def __new__(
                                cls,
                                arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'external_product_id':
                                return super().__new__(
                                    cls,
                                    arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        __annotations__ = {
                            "external_product_id": external_product_id,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["external_product_id"]) -> MetaOapg.properties.external_product_id: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["external_product_id", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["external_product_id"]) -> typing.Union[MetaOapg.properties.external_product_id, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["external_product_id", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    external_product_id: typing.Union[MetaOapg.properties.external_product_id, list, tuple, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'related_products':
                    return super().__new__(
                        cls,
                        *args,
                        external_product_id=external_product_id,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class custom_attributes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ProductCustomAttributes']:
                        return ProductCustomAttributes
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ProductCustomAttributes'], typing.List['ProductCustomAttributes']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'custom_attributes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ProductCustomAttributes':
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "description": description,
                "sku": sku,
                "upc": upc,
                "ean": ean,
                "gtin": gtin,
                "mpn": mpn,
                "link": link,
                "image_link": image_link,
                "price": price,
                "sale_price": sale_price,
                "brand": brand,
                "categories": categories,
                "related_products": related_products,
                "custom_attributes": custom_attributes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sku"]) -> MetaOapg.properties.sku: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upc"]) -> MetaOapg.properties.upc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ean"]) -> MetaOapg.properties.ean: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gtin"]) -> MetaOapg.properties.gtin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mpn"]) -> MetaOapg.properties.mpn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link"]) -> MetaOapg.properties.link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_link"]) -> MetaOapg.properties.image_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sale_price"]) -> MetaOapg.properties.sale_price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["brand"]) -> MetaOapg.properties.brand: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["categories"]) -> MetaOapg.properties.categories: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["related_products"]) -> MetaOapg.properties.related_products: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_attributes"]) -> MetaOapg.properties.custom_attributes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "description", "sku", "upc", "ean", "gtin", "mpn", "link", "image_link", "price", "sale_price", "brand", "categories", "related_products", "custom_attributes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sku"]) -> typing.Union[MetaOapg.properties.sku, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upc"]) -> typing.Union[MetaOapg.properties.upc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ean"]) -> typing.Union[MetaOapg.properties.ean, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gtin"]) -> typing.Union[MetaOapg.properties.gtin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mpn"]) -> typing.Union[MetaOapg.properties.mpn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link"]) -> typing.Union[MetaOapg.properties.link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_link"]) -> typing.Union[MetaOapg.properties.image_link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> typing.Union[MetaOapg.properties.price, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sale_price"]) -> typing.Union[MetaOapg.properties.sale_price, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["brand"]) -> typing.Union[MetaOapg.properties.brand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["categories"]) -> typing.Union[MetaOapg.properties.categories, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["related_products"]) -> typing.Union[MetaOapg.properties.related_products, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_attributes"]) -> typing.Union[MetaOapg.properties.custom_attributes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "description", "sku", "upc", "ean", "gtin", "mpn", "link", "image_link", "price", "sale_price", "brand", "categories", "related_products", "custom_attributes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        sku: typing.Union[MetaOapg.properties.sku, str, schemas.Unset] = schemas.unset,
        upc: typing.Union[MetaOapg.properties.upc, str, schemas.Unset] = schemas.unset,
        ean: typing.Union[MetaOapg.properties.ean, str, schemas.Unset] = schemas.unset,
        gtin: typing.Union[MetaOapg.properties.gtin, str, schemas.Unset] = schemas.unset,
        mpn: typing.Union[MetaOapg.properties.mpn, str, schemas.Unset] = schemas.unset,
        link: typing.Union[MetaOapg.properties.link, str, schemas.Unset] = schemas.unset,
        image_link: typing.Union[MetaOapg.properties.image_link, str, schemas.Unset] = schemas.unset,
        price: typing.Union[MetaOapg.properties.price, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        sale_price: typing.Union[MetaOapg.properties.sale_price, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        brand: typing.Union[MetaOapg.properties.brand, str, schemas.Unset] = schemas.unset,
        categories: typing.Union[MetaOapg.properties.categories, list, tuple, schemas.Unset] = schemas.unset,
        related_products: typing.Union[MetaOapg.properties.related_products, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        custom_attributes: typing.Union[MetaOapg.properties.custom_attributes, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProductPatchRequest':
        return super().__new__(
            cls,
            *args,
            name=name,
            description=description,
            sku=sku,
            upc=upc,
            ean=ean,
            gtin=gtin,
            mpn=mpn,
            link=link,
            image_link=image_link,
            price=price,
            sale_price=sale_price,
            brand=brand,
            categories=categories,
            related_products=related_products,
            custom_attributes=custom_attributes,
            _configuration=_configuration,
            **kwargs,
        )

from egoi_api.model.product_custom_attributes import ProductCustomAttributes
