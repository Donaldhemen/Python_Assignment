
def count_division_steps(number):

	if number < 0:
		number = -number

	steps_count = 0
	while (number != 1):
		if (number % 2 == 0):
			number = number // 2
		else :
			number = (number * 3) + 1

		steps_count += 1
	return steps_count

random_number = int(input("Enter a positive integer: "))
print(count_division_steps(random_number))
