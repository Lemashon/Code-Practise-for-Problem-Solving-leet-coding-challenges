'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.

 
Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 10^4
text consists of lower case English letters only.
'''

def maxNumberOfBalloons(text):
    letter_counts = {}
    for letter in text:
        if letter not in letter_counts:
            letter_counts[letter] = 0
        letter_counts[letter] += 1
    max_instances = 0
    while True:
        enough_letters = True
        for letter in "balloon":
            if letter_counts.get(letter, 0) < 1:
                enough_letters = False
                break
            if enough_letters:
                max_instances += 1
                for letter in "balloon":
                    letter_counts[letter] -= 1
            else:
                break
    return max_instances
            