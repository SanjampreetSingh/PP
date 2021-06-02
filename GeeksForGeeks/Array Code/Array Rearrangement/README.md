# Rearrange an array such that ‘arr[j]’ becomes ‘i’ if ‘arr[i]’ is ‘j’ | Set 1

[Link](https://www.geeksforgeeks.org/rearrange-array-arrj-becomes-arri-j/)

Given an array of size n where all elements are distinct and in range from 0 to n-1, change contents of arr[] so that arr[i] = j is changed to arr[j] = i.

**Example 1:**  
`Input: arr[] = {1, 3, 0, 2};`  
`Output: arr[] = {2, 0, 3, 1};`  
**Explanation:**  
`Since arr[0] is 1, arr[1] is changed to 0`  
`Since arr[1] is 3, arr[3] is changed to 1`  
`Since arr[2] is 0, arr[0] is changed to 2`  
`Since arr[3] is 2, arr[2] is changed to 3`

**Example 2:**  
`Input: arr[] = {2, 0, 1, 4, 5, 3};`  
`Output: arr[] = {1, 2, 0, 5, 3, 4};`

**Explanation:**  
`The idea is to process all cycles one by one. To check whether an element is processed or not, we change the value of processed items arr[i] as -arr[i]. Since 0 can not be made negative, we first change all arr[i] to arr[i] + 1. In the end, we make all values positive and subtract 1 to get old values back.`

**Statistics**

1. Time complexity - O(n)
2. Space complexity - O(1)

**Result**:  
![Result image](https://github.com/SanjampreetSingh/PP/blob/master/GeeksForGeeks/Array%20Code/Array%20Rearrangement/image.jpg)
