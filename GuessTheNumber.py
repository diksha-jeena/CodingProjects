import random
secretNum = random.randint(1,100)
guessNumString = int(input("Guess a number between 1 and 100 inclusive :"))
guessNum = int(input("Guess a number between 1 and 100 inclusive : "))
while (guessNum != secretNum):
    if(guessNum < secretNum):
        print("Your guess is too low")
    else:
        print("Your guess is too high")
print("Congratulations! you guessed the number correctly")