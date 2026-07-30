# file name: Average_Letter_Grade_Python
# read values of 3 scores from user
# calculate average of 3 scores
# if/else for letter grade for A, B, C, D and F

first_score = int (input("Enter first score: "))

second_score = int (input("Enter second score: "))

third_score = int (input("Enter third score: "))

average = (first_score + second_score + third_score) / 3

if 90 <= average <= 100 :
	print("Grade is 'A'")
elif 80 <= average < 90 :
	print("Grade is 'B'")
elif 70 <= average < 80 :
	print("Grade is 'C'")
elif 60 <= average < 70 :
	print("Grade is 'D'")
else : 
	print("Grade is 'F'")