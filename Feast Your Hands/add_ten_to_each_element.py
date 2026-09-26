#1 Use map() to convert a list of strings to a list of integers
def convert_to_integer(values):
    
    return int(values)
        
numbers = ["1","2","3"]

print(list(map(convert_to_integer, numbers)))

#2 A map() function to add 10 to each element in the list
def add_ten_to_element(numbers):

    return numbers + 10
    
values = [0,5,10,15]

print(list(map(add_ten_to_element,values)))

#3 Write a map() function that convert temperatures from celsius to fahrenheit in a list
def convert_celsius_to_fahrenheit(celsius):

    return int(celsius) * 1.8 + 32
    
temperature = [0,20,37,100]

print(list(map(convert_celsius_to_fahrenheit, temperature)))

#4 Use filter() to remove None values from the list
def is_not_none(values):

    return values != None
        
my_list = [1,None,3,None,5]

print(list(filter(is_not_none, my_list)))

#5 filter() function to extract numbers divisible by 3
def is_multiple_of_three(numbers):

    return numbers % 3 == 0
    
my_numbers = [1,3,4,6,9,12]

print(list(filter(is_multiple_of_three, my_numbers)))

#6 Use filter() to keep only positive numbers from list 
def is_positive_number(numbers):

    return numbers > 0
    
my_values = [-2,-1,0,1,2]

print(list(filter(is_positive_number, my_values)))

#7 Use filter() to select elements from a list of dictionaries
def is_older_than_twenty_five(values):

    return values['age'] > 25
    
my_dict = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 20}]

print(list(filter(is_older_than_twenty_five, my_dict)))

#8 Use reduce() to find the sum of all numbers in a list
from functools import reduce

def add_numbers(add, number):

    return add + number
    
numbers = [1,2,3,4,5]

print(reduce(add_numbers, numbers))

#9 Write a reduce() function to find the product of all numbers in a list
def multiply_numbers(first,second):

    return first * second
    
numbers = [2,3,4]

print(reduce(multiply_numbers, numbers))  

#10 Use a reduce() function to find the maximum value in a list
def find_maximum_value(first, second):

    largest = first
    
    if first < second: 
        largest = second
        
    return largest
    
numbers = [3,7,2,9,1]

print(reduce(find_maximum_value, numbers))

#11 Write a reduce function to concatenate all strings in a list
def concatenate_strings(join, strings):

    return join + strings
    
words = ["Hello", " ", "World"]

print(reduce(concatenate_strings, words))

#12 Use reduce() to merge a list of dictionaries into a single a single dictionary
def merge_dictionaries(merge, values):
    return {**merge, **values}

my_list = [{'a':1},{'b':2},{'c':3}]
print(reduce(merge_dictionaries,my_list))    
     
#13 Write a reduce() function to compute the cumulative sum of squares fo a list
def add_squares_of_numbers(total, numbers):

    return total + numbers**2
     
my_numbers = [1,2,3]

print(reduce(add_squares_of_numbers, my_numbers))

