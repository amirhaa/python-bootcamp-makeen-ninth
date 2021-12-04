Q11. Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

Example:

```
count_vowels("number") => 2
```

Q12.Your task is to write a function that takes two dictionaries and returns a new dictionary which combines all the dictionaries.

Example:

```
dictA = { 'a': 10, 'b': 20, 'c': 30 }
dictB = { 'a': 3, 'c': 6, 'd': 3 }

combine_dict(dictA, dictB) => { a: 13, b: 20, c: 36, d: 3 }
```

Q13. Write a function that takes two sequence of numbers and returns the unique items of the first array that is not exists in the second one.

Example:

```
list1 = [1, 2, 3, 3, 4]
list2 = [1, 4, 5]

unique_items(list1, list2) => [2, 3]
```

Q14. Write a function that takes a dictionary and a tuple of two items use first item of the tuple as the key and second item as the value and adds them into the dictionary and return the created dictionary.

Example:

```
person = {"name": "Andy"}

update_dict(person, (age, 20)) => {"name": "Andy", "age": 20}
```

Q15. Write a function that takes a dict and returns the mean of dict values.

Example:

```
scores = {"Mathematics": 18, "History": 16, "Physics": 20}

mean(scores) == 18
```

Q16. Write a function to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)

Example:

```
generate_dicts(n=5) => {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

Q17. Write a script that takes the name of the user and prints a greeting with the user name.

Example:

**user inputs:** ```Amir```

**script should prints:** ```Hello dear Amir, you are very welcomed.```

Q18. Write a script that takes the user age and if the age is bellow 18 it should warn the user that he/she is not allowed to have driving licence, and if he/she is greater that or equal to 18, is able to get a driving licence.

```
# User inputs: 17

program should prints: ```Your age is bellow 18 so you are not allowed to have driving licence.```

# User inputs: 20

program should prints: ```You are allowed to have a driving licence.```
```