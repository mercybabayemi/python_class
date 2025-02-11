def get_score(subjects):
	students = []
	scores = []
	subjects = ["python", "java", "data science", "critical thinking"]

	for i in range(10):
		name = input(f"Enter students {i+1} name: ")
		students.append(name)
		
		for i in range (4):
			subject = subjects[i]
				
			score = int(input(f"Enter {name} {subject} score: "))
	
			while(score < 1 or score > 100):
		
				score = int(input(f"Enter {name} {subject} score: "))
				scores.append(score)

				print(f" {name} score for {subjects[i]} is {score}")
	return scores

print(get_score("python"))