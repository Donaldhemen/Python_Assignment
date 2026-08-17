def multiply_all_third_elements(numbers):
    multiply = 1
    
    for number in range(2, len(numbers), 3):
        multiply *= numbers[number]
        
    return multiply
    
my_list = [1, 2, 2, 3, 3, 3, 4]

print(multiply_all_third_elements(my_list))
