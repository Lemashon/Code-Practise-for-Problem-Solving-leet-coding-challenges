#Given an integer arraynums, find the continous subarray(containing at least
# one number) which has the largest sum and return its sum

class Solution:
    def maxSubarray(self, nums: list[int]) -> int:
        total_sum = max_sum = nums[0]
        
        for i in mums[1:]:
            total_sum = max(i, total_sum + i)
            max_sum = max(max_sum, total_sum)
            
        return max_sum