from netmiko import ConnectHandler
from getpass import getpass

cisco4 = {
    "host":  "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_ios",
}

# send_command_timing with extended ping
net_connect = ConnectHandler(**cisco4)
output = ""
commands = [ "ping", '\n', '8.8.8.8', '\n', '\n', '\n', '\n', '\n' ]
for cmd in commands:
    output += net_connect.send_command_timing(cmd, strip_command = False,
                                                    strip_prompt = False)

print("#### SEND_COMMAND_TIMING IMPLEMENTATION ####")
print(output)

# send_command with extended ping
output = ""
commands = [ "ping", '\n', '8.8.8.8', '\n', '\n', '\n', '\n', '\n' ]
for cmd in commands:
    output += net_connect.send_command(cmd, expect_string = r':',
                            strip_command = False, strip_prompt = False)

print("\n\n#### SEND_COMMAND IMPLEMENTATION ####")
print(output)
