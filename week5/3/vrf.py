from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

vrfs = [ 
    {
    "vrf_name": "white",
    "rd_number": "500:1",
    "ipv4_af": True,
    "ipv6_af": True
    },
    {
    "vrf_name": "blue",
    "rd_number": "100:1",
    "ipv4_af": True,
    "ipv6_af": True
    },
    {
    "vrf_name": "red",
    "rd_number": "200:1",
    "ipv4_af": True,
    "ipv6_af": True
    },
    {
    "vrf_name": "green",
    "rd_number": "300:1",
    "ipv4_af": True,
    "ipv6_af": True
    },
    {
    "vrf_name": "yellow",
    "rd_number": "400:1",
    "ipv4_af": True,
    "ipv6_af": True
    }
]

template_file = "vrf.j2"
template = env.get_template(template_file)
cfg = ""
for vrf in vrfs:
    cfg += template.render(**vrf)
print(cfg)
print()
