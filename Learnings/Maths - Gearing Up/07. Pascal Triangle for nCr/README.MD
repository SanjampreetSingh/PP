# Calculate nCr using Pascal’s Triangle

[Link](https://www.geeksforgeeks.org/calculate-ncr-using-pascals-triangle/)

A useful application of Pascal’s triangle is the calculation of combinations. The formula to find nCr is n! / r! \* (n – r)! which is also the formula for a cell of Pascal’s triangle.

**Example 1:**  
`Input :n = 5, r = 3`  
`Output : 10 `  
**Explanation:**  
`n! / r! * (n - r)! = 5! / 3! * (2!) = 120 / 12 = 10`

1.  **nC0 = 1**, number of ways to select 0 elements from a set of n elements is 0
2.  **nCr = n-1Cr-1 + n-1Cr**, number of ways to select r elements from a set of n elements is summation of ways to select r-1 elements from n-1 elements and ways to select r elements from n-1 elements.

The idea is to use the values of subproblem to calculate the answers for larger values. For example, to calculate nCr, use the values of n-1Cr-1 and n-1Cr. So DP can be used to preprocess all the values in the range.

1.  Create a matrix of size 1000 \* 1000, assign the value of base cases, i.e. run a loop from 0 to 1000 and assign matrix\[i\]\[0\] = 1, nC0 = 1
2.  Run a nested loop from i = 1 to 1000 (outer loop) and the inner loop runs from j = 1 to i + 1.
3.  For every element (i, j) assign the value of _matrix\[i\]\[j\] = matrix\[i-1\]\[j-1\] + matrix\[i-1\]\[j\]_, using the formula nCr = n-1Cr-1 \+ n-1Cr
4.  After filling the matrix return the value of nCr as matrix\[n\]\[r\]

- **Time Complexity:** O(1).   
   The value of all pairs are precomputed so the time to answer the query is O(1), though some time is taken for precomputation but theoretically the precomputation takes constant time.
- **Space Complexity:** O(1).   
   Constant space is required.
