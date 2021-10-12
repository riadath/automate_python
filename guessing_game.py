import random

def guessingGame():
    maximumGuess = 5
    correctNumber = random.randint(0,20)
    currentGuesses = 0
    playerName = input("Enter your name : ")
    print("Hello " + playerName + ", I'm thinking of a number between 1 and 20.")
    ifGuessed = False
    while currentGuesses < maximumGuess:
        guessedNumber = int(input("Please enter your guess : "))
        if guessedNumber > correctNumber : 
            print("Your number is too high")
        elif guessedNumber < correctNumber:
            print("Your numebr is too low")
        else:
            print("You guessed the correct number")
            ifGuessed = True
            break
        currentGuesses += 1
    
    if not ifGuessed:
        print("You are out of guesses. I was thinking of the number",correctNumber)

guessingGame()