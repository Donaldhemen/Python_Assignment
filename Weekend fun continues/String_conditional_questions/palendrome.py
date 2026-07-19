# read a 3 letter word with a lower case function
# if len(word) != 3 print "Re-enter 3 letter word"
# elif word[0] == word[2] print "It is a palendrome"
# else print "It is not a palendrome"
word = input("Enter a 3-letter word").lower()

if len(word) != 3 :
    print("Re-enter a 3-letter word")
elif word[0] == word[2] :
    print("It is a palendrome")
else :
    print("It is not a palendrome")