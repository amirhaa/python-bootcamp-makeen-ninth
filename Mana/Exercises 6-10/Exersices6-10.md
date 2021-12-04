Q6. Write a function that receives a list of numbers, determine whether the sum of its elements is odd or even. the response should be either "odd" or "even".
If the input array is empty consider it as: [0]

Examples:

```
odd_or_even_sum([1, 2, 3, 4]) => even
```

Test Cases:

```[1,2,3,4]``` => even     
```[4,0,2]``` => even       
```[2,5,10,100]``` => odd       
```[]``` => even        
```[1000, 2000, 3000, 4000, 5000]``` => even        
```[0, -1, -5]``` => even       


Q7.Write a function that receives a list of strings and returns
a sorted list containing the same strings, ordered from shortest 
to longest.

if two string has the same lenght, it does not matter the order of them.

Examples:

```sort_strings(["abcde", "abc", "abcd", "a"]) => ["a", "abc", "abcd", "abcde"]```


Test Cases:

```["abcde", "abc", "abcd", "a"]``` => ```["a", "abc", "abcd", "abcde"]```

```["Telescopes", "Glasses", "Eyes", "Monocles"]``` => ```["Eyes", "Glasses", "Monocles", "Telescopes"]```

```["Java", "Python", "Go", "Js"]``` => ```["Go", "Js", "Java", "Python"]```


Q8.Given a two-dimensional array of integers, return the flattened version of the array with all the integers in the sorted (ascending) order.

Examples:

```
[[3, 2, 1], [4, 6, 5], [], [9, 7, 8]] => [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Q9.You will be given an array and a limit value. You must check that all values in the array are below or equal to the limit value. If they are, return true. Else, return false.
You can assume all values in the array are numbers.

Examples:

```
bellow_the_limit([1, 5, 8, 12], 10) => False

bellow_the_limit([4, 7, 10, 20, 18], 20) => True

bellow_the_limit([5, 8, 2, 8], 10) => True
```

Test Cases:

```[2, 7, 5], 7``` => True      
```[3, 7, 10, 2], 7``` => False     
```[-1, -2, -8], -10``` => False
```[-1, -2, 0], 0``` => true


Q10. Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order.

Examples:

```
descending_numbers(42145) => 54421

descending_numbers(145263) => 654321

descending_numbers(123456789) => 987654321
```