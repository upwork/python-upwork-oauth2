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


class Api:
    """ """

    client = None

    def __init__(self, client):
        self.client = client

    def get_my_info(self):
        """Get Auth user info"""
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def get_specific(self, user_reference):
        """Get Specific User Info

        :param user_reference: String

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")
