def average_of_ten_numbers(*number):
	total = 0

	for count in range(10):
	 	number = float(input("Enter number:"))
	 	total += number

	average = total / 10
	return average




print("The average of the 10 numbers is: ", average_of_ten_numbers())