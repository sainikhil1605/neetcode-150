class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = "!@#$%^&*()'[]{};:/,./<>?\|`~-=_+"
        for i in s:
            if i in a:
                s = s.replace(i, "")

        s = s.replace(" ", "")
        s = s.replace('"', "")
        s = s.lower()
        print(s)
        if s == s[::-1]:
            return True
        else:
            return False
