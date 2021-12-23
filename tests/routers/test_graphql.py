import upwork
from upwork.routers import graphql
from unittest.mock import patch


@patch.object(upwork.Client, "post")
def test_execute(mocked_method):
    graphql.Api(upwork.Client).execute({"query": "query{}"})
    mocked_method.assert_called_with("", {"query": "query{}"})
