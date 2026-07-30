#name: choose_day_number
# read number 1 - 7 from user
# if 1 <= number <= 7 
# if number is 1 print "Sunday" 
# if number is 2 print "Monday"
# if number is 3 print "Tuesday"
# if number is 4 print "Wednesday"
# if number is 5 print "Thursday"
# if number is 6 print "Friday"
# if number is 7 print "Saturday"
# else print "Please enter a number between 1 to 7"

day_number = int(input("Enter a number from 1 to 7: "))

if 1 <= day_number <= 7 :
	if day_number == 1 :
		print("Sunday")
	elif day_number == 2 :
		print("Monday")
	elif day_number == 3 :
		print("Tuesday")
	elif day_number == 4 :
		print("Wednesday")
	elif day_number == 5 :
		print("Thursday")
	elif day_number == 6 :
		print("Friday")
	else : 
		print("Saturday")
else :
	print("Please enter a number between 1 to 7.")
	