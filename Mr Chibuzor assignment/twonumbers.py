sum = 0
counter = 1
stop = -1

while counter <= 2:
    number = int(input("Enter number or -1 to terminate: "))
    sum = sum + number
    counter = counter + 1
    answer = int(input("DO you wish to continue, press 1 for(Yes) or 2 for(no) to exit"))
    if answer == 1:
        continue
    elif answer == 2:
        break

print(f"The sum is {sum}")
