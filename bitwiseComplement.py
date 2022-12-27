'''Every non-negative integer N has a binary representation.  For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note that except for N = 0, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  For example, the complement of "101" in binary is "010" in binary.

For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.

 

Example 1:

Input: 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
Example 2:

Input: 7
Output: 0
Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
Example 3:

Input: 10
Output: 5
Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
 

Note:

0 <= N < 10^9
'''
class Solution(object):
    def bitwiseComplement(self, N):
        """
        This function takes in an integer N and returns its bitwise complement.
        The bitwise complement of an integer N is defined as the number obtained by inverting the bits of N,
        that is, replacing each 0 bit with a 1 bit and each 1 bit with a 0 bit.
        """
        
        # If N is 0, return 1
        if N == 0:
            return 1
        
        # Import the math module
        import math
        
        # Calculate the number of bits needed to represent N in binary
        # This is done by taking the floor of the logarithm base 2 of N, and adding 1
        bits = (int)(math.floor(math.log(N) /math.log(2))) + 1
        
        # Return the bitwise complement of N
        # This is done by first generating a number with all bits set to 1, and the same number of bits as N
        # This is done by left-shifting the number 1 by the number of bits needed to represent N in binary
        # Then, the number is subtracted by 1 to set all the bits to 1
        # Finally, the number is XORed with N to invert the bits of N
        return ((1 << bits) - 1) ^ N
