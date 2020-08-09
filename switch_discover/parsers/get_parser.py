from switch_discover.parsers.CDP import CDP
from switch_discover.parsers.LLDP import LLDP


def get_parser(layers):
    if 'cdp' in layers:
        return CDP(layers['cdp'])
    elif 'lldp' in layers:
        return LLDP(layers['lldp'])
