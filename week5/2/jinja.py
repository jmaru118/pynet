from jinja2 import Template

filename = "bgp_config.j2"
with open(filename) as f:
    my_template = f.read()

my_vars = {
    "local_as": 10,
    "peer1_ip": "10.1.20.2",
    "peer1_as": 20,
    "peer2_ip": "10.1.30.2",
    "peer2_as": 30
}

j2_template = Template(my_template)
output = j2_template.render(**my_vars)
print(output)

