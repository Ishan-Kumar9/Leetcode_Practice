class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        cnt = 0
        for i in s:
            if not stk:
                stk.append(i)

            elif i == "(":
                stk.append(i)
            else:
                if stk[-1] == "(":
                    stk.pop()
                else:
                    stk.append(i)
        return len(stk)