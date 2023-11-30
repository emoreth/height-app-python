# coding: utf-8

"""
    Height APP API

    Unofficial Open API 3.1 specification for [Height App API](https://www.notion.so/API-documentation-643aea5bf01742de9232e5971cb4afda). This is not affiliated with Height team.  --- # Authentication  The Height API uses API keys to authenticate requests. **You can view your API key in the Height settings under API**.  Authentication to the API is performed via the `Authorization` header. All API requests should be made over HTTPs.  i.e. Get your workspace.  ```bash curl https://api.height.app/workspace \\   -H \"Authorization: api-key secret_1234\" ```  Third-party applications must connect to the Height API using [OAuth2](https://www.notion.so/API-documentation-643aea5bf01742de9232e5971cb4afda).   See [OAuth Apps on Height](https://www.notion.so/OAuth-Apps-on-Height-a8ebeab3f3f047e3857bd8ce60c2f640) for more information.  # Object formats  All objects have a unique `id` ([UUID v4](https://en.m.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random))) and a `model` attribute to distinguish the model type.  e.g. a task object.  ```json {   \"id\": \"123e4567-e89b-12d3-a456-426655440000\",   \"model\": \"task\",   \"name\": \"Fix bug\",   \"index\": 1,   \"status\": \"backLog\",   [...] } ```  # Date formats  Every date uses the ISO format e.g.  ```js \"2019-11-07T17:00:00.000Z\" ```  # Real-time  Any change that you make to the API will be pushed to every user in real-time: i.e. creating tasks or messages.  # Rate limits  To keep incoming traffic under control and maintain a great experience for all our users, our API is behind a rate limiter. Users who send many requests in quick succession may see error responses that show up as status code 429.  Height allows up to 120 requests/min, but we have stricter limits on these endpoints:  - `POST /activities`: 60 requests/min - `POST /tasks`: 60 requests/min  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gil@beomjun.kr
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GetTaskFormRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'url_key': 'str',
        'key_type': 'str',
        'include': 'list[str]',
        'archived': 'bool',
        'draft': 'bool'
    }

    attribute_map = {
        'url_key': 'urlKey',
        'key_type': 'keyType',
        'include': 'include',
        'archived': 'archived',
        'draft': 'draft'
    }

    def __init__(self, url_key=None, key_type=None, include=None, archived=None, draft=None):  # noqa: E501
        """GetTaskFormRequest - a model defined in Swagger"""  # noqa: E501
        self._url_key = None
        self._key_type = None
        self._include = None
        self._archived = None
        self._draft = None
        self.discriminator = None
        self.url_key = url_key
        if key_type is not None:
            self.key_type = key_type
        if include is not None:
            self.include = include
        if archived is not None:
            self.archived = archived
        if draft is not None:
            self.draft = draft

    @property
    def url_key(self):
        """Gets the url_key of this GetTaskFormRequest.  # noqa: E501


        :return: The url_key of this GetTaskFormRequest.  # noqa: E501
        :rtype: str
        """
        return self._url_key

    @url_key.setter
    def url_key(self, url_key):
        """Sets the url_key of this GetTaskFormRequest.


        :param url_key: The url_key of this GetTaskFormRequest.  # noqa: E501
        :type: str
        """
        if url_key is None:
            raise ValueError("Invalid value for `url_key`, must not be `None`")  # noqa: E501

        self._url_key = url_key

    @property
    def key_type(self):
        """Gets the key_type of this GetTaskFormRequest.  # noqa: E501

        One of key or urlKey, defaulting to id  # noqa: E501

        :return: The key_type of this GetTaskFormRequest.  # noqa: E501
        :rtype: str
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        """Sets the key_type of this GetTaskFormRequest.

        One of key or urlKey, defaulting to id  # noqa: E501

        :param key_type: The key_type of this GetTaskFormRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["key", "urlKey"]  # noqa: E501
        if key_type not in allowed_values:
            raise ValueError(
                "Invalid value for `key_type` ({0}), must be one of {1}"  # noqa: E501
                .format(key_type, allowed_values)
            )

        self._key_type = key_type

    @property
    def include(self):
        """Gets the include of this GetTaskFormRequest.  # noqa: E501

        Array of task form includes  # noqa: E501

        :return: The include of this GetTaskFormRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._include

    @include.setter
    def include(self, include):
        """Sets the include of this GetTaskFormRequest.

        Array of task form includes  # noqa: E501

        :param include: The include of this GetTaskFormRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["RestrictedUsers", "RestrictedLists", "FieldTemplates", "SubtaskForms", "Questions", "Fields"]  # noqa: E501
        if not set(include).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `include` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(include) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._include = include

    @property
    def archived(self):
        """Gets the archived of this GetTaskFormRequest.  # noqa: E501

        only look for archived or unarchived forms  # noqa: E501

        :return: The archived of this GetTaskFormRequest.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this GetTaskFormRequest.

        only look for archived or unarchived forms  # noqa: E501

        :param archived: The archived of this GetTaskFormRequest.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def draft(self):
        """Gets the draft of this GetTaskFormRequest.  # noqa: E501

        only look for archived or unarchived forms  # noqa: E501

        :return: The draft of this GetTaskFormRequest.  # noqa: E501
        :rtype: bool
        """
        return self._draft

    @draft.setter
    def draft(self, draft):
        """Sets the draft of this GetTaskFormRequest.

        only look for archived or unarchived forms  # noqa: E501

        :param draft: The draft of this GetTaskFormRequest.  # noqa: E501
        :type: bool
        """

        self._draft = draft

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GetTaskFormRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetTaskFormRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other