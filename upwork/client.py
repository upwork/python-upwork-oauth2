# Licensed under the Upwork's API Terms of Use;
# you may not use this file except in compliance with the Terms.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author::    Maksym Novozhylov (mnovozhilov@upwork.com)
# Copyright:: Copyright 2020(c) Upwork.com
# License::   See LICENSE.txt and TOS - https://developers.upwork.com/api-tos.html

from . import upwork
from oauthlib.oauth2 import BackendApplicationClient # type: ignore
from requests_oauthlib import OAuth2Session # type: ignore
from urllib.parse import parse_qsl, urlencode


class Client(object):
    """API client for OAuth2 authorization
    
    *Parameters:*
    :config: An instance of upwork.Config class, which contains the configuration keys and tokens
    """

    __data_format = "json"
    __overload_var = "http_method"

    __uri_auth = "/ab/account-security/oauth2/authorize"
    __uri_rtoken = "/v3/oauth2/token"
    __uri_atoken = "/v3/oauth2/token"

    epoint = upwork.DEFAULT_EPOINT

    def __init__(self, config):
        self.config = config
        self.config.tenant_id = None
        try:
            # token is known, use it
            self.__oauth = OAuth2Session(
                self.config.client_id,
                token=self.config.token,
                auto_refresh_url=full_url(self.__uri_rtoken, upwork.DEFAULT_EPOINT),
                auto_refresh_kwargs={
                    "client_id": self.config.client_id,
                    "client_secret": self.config.client_secret,
                },
                token_updater=self.refresh_config_from_access_token,
            )
        except AttributeError as e:
            if self.config.grant_type == "client_credentials":
                client = BackendApplicationClient(client_id=self.config.client_id)
                self.__oauth = OAuth2Session(
                    client=client
                )
            else:
                # start from authorization step
                self.__oauth = OAuth2Session(
                    self.config.client_id, redirect_uri=self.config.redirect_uri
                )

    def get_authorization_url(self):
        """Get authorization URL

        :param redirect_uri:  (Default value = None)

        """
        return self.__oauth.authorization_url(
            "{0}{1}".format(upwork.BASE_HOST, self.__uri_auth)
        )

    def get_access_token(self, authorization_response=None):
        """Finish auth process and get access token

        :param authorization_response: 

        """
        self.config.token = self.__oauth.fetch_token(
            full_url(self.__uri_atoken, upwork.DEFAULT_EPOINT),
            authorization_response=authorization_response,
            client_secret=self.config.client_secret,
        )
        return self.config.token

    def refresh_config_from_access_token(self, token):
        """Callback from OAuth2 client which will refresh config with actual data"""
        self.config.token = token

    def set_org_uid_header(self, tenant_id):
        """Configure X-Upwork-API-TenantId header"""
        self.config.tenant_id = tenant_id

    def get_actual_config(self):
        """Get actual client config"""
        return self.config

    def get(self, uri, params=None):
        """Execute GET request

        :param uri: 
        :param params:  (Default value = None)

        """
        return self.send_request(uri, "get", params)

    def post(self, uri, params=None):
        """Execute POST request

        :param uri: 
        :param params:  (Default value = None)

        """
        return self.send_request(uri, "post", params)

    def put(self, uri, params=None):
        """Execute PUT request

        :param uri: 
        :param params:  (Default value = None)

        """
        return self.send_request(uri, "put", params)

    def delete(self, uri, params=None):
        """Execute DELETE request

        :param uri: 
        :param params:  (Default value = None)

        """
        return self.send_request(uri, "delete", params)

    def send_request(self, uri, method="get", params={}):
        """Send request

        :param uri: 
        :param method:  (Default value = 'get')
        :param params:  (Default value = {})

        """
        # delete does not support passing the parameters
        if method == "delete":
            params[self.__overload_var] = method

        url = full_url(get_uri_with_format(uri, self.epoint), self.epoint)

        if method == "get":
            r = self.__oauth.get(url, params=params)
        elif method == "put":
            headers = {"Content-type": "application/json"}
            r = self.__oauth.put(url, json=params, headers=headers)
        elif method in {"post", "delete"}:
            headers = {"Content-type": "application/json"}
            if self.epoint == "graphql" and self.config.tenant_id:
                headers["X-Upwork-API-TenantId"] = self.config.tenant_id
            r = self.__oauth.post(url, json=params, headers=headers)
        else:
            raise ValueError(
                'Do not know how to handle http method "{0}"'.format(method)
            )

        return r.json()


"""

"""


def full_url(uri, epoint=None):
    """Get full URL

    :param uri: 
    :param epoint:  (Default value = None)

    """
    if epoint == "graphql":
        return upwork.GQL_EPOINT

    if not epoint:
        epoint = upwork.DEFAULT_EPOINT
    return "{0}/{1}{2}".format(upwork.BASE_HOST, epoint, uri)


def get_uri_with_format(uri, epoint):
    """Get URI with format ending

    :param uri: 
    :param epoint: 

    """
    if epoint == upwork.DEFAULT_EPOINT:
        uri += ".json"
    return uri
