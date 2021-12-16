Q1.Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.

Q2. Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

Example:

```
[34, 54, 67, 89, 11, 43, 94] => [34, 54, 11, 67, 89, 43, 94, 11]
```

Q3. Slice list into 3 equal chunks and reverse each chunk then reassemble into a new list.

```
[11, 45, 8, 23, 14, 12, 78, 45, 89]

# Chunk  1 [11, 45, 8]
# After reversing it  [8, 45, 11]
# Chunk  2 [23, 14, 12]
# After reversing it  [12, 14, 23]
# Chunk  3 [78, 45, 89]
# After reversing it  [89, 45, 78]

# Reassemble [8, 45, 11, 12, 14, 23, 89, 45, 78]
```

Q4. Count the occurrence of each element from a list

```
# Sample list [11, 45, 8, 11, 23, 45, 23, 45, 89]

# Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
```

Q5. Create a Python set such that it shows the element from both lists in a pair

```
# first_list = [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]

# Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}
```


Q6. Find the intersection (common) of two sets and remove those elements from the first set

```
# first_set = {23, 42, 65, 57, 78, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}

# Intersection is  {57, 83, 29}
# First Set after removing common element  {65, 42, 78, 23}
```

Q7.  Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list

```
# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

# After removing unwanted elements from list [47, 69, 76, 97]

```

Q8. Get all values from the dictionary and add them to a list but don’t add duplicates

```
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

# result: [47, 52, 44, 53, 54]
```

Q9. Remove duplicates from a list and create a tuple and find the minimum and maximum number

```
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

# unique items [87, 45, 41, 65, 99]
# tuple (87, 45, 41, 65, 99)
# min: 41
# max: 99
```

Q10. Create a string made of the first, middle and last character

```
str1 = "James"

# result: Jms
```

Q11. Arrange string characters such that lowercase letters should come first

```
str1 = PyNaTive

# result: yaivePNT
```

Q12. Count all letters, digits, and special symbols from a given string

```
str1 = "P@#yn26at^&i5ve"

# Chars = 8 
# Digits = 3 
# Symbol = 4
```

Q13. Find all occurrences of a substring in a given string by ignoring the case

```
str1 = "Welcome to Iran. iran awesome, isn't it?"

# The Iran count is: 2
```

Q14. Calculate the sum and average of the digits present in a string

```
str1 = "PYnative29@#8496"

# Sum is: 38 Average is  6.333333333333333
```

Q15.  Write a program to count occurrences of all characters within a string

```
str1 = "Apple"

# {'A': 1, 'p': 2, 'l': 1, 'e': 1}
```

Q16. Remove special symbols / punctuation from a string

```
str1 = "/*Jon is @developer & musician"

# result: "Jon is developer musician"
```

Q17. Find words with both alphabets and numbers

```
str1 = "Emma25 is Data scientist50 and AI Expert"

# Emma25
# scientist50
```

Q18. Use defaultdict from collections module to count all occurence of alphabet letters in a statement.
