# name: String length
# read string input from user
# if len() < 5 print "Short string"
# if len() between 5 and 10, "print medium string"
# if len() > 10 print "Long string"

length = input("Enter a string")

if len(length) < 5 :
	print("Short string")
elif 5 <= len(length) <= 10 :
	print("Medium string")
else :
	print("Long string")