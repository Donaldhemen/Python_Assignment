# initialise and declare variables for p = $1000 and r = 7% 
# if n = 10 : a = p * ((1 + r) ** 10)
# print 'a is the amount on deposit at the 10th year'
# if n = 20 : a = p * ((1 + r) ** 20)
# print 'a is the amount on deposit at the 20th year'
# if n = 30 : a = p * ((1 + r) ** 30)
# print 'a is the amount on deposit at the 30th year'

p = 1000
r = 0.07
n = 10
a = p * ((1 + r) ** n)
print(f"{a} is the amount on deposit at the {n}th year")

n = 20
a = p * ((1 + r) ** n)
print(f"{a} is the amount on deposit at the {n}th year")

n = 30
a = p * ((1 + r) ** n)
print(f"{a} is the amount on deposit at the {n}th year")
