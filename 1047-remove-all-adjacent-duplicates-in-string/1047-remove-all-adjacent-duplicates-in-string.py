class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = []
        for i in s:
            if stk:
                if i == stk[-1]:
                    stk.pop()
                else:
                    stk.append(i)
            else:
                stk.append(i)
        ans = "".join(stk)
        return ans