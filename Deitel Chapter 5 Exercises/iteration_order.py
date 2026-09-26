 
numbers = [[0,0,0],[0,0,0]]
count = 1
for row in range(2):
    for column in range(3):
        numbers[row][column] = count
        count += 1
print(numbers)

print("   0  1  2")
for row in range(2):
    print(row, end="  ")
    for column in range(3):
        print(numbers[row][column], end="  ")
    print()