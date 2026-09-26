
def convert_to_integer(values):
    
    return int(values)
        
numbers = ["1","2","3"]

print(list(map(convert_to_integer, numbers)))

def convert_celsius_to_fahrenheit(celsius):

    return int(celsius) * 1.8 + 32
    
temperature = [0,20,37,100]
print(list(map(convert_celsius_to_fahrenheit, temperature)))


