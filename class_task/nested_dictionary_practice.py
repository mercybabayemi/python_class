school_records = {
     "class_1":{
         "students":[
             {"name": "Harry", "scores": {"Math":88,"English":76}},
              {"name": "Solomon", "scores": {"Math":95,"English":89}},
        ]
     },
     "class_2":{
         "students": [
             {"name": "Daniel", "scores": {"Math": 78, "English": 72}},
              {"name": "Samuel", "scores": {"Math": 85, "English": 80}},
         ]
     }
 }



calculated_total = 0
student_counter = 0
for value in school_records.values():
     for student in value["students"]:
         calculated_total += student["scores"]["Math"]
         student_counter += 1
average = calculated_total / student_counter
print(average)
