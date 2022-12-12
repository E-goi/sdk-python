# egoi_api.model.complex_contact.ComplexContact

Complex contact schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Complex contact schema | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[all_of_0](#all_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[Contact](Contact.md) | [**Contact**](Contact.md) | [**Contact**](Contact.md) |  | 

# all_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[email_stats](#email_stats)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Email stats of the contact | [optional] 
**[sms_stats](#sms_stats)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | SMS stats of the contact | [optional] 
**[push_stats](#push_stats)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Push stats of the contact | [optional] 
**[webpush_stats](#webpush_stats)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Webpush stats of the contact | [optional] 
**[voice_stats](#voice_stats)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Voice stats of the contact | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# email_stats

Email stats of the contact

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Email stats of the contact | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sent** | decimal.Decimal, int,  | decimal.Decimal,  | Emails sent to the contact | [optional] 
**opens** | decimal.Decimal, int,  | decimal.Decimal,  | Emails opened by the contact | [optional] 
**clicks** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of clicks made by the contact | [optional] 
**soft_bounces** | decimal.Decimal, int,  | decimal.Decimal,  | Soft bounces for the contact | [optional] 
**hard_bounces** | decimal.Decimal, int,  | decimal.Decimal,  | Hard bounces for the contact | [optional] 
**forwards** | decimal.Decimal, int,  | decimal.Decimal,  | Emails forwarded by the contact | [optional] 
**conversions** | decimal.Decimal, int,  | decimal.Decimal,  | Total of conversions | [optional] 
**social_actions** | decimal.Decimal, int,  | decimal.Decimal,  | Total of social actions for the contact | [optional] 
**last_send_date** | None, str, datetime,  | NoneClass, str,  | Date of the last email sent to the contact | [optional] value must conform to RFC-3339 date-time
**last_open_date** | None, str, datetime,  | NoneClass, str,  | Date of the last email open of the contact | [optional] value must conform to RFC-3339 date-time
**last_click_date** | None, str, datetime,  | NoneClass, str,  | Date of the last email click of the contact | [optional] value must conform to RFC-3339 date-time
**last_open_country** | None, str,  | NoneClass, str,  | Country where the last email for that contact was opened | [optional] 
**last_open_region** | None, str,  | NoneClass, str,  | Region where the last email for that contact was opened | [optional] 
**last_open_city** | None, str,  | NoneClass, str,  | City where the last email for that contact was opened | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sms_stats

SMS stats of the contact

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | SMS stats of the contact | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sent** | decimal.Decimal, int,  | decimal.Decimal,  | SMS sent to the contact | [optional] 
**delivered** | decimal.Decimal, int,  | decimal.Decimal,  | SMS delivered to the contact | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# push_stats

Push stats of the contact

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Push stats of the contact | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sent** | decimal.Decimal, int,  | decimal.Decimal,  | Push messages sent to the contact | [optional] 
**delivered** | decimal.Decimal, int,  | decimal.Decimal,  | Push messages delivered to the contact | [optional] 
**not_delivered** | decimal.Decimal, int,  | decimal.Decimal,  | Push messages that were not delivered to the contact | [optional] 
**views** | decimal.Decimal, int,  | decimal.Decimal,  | Push messages that were viewed by the contact | [optional] 
**clicks** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of clicks made by the contact | [optional] 
**last_view_date** | None, str, datetime,  | NoneClass, str,  | Date of the last push message view of the contact | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# webpush_stats

Webpush stats of the contact

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Webpush stats of the contact | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sent** | decimal.Decimal, int,  | decimal.Decimal,  | Webpush messages sent to the contact | [optional] 
**delivered** | decimal.Decimal, int,  | decimal.Decimal,  | Webpush messages delivered to the contact | [optional] 
**clicks** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of clicks made by the contact | [optional] 
**bounces** | decimal.Decimal, int,  | decimal.Decimal,  | Bounces for the contact | [optional] 
**last_send_date** | str, datetime,  | str,  | Date of the last webpush message sent to the contact | [optional] value must conform to RFC-3339 date-time
**last_delivery_date** | str, datetime,  | str,  | Date of the last webpush message delivered to the contact | [optional] value must conform to RFC-3339 date-time
**last_click_date** | str, datetime,  | str,  | Date of the last webpush message clicked by the contact | [optional] value must conform to RFC-3339 date-time
**last_bounce_date** | str, datetime,  | str,  | Date of the last webpush bounce for the contact | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# voice_stats

Voice stats of the contact

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Voice stats of the contact | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sent** | decimal.Decimal, int,  | decimal.Decimal,  | Voice campaigns sent to the contact | [optional] 
**answered** | decimal.Decimal, int,  | decimal.Decimal,  | Voice campaigns answered by the contact | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

