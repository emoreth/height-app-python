# TaskFormObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the task form. | [optional] 
**model** | **str** | always \&quot;taskForm\&quot; | [optional] 
**version** | **int** | The version of the task form. | [optional] 
**key** | **str** | The key of the task form. | [optional] 
**url_key** | **str** | The URL key of the task form. | [optional] 
**url** | **str** | The URL of the task form. | [optional] 
**name** | **str** | The name of the task form. | [optional] 
**task_form_description** | **str** | The description of the task form. | [optional] 
**disabled_reason** | **str** | The reason why the task form is disabled. | [optional] 
**archived** | **bool** | Flag to indicate whether the task form is archived. | [optional] 
**draft** | **bool** | Flag to indicate whether the task form is a draft. | [optional] 
**public_access** | **str** | The type of public access for the task form. | [optional] 
**list_ids** | **list[str]** | The IDs of the lists associated with the task form. | [optional] 
**parent_task_id** | **str** | The ID of the parent task. | [optional] 
**status** | **str** | The status of the task. - &#x60;backLog&#x60; - &#x60;inProgress&#x60; - &#x60;done&#x60; - and any *UUID* of available statuses. You can find the *UUIDs* through the field template API. | [optional] 
**questions** | [**list[TaskFormObjectQuestions]**](TaskFormObjectQuestions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

