def add_diary(diary_id, diary_date, diary_content):
	diary_entry = {
		"diary _id" : diary_id,
		"diary_date" : diary_date,
		"diary_content" : diary_content,
		"is_locked" : False
	}
	print("Diary entry created successfully!")
	return diaries.append(diary_entry)

  
diaries = []     	
diary_id = int(input("Enter diary ID: "))
diary_date = input("Enter diary date: ")
diary_content = input("Enter diary content: ")


add_diary(diary_id, diary_date, diary_content)       
lock_response = input("Do you want to lock the diary?\n(Enter yes or no): ")
lock_comparison = "yes"
if lock_response.lower() == lock_comparison.lower():
	is_locked = True
	print("The diary is now locked.")
	for diary_entry in diaries:
		diary_entry["is_locked"] = is_locked
if lock_response.lower() != lock_comparison.lower():
	is_locked = False
	print("The diary is now unlocked.")
	for diary_entry in diaries:
		diary_entry["is_locked"] = is_locked
print(diaries)