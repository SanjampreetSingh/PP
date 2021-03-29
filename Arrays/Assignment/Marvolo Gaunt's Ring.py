import sys

def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_int(): return map(int, sys.stdin.readline().strip().split())

n, p, q, r = get_int()
arr = get_list()

p_max = [0]*n
r_max = [0]*n
ans = -1e20

p_max[0] = p * arr[0]
r_max[n-1] = r * arr[n-1]

for i in range(1, n):
    p_max[i] = max(p*arr[i], p_max[i-1])

for i in range(n-2, -1, -1):
    r_max[i] = max(r_max[i+1], r*arr[i])

for i in range(0, n):
    ans = max(ans, (p_max[i] + (q*arr[i]) + r_max[i]))

print(ans)

"""
https://codeforces.com/problemset/problem/855/B
https://ide.geeksforgeeks.org/9YueBtW5YM

Professor Dumbledore is helping Harry destroy the Horcruxes. He went to Gaunt Shack as he suspected a Horcrux to be present there. He saw Marvolo Gaunt's Ring and identified it as a Horcrux. Although he destroyed it, he is still affected by its curse. Professor Snape is helping Dumbledore remove the curse. For this, he wants to give Dumbledore exactly x drops of the potion he made.

Value of x is calculated as maximum of p·ai + q·aj + r·ak for given p, q, r and array a1, a2, ... an such that 1 ≤ i ≤ j ≤ k ≤ n. Help Snape find the value of x. Do note that the value of x may be negative.

Input
First line of input contains 4 integers n, p, q, r ( - 109 ≤ p, q, r ≤ 109, 1 ≤ n ≤ 105).

Next line of input contains n space separated integers a1, a2, ... an ( - 109 ≤ ai ≤ 109).

Output
Output a single integer the maximum value of p·ai + q·aj + r·ak that can be obtained provided 1 ≤ i ≤ j ≤ k ≤ n.
"""