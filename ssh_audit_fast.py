import yaml
from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor

# Load inventory
with open("inventory.yaml", "r") as f:
    inventory = yaml.safe_load(f)

def audit_device(dev):
    # Select command based on platform
    cmd = "show interface brief" if dev['device_type'] == 'cisco_nxos' else "show ip int brief"
    
    # Clean params
    params = {k: v for k, v in dev.items() if k in ['device_type', 'host', 'username', 'password']}
    
    try:
        with ConnectHandler(**params) as net_connect:
            output = net_connect.send_command(cmd)
            return f"\n--- RESULTS: {dev['name']} ---\n{output}"
    except Exception as e:
        return f"\n--- ERROR: {dev['name']} ---\n{e}"

# Run tasks in parallel
with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(audit_device, inventory['devices'])

for result in results:
    print(result)
