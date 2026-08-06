
def base_to_exponent(number):

	exponent = 1

	for count in range(1, number+1):
		exponent *= number
	return exponent

random_number = int(input("Enter an integer:"))

print(base_to_exponent(random_number))

