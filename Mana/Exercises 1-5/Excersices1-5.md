Q1.create a function that takes a list an return a list with reversed order.

examples:

```
reverse_list([1,2,3,4]) == [4,3,2,1]
```

Q2.create a function that takes a list of numbers, returns the two distinct highest values in the list. if there is 
less that two uniqe values return as many of them as possible.

examples:

```
[4, 10, 10, 9]  =>  [10, 9]
[1, 1, 1]  =>  [1]
[]  =>  []
```

Q3.Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

examples:

```
invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
```

Q4.Given a non-negative integer, return an array / a list of the individual digits in order.

examples:

```
123 => [1,2,3]

1 => [1]

8675309 => [8,6,7,5,3,0,9]
```

Q5.create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

examples:

```
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
```