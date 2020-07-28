#!/usr/bin/env python

from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()

requests.packages.urllib3.disable_warnings()

def get_token():
    load_dotenv()
    payload = {
        "aaaUser":{
            "attributes": {
                "name": os.getenv('UN'),
                "pwd": os.getenv('PW')
            }
        }
    }
    URL = f"https://{os.getenv('APIC')}/api/aaaLogin.json"
    headers = {
        "Content-Type": "application/json"
    }
    resp = requests.post(url=URL, headers=headers, json=payload, verify=False).json()
    apic_token = resp['imdata'][0]['aaaLogin']['attributes']['token']
    return apic_token

def req(endpoint, method='get', json=None):
    #define headers, then use get-token function to add APIC-cookie to headers
    load_dotenv()
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    cookies = {
        "APIC-Cookie": get_token()
    }
    #headers["APIC-Cookie"] = get_token()
    #print(headers)

    resp = requests.request(url=f"https://{os.getenv('APIC')}/api/{endpoint}", method=method, headers=headers, cookies=cookies, json=json, verify=False)

    return resp.json()






if __name__ == "__main__":
    token = get_token()
    print(token)
    
