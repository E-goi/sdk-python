# egoi_api.model.header_footer.HeaderFooter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | [**QueryId**](QueryId.md) | [**QueryId**](QueryId.md) |  | [optional] 
**[header_links](#header_links)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Ignored if provided ID is from a custom template | [optional] 
**[footer_links](#footer_links)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Ignored if provided ID is from a custom template | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# header_links

Ignored if provided ID is from a custom template

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Ignored if provided ID is from a custom template | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**forward** | bool,  | BoolClass,  | Use view forward header link | [optional] if omitted the server will use the default value of False
**view_web** | bool,  | BoolClass,  | Use view view in web header link | [optional] if omitted the server will use the default value of False
**unsubscribe** | bool,  | BoolClass,  | Use view unsubscribe header link | [optional] if omitted the server will use the default value of False
**edit** | bool,  | BoolClass,  | Use view edit header link | [optional] if omitted the server will use the default value of False
**social_share** | bool,  | BoolClass,  | Use view social share header link | [optional] if omitted the server will use the default value of False
**facebook_share** | bool,  | BoolClass,  | Use view facebook share header link | [optional] if omitted the server will use the default value of False
**twitter_share** | bool,  | BoolClass,  | Use view twitter share header link | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# footer_links

Ignored if provided ID is from a custom template

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Ignored if provided ID is from a custom template | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**forward** | bool,  | BoolClass,  | Use view forward footer link | [optional] if omitted the server will use the default value of False
**view_web** | bool,  | BoolClass,  | Use view view in web footer link | [optional] if omitted the server will use the default value of False
**unsubscribe** | bool,  | BoolClass,  | Use view unsubscribe footer link | [optional] if omitted the server will use the default value of False
**edit** | bool,  | BoolClass,  | Use view edit footer link | [optional] if omitted the server will use the default value of False
**social_share** | bool,  | BoolClass,  | Use view social share footer link | [optional] if omitted the server will use the default value of False
**facebook_share** | bool,  | BoolClass,  | Use view facebook share footer link | [optional] if omitted the server will use the default value of False
**twitter_share** | bool,  | BoolClass,  | Use view twitter share footer link | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

