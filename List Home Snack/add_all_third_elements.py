def add_all_third_elements(numbers):
    total_sum = 0
    
    for number in range(2, len(numbers), 3):
        total_sum += numbers[number]
        
    return total_sum
    
my_list = [1, 2, 2, 3, 3, 3, 4]

print(add_all_third_elements(my_list))
