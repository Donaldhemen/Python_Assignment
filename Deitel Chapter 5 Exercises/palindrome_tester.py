def is_palindrome(string):
    reversed_value = ""

    for char in string:
        reversed_value += char.lower()

    stack = []
    for char in reversed_value:
        stack.append(char)

    for char in reversed_value:
        if char != stack.pop():
            return False
    return True

print(is_palindrome('12321'))
print(is_palindrome('12345'))
print(is_palindrome('racecar'))
print(is_palindrome('hello'))