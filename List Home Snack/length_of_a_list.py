def length_of_a_list(numbers):

    count = 0
    
    for number in numbers:
        count += 1
        
    return count
    
my_list = [1, 2, 1, 3, 1, 4, 1]

print(length_of_a_list(my_list))
