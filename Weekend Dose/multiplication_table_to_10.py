
def multiplication_table_to_ten(number):

	for count in range(1, 11):
		multiple = count * number
		
		print(number,'x', count,'=', multiple, end="\n")

random_number = int(input("Enter a number: "))

multiplication_table_to_ten(random_number)