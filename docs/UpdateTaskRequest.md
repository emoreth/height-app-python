# UpdateTaskRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**list_ids** | **list[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **str** | The status of the task. - &#x60;backLog&#x60; - &#x60;inProgress&#x60; - &#x60;done&#x60; - and any *UUID* of available statuses. You can find the *UUIDs* through the field template API. | [optional] 
**assignees_ids** | **list[str]** |  | [optional] 
**parent_task_id** | **str** |  | [optional] 
**fields** | [**list[TaskObjectFields]**](TaskObjectFields.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

