# FieldTemplateObjectLabels

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | UUID or string (backLog, inProgress and done are hard-coded). | 
**model** | **str** | The model is always &#x60;fieldLabel&#x60;. | 
**value** | **str** | The name of the label. | 
**hue** | **float** | The hue of the label&#x27;s color (between 0 and 360). | 
**label_set_id** | **str** | The id of the label set this label belongs to, if any. Only if the type of field template is &#x60;status&#x60;. | [optional] 
**status_state** | **str** | The state of the status, only available when the type of the field template is &#x60;status&#x60;. Note that a task is considered as completed if its status has a state of &#x60;canceled&#x60; or &#x60;completed&#x60;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

