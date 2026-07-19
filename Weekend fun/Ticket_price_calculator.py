# name: Ticket_price_calculator
# read customer age
# if Under 5 -> "Free"
# elif 5 <= age <= 12 -> print "$5"
# elif 13 <= age <= 64 -> print "12"
# else -> print "$8"

age = int( input("Enter customer's age: "))

if age < 5 : 
	print("Free")
elif 5 <= age <= 12 :
	print("Ticket Price is $5")
elif 13 <= age <= 64 :
	print("Ticket Price is $12")
else :
	print("Ticket Price is $8")