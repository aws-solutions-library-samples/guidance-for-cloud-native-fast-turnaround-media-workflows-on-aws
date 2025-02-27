import json
import requests
import credentials


def list_sources(access_token):
    resp = requests.get(
        f"{credentials.TAMS_URL}/sources",
        headers={"Authorization": f"Bearer {access_token}"},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


creds = credentials.request_token()
response = list_sources(creds["access_token"])
print(json.dumps(response, indent=2))
