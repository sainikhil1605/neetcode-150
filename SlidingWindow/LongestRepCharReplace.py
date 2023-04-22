class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        ans = 0
        left = 0
        right = 0
        while right < len(s):
            if s[right] in d:
                d[s[right]] += 1
            else:
                d[s[right]] = 1
            print(d, right, left)
            if (right - left + 1) - max(d.values()) > k:
                d[s[left]] -= 1
                left += 1
            else:
                print(right, left)
                ans = max(ans, right - left + 1)
            right += 1
        return ans
