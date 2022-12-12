# egoi_api.model.import_bulk_file_request_schema.ImportBulkFileRequestSchema

Contact import bulk request schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Contact import bulk request schema | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mode** | str,  | str,  | Add new contacts only (&#x27;add&#x27;) or add and replace existing ones (&#x27;update&#x27;) | must be one of ["add", "update", ] 
**[file](#file)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | File to import | 
**compare_field** | str,  | str,  | Field ID which will be mapped for comparison to prevent duplicates) | 
**force_empty** | bool,  | BoolClass,  | If &#x27;true&#x27; accepts empty values and erases those fields | [optional] if omitted the server will use the default value of False
**[notify](#notify)** | list, tuple,  | tuple,  | Array of IDs of the users to notify | [optional] 
**callback_url** | str,  | str,  | Url to receive the report | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# file

File to import

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | File to import | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ContactBulkFile](ContactBulkFile.md) | [**ContactBulkFile**](ContactBulkFile.md) | [**ContactBulkFile**](ContactBulkFile.md) |  | 

# notify

Array of IDs of the users to notify

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of IDs of the users to notify | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

