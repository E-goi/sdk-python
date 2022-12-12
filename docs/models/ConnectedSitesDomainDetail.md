# egoi_api.model.connected_sites_domain_detail.ConnectedSitesDomainDetail

Domain detail schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Domain detail schema | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**domain** | str,  | str,  | Domain | [optional] 
**list_id** | str,  | str,  | List id | [optional] 
**code** | str,  | str,  | Connected Sites Tracking Code | [optional] 
**[features](#features)** | list, tuple,  | tuple,  | Available features | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# features

Available features

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Available features | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ConnectedSitesProducts**](ConnectedSitesProducts.md) | [**ConnectedSitesProducts**](ConnectedSitesProducts.md) | [**ConnectedSitesProducts**](ConnectedSitesProducts.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

