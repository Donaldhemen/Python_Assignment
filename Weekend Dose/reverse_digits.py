
def reverse_digits(number):
	reversed_number = 0

	for digit in number:
		digit = int(digit)
		number= int (number)
		digit = number % 10
		reversed_number = (reversed_number * 10) + digit 
		number //= 10
	return reversed_number

random_number = input("Enter a number: ")
print(reverse_digits(random_number))