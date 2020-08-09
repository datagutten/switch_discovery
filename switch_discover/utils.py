import os
import re
import subprocess

from pyshark.tshark.tshark import get_process_path


def get_tshark_interfaces(tshark_path=None):
    """Returns a list of interface numbers from the output tshark -D.

    """
    parameters = [get_process_path(tshark_path), "-D"]
    process = subprocess.run(parameters, capture_output=True)
    tshark_interfaces = process.stdout.decode('utf-8')
    # with open(os.devnull, "w") as null:
    # tshark_interfaces = subprocess.check_output(parameters, stderr=null).decode("utf-8")

    interfaces = []
    # for line in tshark_interfaces.splitlines():
    pattern = r'(?P<number>[0-9]+)\.\s(?P<guid>\\Device.+\}|[a-z0-9]+)(?:\s\((?P<name>.+)\))?'
    # matches = re.finditer(r'(?P<number>[0-9]+)\.\s(?P<guid>\\Device.+\})\s\((?P<name>.+)\)', tshark_interfaces)
    matches = re.finditer(pattern, tshark_interfaces)
    for match in matches:
        interfaces.append(match.groupdict())

    return interfaces
