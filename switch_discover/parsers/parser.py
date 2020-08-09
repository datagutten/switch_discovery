class Parser:
    def __init__(self, layer):
        self.layer = layer
        self.values = self.get_values()

    @staticmethod
    def find_key(values, partial_key):
        for key in values.keys():
            strings = [partial_key, ' [truncated]' + partial_key]
            for string in strings:
                if key.find(string) == 0:
                    return key

    def get_values(self, root=None):
        if not root:
            root = self.layer
        values = {}
        for key, value in root.items():
            if type(value) == dict:
                values.update(self.get_values(value))
            else:
                values[key] = value
        return values

    def name(self):
        pass

    def ip(self):
        pass
