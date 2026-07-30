# read three different numbers from user
# if number1 < number2 and number1 < number3
# nested if number2 < number3 print number1, number2, number3
# nested if number2 > number3 print number1, number3, number2
# if number2 < number1 and number2 < number3
# nested if number1 < number3 print number2, number1, number3
# nested if number1 > number3 print number2, number3, number1
# if number3 < number1 and number3 < number2
# nested if number1 < number2 print number3, number1, number2
# nested if number1 > number2 print number3, number2, number1

number_1 = float(input("Enter first number: "))

number_2 = float(input("Enter second number: "))

number_3 = float(input("Enter third number: "))

if number_1 < number_2 and number_1 < number_3 :
	if number_2 < number_3 :
		print(number_1, number_2, number_3)
	if number_2 > number_3 :
		print(number_1, number_3, number_2)
if number_2 < number_1 and number_2 < number_3 :
	if number_1 < number_3 :
		print(number_2, number_1, number_3)
	if number_1 > number_3 :
		print(number_2, number_3, number_1)
if number_3 < number_1 and number_3 < number_2 :
	if number_1 < number_2 :
		print(number_3, number_1, number_2)
	if number_1 > number_2 :
		print(number_3, number_2, number_1)
