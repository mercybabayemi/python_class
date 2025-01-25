start = int(input("Enter the start value: "))
 
stop = int(input("Enter the stop value: "))

number_range = int(input("Enter the range value: ")) 

count = 0 


while start <= stop:
    if start % 3 == 0:
      count += 1
    start +=1

print(count)