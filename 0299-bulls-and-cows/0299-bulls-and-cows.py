class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b = c = 0
        s = Counter(secret)
        g = Counter(guess) 
        for i in s:
            if s[i] >= g[i]:
                c += g[i]
            if g[i] > s[i]:
                c += s[i]

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                b += 1
                c -= 1
        return str(b) + "A" + str(c) + "B"