from entry import Entry
from security_error import SecurityError


class Diary:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_locked = True
        self.entries = []
        self.last_entry_id = 0

    def get_is_locked(self):
        return self.is_locked


    def unlock_diary(self, password):
        if self.password == password:
            self.is_locked = False
        else:
            raise SecurityError("Passwords do not match")

    def lock_diary(self):
        self.is_locked = True

    def create_entry(self, title, entry_body):
        self.last_entry_id += 1
        new_entry = Entry(self.last_entry_id, title, entry_body)
        self.entries.append(new_entry)
        return new_entry.get_id()

    def size(self):
        return len(self.entries)

    def delete_entry(self, id):
        if id <= 0 or id > len(self.entries):
            raise IndexError(f"Index {id} out of bounds for {len(self.entries)}")
        entry_to_delete = self.entries[id - 1]
        self.entries.remove(entry_to_delete)
        self.last_entry_id -= 1

    def find_entry_by_id(self, id):
        if id <= 0 or id > len(self.entries):
            raise IndexError(f"Index {id} out of bounds for {len(self.entries)}")
        return self.entries[id - 1]

    def update_entry(self, id, title, entry_body):
        if id <= 0 or id > len(self.entries):
            raise IndexError(f"Index {id} out of bounds for {len(self.entries)}")
        entry = self.find_entry_by_id(id)
        entry.set_title(title)
        entry.set_entry_body(entry_body)

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password


