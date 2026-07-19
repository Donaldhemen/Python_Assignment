# name: Check_string_case
# read string from user
# check first letter with [0]
# if word[0].isupper() print "Uppercase"
# if word[0].islower() print "Lowercase"

word = input("Enter a string: ")

if word[0].isupper():
    print("Uppercase")
else :
    print("Lowercase")