name = input("Enter your name: ")
answer_extrovert_introvert = ""
answer_sensing_intuition = ""
answer_thinking_feeling = ""
answer_judgement_perception = ""
answer_extrovert_introvert_a = ""
answer_extrovert_introvert_b = ""
answer_sensing_intuition_a = ""
answer_sensing_intuition_b = ""
answer_thinking_feeling_a = ""
answer_thinking_feeling_b = ""
answer_judgement_perception_a = ""
answer_judgement_perception_b = ""

personality = ""

first_section = [
	["A. Expend energy, enjoy groups", "B. Conserve energy, enjoy one-on-one"],
	["A.Interpret literally", "B. Look for meaning and possibilities"], 
	["A. More outgoing, think out loud", "B. More reserved, think to yourself"], 
	["A. Seek many tasks, public activities, interaction with others", "B. Seek private solitary activities with quiet to concentrate"], 
	["A. External, communicative, express yourself", "B. Internal, reticent, keep to yourself"]
]

second_section = [
	["A. Active, initiate", "B. Reflective, deliberate"],
	["A. Practical, realistic, experiential", "B. Imaginative, innovative, theoretical"],
	["A. Standard, usual, conventional", "B. Different, novel, unique"],
	["A. Focus on here-and-now", "B. Look to the future, global perspective, \"big picture\""],
	["A. Facts, things, \"what is\" ", "B. Ideas, dreams, \"what could be\", philosophical"]
]

third_section = [
	["A. Logical, thinking, questioning", "B. Empathetic, feeling, accommodating"],
	["A. Candid, straightforward, frank", "B. Tactful, kind, encouraging"],
	["A. Firm, tend to criticize, hold the line", "B. Gentle, tend to appreciate, conciliate"],
	["A. Tough-minded, just", "B. Tender-hearted, merciful"],
	["A. Matter of fact, issue-oriented", "B. Sensitive, people-oriented, compassionate"]
]

fourth_section = [
	["A. Organized orderly", "B. Flexible, adaptable"],
        ["A. Plan, schedule", "B. Unplanned, spontaneous"],
      	["A. Regulated, structured", "B. Easygoing, \"live and let live\""],
        ["A. Preparation, plan ahead", "B. Go with the flow, adapt as you go"],
        ["A. Control, govern", "B. Latitude, freedom"]
]

for i in range(0,5):
	print(f"{first_section[i][0]}, {first_section[i][1]}\n")
	response = input("Enter a response: ").strip()

	while response.casefold() not in ["a","b"]:
		print("Response is not A or B. Please try again.\n")
		response = input("Enter a response: ").strip
       		
	if response.casefold() == "a":
		answer_extrovert_introvert_a += response
	else:
		answer_extrovert_introvert_b += response

if len(answer_extrovert_introvert_a) > len(answer_extrovert_introvert_b):
	print("You are extroverted\n")
	personality += "E"
else:
	print("You are introverted\n")
	personality += "I"

for i in range(0,5):
	print(f"{second_section[i][0]}, {second_section[i][1]}\n")
	response = input("Enter a response: ").strip()
	
	while response.casefold() not in ["a","b"]:
		print("Response is not A or B. Please try again.\n")
		response = input("Enter a response: ").strip()

	if  response.casefold() == "a":
                answer_sensing_intuition_a += response
	else:
                answer_sensing_intuition_b += response
	
if len(answer_sensing_intuition_a) > len(answer_sensing_intuition_b):
	print("You are sensitive\n")
	personality += "S"
else:
	print("You are intuitive")
	personality += "N"
      	

for i in range(0,5):
	print(f"{third_section[i][0]}, {third_section[i][1]}\n")
	response = input("Enter a response: ").strip()
	while response.casefold() not in ["a","b"]:
		print("Response is not A or B. Please try again.\n")
		response = input("Enter a response: ").strip()
	if response.casefold() == "A":
		answerThinkingFeelingA += response
		answerThinkingFeelingB += response;

if len(answer_thinking_feeling_a) > len(answer_thinking_feeling_b) :
	print("You are thoughtful\n")
	personality += "T"
else:
		print("You are emotional")
		personality += "F"

