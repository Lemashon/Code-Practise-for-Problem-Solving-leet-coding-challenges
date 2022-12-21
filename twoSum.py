'''
	Given an array of integers, return indices of the two numbers such that they add up to a specific target.

	You may assume that each input would have exactly one solution, and you may not use the same element twice.

	Example:

	Given nums = [2, 7, 11, 15], target = 9,

	Because nums[0] + nums[1] = 2 + 7 = 9,
	return [0, 1].
'''

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(1+i, len(nums)):
            if nums[i] + nums[j] == target:
                return[i, j]

#Using Hash table

def twoSum(nums, target):
    seen = {} #Hash table to store elements and their indices.
    
    for i, num in enumerate(nums):
        if target - num in seen: #check if difference exists in hash table.
            return [seen[target-num], i] Return indices of pair
        seen[num] = i :add element and its index to hash table