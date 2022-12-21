'''
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
'''

def SequentialDigits(low: int, high: int) -> list[int]:

    result = []
    
    for i in range(low, high+1):
        #convert integer to string
        s = str(i)
        
        #Check if the integer has sequential digits
        if all(ord(s[j]) == ord(s[j+1]) - 1 for j in range(len(s)-1)):
            result.append(i)
    return result