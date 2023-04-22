class Solution:
    def maxProfit(self, a: List[int]) -> int:
        r = [0] * len(a)
        m = 0
        ans = 0
        for i in range(len(a) - 1, -1, -1):
            print(m, a[i])
            if a[i] <= m:
                ans = max(ans, m - a[i])
            m = max(m, a[i])

        return ans
