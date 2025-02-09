class Entry:
    def __init__(self, entry_id, title, body):
        self.id = entry_id
        self.title = title
        self.body = body
        self.date_created = date.today()

    def get_id(self):
        return self.id

    def set_title(self, new_title):
        self.title = new_title

    def get_title(self):
        return self.title

    def set_entry_body(self, new_body):
        self.body = new_body

    def get_entry_body(self):
        return self.body

    def __str__(self):
        return f"ID: {self.id}\nTitle: {self.title}\nBody: {self.body}\nDateCreated: {self.date_created}"