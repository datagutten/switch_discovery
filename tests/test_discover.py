import json
import unittest

import ddt

from switch_discover.parsers.CDP import CDP
from switch_discover.parsers.get_parser import get_parser
from switch_discover.parsers.LLDP import LLDP
from switch_discover.parsers.parser import Parser

classes = [[CDP, 'test_data/cdp.json', 'cdp'], [LLDP, 'test_data/lldp.json', 'lldp']]
files = ['test_data/cdp.json', 'test_data/lldp.json']


@ddt.ddt
class DiscoverTestCase(unittest.TestCase):
    parser_class = Parser

    @staticmethod
    def load_data(file):
        with open(file, 'r') as fp:
            data = json.load(fp)

        return data[0]['_source']['layers']

    @ddt.idata(files)
    def test_fields(self, file):
        parser = get_parser(self.load_data(file))
        # print(parser_class)
        self.assertEqual('192.168.1.116', parser.ip())
        self.assertEqual('Anders-2960', parser.name())
        self.assertEqual('WS-C2960G-8TC-L', parser.platform())
        self.assertEqual('1', parser.vlan())
        self.assertEqual('GigabitEthernet0/3', parser.interface())


if __name__ == '__main__':
    unittest.main()
