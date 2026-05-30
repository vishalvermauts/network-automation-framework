import yaml
from netmiko import ConnectHandler

def run_audit():
    # 1. Load the inventory from YAML
    with open("inventory.yaml", "r") as f:
        inventory = yaml.safe_load(f)

    # 2. Iterate through each device
    for dev in inventory['devices']:
        print(f"\n--- SSH AUDIT: {dev['name']} ({dev['host']}) ---")
        
        # 3. Choose the command based on the operating system
        if dev['device_type'] == 'cisco_nxos':
            cmd = "show interface brief"
        else:
            cmd = "show ip int brief"
        
        # 4. Prepare connection parameters (excluding 'name' which causes errors)
        connection_params = {
            "device_type": dev["device_type"],
            "host": dev["host"],
            "username": dev["username"],
            "password": dev["password"]
        }
        
        # 5. Connect and execute
        try:
            with ConnectHandler(**connection_params) as net_connect:
                output = net_connect.send_command(cmd)
                print(output)
        except Exception as e:
            print(f"Failed to connect: {e}")

if __name__ == "__main__":
    run_audit()
