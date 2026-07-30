# name: print_a_greeting
# read a name from user
# if 3 <= len(name) <= 5 
# print "Hi 'name'"
# if len(name) > 5
# print "Hello name"

name = input()

if 3 <= len(name) <= 5 :
	print("Hi", name,"!")
else :
	print("Hello", name,"!")