from diary import Diary
from no_such_element_exception import NoSuchElementException


class Diaries:
    def __init__(self):
        self.diaries = []

    def add(self, username, password):
        new_diary = Diary(username, password)
        self.diaries.append(new_diary)

    def find_by_username(self, username):
        for diary in self.diaries:
            if diary.get_username() == username:
                return diary
        raise NoSuchElementException(f"No diary found with username {username}")

    def delete(self, username, password):
        diary_to_delete = None
        for diary in self.diaries:
            if diary.get_password() == password and diary.get_username() == username:
                diary_to_delete = diary
                break
        if diary_to_delete is None:
            raise NoSuchElementException(f"No diary found with username {username} and password ")
        self.diaries.remove(diary_to_delete)

    def get_all_diaries(self):
        return self.diaries

    def size(self):
        return len(self.diaries)
