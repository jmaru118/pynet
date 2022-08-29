from netmiko import ConnectHandler 
from getpass import getpass 

devices = {
    "cisco3": {
        "host":  "cisco3.lasthop.io", 
        "username": "pyclass", 
        "password": getpass(), 
        "device_type": "cisco_ios",
        # "session_log": "my_session.txt"
    },
    "nxos1": {
        "host":  "nxos1.lasthop.io", 
        "username": "pyclass", 
        "password": getpass(), 
        "device_type": "cisco_nxos",
        # "session_log": "my_session.txt"
    },
    "nxos2": {
        "host":  "nxos2.lasthop.io", 
        "username": "pyclass", 
        "password": getpass(), 
        "device_type": "cisco_nxos",
        # "session_log": "my_session.txt"
    }
}

file = open('send.txt', 'w')
for device in devices:
    net_connect = ConnectHandler(**devices[device])
    print(net_connect.find_prompt())
    output = net_connect.send_command("show version")
    file.write(output)
file.close()
