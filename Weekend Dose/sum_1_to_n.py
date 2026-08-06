
def sum_1_to_n(number):
	number = number + 1
	sum = 0
	count = 0
	for count in range(number):
		sum += count
	return sum
number = int(input("Enter a number: "))
print(sum_1_to_n(number))