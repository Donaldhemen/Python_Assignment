
def multiples_of_number(number):
	counter= 0
	for count in range(1, 101):
		if(count % number == 0):
			counter += 1

	return counter

random_number = int(input("Enter an integer: "))

print(multiples_of_number(random_number))