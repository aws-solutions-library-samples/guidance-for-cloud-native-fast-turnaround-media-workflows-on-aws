import json
import requests
import credentials


def get_service(access_token):
    resp = requests.get(
        f"{credentials.TAMS_URL}/service",
        headers={"Authorization": f"Bearer {access_token}"},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


creds = credentials.request_token()
response = get_service(creds["access_token"])
print(json.dumps(response, indent=2))
