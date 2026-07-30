# name: Quadrant_finder
# read two integers x and y
# if x > 0 and y > 0 print "Q1"
# if x < 0 and y > 0 print "Q2"
# if x < 0 and y < 0 print "Q3"
# if x > 0 and y < 0 print "Q4"
# if y == 0 and x != 0 print "x-axis"
# if x == 0 and y != 0 print "y-axis"
# if both zero print "Origin"

x = int (input("Enter first integer: "))

y = int (input("Enter second integer: "))

if x > 0 and y > 0 :
	print("Q1")
elif x < 0 and y > 0 :
	print("Q2")
elif x < 0 and y < 0 :
	print("Q3")
elif x > 0 and y < 0 :
	print("Q4")
elif y == 0 and x != 0 :
	print("X-axis")
elif x == 0 and y != 0 :
	print("Y-axis")
else :
	print("Origin")