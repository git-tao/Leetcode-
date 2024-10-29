class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0 
        
        def helper(l,r):
            local_count = 0
            while l>=0 and r <len(s) and s[l] == s[r]:
                local_count +=1
                l-=1
                r+=1
            return local_count  
        
        for i in range (len(s)):
            count += helper(i,i)
            count += helper(i,i+1)

        return count 

        