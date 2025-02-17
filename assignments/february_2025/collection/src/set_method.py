class SetMethod:
    def __init__(self):
        self.list = []

    def is_empty(self):
        if len(self.list) == 0:
            return True
        return False

    def add(self, item):
        if item is None:
            raise ValueError("Cannot add None")
        if item not in self.list:
            self.list.append(item)
        else:
            raise ValueError("Duplicate entry")

    def size(self):
        return len(self.list)

    def remove(self, item):
        if item in self.list:
            self.list.remove(item)
        else:
            raise ValueError("Element not found")

    def clear(self):
        self.list.clear()

    def contains(self, item):
        return item in self.list

