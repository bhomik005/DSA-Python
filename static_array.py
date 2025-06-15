"""
Static Array - In programming languages like C++ or Java, arrays have to have an allocated size and type.
The size of the static array cannot be changed once it is declared or in other words, it cannot hold elements 
greater than the allocated size.
"""

# arr = [1, 2, 3, 4]
# O(1) time
def insertEnd(arr, n, length, capacity):
    # check if we have a capacity
    if capacity > length:
        arr[length] = n

# O(1) time (soft delete)
def removeEnd(arr, length):
    # soft delete - overwrite the last element with 0
    if length > 0:
        arr[length - 1] = 0

# arr = [1, 2, 3, 5, 6]
# arr = [1, 2, 3, _, 5, 6]
# O(n) time
def insertMiddle(arr, i, n, length):
    # shift the elements to the right
    for i in range(length - 1, i - 1, -1):
        arr[i + 1] = arr[i]
    # insert the element at index i
    arr[i] = n

# arr = [1, 2, 3, 4, 5]
# arr = [1, 3, 4, 5]
# O(n) time
def removeMiddle(arr, i, length):
    for i in range(i + 1, length):
        arr[i - 1] = arr[i]
    
# O(n) time
def printArr(arr, capacity):
    # traversing through the array elements and print
    for i in range(capacity):
        print(arr[i])