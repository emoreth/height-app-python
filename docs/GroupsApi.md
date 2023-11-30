# swagger_client.GroupsApi

All URIs are relative to *https://api.height.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_groups**](GroupsApi.md#get_all_groups) | **GET** /groups | Get all groups

# **get_all_groups**
> ListAllGroupsResponse get_all_groups()

Get all groups

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))

try:
    # Get all groups
    api_response = api_instance.get_all_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_all_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListAllGroupsResponse**](ListAllGroupsResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

