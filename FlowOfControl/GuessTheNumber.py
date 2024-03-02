import random

secretNum = random.randint(1, 100)

while True:
    guessNum = int(input("Guess a number between 1 and 100 inclusive: "))
    
    if guessNum < secretNum:
        print("Your guess is too low")
    elif guessNum > secretNum:
        print("Your guess is too high")
    else:
        print("Congratulations! You guessed the number correctly")
        break
