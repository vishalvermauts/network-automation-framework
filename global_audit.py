from netmiko import ConnectHandler

devices = [
    {"device_type": "cisco_xe", "host": "10.10.20.48", "username": "developer", "password": "C1sco12345"},
    {"device_type": "cisco_nxos", "host": "10.10.20.40", "username": "admin", "password": "RG!_Yw200"}
]

command = "show ip int brief"

for dev in devices:
    print(f"\n--- SSH AUDIT: {dev['host']} ---")
    try:
        net_connect = ConnectHandler(**dev)
        output = net_connect.send_command(command)
        print(output)
        net_connect.disconnect()
    except Exception as e:
        print(f"Failed to connect: {e}")
