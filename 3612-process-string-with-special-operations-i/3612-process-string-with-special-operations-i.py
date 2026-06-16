class Solution:
    def processStr(self, s: str) -> str:
        stk = []
        for i in s:
            if i.isalpha():
                stk.append(i)
            elif i == "#":
                stk = stk + stk
            elif i == "*":
                if stk:
                    stk.pop()
            else:
                stk = stk[::-1]
        ans = "".join(stk)
        return ans