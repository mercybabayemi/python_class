message = """ Enter 1 for java 
Enter 2 for python:  """

options = int(input(message))
match options: 
	case 1:
		print("This is java")
	case 2: 
		print("Python is great")
	case _:
		print("Default")