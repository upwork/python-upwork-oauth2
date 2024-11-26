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

    def get_active_milestone(self, contract_id):
        """Get active Milestone for specific Contract

        :param contract_id: String

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def get_submissions(self, milestone_id):
        """Get active Milestone for specific Contract

        :param milestone_id: String

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def create(self, params):
        """Create a new Milestone
        
        Parameters:

        :param params: 

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def edit(self, milestone_id, params):
        """Edit an existing Milestone
        
        Parameters:

        :param milestone_id: 
        :param params: 

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def activate(self, milestone_id, params):
        """Activate an existing Milestone
        
        Parameters:

        :param milestone_id: 
        :param params: 

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def approve(self, milestone_id, params):
        """Approve an existing Milestone
        
        Parameters:

        :param milestone_id: 
        :param params: 

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def delete(self, milestone_id):
        """Delete an existing Milestone

        :param milestone_id: String

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")
