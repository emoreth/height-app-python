# swagger_client.WorkspaceApi

All URIs are relative to *https://api.height.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_workspace**](WorkspaceApi.md#retrieve_workspace) | **GET** /workspace | Retrieve the workspace

# **retrieve_workspace**
> WorkspaceObject retrieve_workspace()

Retrieve the workspace

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
api_instance = swagger_client.WorkspaceApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve the workspace
    api_response = api_instance.retrieve_workspace()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspaceApi->retrieve_workspace: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WorkspaceObject**](WorkspaceObject.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

