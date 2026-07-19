# name: Vowel_or_consonant
# read one letter from user
# if letter == "a", "e", "i", "o" or "u" print "Vowel"
# elif letter != "a", "e", "i", "o" or "u" print "consonant"
# else print invalid input

letter = input("Enter one letter: ")

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" :
	print("Vowel")
elif letter != "a" or letter != "e" or letter != "i" or letter != "o" or letter != "u" :
	print("Consonant")
else : 
	print("Invalid input")