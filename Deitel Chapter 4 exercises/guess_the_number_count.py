
import random

number = 0

for numbers in range(1, 1000):
    number = random.randrange(numbers)
    
print("Guess a number between 1 and 1000")

counter = 0

while(True):
    guess = int(input("Enter number (negative number to quit)"))
    
    counter += 1
    
    if(guess < 0): break
    elif(guess > number): 
        print("Too high. Try again")
    elif(guess < number): 
        print("Too low. Try again")
    elif(guess == number):
        print("Congratulations. You guessed the number")
        print("Do you want to play again?")
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if(play_again != "yes"):
            print("Thanks for playing")
            break
        else :
            print("Guess a number between 1 and 1000")
            for numbers in range(1, 1000):
                number = random.randrange(numbers)
if counter <= 10 :
    print("Either you know the secret or you got lucky!")
else :
    print("You should be able to do better!")           

