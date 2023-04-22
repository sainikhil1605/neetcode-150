class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = {}
        for i in s1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        right = len(s1) - 1
        left = 0

        def is_valid(s):
            d2 = {}
            for i in s:
                if i in d2:
                    d2[i] += 1
                else:
                    d2[i] = 1
            for i in d1:
                if i not in d2:
                    return False
                elif d2[i] != d1[i]:
                    return False
            return True

        while right < len(s2):
            if is_valid(s2[left : right + 1]):
                return True
            else:
                left += 1
                right += 1
            print(left, right)
        return False
