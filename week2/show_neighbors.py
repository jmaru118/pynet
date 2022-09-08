from netmiko import ConnectHandler 
from getpass import getpass 
import time

device = {
    "host":  "nxos2.lasthop.io", 
    "username": "pyclass", 
    "password": getpass(), 
    "device_type": "cisco_nxos",
    "global_delay_factor": 2,
    "fast_cli": "False"
}

# No-delay implementation
net_connect = ConnectHandler(**device)
output = ""
cmd = "show lldp neighbors detail"
start = time.time()
output += net_connect.send_command_timing(cmd, strip_command = False,
                                                    strip_prompt = False)
end = time.time()
elapsed_time = end - start
print(output)
print("\nElapsed Time: " + str(elapsed_time))

# delay implementation
output = ""
cmd = "show lldp neighbors detail"
start = time.time()
output += net_connect.send_command_timing(cmd, delay_factor = 8, 
                            strip_command = False, strip_prompt = False)
end = time.time()
elapsed_time = end - start
print(output)
print("\nElapsed Time With Delay: " + str(elapsed_time))

net_connect.disconnect()
