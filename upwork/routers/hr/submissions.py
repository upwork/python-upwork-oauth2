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

    def request_approval(self, params):
        """Freelancer submits work for the client to approve
        
        Parameters:

        :param params: 

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def approve(self, submission_id, params):
        """Approve an existing Submission
        
        Parameters:

        :param submission_id: 
        :param params: 

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def reject(self, submission_id, params):
        """Reject an existing Submission
        
        Parameters:

        :param submission_id: 
        :param params: 

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")
