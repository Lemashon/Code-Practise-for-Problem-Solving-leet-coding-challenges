"""You have an array of logs. Each log is a space delimited string of words. Each
For each log, the first word in each log is an alphanumeric identifier. Then, either
> Each word after the identifier will consist only of lowercase letters, or;
>Each word after the identifier will consist only of digits

"""

class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        res1, res2 = [], []
        
        for log in logs:
            if (log.split()[1]).isdigit():
                res2.append(log)
                
            else:
                res1.append(log.split())
        res1.sort(key = lambda x: x[0])
        res1.sort(key = lambda x: x[1:])
        
        for i in range(len(res1)):
            res1[i] = (" ".join(res1[i]))
        res1.extend(res2)
        return s1