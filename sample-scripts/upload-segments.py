import os
import json
import requests
import credentials

###########################

video_flow_id = "<VIDEO FLOW ID>"
audio_flow_id = "<AUDIO FLOW ID>"

###########################


def upload_file(access_token, flow_id, file_name):
    get_url = requests.post(
        f"{credentials.TAMS_URL}/flows/{flow_id}/storage",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        },
        data=json.dumps({"limit": 1}),
        timeout=30,
    )
    print(f"  TAMS get segments storage status code: {get_url.status_code}")
    media_object = get_url.json()["media_objects"][0]
    put_file = requests.put(
        media_object["put_url"]["url"],
        headers={"Content-Type": media_object["put_url"]["content-type"]},
        files={"file": open(f"segments/{file_name}", "rb")},
        timeout=30,
    )
    print(f"  Object upload status code: {put_file.status_code}")
    return media_object["object_id"]


def register_segment(access_token, flow_id, object_id, timerange):
    segment_json = {
        "object_id": object_id,
        "timerange": timerange,
    }

    put_segment = requests.post(
        f"{credentials.TAMS_URL}/flows/{flow_id}/segments",
        data=json.dumps(segment_json),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        },
        timeout=30,
    )
    print(f"  Put segment metadata status code: {put_segment.status_code}")

def upload_audio(folder):
    for file_name in os.listdir(folder):
        if file_name.endswith(".aac"):
            segment_no = int(file_name.split("_audio_")[1].split(".")[0])
            start_time = segment_no * segment_duration - 10
            end_time = segment_no * segment_duration
            timerange = f"[{start_time}:0_{end_time}:0)"
            print(f" Filename: {file_name} | Timerange: {timerange}")

            upload_response = upload_file(
                creds["access_token"], audio_flow_id, file_name
            )
            print(f"  TAMS Object ID: {upload_response}")

            register_segment(
                creds["access_token"], audio_flow_id, upload_response, timerange
            )


def upload_video(folder):
    for file_name in os.listdir(folder):
        if file_name.endswith(".ts"):
            segment_no = int(file_name.split("_video_")[1].split(".")[0])
            start_time = segment_no * segment_duration - 10
            end_time = segment_no * segment_duration
            timerange = f"[{start_time}:0_{end_time}:0)"
            print(f" Filename: {file_name} | Timerange: {timerange}")

            upload_response = upload_file(
                creds["access_token"], video_flow_id, file_name
            )
            print(f"  TAMS Object ID: {upload_response}")

            register_segment(
                creds["access_token"], video_flow_id, upload_response, timerange
            )


creds = credentials.request_token()
segment_duration = 10

print("Uploading audio segments....")
upload_audio("segments")

print("Uploading video segments....")
upload_video("segments")