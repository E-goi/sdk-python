# coding: utf-8

"""
    APIv3 (Beta)

     # Introduction Just a quick pick!!! This is our new version of API. Remember, it is not stable yet!!! But we invite you play with it and give us your feedback ;) # Getting Started  E-goi can be integrated with many environments and programming languages via our REST API. We've created a developer focused portal to give your organization a clear and quick overview of how to integrate with E-goi. The developer portal focuses on scenarios for integration and flow of events. We recommend familiarizing yourself with all of the content in the developer portal, before start using our rest API.   The E-goi  APIv3 is served over HTTPS. To ensure data privacy, unencrypted HTTP is not supported.  Request data is passed to the API by POSTing JSON objects to the API endpoints with the appropriate parameters.   BaseURL = api.egoiapp.com  # HTTP Methods for RESTful Services This API supports 5 HTTP methods:  * <b>GET</b>: The HTTP GET method is used to **read** (or retrieve) a representation of a resource. * <b>POST</b>: The POST verb is most-often utilized to **create** new resources. * <b>PATCH</b>: PATCH is used for **modify** capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource * <b>PUT</b>: PUT is most-often utilized for **update** capabilities, PUT-ing to a known resource URI with the request body containing the newly-updated representation of the original resource. * <b>DELETE</b>: DELETE is pretty easy to understand. It is used to **delete** a resource identified by a URI.  # Authentication   We use a custom authentication method, you will need a apikey that you can find in your account settings. Below you will see a curl example to get your account information:  #!/bin/bash  curl -X GET 'https://api.egoiapp.com/my-account' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>'  Here you can see a curl Post example with authentication:  #!/bin/bash  curl -X POST 'http://api.egoiapp.com/tags' \\  -H 'accept: application/json' \\  -H 'Apikey: <YOUR_APY_KEY>' \\  -H 'Content-Type: application/json' \\  -d '{`name`:`Your custom tag`,`color`:`#FFFFFF`}'  <security-definitions/>  # noqa: E501

    The version of the OpenAPI document: 3.0.0-beta
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from egoi-api.configuration import Configuration


class Product(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'product_identifier': 'str',
        'catalog_id': 'int',
        'name': 'str',
        'description': 'str',
        'sku': 'str',
        'upc': 'str',
        'ean': 'str',
        'gtin': 'str',
        'mpn': 'str',
        'link': 'str',
        'image_link': 'str',
        'price': 'float',
        'sale_price': 'float',
        'brand': 'str',
        'categories': 'list[str]',
        'related_products': 'list[str]'
    }

    attribute_map = {
        'product_identifier': 'product_identifier',
        'catalog_id': 'catalog_id',
        'name': 'name',
        'description': 'description',
        'sku': 'sku',
        'upc': 'upc',
        'ean': 'ean',
        'gtin': 'gtin',
        'mpn': 'mpn',
        'link': 'link',
        'image_link': 'image_link',
        'price': 'price',
        'sale_price': 'sale_price',
        'brand': 'brand',
        'categories': 'categories',
        'related_products': 'related_products'
    }

    def __init__(self, product_identifier=None, catalog_id=None, name=None, description=None, sku=None, upc=None, ean=None, gtin=None, mpn=None, link=None, image_link=None, price=None, sale_price=None, brand=None, categories=None, related_products=None, local_vars_configuration=None):  # noqa: E501
        """Product - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._product_identifier = None
        self._catalog_id = None
        self._name = None
        self._description = None
        self._sku = None
        self._upc = None
        self._ean = None
        self._gtin = None
        self._mpn = None
        self._link = None
        self._image_link = None
        self._price = None
        self._sale_price = None
        self._brand = None
        self._categories = None
        self._related_products = None
        self.discriminator = None

        if product_identifier is not None:
            self.product_identifier = product_identifier
        if catalog_id is not None:
            self.catalog_id = catalog_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if sku is not None:
            self.sku = sku
        if upc is not None:
            self.upc = upc
        if ean is not None:
            self.ean = ean
        if gtin is not None:
            self.gtin = gtin
        if mpn is not None:
            self.mpn = mpn
        if link is not None:
            self.link = link
        if image_link is not None:
            self.image_link = image_link
        if price is not None:
            self.price = price
        if sale_price is not None:
            self.sale_price = sale_price
        if brand is not None:
            self.brand = brand
        if categories is not None:
            self.categories = categories
        if related_products is not None:
            self.related_products = related_products

    @property
    def product_identifier(self):
        """Gets the product_identifier of this Product.  # noqa: E501

        The ID of the product in your store  # noqa: E501

        :return: The product_identifier of this Product.  # noqa: E501
        :rtype: str
        """
        return self._product_identifier

    @product_identifier.setter
    def product_identifier(self, product_identifier):
        """Sets the product_identifier of this Product.

        The ID of the product in your store  # noqa: E501

        :param product_identifier: The product_identifier of this Product.  # noqa: E501
        :type: str
        """

        self._product_identifier = product_identifier

    @property
    def catalog_id(self):
        """Gets the catalog_id of this Product.  # noqa: E501


        :return: The catalog_id of this Product.  # noqa: E501
        :rtype: int
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """Sets the catalog_id of this Product.


        :param catalog_id: The catalog_id of this Product.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                catalog_id is not None and catalog_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `catalog_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._catalog_id = catalog_id

    @property
    def name(self):
        """Gets the name of this Product.  # noqa: E501

        Name of the product  # noqa: E501

        :return: The name of this Product.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Product.

        Name of the product  # noqa: E501

        :param name: The name of this Product.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Product.  # noqa: E501

        Description of the product  # noqa: E501

        :return: The description of this Product.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Product.

        Description of the product  # noqa: E501

        :param description: The description of this Product.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def sku(self):
        """Gets the sku of this Product.  # noqa: E501

        Stock Keeping Unit  # noqa: E501

        :return: The sku of this Product.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this Product.

        Stock Keeping Unit  # noqa: E501

        :param sku: The sku of this Product.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def upc(self):
        """Gets the upc of this Product.  # noqa: E501

        Universal Product Code  # noqa: E501

        :return: The upc of this Product.  # noqa: E501
        :rtype: str
        """
        return self._upc

    @upc.setter
    def upc(self, upc):
        """Sets the upc of this Product.

        Universal Product Code  # noqa: E501

        :param upc: The upc of this Product.  # noqa: E501
        :type: str
        """

        self._upc = upc

    @property
    def ean(self):
        """Gets the ean of this Product.  # noqa: E501

        European Article Numbering  # noqa: E501

        :return: The ean of this Product.  # noqa: E501
        :rtype: str
        """
        return self._ean

    @ean.setter
    def ean(self, ean):
        """Sets the ean of this Product.

        European Article Numbering  # noqa: E501

        :param ean: The ean of this Product.  # noqa: E501
        :type: str
        """

        self._ean = ean

    @property
    def gtin(self):
        """Gets the gtin of this Product.  # noqa: E501

        Global Trade Item Number  # noqa: E501

        :return: The gtin of this Product.  # noqa: E501
        :rtype: str
        """
        return self._gtin

    @gtin.setter
    def gtin(self, gtin):
        """Sets the gtin of this Product.

        Global Trade Item Number  # noqa: E501

        :param gtin: The gtin of this Product.  # noqa: E501
        :type: str
        """

        self._gtin = gtin

    @property
    def mpn(self):
        """Gets the mpn of this Product.  # noqa: E501

        Manufacturer Part Number  # noqa: E501

        :return: The mpn of this Product.  # noqa: E501
        :rtype: str
        """
        return self._mpn

    @mpn.setter
    def mpn(self, mpn):
        """Sets the mpn of this Product.

        Manufacturer Part Number  # noqa: E501

        :param mpn: The mpn of this Product.  # noqa: E501
        :type: str
        """

        self._mpn = mpn

    @property
    def link(self):
        """Gets the link of this Product.  # noqa: E501

        Link for the product  # noqa: E501

        :return: The link of this Product.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this Product.

        Link for the product  # noqa: E501

        :param link: The link of this Product.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def image_link(self):
        """Gets the image_link of this Product.  # noqa: E501

        Link for the product image  # noqa: E501

        :return: The image_link of this Product.  # noqa: E501
        :rtype: str
        """
        return self._image_link

    @image_link.setter
    def image_link(self, image_link):
        """Sets the image_link of this Product.

        Link for the product image  # noqa: E501

        :param image_link: The image_link of this Product.  # noqa: E501
        :type: str
        """

        self._image_link = image_link

    @property
    def price(self):
        """Gets the price of this Product.  # noqa: E501

        Price of the product  # noqa: E501

        :return: The price of this Product.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Product.

        Price of the product  # noqa: E501

        :param price: The price of this Product.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def sale_price(self):
        """Gets the sale_price of this Product.  # noqa: E501

        Sale price of the product  # noqa: E501

        :return: The sale_price of this Product.  # noqa: E501
        :rtype: float
        """
        return self._sale_price

    @sale_price.setter
    def sale_price(self, sale_price):
        """Sets the sale_price of this Product.

        Sale price of the product  # noqa: E501

        :param sale_price: The sale_price of this Product.  # noqa: E501
        :type: float
        """

        self._sale_price = sale_price

    @property
    def brand(self):
        """Gets the brand of this Product.  # noqa: E501

        Brand of the product  # noqa: E501

        :return: The brand of this Product.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this Product.

        Brand of the product  # noqa: E501

        :param brand: The brand of this Product.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def categories(self):
        """Gets the categories of this Product.  # noqa: E501

        Array of product categories, using the character '>' as delimiter for the breadcrumb                                 syntax  # noqa: E501

        :return: The categories of this Product.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this Product.

        Array of product categories, using the character '>' as delimiter for the breadcrumb                                 syntax  # noqa: E501

        :param categories: The categories of this Product.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

    @property
    def related_products(self):
        """Gets the related_products of this Product.  # noqa: E501

        Related products  # noqa: E501

        :return: The related_products of this Product.  # noqa: E501
        :rtype: list[str]
        """
        return self._related_products

    @related_products.setter
    def related_products(self, related_products):
        """Sets the related_products of this Product.

        Related products  # noqa: E501

        :param related_products: The related_products of this Product.  # noqa: E501
        :type: list[str]
        """

        self._related_products = related_products

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Product):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Product):
            return True

        return self.to_dict() != other.to_dict()
