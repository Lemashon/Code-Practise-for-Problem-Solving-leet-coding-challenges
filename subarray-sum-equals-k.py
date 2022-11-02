#Given an array and an integer k, you need to find the total number of continuous subarrays whose sum equals key

#input: nums = [1,1,1], k =2
#output: 2

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        sumdict = {0:1}
        n = len(nums)
        count = 0
        s = 0
        
        for num in nums:
            s += num
            if s-k in sumdict:
                count += sumdict[s-k]
            if s in sumdict:
                sumdict[s] += 1
            else:
                sumdict[s] = 1
        return count