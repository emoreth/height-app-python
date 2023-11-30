# swagger_client.TasksApi

All URIs are relative to *https://api.height.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task**](TasksApi.md#create_task) | **POST** /tasks | Create a task
[**get_task**](TasksApi.md#get_task) | **GET** /tasks/{id} | Get a task
[**move_tasks**](TasksApi.md#move_tasks) | **PUT** /tasks/move | Move tasks
[**patch_tasks**](TasksApi.md#patch_tasks) | **PATCH** /tasks | Patch multiples tasks
[**search_tasks**](TasksApi.md#search_tasks) | **GET** /tasks | Search tasks
[**update_task**](TasksApi.md#update_task) | **PATCH** /tasks/{id} | Update a single task

# **create_task**
> TaskObject create_task(body, realtime=realtime, notify_users=notify_users)

Create a task

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
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateTaskRequest() # CreateTaskRequest | 
realtime = true # bool | (defaults to true) - use false when migrating tasks (optional)
notify_users = true # bool | (defaults to true) - use false when migrating tasks (optional)

try:
    # Create a task
    api_response = api_instance.create_task(body, realtime=realtime, notify_users=notify_users)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTaskRequest**](CreateTaskRequest.md)|  | 
 **realtime** | **bool**| (defaults to true) - use false when migrating tasks | [optional] 
 **notify_users** | **bool**| (defaults to true) - use false when migrating tasks | [optional] 

### Return type

[**TaskObject**](TaskObject.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> TaskObject get_task(id, include=include)

Get a task

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
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | task index (number) or task id (UUID)
include = 'include_example' # str | What you wish to include with the task. (optional)

try:
    # Get a task
    api_response = api_instance.get_task(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| task index (number) or task id (UUID) | 
 **include** | **str**| What you wish to include with the task. | [optional] 

### Return type

[**TaskObject**](TaskObject.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_tasks**
> move_tasks(body)

Move tasks

Not working. https://www.notion.so/Move-tasks-0e612add3e09400bacc6119c8129fa67

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
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
body = swagger_client.MoveTasksRequest() # MoveTasksRequest | 

try:
    # Move tasks
    api_instance.move_tasks(body)
except ApiException as e:
    print("Exception when calling TasksApi->move_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoveTasksRequest**](MoveTasksRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_tasks**
> list[PatchTasksResponse] patch_tasks(body)

Patch multiples tasks

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
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
body = swagger_client.PatchTasksRequest() # PatchTasksRequest | 

try:
    # Patch multiples tasks
    api_response = api_instance.patch_tasks(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->patch_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PatchTasksRequest**](PatchTasksRequest.md)|  | 

### Return type

[**list[PatchTasksResponse]**](PatchTasksResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_tasks**
> SearchTasksResponse search_tasks(filters=filters)

Search tasks

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
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
filters = 'filters_example' # str | JSON object with filters (optional)

try:
    # Search tasks
    api_response = api_instance.search_tasks(filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->search_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| JSON object with filters | [optional] 

### Return type

[**SearchTasksResponse**](SearchTasksResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task**
> TaskObject update_task(body, id)

Update a single task

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
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateTaskRequest() # UpdateTaskRequest | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | task index (number) or task id (UUID)

try:
    # Update a single task
    api_response = api_instance.update_task(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->update_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateTaskRequest**](UpdateTaskRequest.md)|  | 
 **id** | [**str**](.md)| task index (number) or task id (UUID) | 

### Return type

[**TaskObject**](TaskObject.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

