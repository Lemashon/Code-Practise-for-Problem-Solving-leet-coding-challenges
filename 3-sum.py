#Given an array sums of n integers, are there elements a,b,c in nums such that a+b+c = 0?
#Find all unique triplets in the array which gives the sum of zero

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort        
        length = len(nums)
        
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i -1]:
              continue
            l = i + 1
            r = length - l
            
            while l < r:
                total = nums[i] + nums[r] + nums[l]
                if total < 0:
                    #-2, -2, 0, 1
                    l = l + 1
                elif total > 0:
                    r = r-1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l = l+1
                    while l < r and nums[r] == nums[r -1]:
                        r = r - 1
                    l = l+1
                    r = r-1
            return
         
        nums=[-4,2,-1,1,-1,0]
        print("*res: ", res)