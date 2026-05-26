class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        small = set()
        big = set()
        count = 0
        for i in word:
            if i.islower():
                small.add(i)
            else:
                big.add(i)
        for i in small:
            if i.upper() in big:
                count += 1
        return count