import random

correctNumber = random.randint(1, 10)
numberofGuesses = 4
while numberofGuesses != 0:
    userNumber = int(input("Guess a number between 1 to 10 :)\n"))
    
    if userNumber == correctNumber:
        print("Congratulations, you have won!")
        break
    else:
        numberofGuesses -= 1
        if numberofGuesses == 0:
            print(f"Sorry you lost, the correct answer is {correctNumber}")
        else:
            print(f"wrong answer, you have {numberofGuesses} guesses left")
        


