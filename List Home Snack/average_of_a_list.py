def average_of_a_list(numbers):
    total_sum = 0
    
    for number in numbers:
        total_sum += numbers[number]
        
    mean = total_sum / len(numbers)
    return mean
    
my_list = [1, 2, 2, 3, 3, 3, 4]

print(average_of_a_list(my_list))
