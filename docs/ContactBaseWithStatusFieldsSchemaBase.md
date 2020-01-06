# ContactBaseWithStatusFieldsSchemaBase

Contact base fields
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **str** |  | [optional] [readonly] 
**status** | **str** | Status of the contact | [optional] [default to 'active']
**consent** | **str** | Contact consent | [optional] 
**first_name** | **str** | First name of the contact | [optional] 
**last_name** | **str** | Last name of the contact | [optional] 
**birth_date** | **date** | Birth date of the contact | [optional] 
**language** | [**Language**](Language.md) |  | [optional] 
**email** | **str** | Email of the contact | [optional] 
**email_status** | **str** | Email channel status | [optional] 
**cellphone** | **str** | Cellphone of the contact | [optional] 
**cellphone_status** | **str** | Cellphone channel status | [optional] 
**phone** | **str** | Phone of the contact | [optional] 
**phone_status** | **str** | Phone channel status | [optional] 
**push_token_android** | [**list[ContactBaseWithStatusFieldsSchemaBasePushTokenAndroid]**](ContactBaseWithStatusFieldsSchemaBasePushTokenAndroid.md) | Android push token of the contact | [optional] 
**push_token_ios** | [**list[ContactBaseWithStatusFieldsSchemaBasePushTokenIos]**](ContactBaseWithStatusFieldsSchemaBasePushTokenIos.md) | IOS push token of the contact | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


