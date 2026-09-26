class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = {}
        for i in knowledge:
            d[i[0]] = i[1]

        res = ""
        i = 0
        while i < len(s):
            if s[i] == '(':
                i += 1
                k =''
                while s[i] != ')':
                    k += s[i]
                    i += 1
                i += 1
                if k not in d:
                    res += '?'
                else:
                    res += d[k]
            else:
                res += s[i]
                i += 1
        return res
