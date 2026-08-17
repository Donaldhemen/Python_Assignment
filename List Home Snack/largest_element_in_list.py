def largest_element_in_list(numbers):
    
    largest = numbers[0]
    
    for number in range(len(numbers)):
        if(numbers[number] > largest):
            largest = numbers[number]
            
    return largest
    
my_list = [1, 2, 2, 3, 3, 3, 4]

print(largest_element_in_list(my_list))
