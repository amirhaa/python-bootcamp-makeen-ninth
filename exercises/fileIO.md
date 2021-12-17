Q1. Write a program to write a list into a file. each item of the list should be appendend into a new line in the file.

Q2. Write a program that takes a text file as an input and returns the number of words in it.

Q3. Write a program to open and read a file that contains some statements then find the top 10 longest words and return them as the list that is sorted in descending order.

Q4. Write a program to open and read a file that contains some statemetns then find each words frequency (number of repetition) in a list of tuples that the first item of the tuple is the word and second one is the word's frequency.

Q5. We have two files, Write a program that combines each line of the first file with the second file.

Q6. Write a program that removes all newline characters from a file.

Q7. Write a program that each time you run it ask you to enter your notes in terminal and append it in an markdown file (each time you should append to the mardown file). if the user enters a special words (for example `display`) instead of appending to the file display all of entered note to the user.

Q8. Write a catchtime function (context manager) that gives us the time that a peice of code took running like the following:

with catchtime() as t:
    // you can do whatever you like here
    for i in range(0, 10000000):
        pass

print(f"total time took to run the code: {t.time}")

Q9. Write an ```open``` like context manager that when you try read a file (with mode 'r') and if **only**, file does not exists error raised, ask user in terminal that if he/she wants to create this file or not.

Q10. Write a program that create a file like following:


```
# file.txt

yesterday: '2021-12-13 15:19:35'
    today: '2021-12-14 15:19:55'
 tomorrow: '2021-12-15 15:20:44'
```

**Note**: you should use datetime module

**Note**: you should remove microsecond part of datetime ```2021-12-15 15:21:54.626116``` => ```2021-12-15 15:20:44```
