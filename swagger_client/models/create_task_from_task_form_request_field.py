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

class CreateTaskFromTaskFormRequestField(object):
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
        'field_template_id': 'str',
        'value': 'str',
        '_date': 'datetime',
        'labels': 'list[str]',
        'linked_tasks': 'list[TaskObjectLinkedTasks]'
    }

    attribute_map = {
        'field_template_id': 'fieldTemplateId',
        'value': 'value',
        '_date': 'date',
        'labels': 'labels',
        'linked_tasks': 'linkedTasks'
    }

    def __init__(self, field_template_id=None, value=None, _date=None, labels=None, linked_tasks=None):  # noqa: E501
        """CreateTaskFromTaskFormRequestField - a model defined in Swagger"""  # noqa: E501
        self._field_template_id = None
        self._value = None
        self.__date = None
        self._labels = None
        self._linked_tasks = None
        self.discriminator = None
        self.field_template_id = field_template_id
        if value is not None:
            self.value = value
        if _date is not None:
            self._date = _date
        if labels is not None:
            self.labels = labels
        if linked_tasks is not None:
            self.linked_tasks = linked_tasks

    @property
    def field_template_id(self):
        """Gets the field_template_id of this CreateTaskFromTaskFormRequestField.  # noqa: E501

        The id of the appropriate field template  # noqa: E501

        :return: The field_template_id of this CreateTaskFromTaskFormRequestField.  # noqa: E501
        :rtype: str
        """
        return self._field_template_id

    @field_template_id.setter
    def field_template_id(self, field_template_id):
        """Sets the field_template_id of this CreateTaskFromTaskFormRequestField.

        The id of the appropriate field template  # noqa: E501

        :param field_template_id: The field_template_id of this CreateTaskFromTaskFormRequestField.  # noqa: E501
        :type: str
        """
        if field_template_id is None:
            raise ValueError("Invalid value for `field_template_id`, must not be `None`")  # noqa: E501

        self._field_template_id = field_template_id

    @property
    def value(self):
        """Gets the value of this CreateTaskFromTaskFormRequestField.  # noqa: E501

        For text fields: the text value of the field. For select fields: the id of the selected option  # noqa: E501

        :return: The value of this CreateTaskFromTaskFormRequestField.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CreateTaskFromTaskFormRequestField.

        For text fields: the text value of the field. For select fields: the id of the selected option  # noqa: E501

        :param value: The value of this CreateTaskFromTaskFormRequestField.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def _date(self):
        """Gets the _date of this CreateTaskFromTaskFormRequestField.  # noqa: E501

        For date fields: the date value of the field  # noqa: E501

        :return: The _date of this CreateTaskFromTaskFormRequestField.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this CreateTaskFromTaskFormRequestField.

        For date fields: the date value of the field  # noqa: E501

        :param _date: The _date of this CreateTaskFromTaskFormRequestField.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def labels(self):
        """Gets the labels of this CreateTaskFromTaskFormRequestField.  # noqa: E501

        For labels fields: the labels of the field  # noqa: E501

        :return: The labels of this CreateTaskFromTaskFormRequestField.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this CreateTaskFromTaskFormRequestField.

        For labels fields: the labels of the field  # noqa: E501

        :param labels: The labels of this CreateTaskFromTaskFormRequestField.  # noqa: E501
        :type: list[str]
        """

        self._labels = labels

    @property
    def linked_tasks(self):
        """Gets the linked_tasks of this CreateTaskFromTaskFormRequestField.  # noqa: E501

        For linkedTasks fields: the tasks to be linked, in the format: { \"id\": \"UUID\", \"index\": number }  # noqa: E501

        :return: The linked_tasks of this CreateTaskFromTaskFormRequestField.  # noqa: E501
        :rtype: list[TaskObjectLinkedTasks]
        """
        return self._linked_tasks

    @linked_tasks.setter
    def linked_tasks(self, linked_tasks):
        """Sets the linked_tasks of this CreateTaskFromTaskFormRequestField.

        For linkedTasks fields: the tasks to be linked, in the format: { \"id\": \"UUID\", \"index\": number }  # noqa: E501

        :param linked_tasks: The linked_tasks of this CreateTaskFromTaskFormRequestField.  # noqa: E501
        :type: list[TaskObjectLinkedTasks]
        """

        self._linked_tasks = linked_tasks

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
        if issubclass(CreateTaskFromTaskFormRequestField, dict):
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
        if not isinstance(other, CreateTaskFromTaskFormRequestField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
