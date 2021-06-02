# A simple Python3 program to rearrange
# contents of arr[] such that arr[j]
# becomes j if arr[i] is j

# A simple method to rearrange
# 'arr[0..n-1]' so that 'arr[j]'
# becomes 'i' if 'arr[i]' is 'j'
def rearrangeNaive(arr, n):
    for i in range(n):
        if arr[i] >= 0:
            index = arr[i]
            value = i
            while(index != i):
                temp = arr[index]
                arr[index] = -1*(value+1)
                value = index
                index = temp
            arr[index] = -1*(value+1)

    for i in range(n):
        arr[i] = (-1*arr[i])-1

# A utility function to print
# contents of arr[0..n-1]


def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")


# Driver program
arr = [1, 3, 0, 2]
n = len(arr)
print("Given array is", end=" ")
printArray(arr, n)

rearrangeNaive(arr, n)
print("\nModified array is", end=" ")
printArray(arr, n)
