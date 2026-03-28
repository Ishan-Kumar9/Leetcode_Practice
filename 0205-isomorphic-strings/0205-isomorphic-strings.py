class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_set = {}
        t_set = {}

        for i in range(len(s)):
            s1 = s[i]
            t1 = t[i]

            if s1 not in s_set:
                s_set[s1] = i
            if t1 not in t_set:
                t_set[t1] = i

            if s_set[s1] != t_set[t1]:
                return False
        return True