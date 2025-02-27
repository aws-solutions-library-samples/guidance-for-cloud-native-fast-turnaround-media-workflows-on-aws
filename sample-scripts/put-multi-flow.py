import uuid
import json
import requests
import credentials

###########################

video_flow_id = "<VIDEO FLOW ID>"
audio_flow_id = "<AUDIO FLOW ID>"

###########################

new_flow_id = str(uuid.uuid4())
new_source_id = str(uuid.uuid4())

flow_input = {
    "id": new_flow_id,
    "source_id": new_source_id,
    "label": "<FLOW LABEL>",
    "description": "<FLOW DESCRIPTION>",
    "format": "urn:x-nmos:format:multi",
    "flow_collection": [
        {
            "id": video_flow_id,
            "role": "video",
        },
        {
            "id": audio_flow_id,
            "role": "audio",
        },
    ],
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
print(f"New Multi Flow ID: {new_flow_id}")
print("-------------------------------------------------")
