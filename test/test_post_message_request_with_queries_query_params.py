# coding: utf-8

"""
    Height APP API

    Unofficial Open API 3.1 specification for [Height App API](https://www.notion.so/API-documentation-643aea5bf01742de9232e5971cb4afda). This is not affiliated with Height team.  --- # Authentication  The Height API uses API keys to authenticate requests. **You can view your API key in the Height settings under API**.  Authentication to the API is performed via the `Authorization` header. All API requests should be made over HTTPs.  i.e. Get your workspace.  ```bash curl https://api.height.app/workspace \\   -H \"Authorization: api-key secret_1234\" ```  Third-party applications must connect to the Height API using [OAuth2](https://www.notion.so/API-documentation-643aea5bf01742de9232e5971cb4afda).   See [OAuth Apps on Height](https://www.notion.so/OAuth-Apps-on-Height-a8ebeab3f3f047e3857bd8ce60c2f640) for more information.  # Object formats  All objects have a unique `id` ([UUID v4](https://en.m.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random))) and a `model` attribute to distinguish the model type.  e.g. a task object.  ```json {   \"id\": \"123e4567-e89b-12d3-a456-426655440000\",   \"model\": \"task\",   \"name\": \"Fix bug\",   \"index\": 1,   \"status\": \"backLog\",   [...] } ```  # Date formats  Every date uses the ISO format e.g.  ```js \"2019-11-07T17:00:00.000Z\" ```  # Real-time  Any change that you make to the API will be pushed to every user in real-time: i.e. creating tasks or messages.  # Rate limits  To keep incoming traffic under control and maintain a great experience for all our users, our API is behind a rate limiter. Users who send many requests in quick succession may see error responses that show up as status code 429.  Height allows up to 120 requests/min, but we have stricter limits on these endpoints:  - `POST /activities`: 60 requests/min - `POST /tasks`: 60 requests/min  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gil@beomjun.kr
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.post_message_request_with_queries_query_params import PostMessageRequestWithQueriesQueryParams  # noqa: E501
from swagger_client.rest import ApiException


class TestPostMessageRequestWithQueriesQueryParams(unittest.TestCase):
    """PostMessageRequestWithQueriesQueryParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPostMessageRequestWithQueriesQueryParams(self):
        """Test PostMessageRequestWithQueriesQueryParams"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.post_message_request_with_queries_query_params.PostMessageRequestWithQueriesQueryParams()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()