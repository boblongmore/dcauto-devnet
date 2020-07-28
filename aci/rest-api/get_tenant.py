#!usr/bin/env python

#import req function to use in rest calls
from aci_helper import req
import json

def get_tenant():
    endpoint = "node/class/fvTenant.json"
    tenant_list = req(endpoint)
    return tenant_list


if __name__ == "__main__":
    tn_list = get_tenant()
    for tn in tn_list['imdata']:
        print(tn['fvTenant']['attributes']['name'])