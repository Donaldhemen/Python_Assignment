def create_list(number):
    my_list = []
    for number in range(1,number+1):
        my_list += [number]
    return my_list

print(create_list(15))

