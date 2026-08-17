def sum_even_index_elements(numbers):
    
    total_sum = 0
    
    for number in range(0, len(numbers), 2):
        total_sum += numbers[number]
    return total_sum
    
my_list = [1, 2, 1, 3, 1, 4, 1]

print(sum_even_index_elements(my_list))
