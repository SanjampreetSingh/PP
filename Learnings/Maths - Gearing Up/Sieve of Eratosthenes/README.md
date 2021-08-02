# Sieve of Eratosthenes

[Link](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)

Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number.

**Example 1:**  
`Input : n =10`  
`Output : 2 3 5 7 `

**Example 2:**  
`Input : n = 20 `  
`Output: 2 3 5 7 11 13 17 19`

The sieve of Eratosthenes is one of the most efficient ways to find all primes smaller than n when n is smaller than 10 million or so

Following is the algorithm to find all the prime numbers less than or equal to a given integer n by the Eratosthenes's method:
When the algorithm terminates, all the numbers in the list that are not marked are prime.

**Statistics**

1. Time complexity - O(n* log(log(n)))
2. Space complexity - O(n)

