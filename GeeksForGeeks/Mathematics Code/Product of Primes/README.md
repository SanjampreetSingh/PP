# Product of Primes

[Link](https://practice.geeksforgeeks.org/problems/product-of-primes5328/1)

Given two numbers L and R (inclusive) find the product of primes within this range. Print the product modulo 10^9+7. If there are no primes in that range you must print 1.

**Example 1:**  
`Input: L = 1, R = 10`  
`Output: 210`  
**Explanation:**  
`The prime numbers are 2, 3, 5 and 7.`

**Example 2:**  
`Input: L = 1, R = 20`  
`Output: 9699690`  
**Explanation:**  
`The primes are 2, 3, 5, 7, 11, 13, 17 and 19.`

**Your Task:**  
`You don't need to read input or print anything. Your task is to complete the function lcmAndGcd() which takes an Integer N as input and returns a List of two Integers, the required LCM and GCD.`

**Expected Time Complexity:** O((R-L)\*(logR))  
**Expected Auxiliary Space:** O(sqrt(R))

**Constraints:**

- 1 ≤ L ≤ R ≤ 10^9
- 0 ≤ L - R ≤ 10^6

**Statistics**

1. Time complexity - O((R-L)\*(logR))
2. Space complexity - O(sqrt(R))

**Result**:  
![Result image](https://github.com/SanjampreetSingh/PP/blob/master/GeeksForGeeks/Mathematics%20Code/LCM%20And%20GCD/image.jpg)