for i in range(0,5):
	print(f"{fourth_section[i][0]}, {fourth_section[i][1]}\n")
	response = input("Enter a response: ").strip()
	
	while response.casefold() not in ["a","b"]:
		print("Response is not A or B. Please try again.\n")
		response = input("Enter a response: ").strip()

	if  response.casefold() == "A":
		answer_judgement_perception_a += response
	else:
		answer_judgement_perception_b += response

if len(answer_judgement_perception_a) > len(answer_judgement_perception_b):
	print("You are judgemental\n")
	personality += "J"
else:
	print("You are perceptive")
	personality += "P"


print("Your personality type is: " + personality)

match personality:
	case "ENFJ":
		print("ENFJ (Protagonist) is a personality type with the Extroverted, Intuitive, Feeling, and Judging traits. They are charismatic and inspiring leaders, often driven to help others realize their potential.")
	case "ENTJ":
		print("ENTJ (Commander) is a personality type with the Extroverted, Intuitive, Thinking, and Judging traits. Bold and imaginative, they are strong-willed leaders who enjoy organizing and directing people and projects.")
	case "INFP":
		print("INFP (Mediator) is a personality type with the Introverted, Intuitive, Feeling, and Prospecting traits. Idealistic and loyal to their values, they are driven by their beliefs and desire to make the world a better place.")
	case "INTJ":
		print("INTJ (Architect) is a personality type with the Introverted, Intuitive, Thinking, and Judging traits. These thoughtful tacticians love perfecting the details of life, applying creativity and rationality to everything they do. Their inner world is often a private, complex one.")
	case "ESFJ":
		print("ESFJ (Consul) is a personality type with the Extroverted, Sensing, Feeling, and Judging traits. Caring and social, they have a strong sense of duty and are eager to help others.")
	case "ESTJ":
		print("ESTJ (Executive) is a personality type with the Extroverted, Sensing, Thinking, and Judging traits. Organized and driven, they focus on results and managing tasks efficiently.")
	case "ISFP":
		print("ISFP (Adventurer) is a personality type with the Introverted, Sensing, Feeling, and Prospecting traits. Creative and spontaneous, they value freedom and often express themselves through art and other forms of creativity.")
	case "ISTP":
		print("ISTP (Virtuoso) is a personality type with the Introverted, Sensing, Thinking, and Prospecting traits. They tend to have an individualistic mindset, pursuing goals without needing much external connection. They engage in life with inquisitiveness and personal skill, varying their approach as needed.")
	case "ENFP":
		print("ENFP (Campaigner) is a personality type with the Extroverted, Intuitive, Feeling, and Prospecting traits. Enthusiastic and creative, they have a strong sense of possibility and are driven by their values and ideas.")
	case "ENTP":
		print("ENTP (Debater) is a personality type with the Extroverted, Intuitive, Thinking, and Prospecting traits. Quick-witted and clever, they enjoy the challenge of ideas and often think outside the box.")
	case "INTP":
		print("INTP (Logician) is a personality type with the Introverted, Intuitive, Thinking, and Prospecting traits. These flexible thinkers enjoy taking an unconventional approach to many aspects of life. They often seek out unlikely paths, mixing willingness to experiment with personal creativity.")
	case "ISFJ":
		print("ISFJ (Defender) is a personality type with the Introverted, Sensing, Feeling, and Judging traits. Warm and conscientious, they have a strong sense of duty and take pride in their responsibilities.")
	case "ISTJ":
		print("ISTJ (Logistician) is a personality type with the Introverted, Sensing, Thinking, and Judging traits. These people tend to be reserved yet willful, with a rational outlook on life. They compose their actions carefully and carry them out with methodical purpose.")
	case "ESFP":
		println("ESFP (Entertainer) is a personality type with the Extroverted, Sensing, Feeling, and Prospecting traits. Outgoing and spontaneous, they enjoy life in the moment and often seek new experiences.")
	case "ESTP":
		print("ESTP (Entrepreneur) is a personality type with the Extroverted, Sensing, Thinking, and Prospecting traits. Bold and perceptive, they take action to make things happen and enjoy living on the edge.")
	case "INFJ":
		print("INFJ (Advocate) is a personality type with the Introverted, Intuitive, Feeling, and Judging traits. They tend to approach life with deep thoughtfulness and imagination. Their inner vision, personal values, and a quiet, principled version of humanism guide them in all things.")
	case _:
		print("Your personality type is not recognized.")

