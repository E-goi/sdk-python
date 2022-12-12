# egoi_api.model.unsubscription_object.UnsubscriptionObject

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**unsubscription_method** | str,  | str,  | Unsubcription Method | [optional] must be one of ["manual", "form", "unsubscribe_link", "bounce", "api", ] 
**unsubscription_reason** | str,  | str,  | Unsubcription Reason | [optional] must be one of ["not_interested", "lack_of_time", "email_address_change", "spam", "other", ] 
**unsubscription_observation** | str,  | str,  | Unsubcription Observation | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

