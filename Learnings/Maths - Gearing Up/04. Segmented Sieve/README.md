# Segmented Sieve

[Link](https://www.geeksforgeeks.org/segmented-sieve/)

**Problems with Simple Sieve:**  
The Sieve of Eratosthenes looks good, but consider the situation when n is large, the Simple Sieve faces the following issues.

- An array of size Θ(n) may not fit in memory
- The simple Sieve is not cached friendly even for slightly bigger n. The algorithm traverses the array without locality of reference.

**Segmented Sieve**
The idea of a segmented sieve is to divide the range [0..n-1] in different segments and compute primes in all segments one by one. This algorithm first uses Simple Sieve to find primes smaller than or equal to √(n). Below are steps used in Segmented Sieve.

1. Use Simple Sieve to find all primes up to the square root of ‘n’ and store these primes in an array “prime[]”. Store the found primes in an array ‘prime[]’.
2. We need all primes in the range [0..n-1]. We divide this range into different segments such that the size of every segment is at-most √n
3. Do following for every segment [low..high]

   - Create an array mark[high-low+1]. Here we need only O(x) space where x is a number of elements in a given range.
   - Iterate through all primes found in step 1. For every prime, mark its multiples in the given range [low..high].

In Simple Sieve, we needed O(n) space which may not be feasible for large n. Here we need O(√n) space and we process smaller ranges at a time (locality of reference)

Note that time complexity (or a number of operations) by Segmented Sieve is the same as Simple Sieve. It has advantages for large ‘n’ as it has better locality of reference thus allowing better caching by the CPU and also requires less memory space.

**Statistics**

|                      | Pre Computation       | Core Logic              |
| -------------------- | --------------------- | ----------------------- |
| **Time complexity**  | O(√R \* log(log(√R))) | O(R -L \* log(log(√R))) |
| **Space complexity** | O(MAX) or O(10^6)     | O(R-L+1)                |
