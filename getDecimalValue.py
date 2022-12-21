'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

 

Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0
Example 3:

Input: head = [1]
Output: 1
Example 4:

Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880
Example 5:

Input: head = [0,0]
Output: 0
'''

def decimalValue(head):
    
    #initialize the result to 0
    result = 0
    
    #initialize power to 0
    power = 0
    
    #iterate through the linked list
    while head is not None:
        result += head.value*(2**power)
        power += 1
        head = head.next
        
    return result