class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # dp = {} #i, x, y
        
        # def dsf(i,x,y):
        #     if i == len(stones):
        #         return stones[i]
        #     if 

        #use DP to solve this problem.
        #intiate a dictionary to keep track of travrerse 
        sumTotal = sum(stones)
        target = ceil(sumTotal/2)
        dp = {}

        def dsf(i,total):
            if total >= target or i == len(stones):
                return abs (total-(sumTotal-total)) #this line is key 
            if (i,total) in dp:
                return dp[(i,total)]
            dp[(i,total)] = min(

                dsf(i+1,total),
                dsf(i+1,total+stones[i])
            )

            return dp[(i,total)]

        return dsf(0,0)