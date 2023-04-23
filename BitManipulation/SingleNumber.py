class Solution:
    def singleNumber(self, a: List[int]) -> int:
        ans = a[0]
        for i in range(1, len(a)):
            ans = ans ^ a[i]
        return ans
