class Solution:
    def isValid(self, s: str) -> bool:
        brac={")":"(","]":"[","}":"{"}
        s1=[]
        for i in s:
            if s == "([{":
                s1.append(i)
            else:
                if len(s1)>0 and s1[-1]==brac[i]:
                    s1.pop()
        if not s1:
            return True
        else:
            return False