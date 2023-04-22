class Solution:
    def search(self, a: List[int], target: int) -> int:
        piv = -1
        left = 0
        right = len(a) - 1

        def bs(a, left, right):
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if a[mid] == target:
                    return mid
                if a[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1
                print(left, right)
            return ans

        if a[-1] > a[0]:
            return bs(a, 0, len(a) - 1)
        while left <= right:
            mid = (left + right) // 2
            if a[0] > a[mid]:
                right = mid - 1
            else:
                left = mid + 1
                piv = mid
        print(piv)
        if a[0] <= target and target <= a[piv]:
            return bs(a, 0, piv)
        else:
            return bs(a, piv + 1, len(a) - 1)
