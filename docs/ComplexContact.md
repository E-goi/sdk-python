# ComplexContact

Complex contact schema
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | [**ContactInsideBase**](ContactInsideBase.md) | Contact base fields | [optional] 
**extra** | [**list[ContactExtraFields]**](ContactExtraFields.md) | Array of the contact&#39;s extra fields | [optional] 
**tags** | **list[int]** | Array of tags for this contact | [optional] [readonly] 
**email_stats** | [**ComplexContactAllOfEmailStats**](ComplexContactAllOfEmailStats.md) |  | [optional] 
**sms_stats** | [**ComplexContactAllOfSmsStats**](ComplexContactAllOfSmsStats.md) |  | [optional] 
**push_stats** | [**ComplexContactAllOfPushStats**](ComplexContactAllOfPushStats.md) |  | [optional] 
**webpush_stats** | [**ComplexContactAllOfWebpushStats**](ComplexContactAllOfWebpushStats.md) |  | [optional] 
**voice_stats** | [**ComplexContactAllOfVoiceStats**](ComplexContactAllOfVoiceStats.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


