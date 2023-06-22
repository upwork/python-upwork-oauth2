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


class Config:
    """Configuration container"""

    def __init__(self, config):
        self.client_id, self.client_secret = (
            config["client_id"],
            config["client_secret"],
        )

        if "grant_type" in config:
            self.grant_type = config["grant_type"]
        else:
            self.grant_type = None # Authorization Code Grant flow is used by default

        if "redirect_uri" in config:
            self.redirect_uri = config["redirect_uri"]

        # access-, refresh token, and expires_in/at data
        if "token" in config:
            self.token = config["token"]
