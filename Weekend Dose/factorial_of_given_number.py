
def factorial_of_given_number(number):

	factorial= 1
	
	for count in range(number, 0, -1):
		factorial *= count
	return factorial

numbers = int(input("Enter an integer: "))
print(factorial_of_given_number(numbers))
