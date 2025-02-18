numbers = (1,2,3,4,5,6,7,8,9,10)
my_tuple = (1,2,"Esther",[1,4,9])
my_tuple[3][1] = 59
print(my_tuple)
print(numbers)
x = (1,3,9)
y = (2,4,8)
print(x+y)
print(y*3)

z = ("a","p","p","l","e")
print(z.count("p"))
print(z.count("e"))

for x,y in enumerate(numbers):
    print(x,y)

print(all(my_tuple))
print(any(my_tuple))