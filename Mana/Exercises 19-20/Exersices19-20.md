Q19. Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number **(xxx) xxx-xxxx**.

Example:

```
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
```

The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!



Q20. Write a game with python, when the game starts the program would generate a random number between 1 to 10 and user should guess the number. 
user could guess the correct number up to 4 guesses.

Each time user enters a wrong input prints ```wrong answer, you have {number of guesses that left} guesses left``` until the user reach the 4 guesses. and if he/she could not enter the corrcect answer after 4 times prints ```Sorry you lost, the correct answer is {answer}```. if the user guessed the correct answer prints ```Congratulations, you have won!```

Note: program should get number from the user with ```input``` function, and use while loop to solve the program.

Note: [How generate random number](https://stackoverflow.com/a/16376904)

Note: numbers should be between 1 to 10 (not 0 to 9)

Flow of the game:

```
1.program starts (for example number 6 is the correct answer)

> input("Guess a number beween 1 to 10 \n")

2.wait for user to eneters a number

> 3

3.user enters a wrong answer so prints out a warn

> print("wrong answer, you have 3 guesses left")

4.again asks user to enters another number

> input("Guess a number beween 1 to 10 \n")

> 8

5.user enters another wrong answer

> print("wrong answer, you have 2 guesses left")

> input("Guess a number beween 1 to 10 \n")

> 5

> print("Congratulations, you have won!")
```
