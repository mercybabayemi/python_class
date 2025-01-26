from assignments.collection.array_list import ArrayList


class SetMethod:
    def __init__(self):
        self.list = ArrayList()

    def is_empty(self):
        return self.list.is_empty()

    def add(self, first_example):
        if first_example is None:
            raise ValueError("Argument cannot be null")
        if self.contains(first_example):
            raise ValueError("Duplicate entry")
        self.list.add(first_example)

    def size(self):
        return self.list.size()

    def remove(self, second_example):
        self.list.remove(second_example)

    def clear(self):
        self.list.clear()

    def contains(self, first_example):
        return self.list.contains(first_example)