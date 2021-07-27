# Prime Factorization using Sieve O(log n) for multiple queries

[Link](https://www.geeksforgeeks.org/prime-factorization-using-sieve-olog-n-multiple-queries/)

**Key Concept:** `Our idea is to store the Smallest Prime Factor(SPF) for every number. Then to calculate the prime factorization of the given number by dividing the given number recursively with its smallest prime factor till it becomes 1.`

`To calculate to smallest prime factor for every number we will use the sieve of eratosthenes. In original Sieve, every time we mark a number as not-prime, we store the corresponding smallest prime factor for that number (Refer this article for better understanding). Now, after we are done with precalculating the smallest prime factor for every number we will divide our number n (whose prime factorization is to be calculated) by its corresponding smallest prime factor till n becomes 1.`

**Pseudo Code for prime factorization assuming
SPFs are computed :**

    PrimeFactors[] // To store result

    i = 0 // Index in PrimeFactors

    while n != 1 :

    // SPF : smallest prime factor
    PrimeFactors[i] = SPF[n]
    i++
    n = n / SPF[n]

**Example 1:**  
`Input : n = 12246`  
`Output : 2 3 13 157 `

**Time Complexity:** The precomputation for smallest prime factor is done in O(n log log n) using sieve. Where as in the calculation step we are dividing the number every time by the smallest prime number till it becomes 1. So, let’s consider a worst case in which every time the SPF is 2 . Therefore will have log n division steps. Hence, We can say that our Time Complexity will be **O(log n)** in worst case.

**Statistics**

1. Time complexity - O(log n)
