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

class GroupObject(object):
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
        'handle': 'str',
        'hue': 'float',
        'user_ids': 'list[str]',
        'archived': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'model': 'model',
        'name': 'name',
        'handle': 'handle',
        'hue': 'hue',
        'user_ids': 'userIds',
        'archived': 'archived'
    }

    def __init__(self, id=None, model=None, name=None, handle=None, hue=None, user_ids=None, archived=None):  # noqa: E501
        """GroupObject - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._model = None
        self._name = None
        self._handle = None
        self._hue = None
        self._user_ids = None
        self._archived = None
        self.discriminator = None
        self.id = id
        self.model = model
        self.name = name
        self.handle = handle
        self.hue = hue
        self.user_ids = user_ids
        self.archived = archived

    @property
    def id(self):
        """Gets the id of this GroupObject.  # noqa: E501

        The unique ID of the group.  # noqa: E501

        :return: The id of this GroupObject.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupObject.

        The unique ID of the group.  # noqa: E501

        :param id: The id of this GroupObject.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def model(self):
        """Gets the model of this GroupObject.  # noqa: E501

        The model is always `group`.  # noqa: E501

        :return: The model of this GroupObject.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this GroupObject.

        The model is always `group`.  # noqa: E501

        :param model: The model of this GroupObject.  # noqa: E501
        :type: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501
        allowed_values = ["group"]  # noqa: E501
        if model not in allowed_values:
            raise ValueError(
                "Invalid value for `model` ({0}), must be one of {1}"  # noqa: E501
                .format(model, allowed_values)
            )

        self._model = model

    @property
    def name(self):
        """Gets the name of this GroupObject.  # noqa: E501

        The name of the group.  # noqa: E501

        :return: The name of this GroupObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupObject.

        The name of the group.  # noqa: E501

        :param name: The name of this GroupObject.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def handle(self):
        """Gets the handle of this GroupObject.  # noqa: E501

        The handle of the group.  # noqa: E501

        :return: The handle of this GroupObject.  # noqa: E501
        :rtype: str
        """
        return self._handle

    @handle.setter
    def handle(self, handle):
        """Sets the handle of this GroupObject.

        The handle of the group.  # noqa: E501

        :param handle: The handle of this GroupObject.  # noqa: E501
        :type: str
        """
        if handle is None:
            raise ValueError("Invalid value for `handle`, must not be `None`")  # noqa: E501

        self._handle = handle

    @property
    def hue(self):
        """Gets the hue of this GroupObject.  # noqa: E501

        The color/hue (0-360) of the group.  # noqa: E501

        :return: The hue of this GroupObject.  # noqa: E501
        :rtype: float
        """
        return self._hue

    @hue.setter
    def hue(self, hue):
        """Sets the hue of this GroupObject.

        The color/hue (0-360) of the group.  # noqa: E501

        :param hue: The hue of this GroupObject.  # noqa: E501
        :type: float
        """
        if hue is None:
            raise ValueError("Invalid value for `hue`, must not be `None`")  # noqa: E501

        self._hue = hue

    @property
    def user_ids(self):
        """Gets the user_ids of this GroupObject.  # noqa: E501

        The list of user IDs that are in the group.  # noqa: E501

        :return: The user_ids of this GroupObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """Sets the user_ids of this GroupObject.

        The list of user IDs that are in the group.  # noqa: E501

        :param user_ids: The user_ids of this GroupObject.  # noqa: E501
        :type: list[str]
        """
        if user_ids is None:
            raise ValueError("Invalid value for `user_ids`, must not be `None`")  # noqa: E501

        self._user_ids = user_ids

    @property
    def archived(self):
        """Gets the archived of this GroupObject.  # noqa: E501

        Flag to indicate whether the group is archived.  # noqa: E501

        :return: The archived of this GroupObject.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this GroupObject.

        Flag to indicate whether the group is archived.  # noqa: E501

        :param archived: The archived of this GroupObject.  # noqa: E501
        :type: bool
        """
        if archived is None:
            raise ValueError("Invalid value for `archived`, must not be `None`")  # noqa: E501

        self._archived = archived

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
        if issubclass(GroupObject, dict):
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
        if not isinstance(other, GroupObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
