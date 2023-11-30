# coding: utf-8

"""
    Height APP API

    Unofficial Open API 3.1 specification for [Height App API](https://www.notion.so/API-documentation-643aea5bf01742de9232e5971cb4afda). This is not affiliated with Height team.  ---  # Authentication   The Height API uses API keys to authenticate requests. **You can view your API key in the Height settings under API**.  Authentication to the API is performed via the `Authorization` header. All API requests should be made over HTTPs.   i.e. Get your workspace.   ```bash  curl https://api.height.app/workspace \\   -H \"Authorization: api-key secret_1234\" ```   Third-party applications must connect to the Height API using [OAuth2](https://www.notion.so/API-documentation-643aea5bf01742de9232e5971cb4afda).   See [OAuth Apps on Height](https://www.notion.so/OAuth-Apps-on-Height-a8ebeab3f3f047e3857bd8ce60c2f640) for more information.   # Object formats   All objects have a unique `id` ([UUID v4](https://en.m.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random))) and a `model` attribute to distinguish the model type.   e.g. a task object.   ```json  {   \"id\": \"123e4567-e89b-12d3-a456-426655440000\",   \"model\": \"task\",   \"name\": \"Fix bug\",   \"index\": 1,   \"status\": \"backLog\",   [...] }  ```   # Date formats   Every date uses the ISO format e.g.   ```js  \"2019-11-07T17:00:00.000Z\"  ```   # Real-time   Any change that you make to the API will be pushed to every user in real-time: i.e. creating tasks or messages.   # Rate limits   To keep incoming traffic under control and maintain a great experience for all our users, our API is behind a rate limiter. Users who send many requests in quick succession may see error responses that show up as status code 429.   Height allows up to 120 requests/min, but we have stricter limits on these endpoints:   - `POST /activities`: 60 requests/min  - `POST /tasks`: 60 requests/min  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gil@beomjun.kr
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class WorkspaceObject(object):
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
        'id': 'str',
        'model': 'str',
        'name': 'str',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'model': 'model',
        'name': 'name',
        'url': 'url'
    }

    def __init__(self, id=None, model=None, name=None, url=None):  # noqa: E501
        """WorkspaceObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._model = None
        self._name = None
        self._url = None
        self.discriminator = None
        self.id = id
        self.model = model
        self.name = name
        self.url = url

    @property
    def id(self):
        """Gets the id of this WorkspaceObject.  # noqa: E501

        The unique ID of the workspace.  # noqa: E501

        :return: The id of this WorkspaceObject.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkspaceObject.

        The unique ID of the workspace.  # noqa: E501

        :param id: The id of this WorkspaceObject.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def model(self):
        """Gets the model of this WorkspaceObject.  # noqa: E501

        The model is always `workspace`.  # noqa: E501

        :return: The model of this WorkspaceObject.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this WorkspaceObject.

        The model is always `workspace`.  # noqa: E501

        :param model: The model of this WorkspaceObject.  # noqa: E501
        :type: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def name(self):
        """Gets the name of this WorkspaceObject.  # noqa: E501

        The name of the workspace.  # noqa: E501

        :return: The name of this WorkspaceObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkspaceObject.

        The name of the workspace.  # noqa: E501

        :param name: The name of this WorkspaceObject.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def url(self):
        """Gets the url of this WorkspaceObject.  # noqa: E501

        The full URL of the workspace.  # noqa: E501

        :return: The url of this WorkspaceObject.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WorkspaceObject.

        The full URL of the workspace.  # noqa: E501

        :param url: The url of this WorkspaceObject.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

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
        if issubclass(WorkspaceObject, dict):
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
        if not isinstance(other, WorkspaceObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
