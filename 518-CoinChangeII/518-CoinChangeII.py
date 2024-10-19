class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = {}
        count = 0 
        def dfs(i,reminder):
            if i == len(coins): 
                return 0
            if reminder == 0:
                return 1 
            if reminder <0:
                return 0
            if (i,reminder) in dp:
                return dp[(i,reminder)]

            skip = dfs(i+1,reminder)

            use = 0
            if coins[i] <= reminder:
                use = dfs(i,reminder-coins[i]) #not sure about this line
            result = skip + use 
            dp[(i,reminder)] = result 
            return result 
        final= dfs(0,amount)
        return final

        