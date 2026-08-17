def sum_odd_index_elements(numbers):
    total_sum = 0
    
    for number in range(1, len(numbers), 2):
        total_sum += numbers[number]
        
    return total_sum
    
my_list = [1, 2, 2, 3, 3, 3, 4]

print(sum_odd_index_elements(my_list))
