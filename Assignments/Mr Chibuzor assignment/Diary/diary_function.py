diaries = []

def add_diary(diary_id, diary_date, diary_content):
	diary_entry = {
		"diary_id" : diary_id,
		"diary_date" : diary_date,
		"diary_content" : diary_content,
		"is_locked" : False
	}
	diaries.append(diary_entry)
	return "Diary entry created successfully!"

def view_diaries():
	if not diaries:
		return "No diary entries found."
	else:
		for entry in diaries:
			return f"Diary ID: {entry["diary_id"]},Date: {entry["diary_date"]},Content: {entry["diary_content"]},Locked: {entry["is_locked"]}\n"


def update_diary(diary_id, new_id = None, new_date = None, new_content = None):
	for entry in diaries:
		if entry["diary_id"] == diary_id:
			if new_id:
				entry["diary_id"] = new_id
			if new_date:
				entry["diary_date"] = new_date
			if new_content:
				entry["diary_content"] = new_content
			return "Diary entry updated successfully!"
	return "Diary entry not found!"

def delete_diary(diary_id):
	for entry in diaries:
		if entry['diary_id'] == diary_id:
			diaries.remove(entry)
			return "Diary entry removed successfully."
	return "Diary entry not found!"