'''
Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be non-empty after deleting one element.

 

Example 1:

Input: arr = [1,-2,0,3]
Output: 4
Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.
Example 2:

Input: arr = [1,-2,-2,3]
Output: 3
Explanation: We just choose [3] and it's the maximum sum.
Example 3:

Input: arr = [-1,-1,-1,-1]
Output: -1
Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, then get an empty subarray to make the sum equals to 0.
 

Constraints:

1 <= arr.length <= 10^5
-10^4 <= arr[i] <= 10^4
'''

def maximumSum(arr):
    max_sum = [0] * len(arr)
    max_sum[0] = arr[0]
    
    for i in range(1, len(arr)):
        max_sum[i] = max(max_sum[i - 1] + arr[i], arr[i])
        max_sum_with_deletion = max(max_sum)
        for i in range(1, len(arr) - 1):
            max_sum_with_deletion = max(max_sum_with_deletion, arr[i], max_sum[i-1]+max(0, max_sum[i + 1] - arr[i]))
            return max_sum_with_deletion