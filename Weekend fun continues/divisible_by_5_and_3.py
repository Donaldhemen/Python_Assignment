# file name: divisible_by_5_and_3
# read number from user
# if number % 5 == 0 and number % 3 == 0 print divisible
# else print not divisible

number = int(input("Enter number: "))

if number % 5 == 0 and number % 3 == 0 :
	print(f"{number} is divisible by 5 and 3")
else :
	print(f"{number} is not divisible by 5 and 3")