def sum_first_middle_and_last_elements(numbers):
    total_sum = 0
    middle_index = len(numbers) // 2
    
    if(len(numbers) % 2 == 0):
       total_sum = numbers[0] + (numbers[middle_index] + numbers[middle_index-1]) / 2 + numbers[len(numbers)-1]
       
    elif(len(numbers) % 2 != 0):
        total_sum = numbers[0] + numbers[middle_index] + numbers[len(numbers)-1]
        
    return total_sum
    
my_list = [1, 2, 2, 3, 3, 4]

print(sum_first_middle_and_last_elements(my_list))
