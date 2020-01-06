# ContactInsideBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **str** |  | [optional] [readonly] 
**status** | **str** | Status of the contact | [optional] [default to 'active']
**consent** | **str** | Contact consent | [optional] [readonly] [default to 'consent']
**consent_date** | **datetime** | Date and hour of the contact consent | [optional] [readonly] 
**subscription_method** | **str** | Contact subscription method | [optional] [readonly] 
**subscription_date** | **datetime** | Date and hour of the contact subscription | [optional] [readonly] 
**subscription_form** | **int** | Contact subscription form | [optional] [readonly] 
**unsubscription_method** | **str** | Contact unsubscription method | [optional] [readonly] 
**unsubscription_reason** | **str** | Contact unsubscription reason | [optional] [readonly] 
**unsubscription_observation** | **str** | Contact unsubscription observation | [optional] [readonly] 
**unsubscription_date** | **datetime** | Contact unsubscription date | [optional] [readonly] 
**change_date** | **date** | Last modification date of the contact | [optional] [readonly] 
**first_name** | **str** | First name of the contact | [optional] 
**last_name** | **str** | Last name of the contact | [optional] 
**birth_date** | **date** | Birth date of the contact | [optional] 
**language** | [**Language**](Language.md) |  | [optional] 
**email** | **str** | Email of the contact | [optional] 
**email_status** | **str** | Email channel status | [optional] [readonly] [default to 'active']
**cellphone** | **str** | Cellphone of the contact | [optional] 
**cellphone_status** | **str** | Cellphone channel status | [optional] [readonly] [default to 'active']
**phone** | **str** | Phone of the contact | [optional] 
**phone_status** | **str** | Phone channel status | [optional] [readonly] [default to 'active']
**push_token_android** | [**list[ContactBaseWithStatusFieldsSchemaBasePushTokenAndroid]**](ContactBaseWithStatusFieldsSchemaBasePushTokenAndroid.md) | Android push token of the contact | [optional] 
**push_token_ios** | [**list[ContactBaseWithStatusFieldsSchemaBasePushTokenIos]**](ContactBaseWithStatusFieldsSchemaBasePushTokenIos.md) | IOS push token of the contact | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


