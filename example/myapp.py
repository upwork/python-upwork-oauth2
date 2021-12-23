import upwork
from pprint import pprint
from upwork.routers import auth

# from upwork.routers import graphql

# from upwork.routers.jobs import search
# from upwork.routers.activities import team
# from upwork.routers.reports import time
# from urllib.parse import quote


def get_desktop_client():
    """Emulation of desktop app.
    Your keys should be created with project type "Desktop".

    Returns: ``upwork.Client`` instance ready to work.

    """
    print("Emulating desktop app")

    consumer_key = input("Please enter consumer key: > ")
    consumer_secret = input("Please enter key secret: > ")
    config = upwork.Config(
        {
            "client_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "client_secret": "xxxxxxxxxxxxx",
            "redirect_uri": "https://a.callback.url",
        }
    )

    # If token data already known and saved, you can reuse them
    # by adding 'token' parameter to the config
    # token = {'access_token': 'xxxxxxxxxxxxxxxxxx', 'expires_at': 1590479276.547947, 'expires_in': '86400', 'refresh_token': 'xxxxxxxxxxxxxxxxxxxxxxxx', 'token_type': 'Bearer'}
    # config = upwork.Config({'client_id': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'client_secret': 'xxxxxxxxxxxxx', 'token': token})

    client = upwork.Client(config)

    try:
        config.token
    except AttributeError:
        authorization_url, state = client.get_authorization_url()
        # cover "state" flow if needed
        authz_code = input(
            "Please enter the full callback URL you get "
            "following this link:\n{0}\n\n> ".format(authorization_url)
        )

        print("Retrieving access and refresh tokens.... ")
        token = client.get_access_token(authz_code)
        # WARNING: the access token will be refreshed automatically for you
        # in case it's expired, i.e. expires_at < time(). Make sure you replace the
        # old token accordingly in your security storage. Call client.get_actual_config
        # periodically to sync-up the data
        pprint(token)
        print("OK")

    # For further use you can store ``token`` data somewhere

    return client


if __name__ == "__main__":
    client = get_desktop_client()

    try:
        print("My info")
        pprint(auth.Api(client).get_user_info())
        # query = """
#    query {
#      user {
#        id
#        nid
#        rid
#      }
#      organization {
#        id
#      }
#    }"""
        # client.set_org_uid_header("1234567890") # Organization UID
        # pprint(graphql.Api(client).execute({'query': query}))
        # pprint(search.Api(client).find({'q': 'php'}))
        # pprint(team.Api(client).add_activity('mytestcompany', 'mytestcompany', {'code': 'team-task-001', 'description': 'Description', 'all_in_company': '1'}))
        # pprint(time.Gds(client).get_by_freelancer_full('mnovozhilov', {'tq': quote('SELECT task, memo WHERE worked_on >= "2017-06-01" AND worked_on <= "2017-06-02"')}))
    except Exception as e:
        # print("Exception at %s %s" % (client.last_method, client.last_url))
        raise e
