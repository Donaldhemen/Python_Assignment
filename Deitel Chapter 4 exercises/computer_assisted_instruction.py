import random


def multiplication_quiz():
    
    number1 = random.randrange(1, 9)
    number2 = random.randrange(1, 9)

    while True:
        answer = int(input(f"How much is {number1} * {number2}? "))

        if answer == number1 * number2:
            print("Very good!")
            break
        else:
            print("No. Please try again.")


multiplication_quiz()
