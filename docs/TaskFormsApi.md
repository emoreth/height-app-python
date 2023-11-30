# swagger_client.TaskFormsApi

All URIs are relative to *https://api.height.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task_from_task_form**](TaskFormsApi.md#create_task_from_task_form) | **POST** /taskForms/{id}/answers | Create a task from a public task form
[**get_task_form**](TaskFormsApi.md#get_task_form) | **GET** /taskForms/{urlKey} | Get a task form

# **create_task_from_task_form**
> TaskObject create_task_from_task_form(body, id, as_bot=as_bot)

Create a task from a public task form

Task forms have a set number of questions, so it is impossible to set some attributes for a task using this endpoint

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
api_instance = swagger_client.TaskFormsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateTaskFromTaskFormRequest() # CreateTaskFromTaskFormRequest | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | task form id
as_bot = true # bool | Only allowed for public task forms, and required if not authenticated (optional)

try:
    # Create a task from a public task form
    api_response = api_instance.create_task_from_task_form(body, id, as_bot=as_bot)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskFormsApi->create_task_from_task_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTaskFromTaskFormRequest**](CreateTaskFromTaskFormRequest.md)|  | 
 **id** | [**str**](.md)| task form id | 
 **as_bot** | **bool**| Only allowed for public task forms, and required if not authenticated | [optional] 

### Return type

[**TaskObject**](TaskObject.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_form**
> TaskFormObject get_task_form(url_key, key_type=key_type, include=include, archived=archived, draft=draft)

Get a task form

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
api_instance = swagger_client.TaskFormsApi(swagger_client.ApiClient(configuration))
url_key = 'url_key_example' # str | 
key_type = 'key_type_example' # str | One of key or urlKey, defaulting to id (optional)
include = ['include_example'] # list[str] | Array of task form includes (optional)
archived = true # bool |  (optional)
draft = true # bool |  (optional)

try:
    # Get a task form
    api_response = api_instance.get_task_form(url_key, key_type=key_type, include=include, archived=archived, draft=draft)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskFormsApi->get_task_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_key** | **str**|  | 
 **key_type** | **str**| One of key or urlKey, defaulting to id | [optional] 
 **include** | [**list[str]**](str.md)| Array of task form includes | [optional] 
 **archived** | **bool**|  | [optional] 
 **draft** | **bool**|  | [optional] 

### Return type

[**TaskFormObject**](TaskFormObject.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

