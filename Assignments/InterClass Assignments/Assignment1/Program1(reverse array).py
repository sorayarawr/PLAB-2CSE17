# You are given an array of integers arr[]. You have to reverse the given array.
class Solution:
    def reverse_array(self, arr):
        left = 0
        right = len(arr) - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr
    
obj = Solution()
array = [1, 2, 3, 4, 5]
reversed_array = obj.reverse_array(array)
print("Reversed Array:", reversed_array)
