class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        ans = []
        for i in l:
            new = i[::-1]
            ans.append(new)

        result = " ".join(ans)
        return result