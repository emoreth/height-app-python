# swagger_client.FieldTemplatesApi

All URIs are relative to *https://api.height.app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_field_template_option**](FieldTemplatesApi.md#create_field_template_option) | **POST** /fieldTemplates/{id}/options | Create an option for a field template
[**list_all_field_templates**](FieldTemplatesApi.md#list_all_field_templates) | **GET** /fieldTemplates | List all field templates
[**update_field_template_option**](FieldTemplatesApi.md#update_field_template_option) | **PUT** /fieldTemplates/{id}/options/{optionId} | Update or delete an option for a field template

# **create_field_template_option**
> FieldTemplateObject create_field_template_option(body, id)

Create an option for a field template

This endpoint adds an option to a `select` or `labels` field template.

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
api_instance = swagger_client.FieldTemplatesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateFieldTemplateOptionRequest() # CreateFieldTemplateOptionRequest | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | field template id (UUID)

try:
    # Create an option for a field template
    api_response = api_instance.create_field_template_option(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldTemplatesApi->create_field_template_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateFieldTemplateOptionRequest**](CreateFieldTemplateOptionRequest.md)|  | 
 **id** | [**str**](.md)| field template id (UUID) | 

### Return type

[**FieldTemplateObject**](FieldTemplateObject.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_field_templates**
> ListAllFieldTemplatesResponse list_all_field_templates()

List all field templates

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
api_instance = swagger_client.FieldTemplatesApi(swagger_client.ApiClient(configuration))

try:
    # List all field templates
    api_response = api_instance.list_all_field_templates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldTemplatesApi->list_all_field_templates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListAllFieldTemplatesResponse**](ListAllFieldTemplatesResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_field_template_option**
> FieldTemplateObject update_field_template_option(body, id, option_id)

Update or delete an option for a field template

This endpoint updates or deletes an option to a `select` or `labels` field template.  The field template must be unlocked to use this endpoint.  Locking and unlocking field templates is an enterprise feature.

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
api_instance = swagger_client.FieldTemplatesApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateFieldTemplateOptionRequest() # UpdateFieldTemplateOptionRequest | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
option_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Update or delete an option for a field template
    api_response = api_instance.update_field_template_option(body, id, option_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldTemplatesApi->update_field_template_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateFieldTemplateOptionRequest**](UpdateFieldTemplateOptionRequest.md)|  | 
 **id** | [**str**](.md)|  | 
 **option_id** | [**str**](.md)|  | 

### Return type

[**FieldTemplateObject**](FieldTemplateObject.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

