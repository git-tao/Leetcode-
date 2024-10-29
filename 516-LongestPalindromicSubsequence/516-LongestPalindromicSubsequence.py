class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # length = 0
        # dp = {}
        # def dfs(l,r):
        #     if l < 0 or r>=len(s):
        #         return 0 
        #     if (l,r) in dp:
        #         return dp[(l,r)]
            
        #     if s[l] == s[r] and r-l+1>length:
        #         length = r-l+1
        #         dp[(l,r)]= dfs(l-1,r+1)
        #     else:
        #         dp[(l,r)] = max(dfs(l-1,r),dfs(l,r+1))
        #     return dp[(l,r)]
        # for i in range(len(s)):
        #     even = dfs(i,i)
        #     odd = dfs(i,i+1)

        # return max(even,odd)

        dp = {}
        
        def dfs(l,r):
            if l>r:
                return 0 
            if l == r:
                return 1 
            if (l,r) in dp:
                return dp[(l,r)]

            if s[l] == s[r]:
                dp[(l,r)] = 2+ dfs(l+1,r-1)

            else:
                dp[(l,r)] = max(dfs(l+1,r),dfs(l,r-1))
            return dp[(l,r)]

        return dfs(0,len(s)-1)
            

            
                