def rotate(first_arg, second_arg, third_arg):
    return third_arg, first_arg, second_arg

first_value = 'Doug'
second_value = 22
third_value = 1984

result = rotate(first_value, second_value, third_value)
result = rotate(result, result, result)
result = rotate(result, result, result)
print(result)
