class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        if m == 1:
            return ["." * n]
        if n == 1:
            return ["."] * m

        res = ["." * n]
        for i in range(1, m):
            temp = ""
            for j in range(n):
                if j == n-1:
                    temp += "."
                else:
                    temp += "#"
            res.append(temp)
        return res

                