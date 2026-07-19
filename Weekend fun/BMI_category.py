# name: BMI_category
# read weight in kg and height in meters
# calculate bmi = weight / (height * height)
# if bmi < 18.5 print "Underweight"
# elif 18.5 <= bmi <= 24.9 print "Normal"
# elif 25 <= bmi <= 29.9 print "Overweight"
# else bmi >= 18.5 print "Obese"

weight = float( input("Enter weight in kg: "))

height = float( input("Enter height in meters: "))

bmi = weight / (height * height)

if bmi < 18.5 :
	print("Underweight")
elif 18.5 <= bmi <= 24.9 : 
	print("Normal")
elif 25 <= bmi <= 29.9 : 
	print("Overweight")
else : 
	print("Obese") 