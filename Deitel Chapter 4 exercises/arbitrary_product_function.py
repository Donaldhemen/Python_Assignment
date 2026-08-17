
def product(*number):
    
    product = 1
    for value in number:
        product *= value
    return product

print(product(2,3,4))
