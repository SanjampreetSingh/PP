# [1390] Four Divisors

[Link](https://leetcode.com/problems/four-divisors/)

Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.

If there is no such integer in the array, return 0.

**Example 1:**  
`Input: nums = [21,4,7]`  
`Output: 32`  
**Explanation:**  
`21 has 4 divisors: 1, 3, 7, 21`
`4 has 3 divisors: 1, 2, 4`
`7 has 2 divisors: 1, 7`
`The answer is the sum of divisors of 21 only.`

**Constraints:**

- 1 <= nums.length <= 10^4
- 1 <= nums[i] <= 10^5

**Statistics**

1. Time complexity - O(N\*sqrt(nums))
2. Space complexity - O(1)

**Result**:  
![Result image](https://github.com/SanjampreetSingh/PP/blob/master/LeetCode/Mathematic%20Code/Four%20Divisors/image.png)