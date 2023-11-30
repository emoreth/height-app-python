# TaskObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the task | 
**model** | **str** | The model is always &#x60;task&#x60; | 
**index** | **float** | The task index. For example, if the task is T-123, its index is 123. | 
**list_ids** | **list[str]** | Tasks belong to one or more lists. To create tasks, it&#x27;s necessary to know in which list you want to create them. | 
**name** | **str** | The name of the task. | 
**description** | **str** | The description of the task. It&#x27;s only retrieved if you use include. See [&#x27;Get a task&#x27;](https://www.notion.so/Get-a-task-8afda1c08e7f4f07a5c53720710cf24e). | 
**status** | **str** | The status of the task. - &#x60;backLog&#x60; - &#x60;inProgress&#x60; - &#x60;done&#x60; - and any *UUID* of available statuses. You can find the *UUIDs* through the field template API. | 
**assignees_ids** | **list[str]** | The assignees of the task. You can find the UUIDs of users through the users API.  [&#x27;List all users&#x27;](https://www.notion.so/List-all-users-ea66d04e48534b32927903c4deee58e8) | 
**fields** | [**list[TaskObjectFields]**](TaskObjectFields.md) |  | 
**deleted** | **bool** | If the task was deleted. | 
**deleted_at** | **datetime** | The date at which the task was deleted. | [optional] 
**deleted_by_user_id** | **str** | The user that deleted the task. | [optional] 
**completed** | **bool** | If the status is considered as completed (i.e. &#x60;done&#x60;), the value will be &#x60;true&#x60;. | 
**completed_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**created_user_id** | **str** | The user that created the task. | 
**last_activity_at** | **datetime** |  | 
**url** | **str** | The URL of the task. | 
**trashed_at** | **datetime** | A timestamp when the task was moved to the trash. Tasks are deleted after 30 days in the trash. This will be null unless the task is currently in the trash or deleted. | [optional] 
**trashed_by_user_id** | **str** | The id of the user that moved the task to the trash | [optional] 
**parent_task_id** | **str** | If the task is a subtask of another task, &#x60;parentTaskId&#x60; will be the id of the parent task. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

