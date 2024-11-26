class Api:
    """ """

    client = None

    def __init__(self, client):
        self.client = client

    def get_specific(self, engagement_ref):
        """List activities for specific engagement

        :param engagement_ref: String

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def assign(self, company, team, engagement, params):
        """Assign engagements to the list of activities
        
        Parameters:
        :param company: 
        :param team: 
        :param engagement: 
        :param params: 

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def assign_to_engagement(self, engagement_ref, params):
        """Assign to specific engagement the list of activities
        
        Parameters:
        :param engagement_ref: 
        :param params: 

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")
