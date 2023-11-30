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

class PatchTasksFieldsEffectFields(object):
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
        'text': 'str',
        '_date': 'datetime',
        'recursion': 'object',
        'label': 'PatchTasksFieldsEffectFieldsLabel',
        'labels': 'PatchTasksFieldsEffectFieldsLabels',
        'linked_tasks': 'PatchTasksFieldsEffectFieldsLinkedTasks'
    }

    attribute_map = {
        'text': 'text',
        '_date': 'date',
        'recursion': 'recursion',
        'label': 'label',
        'labels': 'labels',
        'linked_tasks': 'linkedTasks'
    }

    def __init__(self, text=None, _date=None, recursion=None, label=None, labels=None, linked_tasks=None):  # noqa: E501
        """PatchTasksFieldsEffectFields - a model defined in Swagger"""  # noqa: E501
        self._text = None
        self.__date = None
        self._recursion = None
        self._label = None
        self._labels = None
        self._linked_tasks = None
        self.discriminator = None
        if text is not None:
            self.text = text
        if _date is not None:
            self._date = _date
        if recursion is not None:
            self.recursion = recursion
        if label is not None:
            self.label = label
        if labels is not None:
            self.labels = labels
        if linked_tasks is not None:
            self.linked_tasks = linked_tasks

    @property
    def text(self):
        """Gets the text of this PatchTasksFieldsEffectFields.  # noqa: E501

        The value of the field when the template type is text.  # noqa: E501

        :return: The text of this PatchTasksFieldsEffectFields.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this PatchTasksFieldsEffectFields.

        The value of the field when the template type is text.  # noqa: E501

        :param text: The text of this PatchTasksFieldsEffectFields.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def _date(self):
        """Gets the _date of this PatchTasksFieldsEffectFields.  # noqa: E501

        The value of the field when the template type is date.  # noqa: E501

        :return: The _date of this PatchTasksFieldsEffectFields.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this PatchTasksFieldsEffectFields.

        The value of the field when the template type is date.  # noqa: E501

        :param _date: The _date of this PatchTasksFieldsEffectFields.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def recursion(self):
        """Gets the recursion of this PatchTasksFieldsEffectFields.  # noqa: E501

        recursion Untyped. Should be documented in [original docs](https://www.notion.so/Update-tasks-53d72cb0059a4e0e81cc2fcbfcbf9d0a)  # noqa: E501

        :return: The recursion of this PatchTasksFieldsEffectFields.  # noqa: E501
        :rtype: object
        """
        return self._recursion

    @recursion.setter
    def recursion(self, recursion):
        """Sets the recursion of this PatchTasksFieldsEffectFields.

        recursion Untyped. Should be documented in [original docs](https://www.notion.so/Update-tasks-53d72cb0059a4e0e81cc2fcbfcbf9d0a)  # noqa: E501

        :param recursion: The recursion of this PatchTasksFieldsEffectFields.  # noqa: E501
        :type: object
        """

        self._recursion = recursion

    @property
    def label(self):
        """Gets the label of this PatchTasksFieldsEffectFields.  # noqa: E501


        :return: The label of this PatchTasksFieldsEffectFields.  # noqa: E501
        :rtype: PatchTasksFieldsEffectFieldsLabel
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this PatchTasksFieldsEffectFields.


        :param label: The label of this PatchTasksFieldsEffectFields.  # noqa: E501
        :type: PatchTasksFieldsEffectFieldsLabel
        """

        self._label = label

    @property
    def labels(self):
        """Gets the labels of this PatchTasksFieldsEffectFields.  # noqa: E501


        :return: The labels of this PatchTasksFieldsEffectFields.  # noqa: E501
        :rtype: PatchTasksFieldsEffectFieldsLabels
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this PatchTasksFieldsEffectFields.


        :param labels: The labels of this PatchTasksFieldsEffectFields.  # noqa: E501
        :type: PatchTasksFieldsEffectFieldsLabels
        """

        self._labels = labels

    @property
    def linked_tasks(self):
        """Gets the linked_tasks of this PatchTasksFieldsEffectFields.  # noqa: E501


        :return: The linked_tasks of this PatchTasksFieldsEffectFields.  # noqa: E501
        :rtype: PatchTasksFieldsEffectFieldsLinkedTasks
        """
        return self._linked_tasks

    @linked_tasks.setter
    def linked_tasks(self, linked_tasks):
        """Sets the linked_tasks of this PatchTasksFieldsEffectFields.


        :param linked_tasks: The linked_tasks of this PatchTasksFieldsEffectFields.  # noqa: E501
        :type: PatchTasksFieldsEffectFieldsLinkedTasks
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
        if issubclass(PatchTasksFieldsEffectFields, dict):
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
        if not isinstance(other, PatchTasksFieldsEffectFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other