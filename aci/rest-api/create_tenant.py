#!/usr/bin/env python

from aci_helper import req

def create_tn(tn_name):
    endpoint = f"mo/uni/tn-{tn_name}.json"
    payload = {
        "fvTenant" : {
            "attributes": {
            }
        }
    }
    resp = req(endpoint, method='post',json=payload)
    print(resp)

if __name__ == "__main__":
    create_tn("BL-rest-tenant")
