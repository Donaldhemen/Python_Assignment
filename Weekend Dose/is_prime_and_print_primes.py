def is_prime(number):
	if number <= 1:
		return False
	for count in range(2, (number**0.5) + 1):
		if number % count == 0:
			return False
	return True
def print_primes(number):
	for count in range(2, number + 1):
		if number % count == 0:
			print(count, " ")

def is_prime_and_print_primes(number):

random_number = int(input("Enter number: "))
print(is_prime(random_number))