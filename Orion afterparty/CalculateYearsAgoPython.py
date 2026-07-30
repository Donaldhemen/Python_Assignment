
# collect input for father's age 
# collect input for son's age
# if statement for age range from 1 to 80 else invalid input
# calculate years to double = fathers age - sons age * 2
# if years to double is positive, display Was twice his sons age at answer
#
fathers_age = int (input("Enter father's current age: "))

sons_age = int (input("Enter son's current age: "))

if 1 <= fathers_age <= 80 and 1 <= sons_age <= 80 :
	years_ago = fathers_age - (sons_age * 2)
	if years_ago >= 0 :
		print("The father will be twice as old as his son in the next", years_ago,"years")
	else:
		print("The father was twice his son's age", 0 - years_ago, "years ago")
else: 
	print("Invalid input")

# 
