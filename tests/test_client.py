import unittest
from upwork import config
from upwork import client
from unittest.mock import patch, Mock
from requests_oauthlib import OAuth2Session  # type: ignore


class TestClient(unittest.TestCase):
    def setUp(self):
        cfg = config.Config(
            {
                "client_id": "clientid",
                "client_secret": "secret",
                "redirect_uri": "https://a.callback.url",
            }
        )
        self.base_client = client.Client(cfg)

    @patch.object(
        OAuth2Session,
        "fetch_token",
        return_value={"access_token": "a", "expires_in": "86400", "refresh_token": "b"},
    )
    def test_get_access_token(self, mocked_post):
        assert self.base_client.get_access_token(
            "https://a.callback.url/?code=xxxxxxxxxx&state=xxxxx"
        ) == {"access_token": "a", "expires_in": "86400", "refresh_token": "b"}

    def test_get_actual_config(self):
        assert isinstance(self.base_client.get_actual_config(), config.Config)
        assert self.base_client.get_actual_config().client_id == "clientid"

    @patch.object(
        OAuth2Session,
        "get",
        return_value=Mock(status_code=200, json=lambda: {"a": "b"}),
    )
    @patch.object(
        OAuth2Session,
        "post",
        return_value=Mock(status_code=200, json=lambda: {"a": "b"}),
    )
    @patch.object(
        OAuth2Session,
        "put",
        return_value=Mock(status_code=200, json=lambda: {"a": "b"}),
    )
    @patch.object(
        OAuth2Session,
        "delete",
        return_value=Mock(status_code=200, json=lambda: {"a": "b"}),
    )
    def test_send_request(self, mocked_get, mocked_post, mocked_put, mocked_delete):
        cfg = config.Config(
            {
                "client_id": "keyxxxxxxxxxxxxxxxxxxxx",
                "client_secret": "secretxxxxxxxxxx",
                "token": {
                    "access_token": "token",
                    "refresh_token": "token",
                    "expires_in": "86400",
                },
            }
        )
        cl = client.Client(cfg)
        assert cl.get("/test/uri", {}) == {"a": "b"}
        assert cl.post("/test/uri", {}) == {"a": "b"}
        assert cl.put("/test/uri", {}) == {"a": "b"}
        assert cl.delete("/test/uri", {}) == {"a": "b"}

        with self.assertRaises(ValueError):
            cl.send_request("/test/uri", "method", {})

    def test_get_authorization_url(self):
        assert (
            self.base_client.get_authorization_url()[0][:-30]
            == "https://www.upwork.com/ab/account-security/oauth2/authorize?response_type=code&client_id=clientid&redirect_uri=https%3A%2F%2Fa.callback.url&state="
        )

    def test_refresh_config_from_access_token(self):
        self.base_client.refresh_config_from_access_token({"access_token": "a"})
        assert self.base_client.config.token == {"access_token": "a"}

    def test_full_url(self):
        assert client.full_url("/test/uri") == "https://www.upwork.com/api/test/uri"
        assert (
            client.full_url("/test/uri", "gds") == "https://www.upwork.com/gds/test/uri"
        )

    def test_get_uri_with_format(self):
        assert client.get_uri_with_format("/test/uri", "api") == "/test/uri.json"
        assert client.get_uri_with_format("/test/uri", "gds") == "/test/uri"
