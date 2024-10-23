#NegativePositiveZeroValues

positive_number = 0
negative_number = 0
zero_number = 0
count = 0
	
while count < 5:	
    number = int(input("Enter your number: "))
	
    if number < 0:
      negative_number += 1
    elif number > 0:
      positive_number += 1
    else:
      zero_number += 1
    count +=1

print(f"Positive number is ", positive_number, "\n")
print(f"Negative number is ", negative_number , "\n")
print(f"Zero number is ", zero_number






 )
