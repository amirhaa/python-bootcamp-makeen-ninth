# Q19:

def create_phone_number(numList):

    return f"({''.join(str(item) for item in numList[0:3])}) {''.join(str(item) for item in numList[3:6])}-{''.join(str(item) for item in numList[6::])}"

# -------------------------------------------------

# Q20:

import random

correct_number = random.randint(1, 10)
number_of_guesses = 4
while number_of_guesses != 0:
    user_number = int(input("Guess a number between 1 to 10 :)\n"))
    
    if user_number == correct_number:
        print("Congratulations, you have won!")
        break
    else:
        number_of_guesses -= 1
        if number_of_guesses == 0:
            print(f"Sorry you lost, the correct answer is {correct_number}")
        else:
            print(f"wrong answer, you have {number_of_guesses} guesses left")