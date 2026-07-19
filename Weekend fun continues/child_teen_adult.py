# file name: child_teen_adult
# read age from user
# if age < 13 print "child"
# if 13 < = age <= 17 print "teen"
# if age > 17 print "adult"

user_age = int(input("Enter user's age"))

if user_age < 13 :
	print("Child")
elif 13 <= user_age <= 17 :
	print("Teen")
else :
	print("Adult")