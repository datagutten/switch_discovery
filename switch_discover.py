import asyncio
import json
import os
from asyncio import get_event_loop

import wx
from pyshark.tshark import tshark
from wxasync import AsyncBind, StartCoroutine, WxAsyncApp

from network_interfaces import network_interfaces
from switch_discover.gui.gui import SwitchFrame
from switch_discover.parsers.get_parser import get_parser
from switch_discover.utils import get_tshark_interfaces


class SwitchFrameExtension(SwitchFrame):
    selected_interface = {}
    counter = True
    seconds = 0

    def __init__(self, parent):
        super().__init__(parent)
        AsyncBind(wx.EVT_BUTTON, self.discoverSwitches, self.load_button)
        self.system_interfaces = get_tshark_interfaces()

    def setInterface(self, event):
        for interface in self.system_interfaces:
            if interface['name'] == event.String:
                self.selected_interface = interface
        self.updateInterfaceText()

    def updateInterfaceText(self):
        guid = network_interfaces.strip_guid(self.selected_interface['guid'])
        self.interface_ip.Label = network_interfaces.ip(guid)
        self.interface_mac.Label = network_interfaces.mac(guid)

    async def run(self, cmd):
        print('Run', cmd)
        proc = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)

        StartCoroutine(self.update_timer, self)
        print('Communicate')
        stdout, stderr = await proc.communicate()

        if stdout:
            self.counter = False
            self.show_output(stdout)
        if stderr:
            print(f'[stderr]\n{stderr.decode()}')

    def show_output(self, stdout):
        data = json.loads(stdout)
        layers = data[0]['_source']['layers']
        parser = get_parser(layers)

        self.switch_ip.Label = parser.ip()
        self.switch_name.Label = parser.name()
        self.switch_model.Label = parser.platform()
        self.vlan.Label = parser.vlan()
        self.port.Label = parser.interface()

    async def discoverSwitches(self, event):
        process = os.path.realpath(tshark.get_process_path())
        process = '"%s"' % process
        cmd = [process, '-i', self.selected_interface['number'], '-f', '"(ether[12:2]==0x88cc or ether[20:2]==0x2000)"',
               '-c', '1', '-T', 'json']

        args = ' '.join(cmd)

        self.load_button.Label = 'Wait...'
        self.load_button.Enable(False)
        self.interface_select.Enable(False)
        await self.run(args)
        self.load_button.Label = 'Discover'
        self.load_button.Enable(True)
        self.interface_select.Enable(True)

        print('After call')

    async def update_timer(self):
        self.counter = True
        while self.counter:
            self.load_button.Label = '%d sec' % self.seconds
            self.seconds += 1
            await asyncio.sleep(1)


app = WxAsyncApp(False)
frame = SwitchFrameExtension(None)

choices = []

default = None
for interface in frame.system_interfaces:
    choices.append(interface['name'])
    if not default and network_interfaces.ip(network_interfaces.strip_guid(interface['guid'])):
        default = int(interface['number']) - 1
        frame.selected_interface = interface

frame.interface_select.SetItems(choices)
if frame.selected_interface != {}:
    frame.interface_select.SetSelection(default)
    frame.updateInterfaceText()

frame.Show(True)
loop = get_event_loop()
loop.run_until_complete(app.MainLoop())
