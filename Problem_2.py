# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        dp = [([False] * (n + 1)) for _ in range(m + 1)]
        dp[0][0] = True
        
        def isMatch(i, j):
            return ((j >= 0) and p[j] == '.') or (s[i] == p[j])
        
        for j, c in enumerate(p):
            if (c == '*' and dp[0][j - 1]):
                dp[0][j + 1] = True
        for i in range(m):
            for j in range(n):
                if p[j] == '*':
                    noRepeat = dp[i + 1][j - 1]
                    doRepeat = (isMatch(i, j - 1) and dp[i][j + 1])
                    dp[i + 1][j+ 1] = (noRepeat or doRepeat)
                elif isMatch(i, j):
                    dp[i + 1][j + 1] = dp[i][j]
        return dp[m][n]