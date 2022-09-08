from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host":  "nxos1.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_nxos",
}
device2 = {
    "host":  "nxos2.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_nxos",
}

for device in (device1, device2):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_from_file(config_file="vlan_changes.txt")
    print(output)
    net_connect.save_config()
    net_connect.disconnect()
