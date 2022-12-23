'''
Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: arr = [1,2], k = 3
Output: 9
Example 2:

Input: arr = [1,-2,1], k = 5
Output: 2
Example 3:

Input: arr = [-1,-2], k = 7
Output: 0
 

Constraints:

1 <= arr.length <= 10^5
1 <= k <= 10^5
-10^4 <= arr[i] <= 10^4
'''

def maxSubarray(arr, k):
    n = len(arr)
    prefix_sum = [0] *(n+1)
    for i in range(i , n+1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i -1]
        max_sum = 0
        for i in range(n):
            curr_sum= prefix_sum[-1] - prefix_sum[i]
            max_sum = max(max_sum, curr_sum)
            for j in range(2, k):
                curr_sum = prefix_sum[-1] - prefix_sum[i] + prefix_sum[n-1]*(j-1)
                max_sum= max(max_sum, curr_sum)
        return max_sum 
                