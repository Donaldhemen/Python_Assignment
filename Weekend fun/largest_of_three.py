# name largest_of_three
# read three integers a, b and c from user
# largest = a 
# if a < b > c print b is largest
# if a < c > b print c is largest
# else print largest

a = int( input("Enter first integer, a: "))

b = int( input("Enter first integer, b: "))

c = int( input("Enter first integer, c: "))

largest = a 

if a < b > c :
	print("Largest integer is: ", b)
if a < c > b :
	print("Largest integer is: ", c)
else :
	print("Largest integer is: ", largest)