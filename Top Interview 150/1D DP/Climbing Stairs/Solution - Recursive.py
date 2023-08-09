class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        dp[0] = dp[1] = 1

        def helper(i):
            nonlocal dp

            if i in dp:
                return dp[i]

            dp[i] = helper(i - 1) + helper(i - 2)
            return dp[i]

        return helper(n)
