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

class UpdateListRequest(object):
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
        'description': 'str',
        'appearance': 'UpdateListRequestAppearance',
        'visualization': 'str',
        'archived_at': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'appearance': 'appearance',
        'visualization': 'visualization',
        'archived_at': 'archivedAt'
    }

    def __init__(self, name=None, description=None, appearance=None, visualization=None, archived_at=None):  # noqa: E501
        """UpdateListRequest - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._appearance = None
        self._visualization = None
        self._archived_at = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if appearance is not None:
            self.appearance = appearance
        if visualization is not None:
            self.visualization = visualization
        if archived_at is not None:
            self.archived_at = archived_at

    @property
    def name(self):
        """Gets the name of this UpdateListRequest.  # noqa: E501


        :return: The name of this UpdateListRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateListRequest.


        :param name: The name of this UpdateListRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateListRequest.  # noqa: E501


        :return: The description of this UpdateListRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateListRequest.


        :param description: The description of this UpdateListRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def appearance(self):
        """Gets the appearance of this UpdateListRequest.  # noqa: E501


        :return: The appearance of this UpdateListRequest.  # noqa: E501
        :rtype: UpdateListRequestAppearance
        """
        return self._appearance

    @appearance.setter
    def appearance(self, appearance):
        """Sets the appearance of this UpdateListRequest.


        :param appearance: The appearance of this UpdateListRequest.  # noqa: E501
        :type: UpdateListRequestAppearance
        """

        self._appearance = appearance

    @property
    def visualization(self):
        """Gets the visualization of this UpdateListRequest.  # noqa: E501


        :return: The visualization of this UpdateListRequest.  # noqa: E501
        :rtype: str
        """
        return self._visualization

    @visualization.setter
    def visualization(self, visualization):
        """Sets the visualization of this UpdateListRequest.


        :param visualization: The visualization of this UpdateListRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["list", "kanban", "calendar", "gantt", "conversation", "figma"]  # noqa: E501
        if visualization not in allowed_values:
            raise ValueError(
                "Invalid value for `visualization` ({0}), must be one of {1}"  # noqa: E501
                .format(visualization, allowed_values)
            )

        self._visualization = visualization

    @property
    def archived_at(self):
        """Gets the archived_at of this UpdateListRequest.  # noqa: E501

        string representing a date the list was archived at, in the form of an ISO 8601 date (e.g. 2011-04-11T10:20:30Z).  # noqa: E501

        :return: The archived_at of this UpdateListRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._archived_at

    @archived_at.setter
    def archived_at(self, archived_at):
        """Sets the archived_at of this UpdateListRequest.

        string representing a date the list was archived at, in the form of an ISO 8601 date (e.g. 2011-04-11T10:20:30Z).  # noqa: E501

        :param archived_at: The archived_at of this UpdateListRequest.  # noqa: E501
        :type: datetime
        """

        self._archived_at = archived_at

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
        if issubclass(UpdateListRequest, dict):
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
        if not isinstance(other, UpdateListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
