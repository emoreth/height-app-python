# ActivityObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the activity. | 
**model** | **str** | The model is always &#x60;activity&#x60;. | 
**created_at** | **datetime** | The date when the activity was created. See [Date formats](https://www.notion.so/API-documentation-643aea5bf01742de9232e5971cb4afda). | 
**task_id** | **str** | The task id of the task this activity is linked to. | 
**created_user_id** | **str** | The user id that posted that activity. | 
**type** | **str** | The type of the activity. | 
**message** | **str** | The message/body of this comment/description. | [optional] 
**old_value** | **str** | For updates, this is the value before the change. | [optional] 
**new_value** | **str** | For status, this is the value after the change. | [optional] 
**reactjis** | [**list[ActivityObjectReactjis]**](ActivityObjectReactjis.md) | An array of reactjis. | 
**read_user_ids** | **list[str]** | The user ids that read this activity. | 
**url** | **str** | The url of the activity. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

