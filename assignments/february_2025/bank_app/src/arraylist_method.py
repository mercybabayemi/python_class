class ArrayListMethod:
    def __init__(self):
        self.capacity = 3
        self.array = []

    def size(self):
        return len(self.array)

    def is_empty(self):
        return len(self.array) == 0

    def add(self, element):
        if element is None:
            raise ValueError("Argument cannot be null")
        if self.is_full():
            self.increase_capacity()
        self.array.append(element)

    def increase_capacity(self):
        self.capacity *= 2

    def is_full(self):
        return len(self.array) == self.capacity

    def add_at_index(self, index, element):
        if element is None:
            raise ValueError("Argument cannot be null")
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.is_full():
            self.increase_capacity()
        self.array.insert(index, element)

    def remove(self, element):
        try:
            self.array.remove(element)
            self.size -= 1
        except ValueError:
            raise ValueError("Element not found!")

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]

    def set(self, index, element):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.array[index] = element

    def contains(self, element):
        return element in self.array

    def clear(self):
        self.array.clear()

    def remove_at(self, index):
        if index < 0 or index >= len(self.array):
            raise IndexError("Index out of bounds")
        self.array.pop(index)

    def remove_all(self):
        self.array.clear()