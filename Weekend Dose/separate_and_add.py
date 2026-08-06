# take any integer as input
# separate into individual digits 
# sum individual digits

def separate_and_add(number):
	sum = 0

	for digit in number:

		digit = int(digit)
		sum += digit
	return sum
numbers = input("Enter an integer: ")
print(separate_and_add(numbers))
