#  Recursion and Dictionaries

## Warming up with the Dictionaries
1. Write a function which takes two dictionaries as parameters and returns the **combined** dictionary.

> {'a': 100, 'b': 200, 'c': 300} + {'d': 300, 'f': 200} -> {'a': 100, 'b': 200, 'c': 300, 'd': 300, 'f':200}

2. Write a function which takes two dictionaries as parameters and returns the summation of the dictionaries. The summation can be defined as element-wise sum for each element. You can assume the keys that do not appear in the dictionaries have a value of 0.

> {'a': 100, 'b': 200, 'c': 300} + {'a': 300, 'b': 200, 'd': 400} -> {'a': 400, 'b': 400, 'c': 300, 'd': 400}

3. Write a function which takes a dictionary and a key in that dictionary as parameters and returns the dictionary by deleting the given key. That is, if the given key appears in the dictionary, it needs to be deleted. 

**Hint:** Do not forget to check if the key is in the dictionary!

> {'a': 100, 'b': 200, 'c': 300}, 'a' -> { 'b': 200, 'c': 300}

4. Write a function which takes two dictionaries as parameters and returns a list which contains the common keys between the two. That is, if a key appears in both dictionaries, it needs to be in the output list.

> {'a': 100, 'b': 200, 'c': 300}, {'a': 300, 'b': 200, 'd': 400} -> ['a','b']

5. Write a function which takes a dictionary as a parameter and returns the multiplication of all the values in the dictionary. 

> {'a': 2, 'b': 5, 'c': 4, 'd':3} -> 120

## Recursion

1. Given a string, return recursively a "cleaned" string where adjacent chars that are the same have been reduced to a single char. So "yyzzza" yields "yza".

string_clean("yyzzza") → "yza"
string_clean("abbbcdd") → "abcd"
string_Clean("Hello") → "Helo"

2. Given a string, compute recursively a new string where all the adjacent chars are now separated by a "*".

all_star("hello") → "h*e*l*l*o"
all_star("abc") → "a*b*c"
all_star("ab") → "a*b"

3. Given a string, return true if it is a nesting of zero or more pairs of parenthesis, like "(())" or "((()))". Suggestion: check the first and last chars, and then recur on what's inside them.

nest_paren("(())") → true
nest_paren("((()))") → true
nest_paren("(((x))") → false

4. Write a recursive function to calculate *the harmonic sum* of n. 

*The harmonic sum* of n is the sum of reciprocals of all the positive integers up to n. 

> 1 + 1/2 + 1/3 + ... + 1/n

5. Write a function which checks whether the given integer is prime or not in a recursive way. Your implementation should be recursive and you should not use any loops. 

**Hint:** You need to check if the given integer is divisible by all the number up until the square root of the given integer. 

For example, for 13, it is enough to check if numbers, 2, 3, 4 do not divide 13, we can say that is a prime number.

6. Write a recursive function that returns the maximum element of a given list. Your implementation should be recursive and you should not use any loops.

7. Find the sum of elements in a given nested list where the element of each list can be another list. Note that there might be more than two levels in the nesting of the lists. 

Some example cases:

> [1,2,[3,4],5] -> 15
> [1,[2,3],[[4,5],6]] -> 21
> [[1,[2,[3,[4,[5,[6,[7,[8,[9,[10]]]]]]]]]]] -> 55

## Example recursion questions from a midterm (Bonus)
1. Write a recursive function P for computing the i'th number in the sequence of numbers below, according to this recursive formula:

> P(0) = 1
> P(1) = 0
> P(2) = 0

> for i > 2, P(i) = P(i-2) + P(i-3)

> (1, 0, 0, 1, 0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49, ...) 


2. Let's define a function f on a number as the number of times we need to apply addition on the digits of that number before we reach a single digit.

> f(67) = 2

> because 6+7 = 13 and 1+3 = 4

> f(48196) = 3

> because 4+8+1+9+6 = 28 and 2+8 = 10 and 1+0=1

Write a recursive function to implement f.



## Kevin's Banana Puzzle (Bonus)
**Note:** This was a PS previously so it might take a while, please take the time to work on it.

Kevin loves to eat, live and dream bananas. During lunch break, Kevin visits a nearby shop that sells one banana at a certain price. Additionally, the shop lets you buy a banana if you can give the shop owner a certain number of banana peels. Kevin has a certain amount of money in his pocket, which he can use to buy a certain number of bananas. Kevin also likes to think about how many total bananas he can eat if he also exchanges the peels.

Your task is to write a recursive function that does this calculation for him because Kevin cannot think when there are bananas around. How many bananas can Kevin eat in total if he spends all his money to buy bananas and exchanges all the peels from the bananas he eats for more bananas?

- `money` is the amount  of money that Kevin has in his pocket
- `price` is the price at which the shop sells each banana
- `price_p` is the number of peels you can trade for an extra banana. You can think of `price_p` as the price of a banana in a different currency, price in peels.

You may assume that all inputs and results will be integers. You should use the `math.floor()` function in your calculations appropriately to make sure of this.