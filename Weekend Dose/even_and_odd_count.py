
list = (3, 4, 5, 11, 13, 16, 18, 8, 7)

even_number = 0
odd_number = 0

for number in list:
	if number % 2 == 0 :
		even_number += 1

	else :
		odd_number += 1

print("The list has ", even_number, " even numbers")
print("The list has ", odd_number, "odd numbers")