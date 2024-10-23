integer = int(input("Enter a five digit integer: "))

firstnumber = integer // 10000

secondtrial = integer // 1000
secondnumber = secondtrial % 10

thirdtrial = integer // 100
thirdnumber = thirdtrial % 10

fourthtrial = integer // 10
fourthnumber = fourthtrial % 10

fifthnumber = integer % 10 

print(firstnumber, " ", secondnumber, " ", thirdnumber, " ", fourthnumber, " ", fifthnumber)

