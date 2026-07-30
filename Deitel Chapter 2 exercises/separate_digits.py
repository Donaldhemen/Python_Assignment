# input five-digit number 
# use modulo and floor division to separate first to fifth digit
# print first to fifth digits

five_digit = int(input("Enter five-digit number: "))

if (9999 < five_digit < 100000) :
    first_digit = five_digit // 10000
    
    second_digit = (five_digit // 1000) % 10

    third_digit = (five_digit // 100) % 10

    fourth_digit = (five_digit // 10) % 10

    fifth_digit = (five_digit) % 10
    
    print(first_digit, second_digit, third_digit, fourth_digit, fifth_digit)
else : 
    print("Please enter a five-digit integer")

 

