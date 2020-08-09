import re

import netifaces


def strip_guid(guid):
    return re.sub(r'.*({[A-F0-9\-]+}).*', r'\1', guid)


def address(interface, address_type, field='addr'):
    try:
        return netifaces.ifaddresses(interface)[address_type][0][field]
    except KeyError:
        return ''
    except ValueError:
        return ''


def ip(interface):
    return address(interface, netifaces.AF_INET)


def mac(interface):
    return address(interface, netifaces.AF_LINK)