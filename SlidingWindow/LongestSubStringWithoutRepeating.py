class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        hs = set()
        left = 0
        right = 0
        ans = 0
        while right < len(s):
            if s[right] not in hs:
                hs.add(s[right])
                ans = max(ans, right - left + 1)
            else:
                while s[right] != s[left]:
                    if s[left] in hs:
                        hs.remove(s[left])
                        left += 1
                    else:
                        break
                left += 1
                # print(hs)
            right += 1
        return ans
