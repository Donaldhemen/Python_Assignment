
def fahrenheit(celsius):

   fahrenheit_temp = (9 / 5) * celsius + 32 
   return fahrenheit_temp
print("Celsius", "Fahrenheit", end="\n")     
for celsius in range(101):
    temp = fahrenheit(celsius)
    print(f"{celsius:>7} {temp:>10.1f}")

