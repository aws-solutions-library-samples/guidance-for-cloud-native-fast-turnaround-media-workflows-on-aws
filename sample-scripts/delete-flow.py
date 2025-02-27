import requests
import credentials

###########################

flow_id = "<FLOW ID>"  # ID of flow to be deleted

###########################


def delete_flow(access_token):
    resp = requests.delete(
        f"{credentials.TAMS_URL}/flows/{flow_id}",
        headers={"Authorization": f"Bearer {access_token}"},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


creds = credentials.request_token()
response = delete_flow(creds["access_token"])
print(response.status_code)
