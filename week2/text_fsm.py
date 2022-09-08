from netmiko import ConnectHandler
from getpass import getpass

device = {
    "host":  "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**device)
output = net_connect.send_command("show version", use_textfsm = True)
print(output)
print("\n\n")

output = net_connect.send_command("show lldp neighbors detail", 
                                                        use_textfsm = True)
print(output)
neighbor_interface = output[0]["neighbor_interface"] 
print("neighbor_interface: " + neighbor_interface)
net_connect.disconnect()
