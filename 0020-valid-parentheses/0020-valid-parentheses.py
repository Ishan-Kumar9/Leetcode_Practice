class Solution:
    def isValid(self, s: str) -> bool:
        brac={")":"(","]":"[","}":"{"}
        s1=[]
        for i in s:
            if i in "([{":
                s1.append(i)
            else:
                if len(s1)> 0 and s1[-1] == brac[i]:
                    s1.pop()
                else:
                    s1.append(i)
        if not s1:
            return True
        else:
            return False