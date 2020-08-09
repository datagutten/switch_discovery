from .parser import Parser


class LLDP(Parser):
    def ip(self):
        return self.values['lldp.mgn.addr.ip4']

    def name(self):
        key = self.find_key(self.layer, 'System Name')
        return self.values['lldp.tlv.system.name']

    def platform(self):
        key = 'Telecommunications Industry Association ' \
              'TR-41 Committee - Inventory - Model Name'
        return self.values['lldp.media.model']

    def interface(self):
        return self.values['lldp.port.desc']

    def vlan(self):
        return self.values['lldp.ieee.802_1.port_vlan.id']