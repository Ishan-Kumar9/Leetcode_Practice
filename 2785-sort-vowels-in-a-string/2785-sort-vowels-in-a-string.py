class Solution:
    def sortVowels(self, s: str) -> str:
        vow = []
        sett = {"a","e","i","o","u","A","E","I","O","U"}
        for i in s:
            if i in sett:
                vow.append(i)
        vow.sort()
        t = ""
        j = 0
        for i in s:
            if i in sett:
                t += vow[j]
                j += 1
            else:
                t += i
        return t