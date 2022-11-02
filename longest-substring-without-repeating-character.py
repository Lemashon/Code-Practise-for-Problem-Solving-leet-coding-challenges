class Solution:
    def lengthOfSubstring(self, s: str) -> int:
        s = ('aaabbaccccff')
        if len(s) == 0:
            return 0
        map = {} #map - name of dictionary
        max_length = start = 0
        
        for i in range(len(s)):
            if s[i] in map and start <= map[s[i]]:
                start = map[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
                map[s[i]] = i
                
        return(max_length)
    print(max_length)
    