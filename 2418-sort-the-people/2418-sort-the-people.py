class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        d = {}
        for i in range(n):
            d[heights[i]] = names[i]

        d_sort = dict(sorted(d.items(), reverse = True))
        return list(d_sort.values())