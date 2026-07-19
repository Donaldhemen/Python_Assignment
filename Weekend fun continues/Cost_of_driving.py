# name: Cost_of_driving
# read the driving distance in miles
# read the fuel efficiency in miles per gallon and the price per gallon
# calculate the cost of the trip = driving distance / miles per gallon * price per gallon
# display cost of driving

distance = float( input("Enter the driving distance: "))

fuel_efficiency = float( input("Enter miles per gallon: "))

price_per_gallon = float( input("Enter price per gallon: "))

cost_of_driving = (distance * price_per_gallon) / fuel_efficiency

print("The cost of driving is $",cost_of_driving)