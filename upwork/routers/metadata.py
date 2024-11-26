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

    def get_categories_v2(self):
        """Get categories (V2)"""
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def get_skills(self):
        """Get skills"""
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def get_skills_v2(self, params):
        """Get skills (V2)

        :param params: 

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def get_specialties(self):
        """Get specialties"""
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def get_regions(self):
        """Get regions"""
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def get_tests(self):
        """Get tests"""
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def get_reasons(self, params):
        """Get reasons

        :param params: 

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")
