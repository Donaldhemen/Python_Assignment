# Read single temperature along with a unit of measurement as 'C' for celsius or 'F' for Fahrenheit
# use split string and cast temperature as float and and unit as string upperCase
# read a threshold value to trigger a heat advisory
# function should convert the temperature to opposite unit using C =(F-32)*5/9 and F = (C*9/5)+32
# if temperature is below threshold, return "cold advisory" 
# if temperature is equal or above the threshold, return "Heat alert" 

def convert_and_check_temperature(temperature_input):
 #  temperature_input = input("Enter temperature(e.g 40C or 80F): ")
    threshold_value = 36

    temperature = float(temperature_input[:-1])
    unit = temperature_input[-1].upper()

    if unit == "F" :
        celsius = (temperature - 32) * 5 / 9
        if celsius < threshold_value :
            return "Cold advisory"
        else : 
            return "Heat alert"
    elif unit == "C" :
        fahrenheit = (temperature * 9 / 5) + 32
        threshold_value = (threshold_value * 9 / 5) + 32
        if fahrenheit < threshold_value :
            return "Cold advisory"
        else :
            return "Heat alert"
    else :
        fahrenheit = (float(temperature_input) * 9 / 5) + 32
        threshold_value = (threshold_value * 9 / 5) + 32
        if fahrenheit < threshold_value :
            return "Cold advisory"
        else :
            return "Heat alert"
temperature_input = input("Enter temperature(e.g 40C or 80F): ")
temp = convert_and_check_temperature(temperature_input)
print(temp)
