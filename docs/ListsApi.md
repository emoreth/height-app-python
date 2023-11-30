# swagger_client.ListsApi

All URIs are relative to *https://api.height.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_list**](ListsApi.md#create_list) | **POST** /lists | Create a list
[**list_all_lists**](ListsApi.md#list_all_lists) | **GET** /lists | List all lists
[**update_list**](ListsApi.md#update_list) | **PUT** /lists/{id} | Update a list

# **create_list**
> ListObject create_list(body)

Create a list

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
api_instance = swagger_client.ListsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateListRequest() # CreateListRequest | 

try:
    # Create a list
    api_response = api_instance.create_list(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListsApi->create_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateListRequest**](CreateListRequest.md)|  | 

### Return type

[**ListObject**](ListObject.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_lists**
> list[ListAllResponse] list_all_lists()

List all lists

Use this endpoint to retrieve all the lists of the workspace. Only lists shared with the entire workspace will be returned.

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
api_instance = swagger_client.ListsApi(swagger_client.ApiClient(configuration))

try:
    # List all lists
    api_response = api_instance.list_all_lists()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListsApi->list_all_lists: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ListAllResponse]**](ListAllResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_list**
> ListObject update_list(body, id)

Update a list

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
api_instance = swagger_client.ListsApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateListRequest() # UpdateListRequest | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique id of the list (UUIDv4)

try:
    # Update a list
    api_response = api_instance.update_list(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ListsApi->update_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateListRequest**](UpdateListRequest.md)|  | 
 **id** | [**str**](.md)| The unique id of the list (UUIDv4) | 

### Return type

[**ListObject**](ListObject.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

