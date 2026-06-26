class Solution:
    def clearDigits(self, s: str) -> str:
        res = []
        for i in s:
            if i.isalpha():
                res.append(i)
            else:
                if res:
                    res.pop()
        ans = "".join(res)
        return ans