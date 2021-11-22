import json
import requests
import os

headers = {"content-type": "application/json", "authorization": "Bearer <token>"}
local_url = 'http://localhost:4000/api/v3/searchsuggestranker'
staging_url = 'http://staging.compass.com/api/v3/searchsuggestranker'

def call_SSR_v5(data):
    pr = json.dumps(data)
    parsed_req = json.loads(pr)
    #parsed_req['apiVersion'] = 'v5.0'
    resp = requests.post(staging_url, json=parsed_req, headers=headers, verify=False)
    return resp

def load_file():
    json_file_path = "/Users/gurpreet.kaur/Downloads/dev_pipeline.json"
    response_list = []
    with open(json_file_path, 'r') as j:
        contents = json.loads(j.read())
    for request_item in contents:
        response = call_SSR_v5(request_item)
        print(response.json())
        response_list.append(response.json())

    with open("/Users/gurpreet.kaur/Downloads/v5_results.json", 'w') as f:
        json.dump(response_list,f)


load_file()
