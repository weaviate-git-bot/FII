from .allow_only_get import AllowOnlyGet
from .allow_only_post import AllowOnlyPost
from .allow_traffic_only_on_port_80 import AllowTrafficOnlyOnPort
from .deny_payloads import DenyPayloads

FILTERS_LIST = [
    AllowOnlyGet,
    AllowOnlyPost,
    AllowTrafficOnlyOnPort,
    DenyPayloads
]