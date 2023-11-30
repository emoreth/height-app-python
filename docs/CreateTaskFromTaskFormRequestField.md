# CreateTaskFromTaskFormRequestField

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_template_id** | **str** | The id of the appropriate field template | 
**value** | **str** | For text fields: the text value of the field. For select fields: the id of the selected option | [optional] 
**_date** | **datetime** | For date fields: the date value of the field | [optional] 
**labels** | **list[str]** | For labels fields: the labels of the field | [optional] 
**linked_tasks** | [**list[TaskObjectLinkedTasks]**](TaskObjectLinkedTasks.md) | For linkedTasks fields: the tasks to be linked, in the format: { \&quot;id\&quot;: \&quot;UUID\&quot;, \&quot;index\&quot;: number } | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

