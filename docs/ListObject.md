# ListObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the list (UUIDv4) | 
**model** | **str** | The model is always &#x60;list&#x60; | 
**type** | **str** | - &#x60;list&#x60;: a list that contains tasks. You can only create tasks in this type of list directly. - &#x60;smartlist&#x60;: a smart list use filters to find tasks across different lists - &#x60;user&#x60;: a special smart list that displays tasks assigned to a user - &#x60;inbox&#x60;: a special smart list to display recent conversations - &#x60;search&#x60;: a special smart list to search tasks | 
**key** | **str** | The unique key of your list is used as their url.  If the key is &#x60;general&#x60;, the url will be: &#x60;https://your-workspace.height.app/general&#x60;  Keys need to respect these rules:  - valid characters are: lower-case letters, dashes and numbers - needs to start with a lower-case letter - key is unique across the workspace | 
**description** | **str** | The description of the list. It can be an empty string. | 
**url** | **str** | The url of the list. | 
**appearance** | [**ListObjectAppearance**](ListObjectAppearance.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

