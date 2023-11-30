# swagger_client.ActivitiesApi

All URIs are relative to *https://api.height.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_activities**](ActivitiesApi.md#list_activities) | **GET** /activities | List activities and messages
[**post_message**](ActivitiesApi.md#post_message) | **POST** /activities | Post a message

# **list_activities**
> ListActivitiesResponse list_activities(task_id=task_id)

List activities and messages

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ActivitiesApi(swagger_client.ApiClient(configuration))
task_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Either the task unique `id` (UUID), or the task unique `index` (the 123 of T-123). (optional)

try:
    # List activities and messages
    api_response = api_instance.list_activities(task_id=task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->list_activities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | [**str**](.md)| Either the task unique &#x60;id&#x60; (UUID), or the task unique &#x60;index&#x60; (the 123 of T-123). | [optional] 

### Return type

[**ListActivitiesResponse**](ListActivitiesResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_message**
> ActivityObject post_message(body)

Post a message

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ActivitiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.PostMessageRequest() # PostMessageRequest | 

try:
    # Post a message
    api_response = api_instance.post_message(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->post_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostMessageRequest**](PostMessageRequest.md)|  | 

### Return type

[**ActivityObject**](ActivityObject.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

