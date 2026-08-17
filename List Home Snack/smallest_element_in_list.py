def smallest_element_in_list(numbers):
    
    smallest = numbers[0]
    
    for number in range(len(numbers)):
        if(numbers[number] < smallest):
            smallest = numbers[number]
            
    return smallest
    
my_list = [1, 2, 2, 3, 3, -2, 4]

print(smallest_element_in_list(my_list))
