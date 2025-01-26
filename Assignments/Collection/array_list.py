class ArrayList():
    def __init__(self):
        self.capacity = 3
        self.array = [None] * self.capacity
        self.size_v = 0
        self.type = None

    def size(self):
        return self.size_v

    def is_empty(self):
        return self.size_v == 0

    def add(self, item):
        if self.type is None:
            self.type = type(item)  # Set the type when first item is added
        elif not isinstance(item, self.type):
            raise TypeError(f"All elements must be of type {self.type}")

        if self.is_full():
            self.increase_capacity()
        self.array[self.size_v] = item
        self.size_v += 1

    def is_full(self):
        return self.size_v == self.capacity

    def increase_capacity(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        for i in range(self.size_v):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def add_at(self, index, item):
        if self.type is None:
            self.type = type(item)
        elif not isinstance(item, self.type):
            raise TypeError(f"All elements must be of type {self.type}")

        if self.is_full():
            self.increase_capacity()
        if index < 0 or index > self.size_v:
            raise IndexError("Index out of bounds")
        for i in range(self.size_v, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = item
        self.size_v += 1

    def get(self, index):
        if index < 0 or index >= self.size_v:
            raise IndexError("Index out of bounds")
        return self.array[index]

    def set(self, index, item):
        if index < 0 or index >= self.size_v:
            raise IndexError("Index out of bounds")
        if index > 0 and index <= self.size_v - 1:
            self.array[index] = item

    def remove(self, item):
        index_to_remove = -1
        for i in range(self.size_v):
            if self.array[i] == item:
                index_to_remove = i
                break
        if index_to_remove == -1:
            raise ValueError(f"{item} not found in the list")

        for i in range(index_to_remove, self.size_v - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size_v - 1] = None
        self.size_v -= 1

    def clear(self):
        self.array = [None] * self.capacity
        self.size_v = 0

    def contains(self, item):
        for i in range(self.size_v):
            if self.array[i] == item:
                return True
        return False
