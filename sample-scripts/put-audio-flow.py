import json
import uuid
import requests
import credentials

new_flow_id = str(uuid.uuid4())
new_source_id = str(uuid.uuid4())

flow_input = {
    "id": new_flow_id,
    "source_id": new_source_id,
    "label": "<AUDIO FLOW LABEL>",
    "description": "<AUDIO FLOW DESCRIPTION>",
    "codec": "audio/aac",
    "container": "video/mp2t",
    "avg_bit_rate": 192000,
    "max_bit_rate": 192000,
    "format": "urn:x-nmos:format:audio",
    "essence_parameters": {
        "sample_rate": 48000,
        "channels": 2,
    },
}


def put_flow(access_token, json_input):
    resp = requests.put(
        f"{credentials.TAMS_URL}/flows/{new_flow_id}",
        data=json.dumps(json_input),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        },
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


creds = credentials.request_token()
response = put_flow(creds["access_token"], flow_input)
print(json.dumps(response, indent=2))
print("-------------------------------------------------")
print(f"New Audio Flow ID: {new_flow_id}")
print("-------------------------------------------------")
