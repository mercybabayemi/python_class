def get_squareroot(x):

	if x % 5 == 0:
		return round(x ** 0.5,2)
	elif x % 5 != 0:
		return x / 5
	if x.isalpha:
		raise TypeError
	if x is float(x):
		return mathsqrt(x)