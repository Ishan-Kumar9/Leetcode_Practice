class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = [("." + "#" * (n-1)) for i in range(m-1)]
        res.append("."* n)

        return res