from .parser import Parser


class CDP(Parser):
    def ip(self):
        data = self.layer['Management Addresses']
        key = self.find_key(data, 'IP address')
        return data[key]['cdp.nrgyz.ip_address']

    def name(self):
        return self.values['cdp.deviceid']

    def platform(self):
        value = self.values['cdp.platform']
        return value.replace('cisco ', '')

    def interface(self):
        return self.values['cdp.portid']

    def vlan(self):
        return self.values['cdp.native_vlan']
