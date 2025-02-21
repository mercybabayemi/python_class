def add_diary(diary_id, diary_date, diary_content):
	diary_entry = {
		"diary_id" : diary_id,
		"diary_date" : diary_date,
		"diary_content" : diary_content,
		"is_locked" : False
	}
	print("Diary entry created successfully!")
	return diaries.append(diary_entry)

def view_diaries():
	if diaries == None:
		print("No diary entries found.")
	else:
		for entry in diaries:
			print(f"Diary ID: {entry["diary_id"]}\nDate: {entry["diary_date"]}\nContent: {entry["diary_content"]}\nLocked: {entry["is_locked"]}\n")


def update_diary(diary_id, new_id = None, new_date = None, new_content = None):
	for entry in diaries:
		if entry["diary_id"] == diary_id:
			if new_id is not None:
				entry["diary_id"] = new_id
			if new_date is not None:
				entry["diary_date"] = new_date
			if new_content is not None:
				entry["diary_content"] = new_content
			print("Diary entry updated successfully!")
			return
	print("Diary entry not found!")

def delete_diary(diary_id):
	for entry in diaries:
		if entry['diary_id'] == diary_id:
			diaries.remove(entry)
			print("Diary entry removed successfully.")
			return
	print("Diary entry not found!")



  
diaries = []   

diary_determinant = input("Do you want to create a new diary ?\n(Enter yes or no): ")
while diary_determinant.casefold() == "yes":
	response = int(input("Welcome To Your Diary App!!!\nWhat do you want to do?\n1. Add new diary\n2. View diary entries\n3. Update a diary entry\n4. Delete a diary entry\n5. Exit\nEnter numerical value: "))

	match response:
		case 1:
			diary_id = int(input("Enter diary ID: "))
			diary_date = input("Enter diary date(dd-mm-yyyy): ")
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
		case 2:
			view_diaries()
		case 3:
			diary_id = int(input("Enter the diary ID to update: "))
			new_id_input = (input("Enter the new diary ID to update or press enter key to continue: "))
			new_date = (input("Enter the new diary date to update or press enter key to continue: "))
			new_content = (input("Enter the new diary content update or press enter key to continue: "))

			new_id = int(new_id_input) if new_id_input else None

			update_diary(diary_id, new_id, new_date, new_content)
		case 4:
			diary_id = int(input("Enter the diary ID to update: "))
			delete_diary(diary_id)
		case 5:
			print("Exiting>>>")
		case _:
			print("Invalid choice!!!\nPlease try again")


	diary_determinant = input("Do you want to create a new diary ?\n(Enter yes or no): ")


