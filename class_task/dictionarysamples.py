my_dict = {"name" : "Alice", "age" : 25, "city" : "New York"}
print(my_dict)
print(my_dict["name"])
print(my_dict.get("age"))

if "city" in my_dict:
	print("City is in the dictionary.")

del my_dict["city"]
print(my_dict)

print(my_dict.get("name"))
print(my_dict.get("salary","Salary not available."))

my_dict["city"] = "Lagos"
print(my_dict)

for key in my_dict:
	print(key)

for value in my_dict.values():
	print(value)

for key, value in my_dict.items():
	print(f"{key}:{value}")

squared = {x: x**2 for x in range(1,6)}
print(squared)


my_items = ['ac', 'board', 'chairs']
size = [4, 2, 40]
our_class = {}
for key,value in zip(my_item,size):
	our_class[key] = value
print(our_class)