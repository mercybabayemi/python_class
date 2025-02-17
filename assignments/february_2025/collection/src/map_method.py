class MapMethod:
    def __init__(self):
        self.keys = []
        self.values = []

    def is_empty(self) -> bool:
        return len(self.keys) == 0 and len(self.values) == 0

    def size(self):
        return len(self.keys) and len(self.values)

    def put(self, key, value):
        self.keys.append(key)
        self.values.append(value)

    def contains_value(self, value):
        return value in self.values

    def contains_key(self, key):
        return key in self.keys

    def get(self, key):
        if key in self.keys:
            index = self.keys.index(key)
            return self.values[index]
        return None

    def remove(self, key):
        if key in self.keys:
            index = self.keys.index(key)
            self.keys.pop(index)
            return self.values.pop(index)
        return None

    def clear(self):
        self.keys.clear()
        self.values.clear()
