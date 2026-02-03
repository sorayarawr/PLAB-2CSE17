#Given an array arr, rotate the array by K positions in clockwise direction.

def rotate(arr, k):
    n = len(arr)
    k %= n              # handle k > n
    return arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5]
print(rotate(arr, 2))