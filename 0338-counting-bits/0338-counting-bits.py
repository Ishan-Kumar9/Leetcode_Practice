class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            x = bin(i)[2:]
            y = x.count("1")
            ans.append(y)
        return ans