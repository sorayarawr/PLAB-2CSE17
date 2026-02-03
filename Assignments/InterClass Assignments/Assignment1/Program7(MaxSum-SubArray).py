# You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].
# Note : A subarray is a continuous part of an array

def max_subarray_sum(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]

    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

array = [-2,1,-3,4,-1,2,1,-5,4]
result = max_subarray_sum(array)
print("Maximum Subarray Sum:", result)  