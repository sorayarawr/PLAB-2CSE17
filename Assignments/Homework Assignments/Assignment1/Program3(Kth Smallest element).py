#given an integer array arr[] and an integer K, your task is to find and return the Kth smallest element in the array. (Kth element is based on the sorted order of the array. Also write the algorithm to sort the given array aswell)
class Solution:
    def kth_smallest(self, arr, k):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        
        return arr[k-1]
    

obj = Solution()
array = [7, 10, 4, 3, 20, 15]
k = 3
kth_smallest_element = obj.kth_smallest(array, k)
print(f"{k}th Smallest Element:", kth_smallest_element)