class Diary:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_locked = True
        self.entries = []
        self.entry_count = 0

    def unlock_diary(self, password):
        self.is_locked = password != self.password

    def is_locked(self):
        return self.is_locked

    def lock_diary(self):
        self.is_locked = True

    def create_entry(self, title, entry_body):
        self.entry_count += 1
        entry = Entry(self.entry_count, title, entry_body)
        self.entries.append(entry)
        return entry.get_id()

    def size(self):
        return len(self.entries)

    def delete_entry(self, entry_id):
        if entry_id <= 0 or entry_id > len(self.entries):
            raise IndexError(f"Index {entry_id} out of bounds for {len(self.entries)} entries")
        entry_to_delete = self.entries[entry_id - 1]
        self.entries.remove(entry_to_delete)
        self.entry_count -= 1

    def find_entry_by_id(self, entry_id):
        if entry_id <= 0 or entry_id > len(self.entries):
            raise IndexError(f"Index {entry_id} out of bounds for {len(self.entries)} entries")
        return self.entries[entry_id - 1]

    def update_entry(self, entry_id, title, entry_body):
        if entry_id <= 0 or entry_id > len(self.entries):
            raise IndexError(f"Index {entry_id} out of bounds for {len(self.entries)} entries")
        entry = self.find_entry_by_id(entry_id)
        entry.set_title(title)
        entry.set_entry_body(entry_body)

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def __str__(self):
        return f"Diary [Username: {self.username}, Entries: {len(self.entries)}]"
