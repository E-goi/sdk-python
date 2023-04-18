# egoi_api.model.contact_export_request.ContactExportRequest

Contact export request schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Contact export request schema | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**format** | str,  | str,  | File extension to export contacts | must be one of ["csv", "xml", ] 
**callback_url** | str,  | str,  | Url to receive the callback &lt;a href&#x3D;&#x27;/usecases/callbacks/#exports-a-list-of-contacts&#x27; target&#x3D;&#x27;_blank&#x27;&gt;[Go to callback documentation]&lt;/a&gt; | [optional] 
**[segments](#segments)** | list, tuple,  | tuple,  | Array of segment IDs to filter contacts to export. ***Note:*** segments of type ***auto*** and  ***tag*** are not yet supported but they are expected to be supported soon! | [optional] 
**[fields](#fields)** | list, tuple,  | tuple,  | Array of field IDs to be displayed in the exported file | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# segments

Array of segment IDs to filter contacts to export. ***Note:*** segments of type ***auto*** and  ***tag*** are not yet supported but they are expected to be supported soon!

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of segment IDs to filter contacts to export. ***Note:*** segments of type ***auto*** and  ***tag*** are not yet supported but they are expected to be supported soon! | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# fields

Array of field IDs to be displayed in the exported file

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of field IDs to be displayed in the exported file | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

