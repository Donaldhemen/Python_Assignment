# name: single_character_check
# read single character from user
# if len of string not 1 print re-enter 
# elif string.idigit() print digit
# elif string.isalpha() print letter
# else print special symbol

string = input("Enter a single character: ")

if len(string) != 1 :
	print("Please re-enter a single character: ")
elif string.isdigit() :
	print("It is a digit")
elif string.isalpha() :
	print("It is a letter")
else : 
	print("It is a special symbol")