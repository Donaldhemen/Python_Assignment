# read user's age 
# calculate maximum heart rate = 220 - age
# calculate upper target heart rate = maximum * 85/100
# calculate lower target heart rate = maximum * 50/100
# display maximum heart rate and range of target heart rate

user_age = int(input("Enter user's age: "))

maximum_heart_rate = 220 - user_age

upper_target_heart_rate = maximum_heart_rate * 85 / 100

lower_target_heart_rate = maximum_heart_rate * 50 / 100

print("Maximum heart rate is ", maximum_heart_rate,"b.p.m")
print("Target heart rate is", lower_target_heart_rate,"-",upper_target_heart_rate,"b.p.m")
