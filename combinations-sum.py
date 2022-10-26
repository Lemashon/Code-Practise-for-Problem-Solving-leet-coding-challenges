def Solution:
    def combinationsSum3(self, k:int, n: int) -> List[List[int]]: 
        #k = 3, n = 7
        
        def dfs(digit, start_num, cur, cur_sum):
            #(0,0,[],0)
            if cur_sum == n and digit == k:
                ans.append(cur[:])
            elif digit >=k or cur_sum> n:
                return
            else:
                for i in range(start_sum+1, 10):
                    #i = 1
                    cur,append(i)
                    #cur = [1, ]
                    dfs(digit+1, i, cur, cur_sum+1)
                    #cur(1,1,[1],1)
                    cur.pop()
        ans = []
        dfs(0,0,[],0)
        return ans