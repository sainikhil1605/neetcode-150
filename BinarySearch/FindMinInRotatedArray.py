class Solution:
    def findMin(self, a: List[int]) -> int:
        left = 0
        right = len(a) - 1
        ans = 2**32
        while left <= right:
            mid = (left + right) // 2
            if a[0] > a[mid]:
                right = mid - 1
            else:
                left = mid + 1
                ans = mid
        if ans == len(a) - 1:
            return a[0]
        return a[ans + 1]
