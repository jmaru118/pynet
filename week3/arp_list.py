data = """
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""

data = data.strip()
data_list = data.splitlines()
data_list = data_list[1:]
formatted_data = []

for entry in data_list:
    _, ip_addr, _, mac_addr, _, intf = entry.split()
    entry_dict = {"mac_addr" : mac_addr, "ip_addr" : ip_addr, "interface" : intf}
    formatted_data.append(entry_dict)

print(formatted_data)
