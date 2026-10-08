class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cnt1 = cnt2 = 0
        res = ""
        for i in range(len(s)):
            if s[i] == "(":
                cnt1 += 1
            else:
                cnt2 += 1

            if cnt1 > 1 and s[i] == "(":
                res += s[i]
            elif cnt2 < cnt1 and s[i] == ")":
                res += s[i]
            elif cnt1 == cnt2:
                cnt1 = 0
                cnt2 = 0

        return res
            