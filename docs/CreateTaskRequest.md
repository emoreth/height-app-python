# CreateTaskRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**list_ids** | **list[str]** | An array of UUIDs (one or more) | 
**description** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**assignees_ids** | **list[str]** | An array of UUIDs of the users assigned to the task (optional). | [optional] 
**parent_task_id** | **str** | The UUID of the parent task (optional). | [optional] 
**fields** | [**list[TaskObjectFields]**](TaskObjectFields.md) |  | [optional] 
**order_intent** | [**CreateTaskRequestOrderIntent**](CreateTaskRequestOrderIntent.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

