class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maxx = 0
        for i in range(len(strs)):
            if strs[i].isnumeric():
                maxx = max(maxx, int(strs[i]))
            else:
                maxx = max(maxx, len(strs[i]))
        return maxx