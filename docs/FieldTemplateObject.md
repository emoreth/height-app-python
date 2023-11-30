# FieldTemplateObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the field template. | 
**model** | **str** | The model is always &#x60;fieldTemplate&#x60;. | 
**name** | **str** | The name of the field template. | 
**type** | **str** | Possible types:  - &#x60;text&#x60;: any text value attribute (i.e. Story Points) - &#x60;labels&#x60;: used for tags for example - &#x60;select&#x60;: used for priority, sprint,â€¦ - &#x60;date&#x60;: used for due date,â€¦ - &#x60;linkedTasks&#x60;: usually used for dependencies and so on - &#x60;status&#x60;: the status attribute (only one field template of that type) | 
**label_sets** | [**list[FieldTemplateObjectLabelSets]**](FieldTemplateObjectLabelSets.md) | An array of label sets, only available when the type of the field template is &#x60;status&#x60;. | [optional] 
**labels** | [**list[FieldTemplateObjectLabels]**](FieldTemplateObjectLabels.md) | Only available when the type of the field template is &#x60;labels&#x60;, &#x60;select&#x60; or &#x60;status&#x60;. | [optional] 
**archive** | **bool** | This attribute has been archived. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

