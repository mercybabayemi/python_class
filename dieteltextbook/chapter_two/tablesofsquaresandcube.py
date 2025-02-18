header = ("number\tsquare\tcube")
print(header)

number = 0
counter = 0

while counter <= 5:
    square = number * number
    cube = number * number * number
    number += 1
    counter += 1
    print(f"{number}\t{square}\t{cube}")