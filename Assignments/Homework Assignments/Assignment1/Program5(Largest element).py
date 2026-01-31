#Given an array arr[]. The task is to find the largest element and return it.
def find_largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
largest_element = find_largest(array)
print("Largest Element:", largest_element)