class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        d = {}
        for i in range(0, len(a)):
            # print(d)
            if a[i] in d:
                return [d[a[i]], i]
            else:
                d[target - a[i]] = i
