
def is_perfect_square(numbers):
    true_list = []
    for number in numbers:
        sqrt_number = int(number ** 0.5)
        if number == sqrt_number ** 2:
            true_list.append(True)
        else:
            true_list.append(False)
    return true_list

