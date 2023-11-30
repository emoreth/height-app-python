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

class CreateSmartListRequest(object):
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
        'name': 'str',
        'type': 'str',
        'description': 'str',
        'filters': 'FiltersObject',
        'appearance': 'CreateNormalListRequestAppearance',
        'visualization': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'filters': 'filters',
        'appearance': 'appearance',
        'visualization': 'visualization'
    }

    def __init__(self, name=None, type=None, description=None, filters=None, appearance=None, visualization='list'):  # noqa: E501
        """CreateSmartListRequest - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._type = None
        self._description = None
        self._filters = None
        self._appearance = None
        self._visualization = None
        self.discriminator = None
        self.name = name
        self.type = type
        if description is not None:
            self.description = description
        self.filters = filters
        if appearance is not None:
            self.appearance = appearance
        if visualization is not None:
            self.visualization = visualization

    @property
    def name(self):
        """Gets the name of this CreateSmartListRequest.  # noqa: E501


        :return: The name of this CreateSmartListRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSmartListRequest.


        :param name: The name of this CreateSmartListRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this CreateSmartListRequest.  # noqa: E501


        :return: The type of this CreateSmartListRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateSmartListRequest.


        :param type: The type of this CreateSmartListRequest.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["list", "smartlist"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def description(self):
        """Gets the description of this CreateSmartListRequest.  # noqa: E501


        :return: The description of this CreateSmartListRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateSmartListRequest.


        :param description: The description of this CreateSmartListRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def filters(self):
        """Gets the filters of this CreateSmartListRequest.  # noqa: E501


        :return: The filters of this CreateSmartListRequest.  # noqa: E501
        :rtype: FiltersObject
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this CreateSmartListRequest.


        :param filters: The filters of this CreateSmartListRequest.  # noqa: E501
        :type: FiltersObject
        """
        if filters is None:
            raise ValueError("Invalid value for `filters`, must not be `None`")  # noqa: E501

        self._filters = filters

    @property
    def appearance(self):
        """Gets the appearance of this CreateSmartListRequest.  # noqa: E501


        :return: The appearance of this CreateSmartListRequest.  # noqa: E501
        :rtype: CreateNormalListRequestAppearance
        """
        return self._appearance

    @appearance.setter
    def appearance(self, appearance):
        """Sets the appearance of this CreateSmartListRequest.


        :param appearance: The appearance of this CreateSmartListRequest.  # noqa: E501
        :type: CreateNormalListRequestAppearance
        """

        self._appearance = appearance

    @property
    def visualization(self):
        """Gets the visualization of this CreateSmartListRequest.  # noqa: E501

        visualization string (optional, default = list) list or kanban  # noqa: E501

        :return: The visualization of this CreateSmartListRequest.  # noqa: E501
        :rtype: str
        """
        return self._visualization

    @visualization.setter
    def visualization(self, visualization):
        """Sets the visualization of this CreateSmartListRequest.

        visualization string (optional, default = list) list or kanban  # noqa: E501

        :param visualization: The visualization of this CreateSmartListRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["list", "kanban"]  # noqa: E501
        if visualization not in allowed_values:
            raise ValueError(
                "Invalid value for `visualization` ({0}), must be one of {1}"  # noqa: E501
                .format(visualization, allowed_values)
            )

        self._visualization = visualization

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
        if issubclass(CreateSmartListRequest, dict):
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
        if not isinstance(other, CreateSmartListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other