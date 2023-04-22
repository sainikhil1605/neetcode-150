class Solution:
    def topKFrequent(self, a: List[int], k: int) -> List[int]:
        d = {}
        for i in a:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        ans = set()
        # print(d)
        for i in sorted(list(d.values()))[::-1][:k]:
            for j in d.keys():
                if d[j] == i:
                    ans.add(j)

        return list(ans)
