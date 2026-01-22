class Solution:
    def find_min_max(self, arr):
        min_val = arr[0]
        max_val = arr[0]

        for num in arr:
            if num < min_val:
                min_val = num
            elif num > max_val:
                max_val = num

        return min_val, max_val
    
obj = Solution()
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_value, max_value = obj.find_min_max(array)
print("Minimum Value:", min_value)
print("Maximum Value:", max_value)