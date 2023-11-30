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

class SentryIssueLinkObjectMetadata(object):
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
        'type': 'str',
        'project': 'SentryIssueLinkObjectMetadataProject',
        'issue_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'project': 'project',
        'issue_id': 'issueId'
    }

    def __init__(self, type=None, project=None, issue_id=None):  # noqa: E501
        """SentryIssueLinkObjectMetadata - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._project = None
        self._issue_id = None
        self.discriminator = None
        self.type = type
        self.project = project
        self.issue_id = issue_id

    @property
    def type(self):
        """Gets the type of this SentryIssueLinkObjectMetadata.  # noqa: E501

        The type of the metadata.  # noqa: E501

        :return: The type of this SentryIssueLinkObjectMetadata.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SentryIssueLinkObjectMetadata.

        The type of the metadata.  # noqa: E501

        :param type: The type of this SentryIssueLinkObjectMetadata.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["sentryIssue"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def project(self):
        """Gets the project of this SentryIssueLinkObjectMetadata.  # noqa: E501


        :return: The project of this SentryIssueLinkObjectMetadata.  # noqa: E501
        :rtype: SentryIssueLinkObjectMetadataProject
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this SentryIssueLinkObjectMetadata.


        :param project: The project of this SentryIssueLinkObjectMetadata.  # noqa: E501
        :type: SentryIssueLinkObjectMetadataProject
        """
        if project is None:
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

    @property
    def issue_id(self):
        """Gets the issue_id of this SentryIssueLinkObjectMetadata.  # noqa: E501

        The ID of the Sentry issue.  # noqa: E501

        :return: The issue_id of this SentryIssueLinkObjectMetadata.  # noqa: E501
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        """Sets the issue_id of this SentryIssueLinkObjectMetadata.

        The ID of the Sentry issue.  # noqa: E501

        :param issue_id: The issue_id of this SentryIssueLinkObjectMetadata.  # noqa: E501
        :type: str
        """
        if issue_id is None:
            raise ValueError("Invalid value for `issue_id`, must not be `None`")  # noqa: E501

        self._issue_id = issue_id

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
        if issubclass(SentryIssueLinkObjectMetadata, dict):
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
        if not isinstance(other, SentryIssueLinkObjectMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
