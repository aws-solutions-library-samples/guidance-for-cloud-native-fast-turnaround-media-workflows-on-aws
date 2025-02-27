import requests

TOKEN_URL = "<TOKEN URL>"
CLIENT_ID = "<CLIENT ID>"
CLIENT_SECRET = "<CLIENT SECRET>"
TAMS_URL = "<TAMS URL>"
OAUTH_SCOPES = ["tams-api/read", "tams-api/write", "tams-api/delete"]


def request_token():
    form_data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials",
        "scope": " ".join(OAUTH_SCOPES),
    }
    resp = requests.post(TOKEN_URL, data=form_data, timeout=30)
    resp.raise_for_status()
    return resp.json()
