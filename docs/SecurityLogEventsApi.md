# swagger_client.SecurityLogEventsApi

All URIs are relative to *https://api.height.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_security_log_events**](SecurityLogEventsApi.md#list_security_log_events) | **GET** /securityLogEvents | List all security log event objects

# **list_security_log_events**
> ListAllSecurityLogEventsResponse list_security_log_events()

List all security log event objects

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
api_instance = swagger_client.SecurityLogEventsApi(swagger_client.ApiClient(configuration))

try:
    # List all security log event objects
    api_response = api_instance.list_security_log_events()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityLogEventsApi->list_security_log_events: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListAllSecurityLogEventsResponse**](ListAllSecurityLogEventsResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

