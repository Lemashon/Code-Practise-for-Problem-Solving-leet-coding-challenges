""""
Given an unsorted integer array, find a pair with the given sum in it.
Input:
 
nums = [8, 7, 2, 5, 3, 1]
target = 10
 
Output:
 
Pair found (8, 2)
or
Pair found (7, 3)
 
 
Input:
 
nums = [5, 2, 6, 8, 1, 9]
target = 12
 
Output: Pair not found
"""

#Using brute force

def findPair(nums, target):
    for i in range(len(nums)- 1):
        for j in range(1+1, len(nums)):
            if nums[i] + nums[j] == target:
                print("Pair found", (nums[i], nums[j]))
                return
    print("Pair not found")

if __name__ == '__main__':
    nums = [8,7,5,4,1]
    target = 10
    findPair(nums, target)
    
#Time complexity is 0(n^2)

#Using sorting

def findPair(nums, target):
    nums.sort()
    (low,high) = (0, len(nums)-1)
    
    while low < high:
        if nums[low] + nums[high] == target:
            print("Pair found", (nums[low],nums[high]))
            return
        
        if nums[low] + nums[high] < target:
            low = low + 1
        else:
            high = high - 1
    print("Pair not found")
    
if __name__ == "__main__":
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
 
    findPair(nums, target)
    
#The time complexity of the above solution is O(n.log(n)) and doesn’t require any extra space.

#Using HashTable

def findPair(nums, target):
    d = {}
    
    for i,e in enumerate(nums):
        if target - e in d:
            print("Pair found", (nums[d.get(target - e)], nums[i]))
            return
        d[e] = i
    print("Pair not found")
if __name__ == '__main__':
 
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
 
    findPair(nums, target)