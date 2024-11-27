import upwork
from pprint import pprint
from upwork.routers import graphql


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

    # For Client Credentials Grant the following config must be used, no other parameters are needed
    # config = upwork.Config({'client_id': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'client_secret': 'xxxxxxxxxxxxx', 'grant_type': 'client_credentials'})

    client = upwork.Client(config)

    try:
        config.token
    except AttributeError:
        # remove client.get_authorization_url and authz_code input in case Client Credentials Grant is used
        authorization_url, state = client.get_authorization_url()
        # cover "state" flow if needed
        authz_code = input(
            "Please enter the full callback URL you get "
            "following this link:\n{0}\n\n> ".format(authorization_url)
        )

        print("Retrieving access and refresh tokens.... ")
        token = client.get_access_token(authz_code)
        # token = client.get_access_token() # for Client Credentials Grant
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
        query = """
    query {
      user {
        id
        nid
        rid
      }
      organization {
        id
      }
    }"""
        # client.set_org_uid_header("1234567890") # Organization UID (optional)
        pprint(graphql.Api(client).execute({'query': query}))
    except Exception as e:
        # print("Exception at %s %s" % (client.last_method, client.last_url))
        raise e
