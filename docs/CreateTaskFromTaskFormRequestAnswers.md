# CreateTaskFromTaskFormRequestAnswers

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question_id** | **str** | The id of the task form question | [optional] 
**name** | **str** | The name of the task - required when the question is for the task name | [optional] 
**status** | **str** | The id of the status of the task - required when the question is for the task status | [optional] 
**assignees_ids** | **list[str]** | The ids of the assignees of the task - required when the question is for the task assignees. | [optional] 
**list_ids** | **list[str]** | The ids of the lists of the task - required when the question is for the lists | [optional] 
**description** | **str** | The description of the string. Accepts markdown. Required when the question is for the description | [optional] 
**field** | [**CreateTaskFromTaskFormRequestField**](CreateTaskFromTaskFormRequestField.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

