class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # m_copy = m
        # n_copy = n 

        # def backtrack(i,count):
        #     if i == len(strs):
        #         return count 

        #     for num in str[i]:
        #         if num == 0:
        #             m_copy -=1
        #         else:
        #             n_copy -=1
        #     if m_copy >=0 and n_copy >=0:
        #         count +=1
        #     m_copy = m
        #     n_copy = n

        #     backtrack(i+1,count)

        # return backtrack(0,0)
        dp = {}
        def dsf(i,m,n):
            if i == len(strs):
                return 0 
            if (i,m,n) in dp:
                return dp[(i,m,n)]
            
            mCnt, nCnt = strs[i].count('0'), strs[i].count('1')
            # do not include 
            dp[(i,m,n)] = dsf(i+1,m,n)
            #include 
            if mCnt <= m and nCnt <= n:
                dp[(i,m,n)] = max(
                    dp[(i,m,n)],
                    1+dsf(i+1,m-mCnt,n-nCnt)
                )
            #don't understand the following code 
            return dp[(i,m,n)]
        return dsf(0,m,n)
        