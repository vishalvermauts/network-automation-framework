import requests
from requests.auth import HTTPBasicAuth
import urllib3
import json

# Ignore SSL warnings for sandbox
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://10.10.20.48/restconf/data/Cisco-IOS-XE-bgp-oper:bgp-state-data/neighbors"
auth = HTTPBasicAuth('developer', 'C1sco12345')
headers = {'Accept': 'application/yang-data+json'}

response = requests.get(url, auth=auth, headers=headers, verify=False)

if response.status_code == 200:
    data = response.json()
    # The BGP neighbor data is nested under the 'neighbor' list
    neighbors = data['Cisco-IOS-XE-bgp-oper:neighbors']['neighbor']
    
    print(f"{'Neighbor IP':<20} | {'Status':<15}")
    print("-" * 40)
    
    for n in neighbors:
        ip = n['neighbor-id']
        # Extract the state from the address-family info
        state = n['address-family-info'][0]['state']
        print(f"{ip:<20} | {state:<15}")
else:
    print(f"Audit Failed! Status Code: {response.status_code}")
