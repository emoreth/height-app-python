# SecurityLogEventObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the event. | 
**model** | **str** | The model is always &#x60;securityLogEvent&#x60;. | 
**created_at** | **datetime** | The date and time the event occurred. See [Date formats](https://developers.notion.com/reference/rich-text#date-property-values). | 
**user_id** | **str** | The ID of the user that initiated the event. | 
**user_email** | **str** | The email of the user that initiated the event. | 
**event_type** | **str** | Possible values are:  - &#x60;FieldTemplateInsert&#x60;: an attribute was created - &#x60;FieldTemplateUpdate&#x60;: an attribute was updated - &#x60;FieldTemplateArchive&#x60;: an attribute was archived - &#x60;FieldTemplateRestore&#x60;: an attribute was restored - &#x60;PermissionUpsert&#x60;: a list permission was created or updated - &#x60;PermissionDelete&#x60;: a list permission was deleted - &#x60;UserInvite&#x60;: an user was invited - &#x60;UserSignUp&#x60;: an user signed up | 
**old_value** | **object** | The old value of the attribute, permission, etc. that was updated or deleted. | [optional] 
**new_value** | **object** | The new value of the attribute, permission, etc. that was updated or created. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

