class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(a) - 1
        while p1 < p2:
            if a[p1] + a[p2] == target:
                return [p1 + 1, p2 + 1]
            if a[p1] + a[p2] > target:
                p2 -= 1
            if a[p1] + a[p2] < target:
                p1 += 1
        return [-1, -1]
